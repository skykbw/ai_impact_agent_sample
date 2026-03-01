from fastapi import HTTPException

from app.features.aimp_16_ai_prompt_template import evaluate


def test_evaluate_success() -> None:
    result = evaluate({"base": 80})
    assert result.issue == "AIMP-16"
    assert result.score == 0.8


def test_evaluate_negative_base() -> None:
    try:
        evaluate({"base": -1})
        raise AssertionError("예외가 발생해야 합니다.")
    except HTTPException as exc:
        assert exc.status_code == 400
