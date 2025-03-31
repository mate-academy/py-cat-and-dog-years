import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should convert into 0 when ages are zeros"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should convert into 0 when "
               "animal ages are less then 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should convert into 1 when "
               "animal ages are less then 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should convert into 1 when "
               "animal ages are less then 24"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should convert into 1 when "
               "animal ages are equal to 24"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should convert into 2 when "
               "cat, dog ages are 27"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should convert into 3, 2 for cat, dog"
               "when animal ages are 28"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should convert into 21, 17 for cat, dog"
               "when animal ages are 100"
        ),
        pytest.param(
            28,
            100,
            [3, 17],
            id="should convert into 3, 17 for cat, dog"
               "when cat, dog ages are 28, 100"
        ),
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="should return zeros when ages are negative numbers"
        )
    ]
)
def test_should_return_correct_output(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
