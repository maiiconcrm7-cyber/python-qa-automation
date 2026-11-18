
# QA Bug Report — Shopping Cart

## Bug ID
BUG-003

## Title
Incorrect shopping cart total for 3 products

## Severity
High

## Priority
High

## Environment
Python 3 / pytest

## Description
The shopping cart calculated an incorrect total
when the customer added three products.

## Steps to Reproduce
1. Open the shopping cart calculation.
2. Set the product price to $50.
3. Set the quantity to 3.
4. Calculate the total.

## Expected Result
The total should be $150.

## Actual Result
The system returned $100.

## Root Cause
An incorrect condition calculated the price
of two products when the quantity was three.

## Fix
Removed the incorrect condition and restored
the standard price multiplication.

## Test Results Before Fix
4 passed, 1 failed.

## Test Results After Fix
5 passed, 0 failed.

## Status
Fixed and Verified

## Tools Used
- Python
- pytest
- VS Code

## Project Type
QA Automation — Educational Simulation
