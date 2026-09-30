# Aadhaar Card Verification System

## Project Overview

Aadhaar Card Verification System is a beginner-level Python console project. It checks whether the entered value has a valid 12-digit format and then searches a small local file containing fictional demonstration records.

The project is made for academic learning. It does not connect to UIDAI or any official Aadhaar database.

## Features

- Checks whether an Aadhaar number contains exactly 12 digits.
- Rejects non-numeric input.
- Rejects a number beginning with zero.
- Searches the local demonstration records.
- Displays the matching name, date of birth and city.
- Shows a clear verified or not verified result.
- Uses separate Python files for different tasks.
- Includes simple validation tests.

## Technologies Used

- Python 3
- Python functions
- Strings and lists
- Dictionaries
- File handling
- Exception handling
- unittest for basic testing
- Git and GitHub

No external package is required for the Python program.

## Project Structure

```text
aadhaar-verification/
│
├── main.py
├── aadhaar_validator.py
├── record_manager.py
├── verification.py
├── display.py
├── README.md
├── statement.md
│
├── data/
│   └── aadhaar_records.txt
│
└── tests/
    └── test_validator.py
```

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run:

```text
python main.py
```

5. Select option 1.
6. Enter one of the fictional demonstration numbers shown below.

Example demonstration number:

```text
234567890123
```

## How to Test

From the project folder, run:

```text
python -m unittest discover -s tests
```

The tests check valid input, short input, alphabetic characters and a leading zero.

## Sample Output

```text
======================================
       AADHAAR CARD VERIFICATION
======================================
1. Verify Aadhaar Number
2. About the Project
3. Exit
======================================
Enter your choice: 1
Enter 12-digit Aadhaar number: 234567890123

------------- RESULT ----------------
Verification Status : VERIFIED
Aadhaar Number      : 234567890123
Name                : Rohan Mehta
Date of Birth       : 12-03-2006
City                : Bhopal
--------------------------------------
```

## Important Note

All records included in this repository are fictional examples created only for educational demonstration. The project must not be treated as an official Aadhaar verification service.

## Author

B.Tech CSE Core  
VIT Bhopal University
