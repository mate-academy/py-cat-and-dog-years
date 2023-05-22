import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (-1, -1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (1000, 1000, [246, 197])
    ],
    ids=[
        "Should return zeros for negative animal ages",
        "Should return zeros up to fourteen animal years",
        "First incrementing of age after fifteen animal years",
        "Should return ones up to 23 animal years",
        "Second incrementing of age after 24 animal years",
        "Third incrementing of 'human-cat' age at cat's 28",
        "Third incrementing of 'heman-dog' age at dog's 29",
        "Should work correct for really old animals"
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"cat {cat_age}, dog {dog_age} = {result}"


def test_cannot_operate_not_int_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("3", [4])
