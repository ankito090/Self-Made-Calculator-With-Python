# A simple calculator that can perform addition, subtraction, multiplication, and division of two numbers.
def main() -> None:
    while True:
        user_input: str = input("Calculate: ")
        print(calculate(user_input))
        exit_default = 1
        while True:
            exit_program = input("Enter c to reuse the calculator or e to exit: ")
            if exit_program == "r":
                exit_default = 1
                break
            elif exit_program == "c":
                exit_default -= 1
                break
            else:
                print("Invalid input")
        if exit_default == 1:
            break
        else:
            continue


def calculate(user_input: str) -> int | float | str:
    try:
        first_num, operator, last_num = user_input.split(" ")
        first_num: int | float | None = check_digit_type(first_num)
        last_num: int | float | None = check_digit_type(last_num)
        if first_num is not None and last_num is not None:
            if operator == "+":
                return first_num + last_num
            elif operator == "-":
                return first_num - last_num
            elif operator == "*":
                return first_num * last_num
            elif operator == "/":
                try:
                    divide: float = first_num / last_num
                    if divide.is_integer():
                        divide: int = int(divide)
                    return divide
                except ZeroDivisionError:
                    return "The denominator cannot be 0"
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        return "Invalid input! Ensure the following format: Number(integer or decimal) Operator(+, -, *, or /) Number(integer or decimal)"


def check_digit_type(x: str) -> int | float | None:
    try:
        x: float = float(x)
        if x.is_integer():
            x: int = int(x)
        return x
    except ValueError:
        return None


if __name__ == "__main__":
    main()
