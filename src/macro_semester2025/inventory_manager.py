'''
Abstract Inventory Management System Exercise (Step‑by‑Step)

Task Overview:
    Build an inventory system using abstraction and inheritance:
      1. Define an abstract base class `InventoryItem`
      2. Create two subclasses, `PhysicalProduct` and `DigitalProduct`
      3. Implement an `Inventory` manager that can hold any `InventoryItem`

Detailed Steps:

1. Import the abstraction tools
   --------------------------------
   - At the top of your file, write:
         from abc import ABC, abstractmethod
   - This gives you the `ABC` base class and the `@abstractmethod` decorator.

2. Define `InventoryItem` (abstract base)
   ----------------------------------------
   a. Declare the class:
         class InventoryItem(ABC):
   b. Write its `__init__`:
         def __init__(self, name: str, price: float, quantity: int):
             self.name = name
             self.price = price
             self.quantity = quantity
   c. Add common behaviors:
      - `restock(self, amount: int)`: 
          • If `amount < 0`, raise `ValueError("…")`  
          • Else add to `self.quantity`.  
      - `sell(self, amount: int)`:
          • If `amount > self.quantity`, raise `ValueError("…")`  
          • Else subtract from `self.quantity`.
   d. Declare the abstract method:
         @abstractmethod
         def total_value(self) -> float:
             """Return price‑based value of current stock."""
             pass

3. Define `PhysicalProduct` (concrete subclass)
   ---------------------------------------------
   a. Declare class, inheriting from `InventoryItem`:
         class PhysicalProduct(InventoryItem):
   b. Write its `__init__`:
         def __init__(self, name, price, quantity, shipping_cost_per_unit):
             super().__init__(name, price, quantity)
             self.shipping_cost_per_unit = shipping_cost_per_unit
   c. Implement `total_value`:
         def total_value(self) -> float:
             return (self.price + self.shipping_cost_per_unit) * self.quantity

4. Define `DigitalProduct` (concrete subclass)
   --------------------------------------------
   a. Declare class:
         class DigitalProduct(InventoryItem):
   b. Write its `__init__`:
         def __init__(self, name, price, quantity):
             super().__init__(name, price, quantity)
   c. Implement `total_value`:
         def total_value(self) -> float:
             return self.price * self.quantity

5. Define the `Inventory` manager
   --------------------------------
   a. Declare class:
         class Inventory:
   b. In `__init__`, initialize an empty list:
         def __init__(self):
             self.products: list[InventoryItem] = []
   c. Add methods:
      - `add_product(self, product: InventoryItem)`:
         • Append `product` to `self.products`.
      - `remove_product(self, product_name: str)`:
         • Loop through `self.products`; if `prod.name == product_name`, delete it and return.  
         • After loop, raise `KeyError("…not found")` if none matched.
      - `list_products(self) -> list[str]`:
         • Return `[prod.name for prod in self.products]`.
      - `find_product(self, product_name: str) -> InventoryItem`:
         • Loop; return matching `prod` or raise `KeyError`.
      - `total_inventory_value(self) -> float`:
         • Return `sum(prod.total_value() for prod in self.products)`.

6. Write an example usage block
   -----------------------------
   At the bottom, guard with:
       if __name__ == "__main__":
   Then:
     a. Instantiate one `PhysicalProduct`, one `DigitalProduct`:
            book = PhysicalProduct("Book", 20.0, 30, shipping_cost_per_unit=2.5)
            course = DigitalProduct("Course", 50.0, 100)
     b. Create an `Inventory` and `add_product` both items.
     c. Call `sell(...)` on each to simulate sales.
     d. Call `restock(...)` on at least one.
     e. Print:
        - `"Products:"`, `inv.list_products()`
        - `"Total inventory value:"`, formatted `inv.total_inventory_value()`

7. (Optional) Test edge‑cases
   ---------------------------
   - Try selling more than in stock to see your error handling.
   - Try restocking negative amounts to confirm your `ValueError`.
   - Remove a non‑existent product to confirm your `KeyError`.

'''

'''
1. Import the abstraction tools
   --------------------------------
   - At the top of your file, write:
         from abc import ABC, abstractmethod
   - This gives you the `ABC` base class and the `@abstractmethod` decorator.

'''

from abc import ABC, abstractmethod
'''
2. Define `InventoryItem` (abstract base)
   ----------------------------------------
   a. Declare the class:
         class InventoryItem(ABC):
   b. Write its `__init__`:
         def __init__(self, name: str, price: float, quantity: int):
             self.name = name
             self.price = price
             self.quantity = quantity
   c. Add common behaviors:
      - `restock(self, amount: int)`: 
          • If `amount < 0`, raise `ValueError("…")`  
          • Else add to `self.quantity`.  
      - `sell(self, amount: int)`:
          • If `amount > self.quantity`, raise `ValueError("…")`  
          • Else subtract from `self.quantity`.
   d. Declare the abstract method:
         @abstractmethod
         def total_value(self) -> float:
             """Return price‑based value of current stock."""
             pass
'''
class InventoryItem(ABC):
    """ Task 2 - a 
    Abstract base class for any inventory item.
    Includes shared attributes and behaviors, and defines an abstract method for value calculation.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """ task 2 - b
        Initialize a general inventory item.
        :param name: Name of the product
        :param price: Unit price
        :param quantity: Quantity in stock
        """
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def restock(self, amount: int) -> None:
        """ task 2 - c 
        Increase the stock by a given amount.
        Raises ValueError if amount is negative.
        """
        if amount < 0:
            raise ValueError("Restock amount must be non-negative.")
        self.quantity += amount

    def sell(self, amount: int) -> None:
        """ task 2 - c 
        Decrease the stock by a given amount.
        Raises ValueError if trying to sell more than is in stock.
        """
        if amount > self.quantity:
            raise ValueError(f"Not enough stock to sell {amount} units of {self.name}.")
        self.quantity -= amount

    @abstractmethod
    def total_value(self) -> float:
        """ task 2 - d
        Abstract method to compute the total value of this item in inventory.
        To be implemented by subclasses.
        """
        pass

class PhysicalProduct(InventoryItem):
    """ TASK 3
    Represents a physical product with an additional shipping cost per unit.
    """

    def __init__(self, name: str, price: float, quantity: int, shipping_cost_per_unit: float):
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
    """ TASK 4
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
    ## TASK 6
    # Create items
    book = PhysicalProduct("Learn Python Book", price=20.0, quantity=30, shipping_cost_per_unit=2.5)
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