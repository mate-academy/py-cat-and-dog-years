import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "for 0 years cat and dog 0",
        "for 14 years cat and dog similar",
        "for 15 years cat and dog similar",
        "for 23 years cat and dog similar all +1 year",
        "for 24 years cat and dog similar all +1 year",
        "for 27 years cat and dog similar all +1 year",
        "for 28 years cat +1 and dog different all +1 year",
        "for 100 years cat +1 and dog different all +1 year"
    ]
)
def test_first(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result
