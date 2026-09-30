DATA_FILE = "data/aadhaar_records.txt"


def load_records():
    records = []

    try:
        file = open(DATA_FILE, "r")
        for line in file:
            line = line.strip()

            if line == "":
                continue

            parts = line.split("|")

            if len(parts) == 4:
                record = {
                    "aadhaar": parts[0],
                    "name": parts[1],
                    "dob": parts[2],
                    "city": parts[3]
                }
                records.append(record)

        file.close()

    except FileNotFoundError:
        print("Demo record file was not found.")

    return records


def find_record(aadhaar):
    records = load_records()

    for record in records:
        if record["aadhaar"] == aadhaar:
            return record

    return None
