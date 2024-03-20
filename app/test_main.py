import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_year, dog_year, expect_error", [
        pytest.param(-1, 0, ValueError, id="cat is not born yet"),
        pytest.param(0, -1, ValueError, id="dog is not born yet"),
        pytest.param(5.1, 6, TypeError, id="cat value is not integer"),
        pytest.param(5, 6.1, TypeError, id="dog value is not integer"),
        pytest.param("5", 6.1, TypeError, id="cat value is not integer"),
        pytest.param(5, "6", TypeError, id="dog value is not integer")
    ]
)
def test_cheking_exeptions(cat_year: int,
                           dog_year: int,
                           expect_error: Exception) -> None:

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
        (100, 100, [21, 17])
    ]
)
def test_cheking_values(cat_year: int,
                        dog_year: int,
                        result: list) -> None:
    func_result = get_human_age(cat_year, dog_year)
    pytest.assume(func_result[0] == result[0],
                  f"Somothing wrong with cat calculate: "
                  f"waited {result[0]}, get {func_result[0]}")
    pytest.assume(func_result[1] == result[1],
                  f"Somothing wrong with dog calculate: "
                  f"waited {result[1]}, get {func_result[1]}")
