import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(0, 0, [0, 0], id="start_all_first_boundary"),
        pytest.param(14, 14, [0, 0], id="finish_all_first_boundary"),
        pytest.param(15, 15, [1, 1], id="start_all_second_boundary"),
        pytest.param(23, 23, [1, 1], id="finish_all_second_boundary"),
        pytest.param(24, 24, [2, 2], id="start_all_three_boundary"),
        pytest.param(27, 27, [2, 2], id="finish_cat_three_boundary"),
        pytest.param(28, 28, [3, 2],
                     id="start_cat_four_boundary_finish_dog_three_boundary"),
        pytest.param(29, 29, [3, 3], id="start_dog_four_boundary"),
        pytest.param(100, 100, [21, 17], id="100_age"),
    ]
)
def test_get_human_age_start_all_first_boundary(cat_age: int,
                                                dog_age: int,
                                                human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_age_cat_or_dog_must_be_positive() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, 0)


def test_age_cat_or_dog_must_be_int() -> None:
    with pytest.raises(TypeError):
        get_human_age(1, True)
