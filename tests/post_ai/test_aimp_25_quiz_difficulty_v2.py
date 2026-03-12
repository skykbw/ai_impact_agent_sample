from fastapi import HTTPException

from app.features.aimp_25_quiz_difficulty_v2 import evaluate


def test_evaluate_success() -> None:
    result = evaluate({"base": 80})
    assert result.issue == "AIMP-25"
    assert result.score == 0.8
    assert result.quality_flag == "stable"


def test_evaluate_non_int() -> None:
    try:
        evaluate({"base": "bad"})  # type: ignore[arg-type]
        raise AssertionError("예외가 발생해야 합니다.")
    except HTTPException as exc:
        assert exc.status_code == 400


def test_evaluate_negative() -> None:
    try:
        evaluate({"base": -1})
        raise AssertionError("예외가 발생해야 합니다.")
    except HTTPException as exc:
        assert exc.status_code == 400
