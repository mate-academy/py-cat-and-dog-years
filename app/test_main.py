from app.main import get_human_age


def test_zero_age_for_both() -> None:
    result = get_human_age(0, 0)
    assert result == [0, 0], f"Expected [0, 0], but got {result}"

def test_age_below_15_for_both() -> None:
    result = get_human_age(14, 14)
    assert result == [0, 0], f"Expected [0, 0], but got {result}"

def test_age_of_15_for_both() -> None:
    result = get_human_age(15, 15)
    assert result == [1, 1], f"Expected [1, 1], but got {result}"

def test_age_of_23_for_both() -> None:
    result = get_human_age(23, 23)
    assert result == [1, 1], f"Expected [1, 1], but got {result}"

def test_age_of_24_for_both() -> None:
    result = get_human_age(24, 24)
    assert result == [2, 2], f"Expected [2, 2], but got {result}"

def test_age_of_27_for_both() -> None:
    result = get_human_age(27, 27)
    assert result == [2, 2], f"Expected [2, 2], but got {result}"

def test_age_of_28_for_both() -> None:
    result = get_human_age(28, 28)
    assert result == [3, 2], f"Expected [3, 2], but got {result}"

def test_age_of_100_for_both() -> None:
    result = get_human_age(100, 100)
    assert result == [21, 17], f"Expected [21, 17], but got {result}"

def test_dog_age_below_15_cat_age_28() -> None:
    result = get_human_age(28, 14)
    assert result == [3, 0], f"Expected [3, 0], but got {result}"

def test_cat_age_below_15_dog_age_28() -> None:
    result = get_human_age(14, 28)
    assert result == [0, 2], f"Expected [0, 2], but got {result}"
