import requests
from Connector_API.dataclasses import Work, User, Composer
from Connector_API.Connectors.ComposerConnector import ComposerConnector


class WorkConector():

    def __init__(self):
        self.link: str = "http://127.0.0.1:8000/works"

    def search_work_db(self, user: User, query: str) -> list[tuple[Work, int | None]] | None:

        rel_link: str = self.link + f"/search-db/{user.id}/{query}"

        try:
            response = requests.get(url=rel_link)
            response.raise_for_status()
            response = response.json()

            composer_connector = ComposerConnector()

            list_of_works: list[tuple[Work, int| None]] = []

            for item in response['works']:

                work = item['work']
                composer_id = work['composer_id']
                composer = composer_connector.get_composer_id_bd(composer_id)

                work_to_append = Work(id=work['id'], title=work['title'], composer_id=composer_id, 
                                      openopus_id=work['openopus_id'], genre=work['genre'], composer=composer)
                
                rating = item['rating']

                list_of_works.append((work_to_append, rating))

            return list_of_works

        except requests.exceptions.HTTPError as e:
            try:
                detail = e.response.json().get("detail", "Error desconocido")
            except Exception:
                detail = e.response.text
            raise ValueError(detail)
        
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API connection error: {e}")
        
    def search_work_openopus(self, composer_query: str, query: str) -> list[Work]:
        rel_link: str = self.link + f"/openopus/{composer_query}/{query}"

        try:
            response = requests.get(url=rel_link)
            response.raise_for_status()
            response = response.json()

            works = response['works']

            composer_conector = ComposerConnector()

            final_work: list[Work] = []
            for work in works:
                composer = composer_conector.get_composer_id_bd(work['composer_id'])
                worky = Work(id=work['id'], title=work['title'], composer_id=work['composer_id'], openopus_id=work['openopus_id'],
                             genre=work['genre'], composer=composer)
                
                final_work.append(worky)

            return final_work

        except requests.exceptions.HTTPError as e:
            try:
                detail = e.response.json().get("detail", "Error desconocido")
            except Exception:
                detail = e.response.text
            raise ValueError(detail)
        
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API connection error: {e}")