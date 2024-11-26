import pytest
from app.main import get_human_age


class TestAnimalToHumanAge:
    def test_result_list_length_should_be_equal_to_2(self) -> None:
        assert len(get_human_age(1, 1)) == 2

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_ages",
        [
            pytest.param(0, 0, [0, 0], id="should be zeros if ages less than 15"),
            pytest.param(14, 14, [0, 0], id="should be zeros if ages less than 15"),
            pytest.param(15, 15, [1, 1], id="should be [1, 1] if ages between 15 and 23"),
            pytest.param(23, 23, [1, 1], id="should be [1, 1] if ages between 15 and 23"),
        ]
    )
    def test_cat_and_dog_ages(self, cat_age, dog_age, expected_human_ages):
        result = get_human_age(cat_age, dog_age)
        assert expected_human_ages == result

    @pytest.mark.parametrize(
        "cat_age,cat_to_human_age",
        [
            pytest.param(24, 2, id="every 4 cats years should be converted to 1 if age greater than 23"),
            pytest.param(27, 2, id="every 4 cats years should be converted to 1 if age greater than 23"),
            pytest.param(28, 3, id="every 4 cats years should be converted to 1 if age greater than 23"),
            pytest.param(100, 21, id="every 4 cats years should be converted to 1 if age greater than 23"),
        ]
    )
    def test_cat_to_human_age(self, cat_age, cat_to_human_age):
        result = get_human_age(cat_age, 0)
        assert result[0] == cat_to_human_age

    @pytest.mark.parametrize(
        "dog_age,dog_to_human_age",
        [
            pytest.param(24, 2, id="every 5 dogs years should be converted to 1 if age greater than 23"),
            pytest.param(28, 2, id="every 5 dogs years should be converted to 1 if age greater than 23"),
            pytest.param(29, 3, id="every 5 dogs years should be converted to 1 if age greater than 23"),
            pytest.param(100, 17, id="every 5 dogs years should be converted to 1 if age greater than 23"),
        ]
    )
    def test_dog_to_human_age(self, dog_age, dog_to_human_age):
        result = get_human_age(0, dog_age)
        assert result[1] == dog_to_human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age,error",
        [
            pytest.param("0", 0, TypeError, id="incoming cat age must be an integer"),
            pytest.param(0, "0", TypeError, id="incoming dog age must be an integer"),
        ]
    )
    def test_check_for_error(self, cat_age, dog_age, error):
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
