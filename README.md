# Custom Sequence Type in Python

## 🎯 Project Goal
This project aims to implement a **custom sequence type in Python** that behaves like built-in sequence types (such as `list`, `tuple`, or `str`) but with additional specialized behavior.  

Through this project, I want to demonstrate:
- How to **design and implement Python classes** that follow the **sequence protocol** (`__getitem__`, `__len__`, `__iter__`, slicing support, etc.).
- How to make custom types **integrate seamlessly** with Python’s built-in operators and idioms (e.g., indexing, iteration, `in` operator).
- How to apply **best practices in object-oriented design** and write **clean, maintainable, and Pythonic code**.

---

## ✨ Key Features
- Implements the **core sequence protocol** in Python:
  - `__getitem__` with support for both indexing and slicing
  - `__len__`
  - `__iter__`
- Supports **common Python idioms**:
  - Membership check (`x in my_sequence`)
  - Iteration in `for` loops
  - Index-based access
- Extendable design for **custom behaviors**, e.g.:
  - Lazy evaluation
  - Type validation
  - Auto-transformation of elements

---

## 🧩 Why This Project?
Python’s built-in collections are powerful, but sometimes developers need a **custom sequence type** for:
- Enforcing constraints (e.g., only storing validated objects).
- Implementing domain-specific collections.
- Creating lightweight wrappers around existing data with extra semantics.

This project shows how to **bridge the gap between Python’s abstract base classes** and **practical use cases**, while following a **Pythonic design philosophy**.

---

## 🚀 Skills Demonstrated
- **Deep understanding of Python’s data model** (special methods, dunder methods).
- **Object-oriented programming** with clean abstractions.
- **Readable and maintainable code style**, following PEP 8 guidelines.
- Experience in **writing tests** (with `pytest`) to validate correctness.
- Use of **typing** for clarity and reliability (`typing.Sequence`, `Generic`, `TypeVar`).

---

## 📖 Usage Example

Here’s a minimal example of how this custom sequence type works:

```python
from collections.abc import Sequence
from typing import Generic, TypeVar, Iterator, Union

T = TypeVar("T")

class CustomSequence(Sequence, Generic[T]):
    def __init__(self, data: list[T]) -> None:
        self._data = list(data)

    def __getitem__(self, index: Union[int, slice]) -> Union[T, list[T]]:
        return self._data[index]

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        return iter(self._data)

    def __contains__(self, item: object) -> bool:
        # Example: enforce case-insensitive matching if elements are strings
        if isinstance(item, str):
            return any(isinstance(x, str) and x.lower() == item.lower() for x in self._data)
        return item in self._data

# Example usage
numbers = CustomSequence([10, 20, 30, 40])
print(numbers[1])        # 20
print(numbers[1:3])      # [20, 30]
print(len(numbers))      # 4
print(30 in numbers)     # True
print(list(numbers))     # [10, 20, 30, 40]

words = CustomSequence(["Python", "Rust", "Go"])
print("python" in words) # True (case-insensitive check)
```

---

## 📂 Repository Structure

```bash
custom-sequence-type/
├── custom_sequence/
│   ├── __init__.py
│   ├── base.py          # Core implementation of the custom sequence
│   └── examples.py      # Example usage
├── tests/
│   └── test_sequence.py # Unit tests with pytest
├── README.md            # Project documentation
├── pyproject.toml       # Project dependencies & metadata
└── LICENSE
```

---

## 🔮 Future Work
- Add support for mutability (e.g., **`__setitem__`**, `append`, `extend`).
- Benchmark performance compared with built-in lists.
- Explore **integration with collections.abc** for automatic interface validation.
- Provide examples of **real-world applications** (e.g., immutable configs, validated datasets).


## 👉 Install dependencies with:
```bash
pip install -r requirements.txt
```

## 👉 To run the tests, simply execute:
```bash
pytest tests/
```