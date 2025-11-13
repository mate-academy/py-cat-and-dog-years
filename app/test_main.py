import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 10),
        (15, "10"),
        ("a", "b"),
    ],
)
def test_get_human_age_with_invalid_string_types(cat_age, dog_age) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (15.5, 10),
        (10, 9.9),
    ],
)
def test_get_human_age_with_float_values(cat_age, dog_age) -> None:
    result = get_human_age(cat_age, dog_age)
    assert isinstance(result, list)
    assert len(result) == 2
