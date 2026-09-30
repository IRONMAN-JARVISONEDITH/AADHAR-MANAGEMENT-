def validate_aadhaar(number):
    if len(number) != 12:
        return False

    if not number.isdigit():
        return False

    if number[0] == "0":
        return False

    return True
