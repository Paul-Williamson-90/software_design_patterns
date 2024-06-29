from abc import ABC, abstractmethod

"""
# State Pattern

**Purpose:**
The State Pattern allows an object to change its behavior when its internal state changes. 
The object will appear to change its class.

**When to Use:**
When an object's behavior depends on its state and it must change its behavior at runtime depending on that state.
When operations have large, multipart conditional statements that depend on the object's state.

**Advantages:**
Localizes state-specific behavior and partitions behavior for different states.
Makes state transitions explicit.
State objects can be shared to reduce the number of objects.

**Disadvantages:**
Can result in many state classes and can be complex to manage.
If state transitions are not well defined, can lead to unexpected behavior.

**Use-Cases:**
Implementing a state machine (e.g., for a vending machine or a game).
Managing states in user interface elements (e.g., buttons with different states like enabled, disabled, hovered).
Handling the states of a network connection (e.g., connecting, connected, disconnected).

**Example in Python (Vending machine use-case):**
"""

# State Interface
class State(ABC):
    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def select_item(self):
        pass

    @abstractmethod
    def dispense_item(self):
        pass

# Concrete States
class NoCoinState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin inserted.")
        self.vending_machine.state = self.vending_machine.has_coin_state

    def select_item(self):
        print("You need to insert a coin first.")

    def dispense_item(self):
        print("You need to insert a coin first.")

class HasCoinState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin already inserted.")

    def select_item(self):
        print("Item selected.")
        self.vending_machine.state = self.vending_machine.item_selected_state

    def dispense_item(self):
        print("You need to select an item first.")

class ItemSelectedState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin already inserted and item selected.")

    def select_item(self):
        print("Item already selected.")

    def dispense_item(self):
        print("Dispensing item...")
        self.vending_machine.state = self.vending_machine.no_coin_state

# Context
class VendingMachine:
    def __init__(self):
        self.no_coin_state = NoCoinState(self)
        self.has_coin_state = HasCoinState(self)
        self.item_selected_state = ItemSelectedState(self)
        self.state = self.no_coin_state

    def insert_coin(self):
        self.state.insert_coin()

    def select_item(self):
        self.state.select_item()

    def dispense_item(self):
        self.state.dispense_item()

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.insert_coin()      # Coin inserted.
    vending_machine.select_item()      # Item selected.
    vending_machine.dispense_item()    # Dispensing item...

    vending_machine.dispense_item()    # You need to insert a coin first.
    vending_machine.select_item()      # You need to insert a coin first.
    vending_machine.insert_coin()      # Coin inserted.
    vending_machine.insert_coin()      # Coin already inserted.
    vending_machine.select_item()      # Item selected.
