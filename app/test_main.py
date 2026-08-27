import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="cat and dog age == 0, so output should be 0"
        ),

        pytest.param(
            14,
            20,
            [0, 1],
            id="cat age == 14, cat output should be 0"
        ),
        pytest.param(
            15,
            20,
            [1, 1],
            id="cat age == 15, cat output should be 1"
        ),
        pytest.param(
            23,
            20,
            [1, 1],
            id="cat age == 23, cat output should still be 1"
        ),
        pytest.param(
            24,
            20,
            [2, 1],
            id="cat age == 24, cat output should be 2"
        ),
        pytest.param(
            27,
            20,
            [2, 1],
            id="cat age == 27, cat output should still be 2"
        ),
        pytest.param(
            28,
            20,
            [3, 1],
            id="cat age == 28, cat output should be 3"
        ),

        pytest.param(
            20,
            14,
            [1, 0],
            id="dog age == 14, dog output should be 0"
        ),
        pytest.param(
            20,
            15,
            [1, 1],
            id="dog age == 15, dog output should be 1"
        ),
        pytest.param(
            20,
            23,
            [1, 1],
            id="dog age == 23, dog output should still be 1"
        ),
        pytest.param(
            20,
            24,
            [1, 2],
            id="dog age == 24, dog output should be 2"
        ),
        pytest.param(
            20,
            28,
            [1, 2],
            id="dog age == 28, dog output should still be 2"
        ),
        pytest.param(
            20,
            29,
            [1, 3],
            id="dog age == 29, dog output should be 3"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="output should be 21 for cat and 17 for dog"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="cat and dog age == 14, so output should be 0"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="cat and dog age == 15, so output should be 1"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="cat and dog age == 23, so output should be 1"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="cat and dog age == 24, so output should be 2"
        ),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            -1,
            5,
            ValueError,
            id="negative cat age, raise ValueError"
        ),
        pytest.param(
            5,
            -1,
            ValueError,
            id="negative dog age, raise ValueError"
        ),
        pytest.param(
            1000,
            5,
            ValueError,
            id="unrealistic large cat age, raise ValueError"
        ),
        pytest.param(
            5,
            1000,
            ValueError,
            id="unrealistic large dog age, raise ValueError"
        ),
        pytest.param(
            "10",
            2,
            TypeError,
            id="incorrect cat age type, raise TypeError"
        ),
        pytest.param(
            10,
            2.1,
            TypeError,
            id="incorrect dog age type, raise TypeError"
        ),
    ],
)
def test_raise_correct_exception(
        cat_age: int,
        dog_age: int,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
