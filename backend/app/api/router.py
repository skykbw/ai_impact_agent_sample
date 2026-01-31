from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/health", summary="헬스 체크")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
