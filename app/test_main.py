from app.main import get_human_age

import pytest


@ pytest.mark.parametrize(
    "cat_age,dog_age,expected_ages",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return '[0, 0]' when ages are '0'"
        ),
        pytest.param(
            -10,
            -10,
            [0, 0],
            id="should return '[0, 0]' when ages are negative",
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return '[0, 0]' when ages are less than '15'",
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return '[1, 1]' when ages are '15'"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should return '[1, 1]' when "
               "ages are more than '15' but less than '24'",
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should return '[2, 2]' when ages are '24'"
        ),
        pytest.param(
            27,
            24,
            [2, 2],
            id="should return '[2, 2]' when: "
               "cat_age are 27 and dog_age = 24",
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should return '[3, 2]' when: "
               "cat_age are 28 and dog_age = 28",
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="should return '[3, 3]' when: "
               " cat_age are 28 and dog_age = 29",
        ),
        pytest.param(
            1000,
            1000,
            [246, 197],
            id="should return '[246, 197]' when ages are '1000'",
        ),
    ],
)
def test_converting_ages_correct(
        cat_age: int, dog_age: int, expected_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_ages


@pytest.mark.parametrize("cat_age,dog_age", [pytest.param("one", [1, 12, 3])])
def test_raising_errors_correctly(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
