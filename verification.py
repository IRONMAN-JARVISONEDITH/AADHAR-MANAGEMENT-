def verify_record(record):
    required_fields = ["aadhaar", "name", "dob", "city"]

    for field in required_fields:
        if field not in record:
            return False

        if record[field] == "":
            return False

    return True
