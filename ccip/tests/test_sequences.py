import path
from sequences import Books


def test_books():
    books = Books(1, 2, 3, 4, 5)

    assert books[-1] == 5
    assert books[0] == 1
    assert len(books) == 5
