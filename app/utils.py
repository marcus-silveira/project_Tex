from app.exceptions.invalid_exception_cpf import InvalidCPFError


class Utils:
    @staticmethod
    def validate_cpf(cpf: str):
        cpf = ''.join(filter(str.isdigit, cpf))

        if len(cpf) != 11:
            raise InvalidCPFError()

        if cpf == cpf[0] * 11:
            raise InvalidCPFError()

        def calculate_digit(cpf: str, weight: int):
            total = sum(int(digit) * weight for digit, weight in zip(cpf, range(weight, 1, -1)))
            digit = (total * 10) % 11
            return digit if digit < 10 else 0

        first_digit = calculate_digit(cpf[:-2], 10)
        second_digit = calculate_digit(cpf[:-1], 11)

        if int(cpf[-2]) != first_digit or int(cpf[-1]) != second_digit:
            raise InvalidCPFError()
