from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="Cats and dogs under 15 years are 0 human years."
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="The age of a cat or dog should be equivalent to 1 human year."
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="The age of a cat or dog is equivalent to 2 human years."
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="Verify the third rule of age conversion for cats and dogs."
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Examine the lifespan of cats and dogs."
        )
    ],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
