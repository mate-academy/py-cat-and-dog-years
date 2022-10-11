from app.main import get_human_age


# Brevity is the soul of wit
def test_check_all_counted_parameters_cat_and_dog() -> None:
    assert get_human_age(28, 29) == [3, 3]
