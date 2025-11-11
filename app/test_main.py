import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0], id="both zero"),
        pytest.param(14, 14, [0, 0], id="below threshold"),
        pytest.param(15, 15, [1, 1], id="first threshold"),
        pytest.param(23, 23, [1, 1], id="just above first threshold"),
        pytest.param(24, 24, [2, 2], id="second threshold"),
        pytest.param(27, 27, [2, 2], id="between second and third"),
        pytest.param(28, 27, [3, 2], id="cat changes to 3"),
        pytest.param(28, 28, [3, 2], id="third threshold"),
        pytest.param(28, 29, [3, 3], id="dog changes to 3"),
        pytest.param(100, 100, [21, 17], id="large numbers"),
    ]
)
def test_get_human_age_boundary_nums(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(-1, 10, [0, 0], id="negative cat"),
        pytest.param(10, -5, [0, 0], id="negative dog"),
        pytest.param(-3, -3, [0, 0], id="both negative"),
    ]
)
def test_get_human_age_negative(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param(10, "dog", id="string dog"),
        pytest.param("cat", "dog", id="both invalid"),
    ]
)
def test_get_human_age_only_int(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
