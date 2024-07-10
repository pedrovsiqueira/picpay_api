from django.core.exceptions import ValidationError


def validate_cpf(value):
    # Remove special chars
    cpf = ''.join([char for char in value if char.isdigit()])

    if len(cpf) != 11:
        raise ValidationError('Invalid CPF')

    if cpf == cpf[0] * 11:
        raise ValidationError('Invalid CPF')

    def calculate_digit(cpf, multipliers):
        total_sum = sum(
            int(cpf[i]) * multipliers[i]
            for i in range(len(multipliers))
        )

        rest = total_sum % 11
        return 0 if rest < 2 else 11 - rest

    first_multipliers = list(range(10, 1, -1))
    first_digit = calculate_digit(cpf, first_multipliers)

    second_multipliers = list(range(11, 1, -1))
    second_digit = calculate_digit(cpf, second_multipliers)

    if not (cpf[-2] == str(first_digit) and cpf[-1] == str(second_digit)):
        raise ValidationError('Invalid CPF')
