import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,age_list", [
        (0, 0, [0, 0]),
        (14, 15, [0, 1]),
        (24, 23, [2, 1]),
        (27, 27, [2, 2]),
        (100, 100, [21, 17]),
        (-67, -3, [0, 0])
    ],
    ids=[
        "age_equals_zero",
        "age_equals_14_15",
        "age_equals_24_23",
        "age_equals_27_27",
        "age_equals_100_100",
        "age_equals_negative_value"
    ]
)
def test_if_get_human_age_returns_correct_value(
    cat_age: int,
    dog_age: int,
    age_list: list
) -> None:
    assert (get_human_age(cat_age, dog_age) == age_list
            ), (f"Cat age({cat_age}) and dog age({dog_age})"
                f" in human years should be equal to {age_list}")


def test_type_error_get_human_age() -> None:
    with pytest.raises(TypeError):
        get_human_age("2", "3")
