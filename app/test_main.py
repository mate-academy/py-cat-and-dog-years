import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected, exception", [
    pytest.param(0, 0, [0, 0], None, id="Test with zero ages"),
    pytest.param(15, 15, [1, 1], None, id=("Test the boundary \
                  of the first segment")),
    pytest.param(23, 23, [1, 1], None, id="Test before the second segment"),
    pytest.param(24, 24, [2, 2], None, id=("Test the boundary of \
                                           the second segment")),
    pytest.param(27, 28, [2, 2], None, id="Test before the third segment"),
    pytest.param(28, 28, [3, 2], None,
                 id=("Test at the third segment start for \
                 cat and just before for dog")),
    pytest.param(30, 29, [3, 3], None, id="Test the third segment"),
    pytest.param(35, 34, [4, 4], None,
                 id="Test another step within the third segment"),
    pytest.param(100, 100, [21, 17], None, id="Test with high ages"),
    pytest.param(-1, -1, [0, 0], None, id="Test with negative ages"),
    pytest.param("twenty", "thirty", None, TypeError, id=("Test with \
                                                           incorrect type")),
    pytest.param(5000, 5000, [1246, 997], None, id="Test with large numbers")
])
def test_get_human_age(cat_age: int, dog_age: int,
                       expected: list, exception: Exception) -> None:
    if exception:
        with pytest.raises(exception):
            get_human_age(cat_age, dog_age)
    else:
        assert get_human_age(cat_age, dog_age) == expected
