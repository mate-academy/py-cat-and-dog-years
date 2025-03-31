import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (50, 50, [8, 7]),
        (24, 24, [2, 2]),
        (23, 25, [1, 2]),
        (27, 25, [2, 2]),
        (0, 0, [0, 0]),
        (-10, -20, [0, 0]),
        (1000, 1000, [246, 197]),
        (15.5, 15.5, [1, 1]),
    ],
    ids=[
        "14 cat/dog years -> 0 human age",
        "15 cat/dog years -> 1 human age",
        "50 cat years -> 8 human, 50 dog years -> 7 human",
        "24 cat/dog years should convert into 2 human age.",
        "23 cat -> 1 human, 25 dog -> 2 human",
        "27 cat -> 2 human, 25 dog -> 2 human",
        "No age -> 0 human age",
        "Negative age -> 0 human age",
        "Very large age -> high human age",
        "Fractional boundary -> correct rounding",
    ],
)
def test_check_age_converting(cat_age: int, dog_age: int,
                              result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
