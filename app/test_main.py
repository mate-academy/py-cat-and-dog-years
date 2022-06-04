from app.main import get_human_age


def test_should_return_excepted_result():
    result = get_human_age(100, 100)

    assert result == [21, 17]
