from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from app import routes

app = FastAPI()

app.include_router(routes.router, prefix="/api", tags=["api"])

@app.get("/")
def root():
    # redireciona automaticamente para /docs
    return RedirectResponse(url="/docs")
