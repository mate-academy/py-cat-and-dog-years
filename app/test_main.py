import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
    ],
    ids=[
        "Converts zeros to zeros",
        "Converts both ages to zero when: age < 15",
        "Converts both ages to 1 when age == 15",
        "Next 9 years should add 1 to both ages",
        "Next 4 years should add 1 to cat years",
        "Next 5 years should add 1 to dog years",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result
