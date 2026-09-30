def show_menu():
    print("\n======================================")
    print("       AADHAAR CARD VERIFICATION")
    print("======================================")
    print("1. Verify Aadhaar Number")
    print("2. About the Project")
    print("3. Exit")
    print("======================================")


def show_result(success, data):
    print("\n------------- RESULT ----------------")

    if success:
        print("Verification Status : VERIFIED")
        print("Aadhaar Number      :", data["aadhaar"])
        print("Name                :", data["name"])
        print("Date of Birth       :", data["dob"])
        print("City                :", data["city"])
    else:
        print("Verification Status : NOT VERIFIED")
        print("Message             :", data)

    print("--------------------------------------")
