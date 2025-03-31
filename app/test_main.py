from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cats_and_dogs_ages, after_transformation",
    [
        pytest.param(
            (14, 14), [0, 0],
            id="get human age cat dog below threshold"
        ),
        pytest.param(
            (15, 15), [1, 1],
            id="get human age cat dog at first threshold"
        ),
        pytest.param(
            (23, 23), [1, 1],
            id="get human age cat dog between thresholds"
        ),
        pytest.param(
            (24, 24), [2, 2],
            id="get human age cat dog between thresholds"
        ),
        pytest.param(
            (27, 27), [2, 2],
            id="get human age cat dog between second and third thresholds"
        ),
        pytest.param(
            (28, 28), [3, 2],
            id="get human age cat dog at third threshold"
        ),
        pytest.param(
            (100, 100), [21, 17],
            id="get human age cat dog large values"
        )
    ]
)
def test_result_equal_to_expected(
        cats_and_dogs_ages: tuple,
        after_transformation: list[int]
) -> None:
    assert get_human_age(
        cats_and_dogs_ages[0],
        cats_and_dogs_ages[1]) == after_transformation


def test_the_inputs_must_be_integer() -> None:
    with pytest.raises(TypeError):
        assert isinstance(get_human_age("Sam", "Nick")[1], int)
        assert isinstance(get_human_age("24", "24")[0], int)


def test_negative_numbers() -> None:
    assert get_human_age(-13, -19) == [0, 0]
