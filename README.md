# Bank Management System
# Project Overview
The **Bank Management System** is a comprehensive Python-based application designed to digitize and streamline core banking operations. It serves two distinct user groups—**Bank Administrators** and **Customers**—providing a secure and efficient platform for managing accounts and performing financial transactions.
<br>
This project demonstrates the implementation of **Object-Oriented Programming (OOP)** principles, persistent data storage (SQLite/File Handling), and secure data processing.
# Key Features
This project implements the required functional modules and non-functional constraints:
## Functional Modules
## •	User Management :
o	Secure Registration and Login authentication.
<br>
o	Role-based access control (Admin vs. Customer).
## •	Account Operations :
o	Create new bank accounts (Savings/Current).
<br>
o	View account details and search specific accounts.
<br>
o	Close/Delete accounts.
## •	Transaction Processing :
o	Deposit and Withdrawal functionality with validation.
<br>
o	Fund Transfer between accounts.
<br>
o	**Transaction History**: view a detailed statement of past actions (Passbook).
## Non-Functional Implementation
•	**Security:** Passwords are hashed before storage (using bcrypt or hashlib)—never stored in plain text.
<br>
•	**Data Persistence:** Uses SQLite3/CSV to ensure data remains available after the program closes.
<br>
•	**Error Handling:** Robust try-except blocks to manage invalid inputs (e.g., negative withdrawal amounts, insufficient funds).
<br>
•	**Scalability:** Modular code structure allows for easy addition of new features (e.g., Loan module).
# Technologies & Tools Used
•	**Language:** Python 
<br>
•	**Database:** SQLite3 / File I/O (CSV)
<br>
•	**Libraries:**
<br>
<ul>
o	random (for account number generation)
<br>
o	datetime (for transaction timestamps)
<br>
o	os/sys (for system file operations)
<br>
o	unittest (for testing validation logic)
</ul>

# Steps to Install & Run
## Prerequisites
•	Ensure Python is installed on your system.
## Installation
### Clone the Repository:
git clone https://github.com/[24anishka10]/Bank-Management-System.git
cd Bank-Management-System
## Running the Application
To launch the system, run the main.py file from the terminal:
python src/main.py
# Instructions for Testing
The project includes unit tests to validate transaction logic (e.g., preventing overdrafts).
<br>
To run the automated tests:
python -m unittest discover tests



### Designed and developed by : Anishka Narang | 25BAI10513

