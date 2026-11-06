import  pytest

from app.main import get_human_age

@pytest.mark.parametrize(
    "cat_age,dog_age,human_age_for_cat,human_age_for_dog",
    [
        (0, 0, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (28, 28, 3, 2),
        (100, 100, 21, 17)
    ]
)
def test_check_age(cat_age, dog_age, human_age_for_cat, human_age_for_dog):
    assert get_human_age(cat_age, dog_age) == [human_age_for_cat, human_age_for_dog]

@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        # pytest.param(0, 0, id="cannot be zero"),
        pytest.param(-1, -1, id="cannot be negative"),
        # pytest.param(201, 201, id="cannot be larger than 200")
    ]
)

def test_cannot_be_negative_or_zero_or_larger_than_200(cat_age, dog_age) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "wrong_value",
    [
        "15",
        15.5,
        None,
        [],
        {},
    ]
)


def test_cat_age_has_wrong_type(wrong_value):
    with pytest.raises(TypeError):
        get_human_age(wrong_value, 15)


def test_dog_age_has_wrong_type(wrong_value):
    with pytest.raises(TypeError):
        get_human_age(15, wrong_value)
