import pytest
from app.main import get_human_age


class TestMain:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(-1, -1, [0, 0],
                         id="should return 0 when cat and "
                            "dog age is less than 15"),
            pytest.param(0, 0, [0, 0],
                         id="should return 0 when cat and "
                            "dog age is less than 15"),
            pytest.param(14, 14, [0, 0],
                         id="should return 0 when cat and "
                            "dog age is less than 15"),
            pytest.param(15, 15, [1, 1],
                         id="should return 1 when cat and "
                            "dog age is less than 24"),
            pytest.param(23, 23, [1, 1],
                         id="should return 1 when cat and "
                            "dog age is less than 24"),
            pytest.param(24, 24, [2, 2],
                         id="should return 1 when cat and "
                            "dog age is less than 24"),
            pytest.param(27, 27, [2, 2],
                         id="should return 2 when cat age is less "
                            "than 28 and dog age is less than 29"),
            pytest.param(28, 28, [3, 2],
                         id="should return 3 when cat age is 28 or bigger"),
            pytest.param(29, 29, [3, 3],
                         id="should return 3 when dog age is 29 or bigger"),
            pytest.param(100, 100, [21, 17],
                         id="should return 21 and 17 when cat "
                            "and dog age is equal 100"),
        ]
    )
    def test_should_return_correct_age(self, cat_age: int,
                                       dog_age: int,
                                       human_age: list
                                       ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    def test_check_incorrect_input_type(self,) -> None:
        with pytest.raises(TypeError):
            get_human_age("cat", "dog")
            get_human_age([], {})
            get_human_age(1, "dog")
            get_human_age("cat", 1)
