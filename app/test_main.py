import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (40, 20, [6, 1]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-2, -5, [0, 0])
    ]
)
def test_modify(cat_age: int, dog_age: int, result: list) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        ("String", ("A", [1, 2, 3], False), TypeError),
        ({dict}, {1, 2, 3}, TypeError)
    ]
)
def test_incorrect_value(cat_age: int, dog_age: int, result: callable) -> None:
    try:
        expected = get_human_age(cat_age, dog_age)
        assert expected == result
    except Exception as e:
        assert isinstance(e, result)


if __name__ == "__main__":
    pytest.main()
