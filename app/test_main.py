import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_for_cat,human_age_for_dog",
    pytest.param(16, 17, 1, 1, id="first human year for dogs and cats"),
    pytest.param(25, 26, 2, 2, id="second human year for dogs and cats"),
    pytest.param(29, 29, 3, 3, id="third human year for dogs and cats"),
)
def test_firsts_cats_and_dogs_years_in_human_age(
        cat_age: int,
        dog_age: int,
        human_age_for_cat: int,
        human_age_for_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [human_age_for_cat, human_age_for_dog]


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_for_cat,human_age_for_dog",
    pytest.param(28, 29, 3, 3, id="tree-years cat and dog"),
    pytest.param(32, 34, 4, 4, id="four-years cat and dog"),
    pytest.param(36, 39, 5, 5, id="five-years cat and dog"),
)
def test_different_in_dogs_and_cats_age_but_same_human_age(
        cat_age: int,
        dog_age: int,
        human_age_for_cat: int,
        human_age_for_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [human_age_for_cat, human_age_for_dog]


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_for_cat,human_age_for_dog",
    pytest.param(28, 28, 3, 2, id="tree-years cat and two-years dog"),
    pytest.param(32, 33, 4, 3, id="four-years cat and three-years dog"),
    pytest.param(36, 38, 5, 4, id="five-years cat and four-years dog"),
)
def test_same_in_dogs_and_cats_age_but_different_in_human_age(
        cat_age: int,
        dog_age: int,
        human_age_for_cat: int,
        human_age_for_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [human_age_for_cat, human_age_for_dog]


def test_cat_age_equals_zero() -> None:
    assert get_human_age(cat_age=0, dog_age=1) == [0, 15], \
        "When age cat = 0 and age dog = 1 its animals year are 0 and 15"


def test_dog_age_equals_zero() -> None:
    assert get_human_age(cat_age=2, dog_age=0) == [24, 0], \
        "When age cat = 2 and age dog = 0 its animals year are 24 and 15"


def test_cat_and_dog_age_equals_zero() -> None:
    assert get_human_age(cat_age=0, dog_age=0) == [0, 0], \
        "When age cat = 2 and age dog = 0 its animals year are 24 and 15"


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_for_cat,human_age_for_dog",
    pytest.param(1, 1, 0, 0, id="tree-years cat and two-years dog"),
    pytest.param(5, 5, 0, 0, id="four-years cat and three-years dog"),
    pytest.param(14, 13, 0, 0, id="five-years cat and four-years dog"),
)
def test_zero_human_age(
        cat_age: int,
        dog_age: int,
        human_age_for_cat: int,
        human_age_for_dog: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [human_age_for_cat, human_age_for_dog]
