from app.main import get_human_age
import pytest

class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age_element, dog_age_element, expected_human_age",
        [
            pytest.param(-1, -2, [0, 0], id="test should return 0 because values is negative"),
            pytest.param(0, 0, [0, 0], id="test should return 0 when values of age is 0"),
            pytest.param(14, 14, [0, 0], id="test should return 0 when animal age less than 15"),
            pytest.param(15, 15, [1, 1], id="test should return 1 when animal age equal or greater than 15"),
            pytest.param(23, 23, [1, 1], id="test should return 1 when animal age less than 24"),
            pytest.param(24, 24, [2, 2], id="test should return 2 when animal age equal or greater than 24"),
            pytest.param(27, 27, [2, 2], id="test should return for cats and dogs 2 because not enough their ages"),
            pytest.param(28, 28, [3, 2], id="test should return 3 for cats and dogs 2 because cats have enough ages"),
            pytest.param(100,100, [21, 17], id="test of big values"),
        ]
    )
    def test_convert_in_human_age(self, cat_age_element, dog_age_element, expected_human_age):
        assert get_human_age(cat_age_element, dog_age_element) == expected_human_age
