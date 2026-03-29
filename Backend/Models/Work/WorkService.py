from Backend.Models.User.UserCRUD import UserCRUD
from Backend.Models.User.UserModel import User
from Backend.Models.Work.WorkModel import Work
from Backend.Models.Composer.ComposerModel import Composer
from Backend.Models.Work.WorkCRUD import WorkCRUD
from Backend.Models.User.UserCRUD import UserCRUD
from Backend.Models.Composer.ComposerCRUD import ComposerCRUD
from Backend.Models.Composer.ComposerService import ComposerService

import requests

class WorkService():

    def __init__(self, userCRUD: UserCRUD, workCRUD: WorkCRUD, composerCRUD: ComposerCRUD, composer_service: ComposerService):

        self.userCRUD: UserCRUD = userCRUD
        self.workCRUD: WorkCRUD = workCRUD
        self.composerCRUD: ComposerCRUD = composerCRUD
        self.composer_service: ComposerService = composer_service

    def create_work_service(self, title: str, genre: str, openopus_id: int, composer: Composer) -> Work:

        if self.workCRUD.get_work_by_openopus_id(openopus_id=openopus_id):
            raise ValueError(f"Alredy existing work {title}!")

        work = Work(title=title, genre=genre, openopus_id=openopus_id)
        composer.works.append(work)
        return self.workCRUD.create_work(work)

    def import_work_from_openopus_by_id_service(self, openopus_id: int) -> Work:
        
        # Comprueba que no exista
        try_work = self.workCRUD.get_work_by_openopus_id(openopus_id=openopus_id)
        if try_work:
            return try_work
        
        url: str = f"https://api.openopus.org/work/detail/{openopus_id}.json"

        response: dict = requests.get(url = url).json()
        print(response)

        try:
            composer: Composer = self.composerCRUD.get_composer_by_openopus_id(response['composer']['id'])

            title = response['work']['title']
            genre = response['work']['genre']
            openopus_id = response['work']['id']

            if composer:
                work = self.create_work_service(title=title, genre=genre, openopus_id=openopus_id, composer=composer)

            else:
                composer = self.composer_service.create_composer_from_openopus_to_local(response=response)
                
                work = self.create_work_service(title=title, genre=genre, openopus_id=openopus_id, composer=composer)
        
        except:
            if response['status']['error'] == 'Work not found':
                raise ValueError('Work not found')
            else:
                raise Exception("Unknown error")


        return work
    
    def search_work_in_db(self, query: str) -> tuple[Work, str] | None:
        searched_by_composer = self.workCRUD.search_work_by_composer(query=query)
        searched_works = []

        if searched_by_composer:
            for work in searched_by_composer:
                searched_works.append((work, 'composer'))

        searched_by_title = self.workCRUD.search_work_by_title(query=query)

        if searched_by_title:
            for work in searched_by_title:
                searched_works.append((work, 'title'))
        
        if searched_works:
            return searched_works
        else:
            return None
        
    def search_composer_in_openopus(self, composer: str) -> Composer:

        base_url = "https://api.openopus.org"

        response = requests.get(f"{base_url}/composer/list/search/{composer}.json")

        print(response.status_code)
        print(response.text)
        if response.status_code != 200:
            raise ConnectionError(
                f"OpenOpus request failed with status {response.status_code}"
            )

        data = response.json()
        
        composers = data.get("composers", [])

        if not composers:
            raise LookupError("Composer not found")

        if len(composers) > 1:
            names: list[str] = []
            for a in range(len(composers)):
                names.append(data['composers'][a]['complete_name'])
            raise ValueError(f"Ambiguous composer: {names}")

        composer: Composer = self.composer_service.create_composer_from_openopus_to_local(first_key='composers', response=data, second_key=0)

        return composer

    def search_work_in_openopus(self, composer: str, query: str) -> list[Work] | None:
        
        try:
            composer: Composer = self.search_composer_in_openopus(composer=composer)

            query = query.lower()
            tokened_query: list[str] = query.split()

            url: str = f"https://api.openopus.org/work/list/composer/{composer.openopus_id}/genre/all/search/{tokened_query[0]}.json"
            response = requests.get(url=url).json()

            works_dicts: list[dict] = []

            for work in response['works']:

                cumple = True
                title: str = work['title'].lower()
                for token in tokened_query:
                    if token not in title:
                        cumple = False
                        break
                
                if cumple:
                    works_dicts.append(work)

            works: list[Work] = []

            for work in works_dicts:
                works.append(self.import_work_from_openopus_by_id_service(work['id']))

            return works

        except LookupError as e:
            raise LookupError(str(e))
        except ValueError as e:
            raise ValueError(str(e))
        except ConnectionError as e:
            raise ConnectionError(str(e))
        except:
            raise Exception("Unknown Error")
