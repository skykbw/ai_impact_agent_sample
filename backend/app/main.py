from fastapi import FastAPI

from app.api.router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="영어 공부 B/E 과제 샘플 API",
        description="AI 도입 전후 생산성/품질 효과 분석용 샘플 API",
        version="0.1.0",
    )
    app.include_router(api_router)
    return app


app = create_app()
