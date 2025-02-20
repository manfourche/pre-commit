# test_ci.py

def greet(name: str) -> str:
    message = "Hello, " + name + "!"
    print(message)  # ✅ Still prints for visibility
    return message  # ✅ Now actually returns a string

greet("world")

