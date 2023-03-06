import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age,result",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (14.489, 14.789, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (23.6848, 23.159, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17])
    ],
    ids=[
        "negative animal years",
        "zero age in animals years - zero age in human years",
        "non zero age in animals years - zero age in human years",
        "float non zero age in animals years - zero age in human years",
        "get first human year",
        "get first human year upper value",
        "float animals years for first human year(upper value)",
        "get second human year",
        "get second human year upper value",
        "get third human year for cat and dog age value",
        "multiply extra human years"
    ]
)
def test_can_sum(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result, (
        f"Result of func for cat_age={cat_age} and dog_age={dog_age} "
        f"should be equal to {result}"
    )


def test_raise_type_error_if_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("100", "100")
