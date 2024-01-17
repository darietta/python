class Product:
    """
    Абстрактный класс, описывающий продукт.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Инициализация атрибутов продукта.

        Args:
            name (str): Название продукта.
            price (float): Цена продукта.
            quantity (int): Количество продукта.

        Raises:
            ValueError: Если количество продукта отрицательное.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

        if self.quantity < 0:
            raise ValueError("Количество продукта не может быть отрицательным")

    def add_to_cart(self, cart_id: str, quantity: int) -> str:
        """
        Добавление продукта в корзину.

        Args:
            cart_id (str): Идентификатор корзины.
            quantity (int): Количество продукта для добавления.

        Returns:
            str: Статус добавления в корзину.
        """
        pass

    def calculate_total_price(self) -> float:
        """
        Расчет общей стоимости продукта.

        Returns:
            float: Общая стоимость продукта.
        """
        pass