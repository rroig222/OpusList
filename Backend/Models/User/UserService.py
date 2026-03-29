from Backend.Models.User.UserCRUD import UserCRUD
from Backend.utils import hash_password, verify_password
from Backend.Models.User.UserModel import User
from Backend.Models.Work.WorkModel import Work
from Backend.Models.User.UserCRUD import UserCRUD
from Backend.Models.UserWorkModel import UserWork

class UserService():

    def __init__(self, userCRUD: UserCRUD):

        self.userCRUD: UserCRUD = userCRUD

    def create_user_service(self, username: str, email: str, password: str) -> User:

        if self.userCRUD.search_user_by_email(email) or self.userCRUD.search_user_by_username(username):
            raise ValueError(f'Already existing user')
        
        else:

            psw_hash: str = hash_password(password=password)

            user: User = User(username=username, email=email, password_hash=psw_hash)

            self.userCRUD.create_user_CRUD(user)

            return user
        
    def check_user_login_service(self, username: str, password: str) -> User:

        user = self.userCRUD.search_user_by_username(username)

        if not user:
            raise ValueError(f'User not found.')
        
        else:
            if verify_password(password=password, password_hash=user.password_hash):
                return user
            else:
                raise ValueError('Incorrect password.')
            
    def rate_work_service(self, work: Work, user: User, rating: int) -> int:
        
        rate = self.userCRUD.get_rating_by_user_and_work(user=user, work=work)
        if rate:
            self.userCRUD.update_rating(user=user, work=work, new_rating=rating)
            return rate
        
        user_work_relation = UserWork(work=work, user=user, rating=rating)
        self.userCRUD.rate_work_CRUD(user_work_relation)

        