from typing import Optional, Union

class Transport:
    """
    Абстрактный класс, описывающий транспортное средство.

    Examples:
        >>> car = Transport(brand="Toyota", model="Camry", year=2022)
        >>> car.start_engine(fuel=50)
        'Engine started successfully'
        >>> car.move(destination="City Center", speed=60)
        'Moving to City Center with speed 60'
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализация атрибутов транспортного средства.

        Args:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.

        Raises:
            ValueError: Если год выпуска меньше 1886 (года изобретения первого автомобиля).
        """
        self.brand = brand
        self.model = model
        self.year = year

        if self.year < 1886:
            raise ValueError("Год выпуска не может быть меньше 1886")

    def start_engine(self, fuel: Optional[Union[int, float]]) -> str:
        """
        Запуск двигателя транспортного средства.

        Args:
            fuel (Optional[Union[int, float]]): Количество топлива (в литрах), необязательный параметр.

        Returns:
            str: Статус запуска двигателя.
        """
        if fuel is not None:
            return "Engine started successfully"
        else:
            return "Engine start failed"

    def move(self, destination: str, speed: int) -> str:
        """
        Перемещение к указанному месту с заданной скоростью.

        Args:
            destination (str): Место назначения.
            speed (int): Скорость перемещения.

        Returns:
            str: Статус перемещения.
        """
        return f"Moving to {destination} with speed {speed}"