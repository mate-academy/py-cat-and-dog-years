import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age_by_cat_age",
    [
        pytest.param(
            3,
            4,
            0,
            id="when cat age < 15 it should give 0 human year"
        ),
        pytest.param(
            15,
            3,
            1,
            id="when 15 <= cat age < 24 it should give 1 human year"
        ),
        pytest.param(
            28,
            3,
            3,
            id="when cat age > 24 it should give 1 human year every 4 next cat years"
        )
    ]
)
def test_cat_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age_by_cat_age: int
) -> None:
    human_age_by_cat_age = get_human_age(cat_age=cat_age, dog_age=dog_age)[0]

    assert human_age_by_cat_age == expected_human_age_by_cat_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age_by_dog_age",
    [
        pytest.param(
            3,
            4,
            0,
            id="when dog age < 15 it should give 0 human year"
        ),
        pytest.param(
            15,
            23,
            1,
            id="when 15 <= dog age < 24 it should give 1 human year"
        ),
        pytest.param(
            28,
            28,
            2,
            id="when dog age > 24 it should give 1 human year every 5 next dog years"
        )
    ]
)
def test_dog_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age_by_dog_age: int
) -> None:
    human_age_by_dog_age = get_human_age(cat_age=cat_age, dog_age=dog_age)[1]

    assert human_age_by_dog_age == expected_human_age_by_dog_age


def test_human_age_with_incorrect_data_types() -> None:
    with pytest.raises(TypeError):
        get_human_age(None, "dog_age")
