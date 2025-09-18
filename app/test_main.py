from app.main import get_human_age


class TestGetHumanAge:

    def test_zero_ages(self) -> None:
        assert get_human_age(0, 0) == [0, 0]

    def test_ages_below_first_threshold(self) -> None:
        assert get_human_age(14, 14) == [0, 0]
        assert get_human_age(10, 5) == [0, 0]
        assert get_human_age(1, 1) == [0, 0]

    def test_ages_at_first_threshold(self) -> None:
        assert get_human_age(15, 15) == [1, 1]

    def test_ages_between_first_and_second_threshold(self) -> None:
        assert get_human_age(16, 16) == [1, 1]
        assert get_human_age(20, 20) == [1, 1]
        assert get_human_age(23, 23) == [1, 1]

    def test_ages_at_second_threshold(self) -> None:
        assert get_human_age(24, 24) == [2, 2]

    def test_ages_after_second_threshold(self) -> None:
        assert get_human_age(25, 25) == [2, 2]
        assert get_human_age(27, 27) == [2, 2]
        assert get_human_age(28, 28) == [3, 2]

    def test_different_cat_dog_ages(self) -> None:
        assert get_human_age(15, 20) == [1, 1]
        assert get_human_age(20, 15) == [1, 1]
        assert get_human_age(30, 25) == [3, 2]
        assert get_human_age(25, 30) == [2, 3]

    def test_large_ages(self) -> None:
        assert get_human_age(100, 100) == [21, 17]
        assert get_human_age(200, 200) == [46, 37]
        assert get_human_age(50, 50) == [8, 7]

    def test_edge_cases(self) -> None:
        assert get_human_age(23, 23) == [1, 1]
        assert get_human_age(24, 24) == [2, 2]
        assert get_human_age(25, 25) == [2, 2]

        assert get_human_age(23, 23) == [1, 1]
        assert get_human_age(24, 24) == [2, 2]
        assert get_human_age(25, 25) == [2, 2]

        assert get_human_age(28, 29) == [3, 3]
        assert get_human_age(29, 28) == [3, 2]

    def test_cat_specific_calculation(self) -> None:
        assert get_human_age(15, 0)[0] == 1
        assert get_human_age(24, 0)[0] == 2
        assert get_human_age(28, 0)[0] == 3
        assert get_human_age(32, 0)[0] == 4

    def test_dog_specific_calculation(self) -> None:
        assert get_human_age(0, 15)[1] == 1
        assert get_human_age(0, 24)[1] == 2
        assert get_human_age(0, 29)[1] == 3
        assert get_human_age(0, 34)[1] == 4

    def test_examples_from_readme(self) -> None:
        assert get_human_age(0, 0) == [0, 0]
        assert get_human_age(14, 14) == [0, 0]
        assert get_human_age(15, 15) == [1, 1]
        assert get_human_age(23, 23) == [1, 1]
        assert get_human_age(24, 24) == [2, 2]
        assert get_human_age(27, 27) == [2, 2]
        assert get_human_age(28, 28) == [3, 2]
        assert get_human_age(100, 100) == [21, 17]
