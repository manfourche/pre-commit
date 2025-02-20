# test_ci.py


def greet(name: str) -> str:
    message = "Hello, " + name + "!"
    return message


if __name__ == "__main__":
    greet("world")
