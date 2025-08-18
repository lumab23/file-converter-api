from fastapi import FastAPI 
from fastapi.responses import RedirectResponse
from app import routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router, prefix="/api", tags=["api"])

@app.get("/")
def root():
    # redireciona automaticamente para /docs
    return RedirectResponse(url="/docs")
