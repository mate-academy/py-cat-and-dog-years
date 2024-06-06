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
def test_non_negative_inputs_get_human_age(cat_age, dog_age, cat_and_dog_age_in_human) -> None:
    assert get_human_age(cat_age, dog_age) == cat_and_dog_age_in_human


def test_negative_inputs_get_human_age() -> None:
    expected_value = [0, 0]
    assert get_human_age(-3, -9) == expected_value
