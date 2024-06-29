
"""
# Observer Pattern

**Purpose:**
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents 
are notified and updated automatically.

**When to Use:** 
When a change to one object requires changing others, and you don't know how many objects need to be changed.

**Advantages:**
Promotes loose coupling.
Supports broadcast communication.

**Disadvantages:**
Can lead to memory leaks if observers are not properly unregistered.
Can be complex to manage dependencies.

**Use-Cases:**
Event handling systems.
Model-View-Controller (MVC) architectures.
Distributed event-driven systems.

**Example in Python (Event handling system use-case):**
"""

class Observer:
    def update(self, message):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")


if __name__=="__main__":
    subject = Subject()
    observer1 = ConcreteObserver()
    observer2 = ConcreteObserver()

    subject.register_observer(observer1)
    subject.register_observer(observer2)

    subject.notify_observers("Event occurred")
