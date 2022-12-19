from app.main import get_human_age
import pytest


class TestGetHumanAge:

    @pytest.mark.parametrize(
                             "cat_age, dog_age, result",
                             [
                                (0, 0, [0, 0]),
                                (14, 14, [0, 0]),
                                (15, 15, [1, 1]),
                                (24, 24, [2, 2]),
                                (-1, -1, [0, 0])
                             ]
                            )
                             
    def test_get_human_age_value_is_int(self, cat_age, dog_age, result) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_get_human_age_value_is_not_int(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("10", 10)
