import pytest

from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "first_num, second_num, expected",
        [
            pytest.param(15, 15, [1, 1],
                         id="human age is int"),
            pytest.param(28, 28, [3, 2],
                         id="human age is int")
        ]
    )
    def test_human_age_is_int(self,
                              first_num: int,
                              second_num: int,
                              expected: list
                              ) -> None:
        if isinstance(first_num, int) and isinstance(second_num, int):
            assert get_human_age(first_num, second_num) == expected
        else:
            raise TypeError

    @pytest.mark.parametrize(
        "first_num, second_num, expected",
        [
            pytest.param(14, 14, [0, 0],
                         id="14 cat/dog years it's 0 human age."),
            pytest.param(15, 15, [1, 1],
                         id="15 cat/dog years it's 1 human age."),
            pytest.param(23, 23, [1, 1],
                         id="23 cat/dog years it's 1 human age."),
            pytest.param(24, 24, [2, 2],
                         id="24 cat/dog years it's 2 human age."),
            pytest.param(27, 28, [2, 2],
                         id="27/28 cat/dog years it's 2 human age."),
            pytest.param(28, 29, [3, 3],
                         id="28/29 cat/dog years it's 3 human age.")
        ]
    )
    def test_ages(self,
                  first_num: int,
                  second_num: int,
                  expected: list
                  ) -> None:
        assert get_human_age(first_num, second_num) == expected
