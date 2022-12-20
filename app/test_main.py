from app.main import get_human_age

import pytest


class TestGetHumanAge:

    @pytest.mark.parametrize("cat_age, dog_age, result",
                             [
                                 pytest.param(0, 0, [0, 0],
                                              id="return list of zero if age = 0"),
                                 pytest.param(14, 14, [0, 0],
                                              id="return list of zero if age < 15"),
                                 pytest.param(15, 15, [1, 1],
                                              id="return [1, 1] if 15<age<24"),
                                 pytest.param(24, 24, [2, 2],
                                              id="return [2, 2] if 24<age<28"),
                                 pytest.param(-1, -1, [0, 0],
                                              id="return list of zero if age<0 ")
                             ])
    def test_get_human_age_value_is_int(self,
                                        cat_age: int,
                                        dog_age: int,
                                        result: list) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_get_human_age_value_is_not_int(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("10", 10)
