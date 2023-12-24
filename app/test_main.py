import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        pytest.param(
            14, 14, [0, 0],
            id="should return correct age if cat and dog age is under 15"
        ),
        pytest.param(
            15, 14, [1, 0],
            id="should return correct age if dog age is under 15"
        ),
        pytest.param(
            14, 15, [0, 1],
            id="should return correct age if cat age is under 15"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="should return 0 if animal age is 0"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="should return 0 if animal age is negative"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should work correct with big numbers"
        ),
        pytest.param(
            24, 39, [2, 5],
            id="should return correct age with random numbers"
        ),
        pytest.param(
            30, 30, [3, 3],
            id="should return correct age if cat and dog age is 30"
        ),
        pytest.param(
            45, 18, [7, 1],
            id="should return correct age with old cat and young dog"
        )
    ]
)
def test_get_correct_age(
        cat_age,
        dog_age,
        expected_human_age
):
    assert get_human_age(cat_age, dog_age) == expected_human_age
