# 🏦 ICICI ATM Machine – Python

A simple **ATM Machine simulation project** built using **Python**.
This project demonstrates basic Python concepts such as **variables, loops, conditional statements, user input, and arithmetic operations**.

## 📌 Project Overview

This ATM simulation allows the user to:

* 🔐 Enter a PIN
* 💰 Check account balance
* 💸 Withdraw money
* 💵 Deposit money
* 🚪 Exit the ATM
* ❌ Handle invalid PINs and incorrect menu options

The initial account balance is set to **₹10,000** and the PIN is **1234**.

## 🛠️ Technologies Used

* **Python 3**
* `while` loop
* `if / elif / else`
* `input()`
* Variables
* Arithmetic operators
* f-strings

## ⚙️ Features

### 1. PIN Verification

The user must enter the correct PIN to access the ATM menu.

```text
Enter Your Pin No : 1234
```

### 2. Check Balance

Displays the current account balance.

```text
1.Check Balance
2.Withdraw
3. Deposit
4. Exit

Choose your Option : 1
10000
```

### 3. Withdraw Money

Allows the user to enter an amount and subtracts it from the balance.

### 4. Deposit Money

Allows the user to enter an amount and adds it to the balance.

### 5. Exit

Closes the ATM program when the user selects option `4`.

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

Check the Python version:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/icici-atm-python.git
```

### Step 3: Open the Project

Navigate to the project folder:

```bash
cd icici-atm-python
```

### Step 4: Run the Program

```bash
python atm.py
```

## 💻 Sample Output

```text
Welcome to ICICI Bank
Insert Your Card
Your card is valid!

Enter Your Pin No : 1234

1.Check Balance
2.Withdraw
3. Deposit
4. Exit

Choose your Option : 1
10000

Choose your Option : 2
Enter your withdraw amount : 2000
Your Withdrawal Amount : 8000

Choose your Option : 3
Enter your Deposit amount : 5000
Your Deposit amount is : 13000

Choose your Option : 4
Thankyou For our Visiting ICICI ATM!
```

## 📚 Python Concepts Practiced

| Concept              | Usage                                 |
| -------------------- | ------------------------------------- |
| Variables            | Store balance, PIN, option and amount |
| `input()`            | Get user input                        |
| `if / elif / else`   | Check PIN and menu options            |
| `while` loop         | Keep the ATM running                  |
| Arithmetic operators | Deposit and withdrawal calculations   |
| f-string             | Display dynamic output                |
| `exit()`             | End the program                       |

## 🚀 Future Improvements

The project can be enhanced by adding:

* 🔒 Limited PIN attempts
* 💰 Withdrawal balance validation
* 🚫 Insufficient balance checking
* 🔢 Transaction history
* 🔐 PIN change option
* 🧾 Mini statement
* ⚠️ Exception handling for invalid input
* 👥 Multiple account support



This project was created as a beginner-level Python practice project to understand **ATM transaction logic and core Python programming concepts**.


