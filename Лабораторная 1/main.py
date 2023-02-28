import doctest

class Car:
    """
    Документация на класс. Класс описывает модель машины
    """
    def __init__(self, fuel_volume: float, fuel_consumption: float):
        """
        Инициализация экземпляра класса
        :param fuel_volume: Объём топлива
        :param fuel_consumption: Расход топлива на 100 км

        Примеры:
        >>> car = Car(30,10)
        """
        if not isinstance(fuel_volume, (int, float)):
            raise TypeError("Объём топлива должен быть типа int или float")
        if fuel_volume < 0:
            raise ValueError("Объём топлива не может быть отрицательным числом")
        self.fuel_volume = fuel_volume

        if not isinstance(fuel_consumption, (int, float)):
            raise TypeError("Расход топлива должен быть типа int или float")
        if fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть положительным числом")
        self.fuel_consumption = fuel_consumption

    def tank_fullness(self, tank_volume: int) -> float:
        """
        Метод, который определяет, на сколько процентов бак заполнен топливом
        :param tank_volume: Объём бака
        :raise ValueError: Если объём бака меньше объёма топлива, то вызываем ошибку
        :return: Процент наполненности бака

        Примеры:
        >>> car = Car(30,10)
        >>> car.tank_fullness(55)
        """
        if not isinstance(tank_volume, int):
            raise TypeError("Объём бака должен быть целым числом")
        if tank_volume < 45:
            raise ValueError("Объём бака для легковой машины должен быть не менее 45 л")
        ...

    def drive(self, distance: float) -> bool:
        """
        Метод, который проверяет, хватит ли топлива в баке
        :param distance: Дистанция, которую нужно проехать
        :return: Хватит ли топлива в баке

        Примеры:
        >>> car = Car(30,10)
        >>> car.drive(110)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Дистанция должна быть типа int или float")
        if distance <= 0:
            raise ValueError("Дистанция должна быть положительным числом")
        ...

class SchoolDairy:
    """
    Документация на класс. Класс описывает модель школьного дневника
    """
    def __init__(self, name: str, subject: str, marks: list[int]):
        """
        Инициализация экземпляра класса
        :param name: Имя ученика
        :param subject: Название предмета в дневнике
        :param marks: Оценки по данному предмету

        Примеры:
        >>> school_dairy = SchoolDairy('Матвей', 'Математика', [5,5,4,3,5])
        """
        self.name = name
        self.subject = subject
        for i in marks:
            if not isinstance(i, int):
                raise TypeError("Оценка должна быть типа int")
            if i <= 0 and i > 5:
                raise ValueError("Оценка должна быть от 1 до 5 включительно")
        self.mark = marks

    def adding_mark(self, new_mark: int) -> list:
        """
        Метод, который добавляет новую оценку в дневник по данному предмету
        :param new_mark: Новая полученная оценка
        :return: Список оценок по данному предмету

        Примеры:
        >>> school_dairy = SchoolDairy('Матвей', 'Математика', [5,5,4,3,5])
        >>> school_dairy.adding_mark(2)
        """
        if not isinstance(new_mark, int):
            raise TypeError("Оценка должна быть типа int")
        if new_mark <= 0 and new_mark > 5:
            raise ValueError("Оценка должна быть от 1 до 5 включительно")
        ...

    def average_mark(self) -> float:
        """
        Метод, который вычисляет среднюю арифметическую оценку по данному предмету
        :return: Средняя арифметическая оценка

        Примеры:
        >>> school_dairy = SchoolDairy('Матвей', 'Математика', [5,5,4,3,5])
        >>> school_dairy.average_mark()
        """
        ...

class Telegram:
    """
    Документация на класс. Класс описывает модель приложения Telegram
    """
    def __init__(self, status: bool, contacts: list[str]):
        """
        Инициализация экземпляра класса
        :param status: Статус "В сети" (True) или "Не в сети" (False)
        :param contacts: Имена контактов

        Примеры:
        >>> telegram = Telegram(False, ['Дарья', 'Виталий', 'Александр'])
        """
        self.status = status
        for i in contacts:
            if not isinstance(i, str):
                raise TypeError("Имена должны быть типа str")
        self.contacts = contacts

    def change_status(self) -> bool:
        """
        Метод, обеспечивающий изменение статуса на противоположный
        :return: Статус

        Примеры:
        >>> telegram = Telegram(False, ['Дарья', 'Виталий', 'Александр'])
        >>> telegram.change_status()
        """
        ...

    def removing_contact(self, name: str) -> list:
        """
        Метод, удаляющий контакт из списка контактов
        :param name: Имя контакта, который нужно удалить
        :return: Список контактов

        Примеры:
        >>> telegram = Telegram(False, ['Дарья', 'Виталий', 'Александр'])
        >>> telegram.removing_contact('Виталий')
        """
        if name not in self.contacts:
            raise ValueError("Если имя контакта, который нужно удалить, не содержится в списке контактов")
        ...

if __name__ == "__main__":
    doctest.testmod()