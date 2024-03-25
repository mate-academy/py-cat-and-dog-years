from app.main import get_human_age
import pytest


class TestGetAgeValidData:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_ages",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return [0, 0]"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return [1, 1]"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return [2, 2]"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="should return [2, 2]"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should return [3, 2]"
            ),
            pytest.param(
                64, 56, [12, 8],
                id="should return [12, 8]"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return [21, 17]"
            )
        ]
    )
    def test_get_ages_with_valid_data(self,
                                      cat_age: int,
                                      dog_age: int,
                                      expected_ages: list
                                      ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_ages


class TestGetAgeInvalidData:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                "451", "501", TypeError,
                id="should raise TypeError exception"
            )
        ]
    )
    def test_get_ages_with_invalid_data(self,
                                        cat_age: int,
                                        dog_age: int,
                                        expected_error: type
                                        ) -> None:
        with pytest.raises(expected_error):
            assert get_human_age(cat_age, dog_age)
