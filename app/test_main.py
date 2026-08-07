import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15, "15"),
        (None, 15),
        (15, None),
    ],
)
def test_get_human_age_with_incorrect_type(
    cat_age: int | str | None,
    dog_age: int | str | None,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
