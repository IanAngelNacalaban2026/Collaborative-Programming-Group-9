# Collaborative-Programming-Group-9

Members

IanAngelNacalaban2026

CelistineC

ParanKurtGadaga

PSHS Grade Calculator

A simple Python script to calculate grades for Philippine Science High School (PSHS) students.

Features
- Calculates weighted grades for each quarter (**30% Formative**, **70% Summative**).
- Computes cumulative grades across all 4 quarters.
- Converts grades to the official PSHS scale (1.00 to 5.00).

# PSHS Grade Calculator

A simple Python script to calculate grades for Philippine Science High School (PSHS) students.

Features
- Calculates weighted grades for each quarter (**30% Formative**, **70% Summative**).
- Computes cumulative grades across all 4 quarters.
- Converts grades to the official PSHS scale (1.00 to 5.00).

How to Use

1. Requirements
- Python 3 installed on your computer.

2. Run the Program
Save the script as `calculator.py` and run this command in your terminal:
```bash
python calculator.py
```

3. Enter Your Data
The script will prompt you to enter your percentage scores for 3 Formative Assessments (FA) and 3 Summative Assessments (SA) for each quarter.

Grading Scale
The script maps your final score to the PSHS system:
- **96 - 100%**: 1.00 (EXCELLENT)
- **90 - 95%**: 1.25 (VERY GOOD)
- **84 - 89%**: 1.50 (VERY GOOD)
- **78 - 83%**: 1.75 (GOOD)
- **72 - 77%**: 2.00 (GOOD)
- **66 - 71%**: 2.25 (SATISFACTORY)
- **60 - 65%**: 2.50 (SATISFACTORY)
- **55 - 59%**: 2.75 (FAIR)
- **50 - 54%**: 3.00 (FAIR)
- **40 - 49%**: 4.00 (FAILED ON CONDITION)
- **Below 40%**: 5.00 (FAILED)

How to Calculate Tentative Grade

1. Get the scores and average of the Formative Assessments (FA) and Summative Assessments (SA)

 Average = (FA 1 + ... + FA #)/# of FA
 
 Average = (SA 2 + ... + SA #)/# of SA

70% = SA

30% = FA

 Tentative Grade = 0.70((SA 2 + ... + SA #)/# of SA)) + 0.30((FA 1 + ... + FA #)/# of FA))

Grade Formula:
 
 (Previous Quarter + 2(Current Quarter))/3
