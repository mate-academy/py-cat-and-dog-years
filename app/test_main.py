import pytest

from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "first_num, second_num, expected",
        [
            pytest.param(15, "15", TypeError,
                         id="human age isn't int"),
            pytest.param("27", 28, TypeError,
                         id="human age isn't int")
        ]
    )
    def test_human_age_is_int(self,
                              first_num: int,
                              second_num: int,
                              expected: list
                              ) -> None:
        with pytest.raises(TypeError):
            assert get_human_age(first_num, second_num)

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

    @pytest.mark.parametrize(
        "first_num, second_num, expected",
        [
            pytest.param(21434234123, 21344324234132,
                         [5358558526, 4268864846823],
                         id="test_very_big_nums"),
            pytest.param(351425423534252345432, 54354235432532453245,
                         [87856355883563086354, 10870847086506490646],
                         id="test_very_big_nums"),
        ]
    )
    def test_very_big_nums(self,
                           first_num: int,
                           second_num: int,
                           expected: list
                           ) -> None:
        assert get_human_age(first_num, second_num) == expected

    @pytest.mark.parametrize(
        "first_num, second_num, expected",
        [
            pytest.param(-1, -1,
                         [0, 0],
                         id="test_negative_nums"),
            pytest.param(-125, -2,
                         [0, 0],
                         id="test_negative_nums"),
            pytest.param(-25, 15,
                         [0, 1],
                         id="test_negative_nums"),
        ]
    )
    def test_negative_nums(self,
                           first_num: int,
                           second_num: int,
                           expected: list
                           ) -> None:
        assert get_human_age(first_num, second_num) == expected
