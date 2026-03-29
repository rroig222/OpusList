from sqlalchemy.orm import Session

from Backend.Models.Work.WorkModel import Work
from Backend.Models.Composer.ComposerModel import Composer

class ComposerCRUD():

    def __init__(self, session: Session):
        self.session: Session = session

    def create_composer(self, composer: Composer) -> Composer:
        self.session.add(composer)
        self.session.commit()
        self.session.refresh(composer)

        return composer

    def get_composer_by_openopus_id(self, openopus_id: int) -> Composer | None:

        print("self.session =", self.session)
        print("type(self.session) =", type(self.session))
        print("Composer =", Composer)
        print("type(Composer) =", type(Composer))

        return self.session.query(Composer).filter(Composer.openopus_id == openopus_id).first()
    
    def get_composer_by_id_bd_CRUD(self, id: int) -> Composer | None:

        return self.session.query(Composer).filter(Composer.id == id).first()

