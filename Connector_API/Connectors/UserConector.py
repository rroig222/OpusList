import requests
from Connector_API.dataclasses import Work, User, Composer
from Connector_API.Connectors.ComposerConnector import ComposerConnector


class UserConector():

    def __init__(self):
        self.link: str = "http://127.0.0.1:8000/users"

    def create_user(self, username: str, email: str, password:str):
        rel_link: str = self.link + "/new"

        data = {'username': username,
                'email': email,
                'password': password}


        try:

            response = requests.post(url=rel_link, json=data)

            response.raise_for_status()

            return response.json()
        
        except requests.exceptions.HTTPError:

            raise ValueError("Alredy existing user.")
        
        except requests.exceptions.RequestException as e:

            raise ConnectionError(f"API connection error: {e}")

    def login_check(self, username: str, password: str) -> User:

        rel_link: str = self.link + "/login"

        data = {
            'username': username,
            'password': password
        }

        try:
            response = requests.post(url=rel_link, json=data)

            response.raise_for_status()
            response = response.json()

            user = User(id=response['id'], username=response['username'], email=response['email'])

            return user
        
        except requests.exceptions.HTTPError as e:

            try:
                detail = e.response.json().get("detail", "Error desconocido")
            except Exception:
                detail = e.response.text

            raise ValueError(detail)
        
        except requests.exceptions.RequestException as e:

            raise ConnectionError(f"API connection error: {e}")

    def rate_work(self, user: User, work: Work, rating: int):

        data = {
            'user_id': user.id,
            'work_id': work.id,
            'rating': rating
        }

        rel_link = self.link +"/rate"

        try:

            response = requests.post(url=rel_link, json=data)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as e:
            raise e
        except requests.exceptions.ConnectionError as e:
            raise e
        
    def get_rated_works(self, user_id: int) -> tuple[User, list[Work]]:

        # users/works/{user_id}

        rel_link = self.link + "/works/" + str(user_id)

        try:

            response = requests.get(url=rel_link)
            response.raise_for_status()
            response = response.json()
            user = User(id=response['id'], username=response['username'], email=response['email'])

            composer_connector = ComposerConnector()

            works = []
            for work in response['works']:

                composer_id = work['composer_id']
                composer = composer_connector.get_composer_id_bd(composer_id)

                works.append(Work(id=work['id'], title=work['title'], composer_id=composer_id, 
                                  openopus_id=work['openopus_id'], genre = work['genre'], composer=composer))

            final_answer = (user, works)

            return final_answer
            
        
        except requests.exceptions.HTTPError as e:
            try:
                detail = e.response.json().get("detail", "Error desconocido")
            except Exception:
                detail = e.response.text

            raise ValueError(detail)

        except requests.exceptions.RequestException as e:

            raise ConnectionError(f"API connection error: {e}")

    def get_rate(self, work: Work, user: User) -> int:

        rel_link = self.link + f"/rate/{work.id}/{user.id}"

        try:
            response = requests.get(url=rel_link)
            response.raise_for_status()
            response = response.json()

            rating = response['rating']
            
            return rating
        

        
        except requests.exceptions.HTTPError as e:
            try:
                detail = e.response.json().get("detail", "Error desconocido")
            except Exception:
                detail = e.response.text
            raise ValueError(detail)
        
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API connection error: {e}")
        