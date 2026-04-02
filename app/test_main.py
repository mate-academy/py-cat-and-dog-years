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
                                 (100, 100, [21, 17])
                             ])
    def test_border_values(
            self,
            cat_age: int,
            dog_age: int,
            human_list: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_list
