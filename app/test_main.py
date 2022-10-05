import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(
                0, 0, [0, 0],
                id="test should return [0, 0] when cat and dog age == 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="test should return [0, 0] when cat and dog age < 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="test should return [1, 1] when cat and dog age == 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="test should return [1, 1] when cat "
                   "and dog age in range 16-23"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="test should return [2, 2] when cat age and dog age == 24"
            ),
            pytest.param(
                27, 28, [2, 2],
                id="test should return [2, 2] when cat age in range "
                   "25-27 and dog age in range 25-28"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="test should return [3, 3] when cat age == 28 "
                   "and dog age == 29"
            ),
            pytest.param(
                35, 47, [4, 6],
                id="test should return [4, 6] when cat age == 35 "
                   "and dog age == 47"
            )
        ]
    )
    def test_should_return_age_converted_to_human(self, cat_age,
                                                  dog_age, human_age):
        assert get_human_age(cat_age, dog_age) == human_age
