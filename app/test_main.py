import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,exp_human_age",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (128, 129, [28, 23]),
        (99999, 99999, [24995, 19997]),
    ]
)
def test_human_age_boundaries(
    cat_age: int,
    dog_age: int,
    exp_human_age: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == exp_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,exp_exception",
    [
        # (14.0, 16, True),
        # (14, 16.0, True),
        (15, "15", True),
        ("15", 15, True),
        # (True, 15, True),
        # (15, True, True),
        # ([15], 15, True),
        # 15, [15], True),
        ({"age": 15}, 29, True),
        (15, {"age": 15}, True),
        # ((15), 15, True),
        # (15, (15), True),
        (15, 15, False)
    ]
)
def test_incorrect_type_raises_exception(
    cat_age: any,
    dog_age: any,
    exp_exception: bool
) -> None:
    try:
        get_human_age(cat_age, dog_age)
    except TypeError:
        assert exp_exception
    except Exception:
        assert not exp_exception
