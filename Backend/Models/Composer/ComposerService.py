from Backend.Models.User.UserCRUD import UserCRUD
from Backend.Models.User.UserModel import User
from Backend.Models.Work.WorkModel import Work
from Backend.Models.Composer.ComposerModel import Composer
from Backend.Models.Work.WorkCRUD import WorkCRUD
from Backend.Models.User.UserCRUD import UserCRUD
from Backend.Models.Composer.ComposerCRUD import ComposerCRUD

import requests

class ComposerService():

    def __init__(self, userCRUD: UserCRUD, workCRUD: WorkCRUD, composerCRUD: ComposerCRUD):

        self.userCRUD: UserCRUD = userCRUD
        self.workCRUD: WorkCRUD = workCRUD
        self.composerCRUD: ComposerCRUD = composerCRUD

    def create_composer_service(self, name: str, complete_name: str, epoch: str, openopus_id: int) -> Composer:
        
        if self.composerCRUD.get_composer_by_openopus_id(openopus_id=openopus_id):
            raise ValueError(f"Alredy existing composer {complete_name}!")
        
        else:
            composer = Composer(name=name, complete_name=complete_name, epoch=epoch, openopus_id=openopus_id)
            self.composerCRUD.create_composer(composer=composer)
            return composer
        
    def create_composer_from_openopus_to_local(self, first_key: str,response: dict, second_key = None) -> Composer:

        if second_key is not None:
            name = response[first_key][second_key]['name']
            complete_name = response[first_key][second_key]['complete_name']
            composer_openopus_id = int(response[first_key][second_key]['id'])
            epoch = response[first_key][second_key]['epoch']
        else:
            name = response[first_key]['name']
            complete_name = response[first_key]['complete_name']
            composer_openopus_id = int(response[first_key]['id'])
            epoch = response[first_key]['epoch']

        try:
            composer: Composer = self.create_composer_service(name=name, complete_name=complete_name, 
                                                    openopus_id=composer_openopus_id, epoch=epoch)
            
            return composer
        
        except ValueError as e:

            return self.composerCRUD.get_composer_by_openopus_id(composer_openopus_id)
        
    def get_composer_by_id_db(self, id: int) -> Composer:
        
        composer = self.composerCRUD.get_composer_by_id_bd_CRUD(id=id)

        if not composer:
            raise ValueError("Composer not found")
        
        else:
            return composer