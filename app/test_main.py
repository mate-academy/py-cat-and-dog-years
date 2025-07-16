import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_ages",
    [
        pytest.param(
            14, 14, [0, 0], id="bounded test with animal's age = 0"
        ),
        pytest.param(
            23, 23, [1, 1], id="bounded test with animal's age = 1"
        ),
        pytest.param(
            27, 28, [2, 2], id="bounded test with animal's age = 2"
        ),
        pytest.param(
            -14, -5, [0, 0], id="Negative values for animal age"
        ),
        (
            0, 0, [0, 0]
        ),
        (
            1000, 1000, [246, 197]
        )
    ]
)
def test_get_human_age_bounded_values(
        cat_age: int,
        dog_age: int,
        expected_ages: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_ages


def test_get_human_age_data_out_of_normal_range() -> None:
    with pytest.raises(TypeError):
        assert get_human_age("12", 12)
