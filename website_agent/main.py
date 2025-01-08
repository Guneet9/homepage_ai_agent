from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ai_agent_route import analysis_router

app = FastAPI(title="FastAPI AI Agent for Website Scraping")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the AI Agent for Website Scraping!"}

@app.get("/test", tags=["Test"])
async def test_route():
    return {"message": "Test route works!"}



