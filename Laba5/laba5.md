Proxy (Прокси)
```python

from abc import ABC, abstractmethod

# Subject
class Database(ABC):
    @abstractmethod
    def query(self, sql: str):
        pass

# RealSubject
class RealDatabase(Database):
    def query(self, sql: str):
        print(f"Executing query: {sql}")

# Proxy
class DatabaseProxy(Database):
    def __init__(self, has_access: bool):
        self.real_database = RealDatabase()
        self.has_access = has_access

    def query(self, sql: str):
        if self.has_access:
            self.real_database.query(sql)
        else:
            print("Access denied. Query cannot be executed.")

# Usage
user_db = DatabaseProxy(has_access=False)
admin_db = DatabaseProxy(has_access=True)

user_db.query("SELECT * FROM users")  # Вывод: Access denied. Query cannot be executed.
admin_db.query("SELECT * FROM users")  # Вывод: Executing query: SELECT * FROM users

```

Adapter (Адаптер)
```python
from abc import ABC, abstractmethod

# Adaptee
class ExternalLogger:
    def log_message(self, msg: str):
        print(f"External log: {msg}")

# Target
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Adapter
class LoggerAdapter(Logger):
    def __init__(self, external_logger: ExternalLogger):
        self.external_logger = external_logger

    def log(self, message: str):
        self.external_logger.log_message(message)

# Usage
external_logger = ExternalLogger()
logger = LoggerAdapter(external_logger)

logger.log("This is a test message.")  # Вывод: External log: This is a test message.

```


Bridge (мост) *

```python
from abc import ABC, abstractmethod

# Implementor
class Device(ABC):
    @abstractmethod
    def print(self, data: str):
        pass

# ConcreteImplementors
class Monitor(Device):
    def print(self, data: str):
        print(f"Displaying on monitor: {data}")

class Printer(Device):
    def print(self, data: str):
        print(f"Printing to paper: {data}")

# Abstraction
class Output(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def render(self, data: str):
        pass

# RefinedAbstractions
class TextOutput(Output):
    def render(self, data: str):
        self.device.print(f"Text: {data}")

class ImageOutput(Output):
    def render(self, data: str):
        self.device.print(f"Image: [Binary data: {data}]")

# Usage
monitor = Monitor()
printer = Printer()

text_on_monitor = TextOutput(monitor)
text_on_printer = TextOutput(printer)

text_on_monitor.render("Hello, world!")  # Вывод: Displaying on monitor: Text: Hello, world!
text_on_printer.render("Hello, world!")  # Вывод: Printing to paper: Text: Hello, world!

image_on_monitor = ImageOutput(monitor)
image_on_monitor.render("101010101")  # Вывод: Displaying on monitor: Image: [Binary data: 101010101]
```