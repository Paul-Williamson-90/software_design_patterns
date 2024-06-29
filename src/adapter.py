
"""
# Adapter Pattern

**Purpose:**
The Adapter Pattern allows the interface of an existing class to be used as another interface. 
It is often used to make existing classes work with others without modifying their source code.

**When to Use:**
When you want to use an existing class, and its interface does not match the one you need.
When you need to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don’t necessarily have compatible interfaces.
When you need to use several existing subclasses, but it’s impractical to adapt their interface by subclassing every one.

**Advantages:**
It allows two or more previously incompatible interfaces to work together.
It enhances the reusability of classes.
It simplifies code integration by making interfaces compatible.

**Disadvantages:**
Can increase the complexity of the code by introducing additional classes.
Overuse of adapters can make the code messy and harder to understand.

**Use-Cases:**
Integrating a new library with an existing codebase that has a different interface.
Allowing legacy code to interact with new classes.
Bridging two systems with incompatible interfaces.

**Example in Python (Integrating a legacy payment system with a new one use-case):**
"""

# Existing interfaces (adaptee)
class LegacyPaymentSystem:
    def make_payment(self, amount):
        print(f"Processing payment of {amount} using the legacy system.")

# New interface (target)
class PaymentProcessor:
    def process_payment(self, amount):
        pass

# Adapter class
class PaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_payment_system):
        self.legacy_payment_system = legacy_payment_system

    def process_payment(self, amount):
        self.legacy_payment_system.make_payment(amount)

if __name__ == "__main__":
    legacy_system = LegacyPaymentSystem()
    payment_processor = PaymentAdapter(legacy_system)

    payment_processor.process_payment(100)  # Processing payment of 100 using the legacy system.
