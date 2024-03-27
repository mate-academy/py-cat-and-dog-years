import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "value1,value2,result",
    [
        (-3, -3, [0, 0]),
        (14, 14, [0, 0]),
        (16, 16, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17]),
        (32, 94, [4, 16])
    ]
)
def test_gethuman_age(value1: int, value2: int, result: list) -> None:
    assert get_human_age(value1, value2) == result


@pytest.mark.parametrize(
    "value1,value2",
    [
        ([1], [2]),
        ((1), (2)),
        ({1: 2}, {1: 2}),
        ({1}, {2}),
        ("a", "b"),
        (None, None)
    ]
)
def test_not_supported_type_of_data(
    value1: list | tuple | dict | set | str | None,
    value2: list | tuple | dict | set | str | None,
) -> None:
    with pytest.raises(TypeError):
        get_human_age("a", "b")
