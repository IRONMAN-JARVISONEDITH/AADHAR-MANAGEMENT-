from aadhaar_validator import validate_aadhaar
from record_manager import find_record
from verification import verify_record
from display import show_result, show_menu


def verify_aadhaar():
    aadhaar = input("Enter 12-digit Aadhaar number: ").strip()

    if not validate_aadhaar(aadhaar):
        show_result(False, "Invalid Aadhaar number. Enter exactly 12 digits.")
        return

    record = find_record(aadhaar)

    if record is None:
        show_result(False, "Record not found in the demo records.")
        return

    if verify_record(record):
        show_result(True, record)
    else:
        show_result(False, "The demao record could not be verified.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            verify_aadhaar()
        elif choice == "2":
            print("\nThis project uses fictional demo records only.")
            print("It is not connected to any official Aadhaar service.")
        elif choice == "3":
            print("\nThank you for using Aadhaar Card Verification.")
            break
        else:
            print("\nPlease enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
