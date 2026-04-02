import pytest

from app.main import get_human_age


class TestErrors:
    @pytest.mark.parametrize("cat_age, dog_age",
                             [
                                 pytest.param(
                                     -10,
                                     10,
                                     id="should raise error "
                                        "when cat_age is negative"
                                 ),
                                 pytest.param(
                                     5,
                                     -14,
                                     id="should raise error "
                                        "when dog_age is negative"
                                 ),
                                 pytest.param(
                                     -31,
                                     -29,
                                     id="should raise error "
                                        "when both ages is negative"
                                 )
                             ])
    def test_negative_age_value(self, cat_age: int, dog_age: int) -> None:
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize("cat_age, dog_age",
                             [
                                 pytest.param(4.6, 7.8,
                                              id="should raise error "
                                                 "when var is float"),
                                 pytest.param("31", "25",
                                              id="should raise error "
                                                 "when var is str"),
                                 pytest.param((1,), (2,),
                                              id="should raise error "
                                                 "when var is tuple"),
                                 pytest.param(None, None,
                                              id="should raise error "
                                                 "when var is None"),
                                 pytest.param({22}, {10},
                                              id="should raise error "
                                                 "when var is set"),
                                 pytest.param({"cat": 12}, {"dog": 11},
                                              id="should raise error "
                                                 "when var is dict"),
                                 pytest.param([12], [19],
                                              id="should raise error "
                                                 "when var is list")
                             ]
                             )
    def test_should_error_when_age_is_not_int(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)


class TestOutput:
    @pytest.mark.parametrize("cat_age, dog_age, human_list",
                             [
                                 (0, 0, [0, 0]),
                                 (14, 14, [0, 0]),
                                 (15, 15, [1, 1]),
                                 (23, 23, [1, 1]),
                                 (24, 24, [2, 2]),
                                 (27, 27, [2, 2]),
                                 (28, 28, [3, 2]),
                                 (28, 29, [3, 3]),
                                 (100, 100, [21, 17]),
                             ])
    def test_border_values(
            self,
            cat_age: int,
            dog_age: int,
            human_list: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_list
