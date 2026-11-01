import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 10),
        (10, "15"),
        (15.5, 10),
        (10, 15.5),
        (None, 10),
        (10, None),
        ([15], 10),
        (10, {"age": 15}),
    ],
    ids=[
        "string_cat_age",
        "string_dog_age",
        "float_cat_age",
        "float_dog_age",
        "none_cat_age",
        "none_dog_age",
        "list_cat_age",
        "dict_dog_age",
    ],
)
def test_get_human_age_raises_type_error_for_invalid_types(
    cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
