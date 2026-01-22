import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_ages",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should return zeros when cat or dog age equals zeros"
        ),
        pytest.param(
            14, 14, [0, 0],
            id=("14 for cat or dog year-values is largest "
                "possible value that returns 0 human years")
        ),
        pytest.param(
            15, 15, [1, 1],
            id=("15 for cat or dog year-values is smallest "
                "possible value that returns 1 human year")
        ),
        pytest.param(
            23, 23, [1, 1],
            id=("23 for cat or dog year-values is "
                "largest possible value that returns 1 human year")
        ),
        pytest.param(
            24, 24, [2, 2],
            id=("24 for cat or dog year-values is "
                "smallest possible value that returns 2 human year")
        ),
        pytest.param(
            27, 27, [2, 2],
            id=("27 for cat year-values is "
                "largest possible value that returns 2 human year")
        ),
        pytest.param(
            28, 28, [3, 2],
            id=("28 for dog year-values is "
                "largest possible value that returns 2 human year")
        ),
        pytest.param(
            28, 28, [3, 2],
            id=("28 for cat year-values is "
                "smallest possible value that returns 3 human year")
        ),
        pytest.param(
            29, 29, [3, 3],
            id=("29 for dog year-values is "
                "smallest possible value that returns 3 human year")
        ),
        pytest.param(
            100, 100, [21, 17],
            id=("every 4 next cat years and "
                "every 5 next dog years should give 1 extra human year")
        )
    ]
)
def test_handle_correct_results(
        cat_age: int,
        dog_age: int,
        human_ages: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == human_ages


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "29", [], TypeError,
            id="should rise error if age not integer"
        ),
        pytest.param(
            -100, 1000, AssertionError,
            id="should rise error if age not in normal range"
        )
    ]
)
def test_handle_correct_data_input(
        cat_age: int,
        dog_age: int,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        assert 0 <= cat_age <= 100, "cat_age must be in range from 0 to 100"
        assert 0 <= dog_age <= 100, "dog_age must be in range from 0 to 100"
        get_human_age(cat_age, dog_age)
