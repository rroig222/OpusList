import requests
from Connector_API.dataclasses import Work, User, Composer


class ComposerConnector():

    def __init__(self):

        self.link = "http://127.0.0.1:8000/composers"

    def get_composer_id_bd(self, id: int) -> Composer:


        rel_link = self.link + f"/{id}"

        try:
            response = requests.get(url=rel_link)
            response.raise_for_status()
            response = response.json()

            composer = Composer(id=response['id'], full_name=response['complete_name'],name=response['name'], epoch=response['epoch'])
            return composer

        except requests.exceptions.HTTPError as e:

            try:
                detail = e.response.json().get("detail", "Error desconocido")
            except Exception:
                detail = e.response.text

            raise ValueError(detail)
        
        except Exception as e:
            raise ConnectionError(f"API connection error: {e}")