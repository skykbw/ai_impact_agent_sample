\"\"\"
System.Collections.Hashtable.key - pytest 기반 API 테스트 초안 추가
phase: pre_ai
작업일자: 2026-02-13T10:00:00+09:00
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


@router.post("/pytest_draft/run")
def run(payload: dict):
    base = payload.get("base", 0)
    score = calc(base)
    return {"issue":"AIMP-13","score":score,"phase":"pre_ai"}


@router.get("/pytest_draft/health")
def health():
    return {"status":"ok","issue":"AIMP-13"}
