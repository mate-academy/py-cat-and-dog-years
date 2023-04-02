import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result", [
            pytest.param(0, 0, [0, 0],
                         id="cat/dog convert_age should be equal zero"),
            pytest.param(14, 14, [0, 0],
                         id="cat/dog convert_age should be equal zero"),
            pytest.param(15, 15, [1, 1],
                         id="cat/dog convert_age should be equal zero"),
            pytest.param(23, 23, [1, 1],
                         id="cat/dog convert_age should be equal 1"),
            pytest.param(24, 24, [2, 2],
                         id="cat/dog convert_age should be equal 2"),
            pytest.param(27, 28, [2, 2],
                         id="cat/dog convert_age should be equal"),
            pytest.param(28, 28, [3, 2],
                         id="cat/dog convert_age should be different"),
            pytest.param(100, 100, [21, 17],
                         id="cat/dog convert_age should be different")
        ]

    )
    def test_count_human_age_correctly(self,
                                       cat_age: int,
                                       dog_age: int,
                                       result: list
                                       ) -> None:
        assert get_human_age(cat_age, dog_age) == result


def test_human_age_correct_type() -> None:
    with pytest.raises(TypeError):
        get_human_age("3", None)
