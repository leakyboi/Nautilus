from fastapi import FastAPI

def init_routers(app: FastAPI) -> None:
    ...

def init_events(app: FastAPI) -> None:
    @app.on_event("startup")
    async def on_startup() -> None:
        ...

def init_app() -> FastAPI:
    app = FastAPI(
        title= "Weimar",
        description= "The modern Bancho implementation for the RealistikOsu stack.",
        docs_url= None,
        openapi_url= None,
    )
    
    init_events(app)
    init_routers(app)
    
    return app

fastapi_app = init_app()
