import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat,dog,result",
    [
        (0, 0, [0, 0]),
        (-27, -15, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (10000, 10000, [2496, 1997])
    ],
    ids=[
        "should return [0, 0] age for cat:0 and dog:0",
        "should return [0, 0] age for cat:-27 and dog:-15",
        "should return [0, 0] age for cat:14 and dog:14",
        "should return [1, 1] age for cat:15 and dog:15",
        "should return [1, 1] age for cat:23 and dog:23",
        "should return [2, 2] age for cat:24 and dog:24",
        "should return [2, 2] age for cat:27 and dog:27",
        "should return [3, 2] age for cat:28 and dog:28",
        "should return [3, 3] age for cat:22 and dog:22",
        "should return [2496, 1997] age for cat:10000 and dog:10000",

    ]
)
def test_convert_to_human(cat: int, dog: int, result: list) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize(
    "cat,dog",
    [
        ("dog", "cat"),
        ([], ()),
        (14, "12"),
    ]
)
def test_convert_to_human_if_input_not_int(cat: str, dog: str) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
