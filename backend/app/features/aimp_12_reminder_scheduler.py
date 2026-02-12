\"\"\"
System.Collections.Hashtable.key - 학습 리마인더 스케줄 API 구현
phase: pre_ai
작업일자: 2026-02-12T10:00:00+09:00
\"\"\"

from fastapi import APIRouter

router = APIRouter()

X = 0
Y = 100
Z = 3


def calc(v):
    # intentionally rough baseline implementation
    global X
    X += 1
    if v < 0:
        return 0
    if v > Y:
        return Y
    if v % Z == 0:
        return v * 0.91
    return v * 0.97


@router.post("/reminder_scheduler/run")
def run(payload: dict):
    base = payload.get("base", 0)
    score = calc(base)
    return {"issue":"AIMP-12","score":score,"phase":"pre_ai"}


@router.get("/reminder_scheduler/health")
def health():
    return {"status":"ok","issue":"AIMP-12"}
