from abc import ABC, abstractmethod

"""
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

**Example in Python (Authorization system use-case):**
"""

# Handler Interface
class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self, request):
        if self._successor:
            return self._successor.handle_request(request)
        return None

# Concrete Handlers
class AuthenticationHandler(Handler):
    def handle_request(self, request):
        if request.get('authenticated', False):
            print("Authentication successful")
            return super().handle_request(request)
        else:
            print("Authentication failed")
            return "Unauthorized"

class AuthorizationHandler(Handler):
    def handle_request(self, request):
        if request.get('authorized', False):
            print("Authorization successful")
            return super().handle_request(request)
        else:
            print("Authorization failed")
            return "Forbidden"

class DataHandler(Handler):
    def handle_request(self, request):
        print("Handling request data")
        return "Request processed successfully"

if __name__ == "__main__":
    # Create the chain of responsibility
    handler_chain = AuthenticationHandler(
        AuthorizationHandler(
            DataHandler()
        )
    )

    # Example requests
    request1 = {'authenticated': True, 'authorized': True}
    request2 = {'authenticated': True, 'authorized': False}
    request3 = {'authenticated': False, 'authorized': True}

    # Process requests through the chain
    print(handler_chain.handle_request(request1))  # Authentication successful, Authorization successful, Handling request data, Request processed successfully
    print(handler_chain.handle_request(request2))  # Authentication successful, Authorization failed, Forbidden
    print(handler_chain.handle_request(request3))  # Authentication failed, Unauthorized
