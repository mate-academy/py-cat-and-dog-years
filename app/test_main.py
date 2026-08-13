from typing import Any

import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_age",
    [
        pytest.param(0, 0, [0, 0], id="zero age gives 0 human years"),
        pytest.param(
            14, 14, [0, 0],
            id="14 cat and dog years give 0 human years"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="15 cat and dog years give 1 human year"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="23 cat and dog years still give 1 human year"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="24 cat and dog years give 2 human years"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="27 cat and dog years still give 2 human years"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="28 years give 3 human years for cat and 2 for dog"
        ),
        pytest.param(
            29, 29, [3, 3],
            id="29 cat and dog years give 3 human years"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="100 years give 21 human years for cat and 17 for dog"
        ),
        pytest.param(
            -10, -10, [0, 0],
            id="negative age gives 0 human years"
        ),
        pytest.param(
            1000000, 1000000, [249996, 199997],
            id="very large age is converted without overflow"
        ),
        pytest.param(
            100, 0, [21, 0],
            id="cat and dog ages are converted independently"
        ),
    ]
)
def test_should_convert_animal_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected_age: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("15", 15, id="string cat age raises TypeError"),
        pytest.param(15, None, id="none dog age raises TypeError"),
    ]
)
def test_should_raise_type_error_on_wrong_data_type(
        cat_age: Any,
        dog_age: Any
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
