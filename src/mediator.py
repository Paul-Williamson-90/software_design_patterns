from abc import ABC, abstractmethod

"""
# Mediator Pattern

**Purpose:**
To define an object that encapsulates how a set of objects interact. 
This pattern promotes loose coupling by keeping objects from referring to each other explicitly, 
and it allows their interaction to be varied independently.

**When to Use:**
When a set of objects communicate in complex but well-defined ways.
When reusing an object is difficult because it refers to and communicates with many other objects.
When you want to decouple many classes to simplify their interactions.

**Advantages:**
Reduces the dependencies between communicating objects, thus promoting loose coupling.
Centralizes control logic that can be complex and difficult to maintain if distributed.
Simplifies object protocols by allowing interaction through a central point.

**Disadvantages:**
Can become a complex and monolithic class as more communication is handled by the mediator.
Might inadvertently centralize too much behavior in the mediator, making it a "god object".

**Use-Cases:**
Chat applications where messages are routed through a central server.
Aircraft traffic control systems.
GUI frameworks where various components communicate through a central controller.

**Example in Python (Chat application use-case):**
"""

# Colleague Interface
class Colleague(ABC):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass

# Concrete Colleagues
class User(Colleague):
    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} receives: {message}")

# Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def send_message(self, message, colleague):
        pass

# Concrete Mediator
class ChatMediator(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, sender):
        for user in self.users:
            if user != sender:
                user.receive(message)

if __name__ == "__main__":
    mediator = ChatMediator()

    user1 = User(mediator, "User1")
    user2 = User(mediator, "User2")
    user3 = User(mediator, "User3")

    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)

    user1.send("Hello everyone!")  # User1 sends: Hello everyone!, User2 receives: Hello everyone!, User3 receives: Hello everyone!
    user2.send("Hi User1!")        # User2 sends: Hi User1!, User1 receives: Hi User1!, User3 receives: Hi User1!
