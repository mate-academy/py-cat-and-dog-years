import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(-1, -1, [0, 0],
                     id="Age of pets should be positive number"),
        pytest.param(0, 0, [0, 0],
                     id="Zero ages for pets are 0 for people"),
        pytest.param(14, 14, [0, 0],
                     id="First 15 pets years give 1 human year"),
        pytest.param(15, 15, [1, 1],
                     id="First 15 pets years give 1 human year"),
        pytest.param(23, 23, [1, 1],
                     id="The next 9 pets years give 1 more human year"),
        pytest.param(24, 24, [2, 2],
                     id="The next 9 pets years give 1 more human year"),
        pytest.param(27, 27, [2, 2],
                     id="The next 9 pets years give 1 more human year"),
        pytest.param(28, 28, [3, 2],
                     id="Every 4 next cat years give 1 extra human year"),
        pytest.param(100, 100, [21, 17],
                     id="Every 4 next cat years give 1 extra human year"),
    ]
)
def test_convert_animal_age_to_human(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        pytest.param("-1", "-1",
                     id="Ages have to be integers"),
        pytest.param("0", 0,
                     id="Cats age have to be an integer"),
        pytest.param(0, "0",
                     id="Dogs age have to be an integer"),
    ]
)
def test_types_of_input_data(cat_age: int, dog_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


def test_length_of_output() -> None:
    assert len(
        get_human_age(0, 16)
    ) == 2, "Expected output is a list of 2 values"
