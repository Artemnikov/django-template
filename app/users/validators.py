from django.core.exceptions import ValidationError

def validate_passport_id(value):
    if len(value) != 10:
        raise ValidationError("Passport ID must be 10 characters long.")

def is_valid_israeli_id(id_number):
    if not id_number.isdigit() or len(id_number) != 9:
        raise ValidationError("State ID must be 9 characters long.")

    id_digits = [int(digit) for digit in id_number]
    checksum = sum(digit if idx % 2 == 0 else sum(divmod(2 * digit, 10)) for idx, digit in enumerate(id_digits))
    if checksum % 10 != 0:
        raise ValidationError("State ID is not valid.")
