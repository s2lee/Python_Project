from collections.abc import Sequence


class Books(Sequence):
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)


books = Books("a", "b", "c")
print(len(books))
for book in books:
    print(book)

print(books)
print(books[1:3])
