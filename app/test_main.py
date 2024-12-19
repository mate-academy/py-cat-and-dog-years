from app.main import get_human_age

def test_get_human_age_should_return_animal_age_in_human_years() -> None:
    assert get_human_age(28, 28) == [3, 2]