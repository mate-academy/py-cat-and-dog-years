import pytest
from app.main import get_human_age


# write your code here
@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="Should return 0 if animals have negative number"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="Only first 15 dog/cat years give 1 human year"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="Only first 15 dog/cat years give 1 human year"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="Only next 9 dog/cat years after 15 give 1 more year"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="Every 4 years for cat after 24 give 1 extra human year"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="Every 5 years for dog years after 24 give 1 extra human year"
        ),
    ],
)
def test_cat_and_dog_years_in_human_years_correctly(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("10", 5),
        (10, "5"),
        ("10", "5"),
    ],
)
def test_with_wrong_types(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
