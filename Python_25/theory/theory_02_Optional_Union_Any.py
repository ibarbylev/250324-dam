from typing import Optional, Union, Any


def greet(name: Optional[str]) -> Union[str, int]:
    if name is None:
        return "Hello, anonymous"
    else:
        return f"Hello, {name}"


print(greet(None))
print(greet(5))


def greet_2(name: Union[str, int, None]) -> Any:
    if name is None:
        return "Hello, anonymous"
    else:
        return f"Hello, {name}"


print(greet_2(None))
print(greet_2(5))


def greet_3(name: str | int | None) -> Any:
    if name is None:
        return "Hello, anonymous"
    else:
        return f"Hello, {name}"


print(greet_3(None))
print(greet_3(5))
