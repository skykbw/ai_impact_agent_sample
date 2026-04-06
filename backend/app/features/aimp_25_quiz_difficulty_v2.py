\"\"\"
System.Collections.Hashtable.key - AI 기반 퀴즈 난이도 조절 로직 개선
phase: post_ai
작업일자: 2026-03-12T10:00:00+09:00
\"\"\"

from dataclasses import dataclass
from typing import Final

from fastapi import APIRouter, HTTPException

router = APIRouter()
MAX_SCORE: Final[float] = 1.0
MIN_SCORE: Final[float] = 0.0


@dataclass(frozen=True)
class QualityResult:
    issue: str
    score: float
    quality_flag: str


def evaluate(payload: dict[str, int]) -> QualityResult:
    base = payload.get("base", 0)
    if not isinstance(base, int):
        raise HTTPException(status_code=400, detail="base는 정수여야 합니다.")
    if base < 0:
        raise HTTPException(status_code=400, detail="base는 0 이상이어야 합니다.")

    score = min(max(base / 100.0, MIN_SCORE), MAX_SCORE)
    quality_flag = "stable" if score >= 0.7 else "review_needed"
    return QualityResult(issue="AIMP-25", score=round(score, 2), quality_flag=quality_flag)


@router.post("/quiz_difficulty_v2/evaluate")
def evaluate_endpoint(payload: dict[str, int]) -> dict[str, str | float]:
    result = evaluate(payload)
    return {"issue": result.issue, "score": result.score, "quality_flag": result.quality_flag, "phase": "post_ai"}


@router.get("/quiz_difficulty_v2/health")
def health() -> dict[str, str]:
    return {"status": "ok", "issue": "AIMP-25", "phase": "post_ai"}
