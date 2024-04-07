import pytest
from app.main import get_human_age


class TestHumanAgeConversion:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(-1, -1, [0, 0]),
            pytest.param(0, 0, [0, 0]),
            pytest.param(14, 14, [0, 0]),
            pytest.param(15, 15, [1, 1]),
            pytest.param(23, 23, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(27, 27, [2, 2]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(100, 100, [21, 17]),
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           expected_result: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param(None, None,
                         id="`None` should raise `TypeError`"),
            pytest.param("10", "10",
                         id="`str` should raise `TypeError`"),
            pytest.param({1, 2}, {1, 2},
                         id="`set` should raise `TypeError`")
        ]
    )
    def test_test_get_human_age_errors(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
