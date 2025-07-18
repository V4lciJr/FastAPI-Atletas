from fastapi import FastAPI
from cross_api.routers import api_router

app = FastAPI(title="API-Cross FIT - API")
app.include_router(api_router)


if __name__ == "main":
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)