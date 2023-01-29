class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def book_name(self):
        return self._name

    @property
    def book_author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str} Количество страниц: {self.pages!r}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._name!r}, {self._author!r}, {self.pages!r})"

    @property
    def book_pages(self):
        return self.pages

    @book_pages.setter
    def book_pages(self, number_of_pages: int) -> None:
        if not isinstance(number_of_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if number_of_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = number_of_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str} Продолжительность: {self.duration!r}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._name!r}, {self._author!r}, {self.duration!r})"

    @property
    def book_duration(self):
        return self.duration

    @book_duration.setter
    def book_duration(self, book_duration: float) -> None:
        if not isinstance(book_duration, float):
            raise TypeError("Количество страниц должно быть типа float")
        if book_duration <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.duration = book_duration
