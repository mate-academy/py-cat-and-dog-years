import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,cat_and_dog_age_in_human",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        [24, 24, [2, 2]],
        [27, 27, [2, 2]],
        [28, 28, [3, 2]],
        [100, 100, [21, 17]]
    ],
    ids=[
        "zeros",
        "almost 1 human year",
        "1 human year after 15 animal",
        "almost 2 human year",
        "2 human year after 24 animal",
        "almost 3 human year",
        "human age for cat is one more than for dog when animals ages are 28",
        "human age equal two plus animal age divided by 4 for cat and by 5 for dog"
    ]
)
def test_non_negative_inputs_get_human_age(
        cat_age: int,
        dog_age: int,
        cat_and_dog_age_in_human: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == cat_and_dog_age_in_human


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("3", 7),
        ((3,), 7),
        (None, 7)
    ]
)
def test_type_err_exceptions(
        cat_age: int,
        dog_age: int,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
