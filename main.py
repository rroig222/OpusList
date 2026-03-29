from GUI.Windows.Auth.Login import LoginWindow
from GUI.Windows.User.Dashboard import DashboardWindow
from Backend.DataBase.DB_initializer import Base, engine

import customtkinter as ctk

from Connector_API.dataclasses import User as ModelUser

from Backend.Models.User.UserModel import User
from Backend.Models.Composer.ComposerModel import Composer
from Backend.Models.Work.WorkModel import Work
from Backend.Models.UserWorkModel import UserWork

from Connector_API.Connectors.UserConector import UserConector

def create():
    Base.metadata.create_all(engine)

if __name__=="__main__":
    user_conector = UserConector()
    create()
    ctk.set_appearance_mode("light")
    LoginWindow(user_conector=user_conector)

