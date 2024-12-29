
Singleton (Одиночка)

```python

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def some_method(self):
        print("Метод экземпляра Singleton")
```

Factory Method (Фабричный метод)
```python
from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class FileLogger(Logger):
    def log(self, message: str):
        print(f"Logging to file: {message}")


class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Logging to console: {message}")


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass


class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


```
Abstract Factory (Абстрактная фабрика)

```python

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("Windows Button")


class MacButton(Button):
    def paint(self):
        print("Mac Button")


class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Windows Checkbox")


class MacCheckbox(Checkbox):
    def paint(self):
        print("Mac Checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

```
 
Builder (Строитель)
```python

class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, and {self.topping} topping."


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self, dough: str):
        self.pizza.dough = dough

    def build_sauce(self, sauce: str):
        self.pizza.sauce = sauce

    def build_topping(self, topping: str):
        self.pizza.topping = topping

    def get_result(self) -> Pizza:
        return self.pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_hawaiian_pizza(self):
        self.builder.build_dough("cross")
        self.builder.build_sauce("mild")
        self.builder.build_topping("ham and pineapple")

    def construct_spicy_pizza(self):
        self.builder.build_dough("thin crust")
        self.builder.build_sauce("hot")
        self.builder.build_topping("pepperoni and jalapenos")


```

