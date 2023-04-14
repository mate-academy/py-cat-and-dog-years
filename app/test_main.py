from app.main import get_human_age
import pytest


class TestConvertAnimalAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_array",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="Should return list with two 0 "
                   "if both ages are less then 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="Should return list with two 1 "
                   "if both ages are equal to 15"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="Should return list with both 3"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Should return list with both 0 if both ages are 14"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="Should return list with both 1 if both ages are 23"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Should calculate each year "
                   "after 28 for cats "
                   "and after 29 for dogs correctly"
            )
        ]
    )
    def test_convert_animal_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_array: list[int]
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected_array
