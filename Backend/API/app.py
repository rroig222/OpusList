from fastapi import FastAPI
from Backend.API.Routers.UserRouter import router as user_router
from Backend.API.Routers.WorkRouter import router as work_router
from Backend.API.Routers.ComposerRouter import router as composer_router

app = FastAPI(title="OpusList API")

app.include_router(user_router)
app.include_router(work_router)
app.include_router(composer_router)