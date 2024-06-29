from abc import ABC, abstractmethod

"""
# Decorator Pattern

**Purpose:**
Allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class.

**When to Use:**
When you want to add responsibilities to individual objects, not to an entire class.

**Advantages:**
Provides flexible alternatives to subclassing for extending functionality.
Promotes single responsibility principle.

**Disadvantages:**
Can result in a large number of small classes.

**Use-Cases:**
Adding features to a GUI component.
Extending functionalities of an object in a library.
Adding logging, authentication, or security features.

**Example in Python (Adding logging use-case):**
"""

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def operation(self):
        print("Decorator does something before")
        result = self._component.operation()
        print("Decorator does something after")
        return result


class LoggingDecorator(Decorator):
    def operation(self):
        result = self._component.operation()
        print(f"Logging: {result}")
        return result


if __name__ == "__main__":
    component = ConcreteComponent()
    decorated_component = LoggingDecorator(component)
    decorated_component.operation()