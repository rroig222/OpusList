from sqlalchemy.orm import Session

from Backend.Models.Work.WorkModel import Work
from Backend.Models.Composer.ComposerModel import Composer

class WorkCRUD():

    def __init__(self, session: Session):
        self.session: Session = session

    def create_work(self, work: Work) -> Work:
        self.session.add(work)
        self.session.commit()
        self.session.refresh(work)

        return work
    
    def get_work_by_id(self, id: int) -> Work | None:
        return self.session.query(Work).filter(Work.id == id).first()

    def get_work_by_openopus_id(self, openopus_id: int) -> Work | None:
        return self.session.query(Work).filter(Work.openopus_id == openopus_id).first()
    
    def search_work_by_title(self, query: str) -> list[Work] | None:
        results = self.session.query(Work).filter(Work.title.ilike(f"%{query}%")).all()
        
        if results:
            return results
        else:
            return None
        
    def search_work_by_composer(self, query: str) -> list[Work] | None:
        results =     self.session.query(Work).join(Work.composer).filter(Composer.name.ilike(f"%{query}%"))

        if results:
            return results
        else:
            return None