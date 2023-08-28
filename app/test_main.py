import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            -3, -3, [0, 0], id="negative age should give list with zeros"
        ),
        pytest.param(
            0, 0, [0, 0], id="zero age should give list with zeros"
        ),
        pytest.param(
            1200, 1200, [296, 237], id="big ages"
        ),
        pytest.param(
            14, 14, [0, 0], id="pet's age is less than 1 human's year"
        ),
        pytest.param(
            15, 15, [1, 1], id="14 pet years equals 1 human year"
        ),
        pytest.param(
            23, 23, [1, 1], id="15 pet years equals 1 human year"
        ),
        pytest.param(
            24, 24, [2, 2], id="24 pet years equals 2 human years"
        ),
        pytest.param(
            27, 27, [2, 2], id="27 pet years equals 2 human year"
        ),
        pytest.param(
            28, 28, [3, 2], id="28 cat years equals 3 human year and "
                               "28 dog years equals 2 human year"
        ),
        pytest.param(
            29, 29, [3, 3], id="29 pet years equals 3 human years"
        ),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("1", 1),
        (23, "23"),
        (300, [300]),
    ]
)
def test_correct_param(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
