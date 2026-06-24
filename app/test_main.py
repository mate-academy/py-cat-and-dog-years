import pytest
from app import main


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (23, 23, [1, 1]),
    (24, 24, [2, 2]),
    (27, 27, [2, 2]),
    (28, 28, [3, 2]),
    (28, 29, [3, 3]),
    (100, 100, [21, 17]),
])
def test_get_human_age_returns_correct_result(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize("cat_age, dog_age", [
    (0, 0), (14, 14), (15, 15), (23, 23), (24, 24), (100, 100),
])
def test_get_human_age_returns_list_of_two_elements(
    cat_age: int,
    dog_age: int
) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert len(result) == 2


@pytest.mark.parametrize("cat_age, dog_age", [
    (0, 0), (15, 15), (100, 100),
])
def test_get_human_age_returns_integers(
    cat_age: int,
    dog_age: int
) -> None:
    result = main.get_human_age(cat_age, dog_age)
    assert all(isinstance(age, int) for age in result)


# --- Boundary: first 15 years -> 1 human year ---

@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),  # one year short of the first threshold
    (15, 15, [1, 1]),  # exactly at the first threshold
])
def test_get_human_age_first_year_threshold(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


# --- Boundary: next 9 years -> 1 more human year ---

@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (23, 23, [1, 1]),  # one year short of the second threshold (15 + 9 - 1)
    (24, 24, [2, 2]),  # exactly at the second threshold (15 + 9)
])
def test_get_human_age_second_year_threshold(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


# --- Boundary: every extra block (4 cat / 5 dog) -> 1 extra human year ---

@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (27, 28, [2, 2]),  # one year short of the cat/dog extra-block thresholds
    (28, 29, [3, 3]),  # exactly at the cat/dog extra-block thresholds
])
def test_get_human_age_extra_block_threshold(
    cat_age: int,
    dog_age: int,
    expected: list
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


# --- Cat-specific extra block step (4 years) isolated from dog logic ---

@pytest.mark.parametrize("cat_age, expected_human_age", [
    (0, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (27, 2),
    (28, 3),
    (31, 3),
    (32, 4),
    (100, 21),
])
def test_get_human_age_cat_years_conversion(
    cat_age: int,
    expected_human_age: int
) -> None:
    result = main.get_human_age(cat_age, 0)
    assert result[0] == expected_human_age


# --- Dog-specific extra block step (5 years) isolated from cat logic ---

@pytest.mark.parametrize("dog_age, expected_human_age", [
    (0, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (28, 2),
    (29, 3),
    (33, 3),
    (34, 4),
    (100, 17),
])
def test_get_human_age_dog_years_conversion(
    dog_age: int,
    expected_human_age: int
) -> None:
    result = main.get_human_age(0, dog_age)
    assert result[1] == expected_human_age


def test_get_human_age_discards_fractional_remainder() -> None:
    # 17 cat years: 15 -> 1 year, remaining 2 of next 9-year block -> 0 extra
    assert main.get_human_age(17, 0)[0] == 1
    # 19 dog years: 15 -> 1 year, remaining 4 of next 9-year block -> 0 extra
    assert main.get_human_age(0, 19)[1] == 1
