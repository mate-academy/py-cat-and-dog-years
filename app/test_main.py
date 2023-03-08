import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age ",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
)
def tests_get_human_age(cat_age, dog_age, human_age):
    assert get_human_age(cat_age, dog_age) == human_age, (
        f"Function should return {human_age}, "
        f"when cat age equal {cat_age} and dog age equal {dog_age} "
    )
