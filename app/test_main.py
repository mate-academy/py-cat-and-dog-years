import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="Should return zero if age of animal is zero"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="Should return zero if age of animal is less than 15"),
        pytest.param(
            15,
            15,
            [1, 1],
            id="Should return 1 if age of animal equals 15"),
        pytest.param(
            23,
            17,
            [1, 1],
            id="Cats age is 1 if age of animal "
               "less than 15 + 9, but more than 15"
        ),
        pytest.param(
            18,
            23,
            [1, 1],
            id="Dogs age is 1 if age of animal "
               "less than 15 + 9, but more than 15"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="If age equals to 24-27, "
               "for both  human age must be 2"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="If age less than 28, "
               "for both  human age must be 2"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="If age is 28, cats start to age, "
               "changing to 3 and dogs stay at 2"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="Both age on 5 years after 24, moving to 3"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="Check between cats and dogs "
               "age increase difference"
        ),
        pytest.param(
            92,
            98,
            [19, 16],
            id="Check for different values"
               " provided as dog and cats age"
        )
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"{cat_age} and {dog_age} should be "
        f"converted as {result[0]} and {result[1]}")


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        pytest.param(
            0,
            -1,
            ValueError,
            id="Should raise error on negative dog_age"
        ),
        pytest.param(
            -1,
            0,
            ValueError,
            id="Should raise error on negative cat_age"
        ),
    ]
)
def test_get_human_age_invalid_input(
    cat_age: int,
    dog_age: int,
    expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
