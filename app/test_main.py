import pytest
from unittest.mock import patch
from app.main import get_human_age


class TestForGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_cat_human_age, expected_dog_human_age",
        [
            (0, 0, 0, 0),
            (14, 14, 0, 0),
            (15, 15, 1, 1),
            (23, 23, 1, 1),
            (24, 24, 2, 2),
            (27, 27, 2, 2),
            (28, 28, 3, 2),
            (100, 100, 21, 17),
        ]
    )
    @patch("app.main.convert_to_human")
    def test_get_human_age_with_mock(self,
                                     mock_convert_to_human: any,
                                     cat_age: any,
                                     dog_age: any,
                                     expected_cat_human_age: any,
                                     expected_dog_human_age: any) -> None:
        mock_convert_to_human.side_effect = [
            expected_cat_human_age,
            expected_dog_human_age
        ]
        result = get_human_age(cat_age, dog_age)
        assert result == [expected_cat_human_age, expected_dog_human_age]
        assert mock_convert_to_human.call_count == 2
        mock_convert_to_human.assert_any_call(cat_age, 15, 9, 4)
        mock_convert_to_human.assert_any_call(dog_age, 15, 9, 5)
