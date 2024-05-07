import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(-1, -2, [0, 0],
                         id="-1, -2 should equal [0, 0]"),
            pytest.param(0, 0, [0, 0],
                         id="0, 0 should equal [0, 0]"),
            pytest.param(14, 14, [0, 0],
                         id="14, 14 should equal [0, 0]"),
            pytest.param(15, 15, [1, 1],
                         id="15, 15 should equal [1, 1]"),
            pytest.param(23, 23, [1, 1],
                         id="23, 23 should equal [1, 1]"),
            pytest.param(24, 24, [2, 2],
                         id="24, 24 should equal [2, 2]"),
            pytest.param(27, 27, [2, 2],
                         id="27, 27 should equal [2, 2]"),
            pytest.param(28, 28, [3, 2],
                         id="28, 28 should equal [3, 2]"),
            pytest.param(100, 100, [21, 17],
                         id="100, 100 should equal [21, 17]"),
        ]
    )
    def test_get_human_age_with_correct_args(self,
                                             cat_age: int,
                                             dog_age: int,
                                             human_age: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param("age1", "age2"),
            pytest.param(["1"], ["22"]),
            pytest.param({1: "dog"}, 22)
        ]
    )
    def test_get_human_age_with_incorrect_args(self,
                                               cat_age: int,
                                               dog_age: int) -> None:
        with pytest.raises(TypeError):
            assert get_human_age(cat_age, dog_age)
