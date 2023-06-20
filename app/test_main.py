import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        pytest.param(
            -3, -4, [0, 0],
            id="dog and cat ages lesser than 0 should return 0 human years"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="first dog and cat ages should return 0 human years"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="dog and cat ages lesser than 15 should return 0 human years"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="dog and cat ages from 15 to 24 should return 1 human years"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="dog and cat ages from 15 to 24 should return 1 human years"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="dog and cat ages after 23 should return calculated human years"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="dog and cat ages after 23 should return calculated human years"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="dog and cat ages after 23 should return calculated human years"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="dog and cat ages after 23 should return calculated human years"
        ),
        pytest.param(
            999999999999999999999999999, 9999999999999999999999999,
            [249999999999999999999999995, 1999999999999999999999997],
            id="dog and cat ages after 23 should return calculated human years"
        )
    ]
)
def test_convert_dog_and_cat_ages_in_human_age(
        cat_age: int, dog_age: int, expected_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(
            [10, 10], 100,
            id="cat and dog age should be integer"
        ),
        pytest.param(
            "100", 100,
            id="dog and cat ages should be integer"
        )
    ]
)
def test_get_human_age_with_wrong_data_type(
        cat_age: int, dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
