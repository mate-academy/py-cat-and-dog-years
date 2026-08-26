import pytest

from app.main import get_human_age

TEST_CASES = [
    (0, 0, [0, 0], "zero age gives zero human years for both"),
    (14, 14, [0, 0], "one year below the first threshold stays at 0"),
    (15, 15, [1, 1], "first threshold (15) gives 1 human year"),
    (23, 23, [1, 1], "one year below the second threshold stays at 1"),
    (24, 24, [2, 2], "second threshold (15+9=24) gives 2 human years"),
    (27, 27, [2, 2], "one year below cat's next step stays at 2"),
    (28, 28, [3, 2], "cat steps up every 4 years (24+4=28), dog not yet"),
    (29, 29, [3, 3], "dog steps up every 5 years (24+5=29)"),
    (100, 100, [21, 17], "large ages are handled correctly"),
    (0, 15, [0, 1], "cat and dog ages are converted independently"),
    (15, 0, [1, 0], "arguments are not swapped internally"),
]


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [case[:3] for case in TEST_CASES],
    ids=[case[3] for case in TEST_CASES],
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
