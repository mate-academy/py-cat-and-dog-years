import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_year, dog_year, expect_error", [
        pytest.param("5", 6.1, TypeError, id="cat value is not integer"),
        pytest.param(5, "6", TypeError, id="dog value is not integer")
    ]
)
def test_checking_exeptions(cat_year: int,
                            dog_year: int,
                            expect_error: TypeError) -> None:

    with pytest.raises(expect_error):
        get_human_age(cat_year, dog_year)


@pytest.mark.parametrize(
    "cat_year, dog_year, result", [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
        (-5, 100, [0, 17]),
        (100, -20, [21, 0]),
        (-3, -70, [0, 0]),
    ], ids=[
        "0 cat/dog years should convert into 0 human age.",
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27 cat/dog years should convert into 2 human age.",
        "28 year of cat = 3 human year, 28 dog years = 2 human age.",
        "100 year of cat = 21 human year, 100 dog years = 17 human age.",
        "negative value for cat return 0",
        "negative value for dog return 0",
        "negative value for both return [0,0]",
    ]
)
def test_checking_values(cat_year: int,
                         dog_year: int,
                         result: list) -> None:
    func_result = get_human_age(cat_year, dog_year)
    assert (func_result
            == result), (f"We thought for cat years {cat_year} "
                         f"would be {result[0]} human years "
                         f"and for dog {dog_year} "
                         f"would be - {result[1]}, "
                         f"but got {func_result}")
