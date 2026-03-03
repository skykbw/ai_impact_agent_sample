\"\"\"
System.Collections.Hashtable.key - 스키마/DTO 정리 리팩터링
phase: post_ai
작업일자: 2026-03-03T12:00:00+09:00
\"\"\"

from dataclasses import dataclass
from typing import Final

from fastapi import APIRouter, HTTPException

router = APIRouter()
MAX_SCORE: Final[float] = 1.0


@dataclass(frozen=True)
class FeatureResult:
    issue: str
    score: float
    detail: str


def evaluate(payload: dict[str, int]) -> FeatureResult:
    base = payload.get("base", 0)
    if base < 0:
        raise HTTPException(status_code=400, detail="base는 0 이상이어야 합니다.")

    score = min(base / 100.0, MAX_SCORE)
    return FeatureResult(issue="AIMP-18", score=round(score, 2), detail="ok")


@router.post("/schema-refactor/evaluate")
def evaluate_endpoint(payload: dict[str, int]) -> dict[str, str | float]:
    result = evaluate(payload)
    return {"issue": result.issue, "score": result.score, "detail": result.detail}


@router.get("/schema-refactor/health")
def health() -> dict[str, str]:
    return {"issue": "AIMP-18", "status": "ok", "phase": "post_ai"}
