from abc import ABC, abstractmethod

"""
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

**Example in Python (Text editor with undo functionality use-case):**
"""

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

# Concrete Command for adding text
class AddTextCommand(Command):
    def __init__(self, document, text):
        self.document = document
        self.text = text

    def execute(self):
        self.document.add_text(self.text)

    def undo(self):
        self.document.remove_text(self.text)

# Concrete Command for removing text
class RemoveTextCommand(Command):
    def __init__(self, document, text):
        self.document = document
        self.text = text

    def execute(self):
        self.document.remove_text(self.text)

    def undo(self):
        self.document.add_text(self.text)

# Receiver class
class Document:
    def __init__(self):
        self.content = ""

    def add_text(self, text):
        self.content += text
        print(f"Document content: '{self.content}'")

    def remove_text(self, text):
        self.content = self.content.replace(text, "", 1)
        print(f"Document content: '{self.content}'")

# Invoker class
class TextEditor:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()

    def undo(self):
        if not self.history:
            print("Nothing to undo")
            return
        command = self.history.pop()
        command.undo()
        self.redo_stack.append(command)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return
        command = self.redo_stack.pop()
        command.execute()
        self.history.append(command)

if __name__ == "__main__":
    document = Document()
    editor = TextEditor()

    add_command = AddTextCommand(document, "Hello, ")
    editor.execute_command(add_command)  
    add_command = AddTextCommand(document, "world!")
    editor.execute_command(add_command)  

    editor.undo()  
    editor.undo()  
    editor.redo()  
    editor.redo()
    editor.redo() 
