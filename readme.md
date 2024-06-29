# A library of python software design pattern templates

## Included:
- Adapter
- Chain of Responsibility
- Command
- Decorator
- Factory
- Mediator
- Observer
- Singleton
- State
- Strategy

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

# Chain of Responsibility Pattern

**Purpose:**
To avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. 
Chain the receiving objects and pass the request along the chain until an object handles it.

**When to Use:**
When multiple objects can handle a request and the handler is not known a priori.
When you want to issue a request to one of several objects without specifying the receiver explicitly.
When the set of objects that can handle a request should be specified dynamically.

**Advantages:**
Reduces the coupling between the sender and the receiver.
Adds flexibility in assigning responsibilities to objects.
Simplifies the object by allowing them to share the responsibility.

**Disadvantages:**
No guarantee that a request will be handled.
Can be harder to debug if the chain is long and complex.

**Use-Cases:**
Event handling systems.
Logging frameworks with multiple log levels.
Authorization/authentication systems.

# Command Pattern

**Purpose:**
Encapsulates a request as an object, thereby allowing for the parameterization of clients with different requests, queueing of requests, and logging of the requests. It also provides support for undoable operations.

**When to Use:**
When you want to parameterize objects with operations.
When you want to queue operations, schedule their execution, or execute them remotely.
When you want to support undo functionality.

**Advantages:**
Decouples the object that invokes the operation from the one that knows how to perform it.
Enables you to add new commands without changing existing code.
Supports undo/redo functionality.

**Disadvantages:**
Can lead to a proliferation of command classes.
Increases complexity by adding additional layers of abstraction.

**Use-Cases:**
Implementing a text editor with undo/redo functionality.
Creating a menu system with multiple actions in a GUI.
Logging operations for auditing purposes.

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

# Factory Pattern

**Purpose:**
Provides an interface for creating objects in a superclass, but allows subclasses to alter the 
type of objects that will be created.

**When to Use:** 
When the exact type of the object cannot be predicted until runtime.

**Advantages:**
Promotes loose coupling.
Adds a level of abstraction to the instantiation process.

**Disadvantages:**
Can increase complexity of the codebase.

**Use-Cases:**
GUI toolkit (creating buttons, textboxes, etc.).
Document reader (reading different file formats).
Shape generator.

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

# Singleton Pattern

**Purpose:**
Ensures that a class has only one instance and provides a global point of access to it.

**When to Use:** 
When exactly one instance of a class is needed to coordinate actions across the system.

**Advantages:**
Controlled access to the single instance.
Reduced namespace usage.

**Disadvantages:**
Can be overused leading to bad design.
Hard to subclass.

**Use-Cases:**
Logger class.
Configuration manager.
Connection pool.

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

# Strategy Pattern

**Purpose:**
Defines a family of algorithms, encapsulates each one, and makes them interchangeable. 
The strategy pattern lets the algorithm vary independently from clients that use it.

**When to Use:**
When you have multiple algorithms for a specific task and want to switch between them.

**Advantages:**
Enables easy swapping of algorithms.
Promotes single responsibility principle.

**Disadvantages:**
Can increase the number of objects.

**Use-Cases:**
Sorting algorithms.
Compression algorithms.
Payment methods in an e-commerce application.