def is_divisible(number, divisor):
    return number % divisor == 0


def foobarqix(number):
    result = ""
    if is_divisible(number, 3):
        result += "Foo"
    if is_divisible(number, 5):
        result += "Bar"
    if is_divisible(number, 7):
        result += "Qix"
    if result != "":
        return result
    else:
        return str(number)
