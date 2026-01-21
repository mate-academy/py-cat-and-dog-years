import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,cat_age_to_human_age,dog_age_to_human_age",
    [
        (-1, -1, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 28, 2, 2),
        (28, 29, 3, 3),
    ],
    ids=[
        "-1 cat/dog should return 0 human age",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age.",
    ]
)
def test_age_correct(cat_age: int,
                     dog_age: int,
                     cat_age_to_human_age: int,
                     dog_age_to_human_age: int) -> None:
    assert (get_human_age(cat_age, dog_age)
            == [cat_age_to_human_age, dog_age_to_human_age])


@pytest.mark.parametrize(
    "cat_age,dog_age, error_type",
    [
        (14, "14", TypeError),
        ("14", 14, TypeError),
        ("14", "14", TypeError),
    ],
    ids=[
        '14 and "14" should rise TypeError',
        '"14" and 14 should rise TypeError',
        '"14" and "14" should rise TypeError',
    ]
)
def test_error_correct(cat_age: int,
                       dog_age: int,
                       error_type: Exception) -> None:
    with pytest.raises(error_type):
        get_human_age(cat_age, dog_age)
