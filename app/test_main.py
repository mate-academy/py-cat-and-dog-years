import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat, dog, result",
    [
        pytest.param(23, 23, [1, 1],
                     id="should convert into 1 human age"),
        pytest.param(24, 24, [2, 2],
                     id="should convert into 2 human age"),
        pytest.param(0, 0, [0, 0],
                     id="should return 0 if if input values are 0"),
        pytest.param(-1, -2, [0, 0],
                     id="should return 0 if if input values are less than 0"),
        pytest.param(14, 14, [0, 0],
                     id="check for cat age - 14 and dog age - 14"),
        pytest.param(15, 15, [1, 1],
                     id="check for cat age - 15 and dog age - 15"),
        pytest.param(27, 27, [2, 2],
                     id="check for cat age - 27 and dog age - 27"),
        pytest.param(28, 28, [3, 2],
                     id="check for cat age - 28 and dog age - 28"),
        pytest.param(100, 100, [21, 17],
                     id="check for cat age - 100 and dog age - 100"),
        pytest.param(1_000_000, 1_000_000, [249996, 199997],
                     id="check for large numbers")

    ]
)
def test_should_convert_into_human_age(
        cat: int,
        dog: int,
        result: list
) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize(
    "cat, dog, expected_error",
    [
        pytest.param("3",
                     "age",
                     TypeError,
                     id="should raise error when cat or dog age is string")
    ]
)
def test_raising_errors_correctly(
        cat: int,
        dog: int,
        expected_error: list
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat, dog)
