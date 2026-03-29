from sqlalchemy.orm import Session

from Backend.Models.UserWorkModel import UserWork
from Backend.Models.User.UserModel import User
from Backend.Models.Work.WorkModel import Work

class UserCRUD():

    def __init__(self, session: Session):
        self.session: Session = session

    def create_user_CRUD(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user
    
    def rate_work_CRUD(self, work_user: UserWork) -> UserWork:
        self.session.add(work_user)
        self.session.commit()
        self.session.refresh(work_user)

        return work_user
    
    def update_rating(self, user: User, work: Work, new_rating: int) -> None:
        user_work = (self.session.query(UserWork).filter_by(user_id=user.id, work_id=work.id).first())

        if not user_work:
            raise ValueError("Rating no encontrado")

        user_work.rating = new_rating
        self.session.commit()

    def get_rating_by_user_and_work(self, user: User, work: Work) -> int | None:
        user_work = (self.session.query(UserWork).filter_by(user_id=user.id, work_id=work.id).first())

        if user_work:
            return user_work.rating

        return None
    
    def search_user_by_id(self, id: int) -> User | None:
        return self.session.query(User).filter(User.id == id).first()

    def search_user_by_username(self, username: str) -> User | None:
        return self.session.query(User).filter(User.username == username).first()

    def search_user_by_email(self, email: str) -> User | None:
        return self.session.query(User).filter(User.email == email).first()
