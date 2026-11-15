import pytest


from app.main import get_human_age, BadInputError


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error", [
        pytest.param(-1, 0, BadInputError, id="Check non negative cat_age."),
        pytest.param(0, -1, BadInputError, id="Check non negative dog_age."),
        pytest.param(-1, -1, BadInputError, id="Check non negative age."),
        pytest.param("0", 0, BadInputError, id="Check no cat_age string."),
        pytest.param(0, "0", BadInputError, id="Check no dog_age string."),
        pytest.param("0", "0", BadInputError, id="Check no age as string."),
        pytest.param(2.5, 0, BadInputError, id="Check no floating cat_age."),
        pytest.param(0, 2.5, BadInputError, id="Check no floating dog_age."),
        pytest.param(2.5, 2.5, BadInputError, id="Check no floating age."),
        pytest.param([0], 0, BadInputError, id="Check no cat_age list."),
        pytest.param(0, [0], BadInputError, id="Check no dog_age list."),
        pytest.param([0], [0], BadInputError, id="Check no age list.")
    ]
)
def test_get_human_age_type_input(cat_age: int | str | list | float,
                                  dog_age: int | str | list | float,
                                  expected_error: BadInputError) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age", [
        pytest.param(0, 0, [0, 0], id="Check zero age - start."),
        pytest.param(14, 14, [0, 0], id="Check zero age - end."),
        pytest.param(15, 15, [1, 1], id="Check one age - start."),
        pytest.param(23, 23, [1, 1], id="Check one age - end."),
        pytest.param(24, 24, [2, 2], id="Check two age - start."),
        pytest.param(27, 28, [2, 2], id="Check two age - end."),
        pytest.param(28, 29, [3, 3], id="Check three age - start."),
        pytest.param(31, 33, [3, 3], id="Check three age - end."),
        pytest.param(100, 100, [21, 17], id="Check hundread animal age."),
        pytest.param(200, 250, [46, 47], id="Check outliers.")
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       human_age: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_age
    ), (f"If cat and dog age are [{cat_age}, {dog_age}], their human age "
        f"shall be {human_age}!")
