import pytest
from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_cat_to_human,"
        "expected_dog_to_human",
        [
            (0, 0, 0, 0),
            (14, 14, 0, 0),
            (15, 15, 1, 1),
            (23, 23, 1, 1),
            (24, 24, 2, 2),
            (27, 27, 2, 2),
            (28, 28, 3, 2),
            (100, 100, 21, 17),
            (-23, 23, 0, 1),
            (24, -24, 2, 0),
            (-27, -27, 0, 0),
        ]
    )
    def test_get_human_age_validation(self,
                                      initial_cat_age,
                                      initial_dog_age,
                                      expected_cat_to_human,
                                      expected_dog_to_human):
        result = get_human_age(initial_cat_age, initial_dog_age)
        assert result == [expected_cat_to_human, expected_dog_to_human]
