# Pharmacy Management System

## Description

This program demonstrates the fundamentals of Object-Oriented Programming (OOP) in Python by implementing a simple pharmacy management system.

It models drugs and pharmacies using classes and provides basic functionality for managing drug inventory, storing employee information, calculating the total inventory value, and generating a formatted employee summary.

## How It Works

The program begins by creating `Drug` objects, each representing a specific medicine with its name, available quantity, and unit price.

A `Pharmacy` object is then created to manage the pharmacy's inventory and employee records. Drug objects are added to the pharmacy, while employee information is stored as dictionaries containing each employee's first name, last name, and age.

The program calculates the total inventory value by multiplying the quantity of each drug by its unit price and summing the results. Finally, it generates a formatted report listing all registered employees.

## Example

After adding three drugs and two employees to the pharmacy, the program produces the following output:

```text
Created Pharmacy: City Pharmacy
--------------------
Number of drugs in City Pharmacy: 3
--------------------
Total value of drugs in City Pharmacy: 24500000
--------------------
Employees:
The employee number 1 is Alice Smith who is 25 years old.
The employee number 2 is Bob Johnson who is 30 years old.
```

## Source Code

**File:** `1_pharmacy_management_system.py`

---

#### Author: AiPixelCode
