import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return 0 when the age of the cat and dog is 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="If a dog and cat are under 14 years old, that's 0 human years"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 dog and cat years is 1 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 dog and cat years is still 1 human year"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24 dog and cat years - 2 human years"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="28 dog and 29 cat years - 3 human years"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Life expectancy test"
        ),
        # pytest.param(
        #     15,
        #     None,
        #     TypeError,
        #     id="should return 'TypeError' when pet age isn't 'int'"
        # ),
        pytest.param(
            -2,
            -1,
            [0, 0],
            id="should return 0 when ages are negative"
        ),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_if_data_is_wrong_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", ["dog"])
