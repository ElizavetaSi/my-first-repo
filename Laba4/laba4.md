```python
from abc import ABC, abstractmethod

# Интерфейс стратегии
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

# Конкретная стратегия: сортировка пузырьком
class BubbleSortStrategy(SortingStrategy):
    def sort(self, array):
        print("Sorting using Bubble Sort")
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

# Конкретная стратегия: быстрая сортировка
class QuickSortStrategy(SortingStrategy):
    def sort(self, array):
        print("Sorting using Quick Sort")
        self._quick_sort(array, 0, len(array) - 1)

    def _quick_sort(self, array, low, high):
        if low < high:
            pi = self._partition(array, low, high)
            self._quick_sort(array, low, pi - 1)
            self._quick_sort(array, pi + 1, high)

    def _partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

# Контекст
class Sorter:
    def __init__(self, strategy: SortingStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_array(self, array):
        if self.strategy:
            self.strategy.sort(array)
        else:
            print("No strategy set")

# Пример использования
if __name__ == "__main__":
    sorter = Sorter()

    array1 = [5, 3, 8, 4, 2]
    sorter.set_strategy(BubbleSortStrategy())
    sorter.sort_array(array1)
    print(array1)

    array2 = [5, 3, 8, 4, 2]
    sorter.set_strategy(QuickSortStrategy())
    sorter.sort_array(array2)
    print(array2)
```

Цепочка обязаностей 
```ypthon 
from abc import ABC, abstractmethod

# Интерфейс обработчика
class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle_request(self, request):
        pass

# Конкретный обработчик A
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "TYPE_A":
            print("ConcreteHandlerA handled the request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)

# Конкретный обработчик B
class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "TYPE_B":
            print("ConcreteHandlerB handled the request.")
        elif self.next_handler:
            self.next_handler.handle_request(request)

# Пример использования
if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()

    handler_a.set_next_handler(handler_b)

    handler_a.handle_request("TYPE_A")  # Вывод: ConcreteHandlerA handled the request.
    handler_a.handle_request("TYPE_B")  # Вывод: ConcreteHandlerB handled the request.
    handler_a.handle_request("TYPE_C")  # Ничего не выводится, так как обработчик отсутствует
```
Итератор
```python
class ArrayIterator:
    def __init__(self, items):
        self.items = items
        self.position = 0

    def has_next(self):
        return self.position < len(self.items)

    def next(self):
        if self.has_next():
            item = self.items[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration("No more elements in the collection")

# Пример использования
if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]
    iterator = ArrayIterator(items)

    while iterator.has_next():
        print(iterator.next())
```