import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
        (100, 100, [21, 17]),
    ]
)
def test_logic_of_the_function(
    cat_age: int, dog_age: int, human_age: list[int]
) -> None:
    result = get_human_age(cat_age, dog_age)
    assert result == human_age
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)


@pytest.mark.parametrize(
    "cat, dog",
    [
        ("cat", "dog"),
        ([4.5, 5, 3], 6.1),
        (None, 6,)
    ]
)
def test_ages_are_numbers(cat: int, dog: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
