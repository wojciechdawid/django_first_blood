def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("You cannot divide by 0")
    return a / b

operations = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div
}
class AlgebraService:
    @staticmethod
    def calculate(calc: str, a: int, b: int) -> int | float:
        return operations[calc](a, b)

