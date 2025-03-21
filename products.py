class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty")

        self.name = name
        self.price = self._validate_non_negative(price, "Price")
        self.quantity = self._validate_non_negative(quantity, "Quantity")
        self.active = True

    @staticmethod
    def _validate_non_negative(value: float, field_name: str) -> float:
        """General validation method for non-negative values."""
        if value < 0:
            raise ValueError(f"{field_name} cannot be negative")
        return value

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        self.quantity = self._validate_non_negative(quantity, "Quantity")
        if self.quantity == 0:
            self.active = False

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        quantity = self._validate_non_negative(quantity, "Quantity to buy")

        if quantity > self.quantity:
            raise ValueError("Not enough stock available. Try buying a smaller quantity")

        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return quantity * self.price
