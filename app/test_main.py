import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            14, 14, [0, 0],
            id="should return 0 when dog/cat years lower than 15"
        ),
        pytest.param(
            16, 16, [1, 1],
            id="should add 1 when (15 <= dog/cat years < 24)"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="should add 1 to cat years for next 4 cat years"
        ),
        pytest.param(
            27, 29, [2, 3],
            id="should add 1 to dog years for next 5 dog years"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should return when animals have 100 years"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="should return 0 when age < 0"
        )
    ]
)
def test_get_human_age_values(
        cat_age: int,
        dog_age: int,
        human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age

@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("25", 0, id="string cat age"),
        pytest.param(15, "0", id="string dog age"),
        pytest.param(None, None, id="None values")
    ]
)
def test_get_human_age_types(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)