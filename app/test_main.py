from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            15,
            14,
            [1, 0],
            id="15 years dog/cat is 1 year human"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 years dog/cat is 2 year human"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28/29 cat/dogs years is 3 years human"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="every next 4/5 years cat/dog is 1 extra human year"
        ),
    ]
)
def test_modify_convert_to_human(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
