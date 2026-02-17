import pytest
import app.main as main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "0 cat/dog years -> 0 human age",
        "14 cat/dog years -> 0 human age",
        "15 cat/dog years -> 1 human age",
        "23 cat/dog years -> 1 human age",
        "24 cat/dog years -> 2 human age",
        "27 cat/dog years -> 2 human age",
        "28 cat/dog years -> 3/2 human age",
        "100 cat/dog years -> 21/17 human age",
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    result = main.get_human_age(
        cat_age,
        dog_age
    )
    assert isinstance(
        result,
        list
    ), "Result should be a list"
    assert result == expected, \
        (
            f"For cat_age={cat_age}, "
            f"dog_age={dog_age}, "
            f"expected {expected}, "
            f"got {result}"
        )


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -1),
        (-5, -5),
    ],
    ids=[
        "negative cat age",
        "negative dog age",
        "both negative",
    ]
)
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 10),
        (10, "10"),
        (1.5, 10),
        (10, 1.5),
        (None, 10),
    ],
    ids=[
        "cat as string",
        "dog as string",
        "cat as float",
        "dog as float",
        "cat as None",
    ]
)
def test_get_human_age_incorrect_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
