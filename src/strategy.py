
"""
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

**Example in Python (Sorting algorithms use-case):**
"""

class SortStrategy:
    def sort(self, data):
        pass


class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)


class BubbleSort(SortStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data


class Context:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort(data)


if __name__=="__main__":
    data = [5, 2, 9, 1, 5, 6]

    context = Context(QuickSort())
    print(context.sort_data(data))  

    context.set_strategy(BubbleSort())
    print(context.sort_data(data)) 
