'''
Inventory System with Mixins and Polymorphism

This exercise will guide you through building a flexible inventory system
using abstract base classes, mixins, multiple inheritance, and polymorphism.

Steps:

1. Create Mixins:
   - Discountable Mixin:
     - Define a class named `Discountable`.
     - Implement a method `apply_discount(percent)` that takes a percentage and reduces the item's price by that percentage.

   - Trackable Mixin:
     - Define a class named `Trackable`.
     - Implement a method `move_to(location)` that takes a location string and assigns it to the item.

2. Create Concrete Item Classes:
   - Book Class:
     - Define a class named `Book` that inherits from both `PhysicalProduct` and `Discountable`.
     - Ensure it initializes with properties like name, price, quantity, and shipping cost per unit.

   - Electronics Class:
     - Define a class named `Electronics` that inherits from both `PhysicalProduct` and `Trackable`.
     - Ensure it initializes with properties like name, price, quantity, and shipping cost per unit.

3. Expand the Inventory Class:
   - Apply Discounts:
     - Add a method `apply_discounts(percent)` to the `Inventory` class.
     - Iterate over all items in the inventory and apply the discount to items that have the `apply_discount` method.

   - Move Items:
     - Add a method `move_items(location)` to the `Inventory` class.
     - Iterate over all items in the inventory and move items that have the `move_to` method to the specified location.

4. Demonstrate Functionality in the `__main__` Section:
   - Create Instances:
     - Create an instance of `Book` with a name, price, quantity, and shipping cost per unit.
     - Create an instance of `Electronics` with a name, price, quantity, and shipping cost per unit.

   - Add to Inventory:
     - Create an instance of `Inventory`.
     - Add the `Book` and `Electronics` instances to the inventory.

   - Apply Discounts and Move Items:
     - Call the `apply_discounts` method on the inventory with a discount percentage (e.g., 10%).
     - Call the `move_items` method on the inventory with a location string (e.g., "Warehouse A").

   - Print Total Value:
     - Call the `get_value` method on the inventory to calculate the total value.
     - Print the total value of the inventory.
'''

from abc import ABC, abstractmethod

class InventoryItem(ABC):
    """
    Abstract base class for any inventory item.
    Includes shared attributes and behaviors, and defines an abstract method for value calculation.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a general inventory item.
        :param name: Name of the product
        :param price: Unit price
        :param quantity: Quantity in stock
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, amount: int) -> None:
        """
        Increase the stock by a given amount.
        Raises ValueError if amount is negative.
        """
        if amount < 0:
            raise ValueError("Restock amount must be non-negative.")
        self.quantity += amount

    def sell(self, amount: int) -> None:
        """
        Decrease the stock by a given amount.
        Raises ValueError if trying to sell more than is in stock.
        """
        if amount > self.quantity:
            raise ValueError(f"Not enough stock to sell {amount} units of {self.name}.")
        self.quantity -= amount

    @abstractmethod
    def total_value(self) -> float:
        """
        Abstract method to compute the total value of this item in inventory.
        To be implemented by subclasses.
        """
        pass


class PhysicalProduct(InventoryItem):
    """
    Represents a physical product with an additional shipping cost per unit.
    """

    def __init__(
        self, name: str, price: float, quantity: int, shipping_cost_per_unit: float
    ):
        """
        Initialize a physical product.
        :param shipping_cost_per_unit: Additional cost per unit for shipping
        """
        super().__init__(name, price, quantity)
        self.shipping_cost_per_unit = shipping_cost_per_unit

    def total_value(self) -> float:
        """
        Calculate total inventory value including shipping cost.
        Formula: (price + shipping) * quantity
        """
        return (self.price + self.shipping_cost_per_unit) * self.quantity


class DigitalProduct(InventoryItem):
    """
    Represents a digital product with no shipping cost.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initialize a digital product.
        """
        super().__init__(name, price, quantity)

    def total_value(self) -> float:
        """
        Calculate total inventory value.
        Formula: price * quantity
        """
        return self.price * self.quantity


class Inventory:
    """
    Manages a collection of InventoryItem objects.
    Supports operations for adding, removing, searching, and computing total value.
    """

    def __init__(self):
        """
        Initialize an empty inventory list.
        """
        self.products: list[InventoryItem] = []

    def add_product(self, product: InventoryItem) -> None:
        """
        Add a product (Physical or Digital) to the inventory.
        """
        self.products.append(product)

    def remove_product(self, product_name: str) -> None:
        """
        Remove a product by name.
        Raises KeyError if not found.
        """
        for i, prod in enumerate(self.products):
            if prod.name == product_name:
                del self.products[i]
                return
        raise KeyError(f"Product '{product_name}' not found in inventory.")

    def list_products(self) -> list[str]:
        """
        Return a list of product names in inventory.
        """
        return [prod.name for prod in self.products]

    def find_product(self, product_name: str) -> InventoryItem:
        """
        Find and return a product by name.
        Raises KeyError if not found.
        """
        for prod in self.products:
            if prod.name == product_name:
                return prod
        raise KeyError(f"Product '{product_name}' not found in inventory.")

    def total_inventory_value(self) -> float:
        """
        Calculate and return the total value of all products in inventory.
        """
        return sum(prod.total_value() for prod in self.products)


if __name__ == "__main__":
    # Create items
    book = PhysicalProduct(
        "Learn Python Book", price=20.0, quantity=30, shipping_cost_per_unit=2.5
    )
    e_course = DigitalProduct("Advanced OOP Course", price=50.0, quantity=100)

    # Initialize inventory
    inv = Inventory()
    inv.add_product(book)
    inv.add_product(e_course)

    # Simulate transactions
    book.sell(5)
    e_course.sell(10)
    book.restock(10)

    # Output
    print("Products:", inv.list_products())
    print(f"Total inventory value: €{inv.total_inventory_value():.2f}")
