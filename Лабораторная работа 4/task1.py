import doctest

class Scopus:
    LIST_OF_JOURNALS = [{"article": "OES diagnostics as a universal technique to control the Si etching structures profile in ICP", "journal": "Scientific Reports"},  # пример списка с названиями журналов, в которых опубликованы статьи
                      {"article": "Nanosphere Lithography: A Powerful Method for the Controlled Manufacturing of Nanomaterials", "journal": "Journal of Nanomaterials"},
                      {"article": "Controllable fabrication of 2D colloidal-crystal films with polystyrene nanospheres of various diameters by spin-coating", "journal": "Applied Surface Science"}]

    def __init__(self, title: str, author: str, topic: str):
        """ Базовый класс - База научных статей Scopus
        :param title: Название статьи
        :param author: Фамилия первого автора статьи
        :param topic: Тематика статьи
        Пример:
        >>> article_1 = Scopus("OES diagnostics as a universal technique to control the Si etching structures profile in ICP", "Osipov", "microelectronics")  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название статьи должно быть типа str")
        self._title = title

        if not isinstance(author, str):
            raise TypeError("Фамилия автора должна быть типа str")
        self._author = author

        if not isinstance(topic, str):
            raise TypeError("Тематика статьи должна быть типа str")
        self._topic = topic

    def __str__(self) -> str:
        """ Магический метод __str__. """
        return f"Статья {self._title}. Автор {self._author}. Тематика {self._topic}"

    def __repr__(self) -> str:
        """ Магический метод __repr__. """
        return f"{self.__class__.__name__}(title={self._title!r}, author={self._author!r}, topic={self._topic!r})"

    def print_name_of_journal(self) -> str:
        """ Узнать название журнала, в котором опубликована статья
        :return: Название журнала
        Примеры:
        >>> article_1 = Scopus("OES diagnostics as a universal technique to control the Si etching structures profile in ICP", "Osipov", "microelectronics")
        >>> article_1.print_name_of_journal()
        'Scientific Reports'
        """
        names = [i["journal"] for i in self.LIST_OF_JOURNALS if i["article"] == self._title]
        return names[0]

    @property
    def title(self) -> str:
        """Возвращает название статьи. Причина инкапсуляции: нельзя менять название статьи, либо только с использованием каких-либо особых функций"""
        return self._title

    @property
    def author(self) -> str:
        """Возвращает фамилию автора. Причина инкапсуляции: нельзя менять название статьи, либо только с использованием каких-либо особых функций"""
        return self._author


class ClosedAccess(Scopus):
    def __init__(self, title: str, author: str, topic: str, cost: float):
        """Дочерний класс - База статей с платным доступпом в Scopuse
        Магический метод __str__  и метод print_name_of_journal наследуем от базового класса - оставляем такие же выходные данные
        :param title: Название статьи
        :param author: Фамилия первого автора статьи
        :param topic: Тематика статьи
        :param cost: Стоимость просмотра статьи в долларах
        Примеры:
        >>> article_2 = ClosedAccess("Nanosphere Lithography: A Powerful Method for the Controlled Manufacturing of Nanomaterials", "Colson", "Nanotechnology", 100.5)
        """
        super().__init__(title, author, topic)

        if not isinstance(cost, float):
            raise TypeError("Стоимость просмотра должна быть типа float")
        if cost < 0:
            raise ValueError("Стоимость просмотра статьи не должна быть отрицательным числом")
        self._cost = cost

    def __repr__(self) -> str:
        """ Магический метод __repr__. Перегружаем с добавлением новой информации"""
        return f"{self.__class__.__name__}(title={self._title!r}, author={self._author!r}, topic={self._topic!r}, " \
               f"cost={self._cost!r})"

    def buy_article(self, money: float) -> float:
        """ Просмотр платной статьи
        :param money: Количество имеющихся денег в личном кабинете
        :return: Сдача
        Примеры:
        >>> article_2 = ClosedAccess("Nanosphere Lithography: A Powerful Method for the Controlled Manufacturing of Nanomaterials", "Colson", "Nanotechnology", 100.5)
        >>> article_2.buy_article(235)
        134.5
        """
        if not isinstance(money, float):
            raise TypeError("Количество денег должно быть типа float")
        if money < 0:
            raise ValueError("Количество денег не должно быть отрицательным числом")
        return money - self._cost


if __name__ == "__main__":
    doctest.testmod()
    pass
