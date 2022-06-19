from fastapi import FastAPI
import app.state

def init_routers(app: FastAPI) -> None:
    ...

def init_events(f_app: FastAPI) -> None:
    @f_app.on_event("startup")
    async def on_startup() -> None:
        await app.state.database.create_mysql_pool()

def init_app() -> FastAPI:
    f_app = FastAPI(
        title= "Weimar",
        description= "The modern Bancho implementation for the RealistikOsu stack.",
        docs_url= None,
        openapi_url= None,
    )
    
    init_events(f_app)
    init_routers(f_app)
    
    return f_app

fastapi_app = init_app()
