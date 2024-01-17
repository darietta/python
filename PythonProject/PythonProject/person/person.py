class Person:

    """
    Абстрактный класс, описывающий человека.
    """

    def __init__(self, name: str, age: int, gender: str):

        """
        Инициализация атрибутов человека.

        Args:
            name (str): Имя человека.
            age (int): Возраст человека.
            gender (str): Пол человека.

        Raises:
            ValueError: Если возраст меньше 0 или больше 150.
        """

        self.name = name
        self.age = age
        self.gender = gender

        if self.age < 0 or self.age > 150:
            raise ValueError("Возраст не может быть меньше 0 или больше 150")
        

    def greet(self) -> str:
        """
        Приветствие.

        Returns:
            str: Приветствие от человека.
        """
        pass

    def take_vacation(self, place: str) -> str:
        """
        Отдых в указанном месте.

        Returns:
            str: Сообщение об отдыхе.
        """
        pass

    def sleep(self, hours: int) -> str:
        """
        Сон на указанное количество часов.

        Args:
            hours (int): Количество часов сна.

        Returns:
            str: Сообщение о сне.
        """
        pass