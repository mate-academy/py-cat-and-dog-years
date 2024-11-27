import pytest

from app.main import get_human_age

class TestTypes:
    def test_should_output_list_with_integer(self) -> None:
        cat_age = 15
        dog_age = 20
        result = get_human_age(cat_age, dog_age)
        assert all(isinstance(year, int) for year in result)


class TestResults:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(0, 0, [0, 0], id="if parameters is zero"),
            pytest.param(14, 14, [0, 0], id="if yars less then 15"),
            pytest.param(15, 15, [1, 1], id="if yars more then 15 and less then 24"),
            pytest.param(24, 24, [2, 2], id="if yars more then 24"),
            pytest.param(28, 28, [3, 2], id="if yars more then 28"),
            pytest.param(100, 100, [21, 17], id="if very many yars")
        ],
    )
    def test_program_counts_correctly(self, cat_age: int, dog_age: int, expected_result: list) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected_result
