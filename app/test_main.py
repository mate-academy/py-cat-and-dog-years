import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return 0 for 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return 0 for 14"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return first year for min accepted"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return first year for max accepted"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return second year for min accepted"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should return second year for max accepted"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return third year for cad and second year for dog"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should accept 100 year for cad and dog"
        ),
        pytest.param(
            -5,
            -10,
            [0, 0],
            id="should return zero if negative"
        )
    ]
)
def test_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_human_age_should_raise_type_error_for_invalid_input_value() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")
