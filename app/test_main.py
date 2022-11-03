import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,cat_dog_human_age",
    [
        (
            14, 14, [0, 0]
        ),
        (
            23, 23, [1, 1]
        ),
        (
            24, 24, [2, 2]
        ),
        (
            28, 28, [3, 2]
        ),
        (
            100, 100, [21, 17]
        )

    ]
)
def test_should_return_age_convert_to_human(cat_age: int,
                                            dog_age: int,
                                            cat_dog_human_age: list) -> None:
    age = get_human_age(cat_age, dog_age)

    assert age == cat_dog_human_age
