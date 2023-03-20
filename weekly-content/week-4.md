---
layout: default
title: Week 4 - How To Make Decisions
nav_order: 5
permalink: /weekly-content/week-4
---

# Week 4 - How To Make Decisions
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

<!-- [Do the Practical](../practicals/week-4){: .btn .btn-blue .fs-5 .mb-4 .mb-md-0 .mr-2 } -->

---

## Boolean Expressions

The Boolean data type is used to represent a logical value. It can only have two values: `True` or `False` (in Python, the T and F are capitalised).

### Relational Operators

Relational operators are used to compare two values and return a boolean value. The following table shows some expressions using relational operators:

| Expression | Meaning |
| ---------- | ------- |
| `x == y` | Is `x` equal to `y`? |
| `x != y` | Is `x` not equal to `y`? |
| `x < y` | Is `x` less than `y`? |
| `x <= y` | Is `x` less than or equal to `y`? |
| `x > y` | Is `x` greater than `y`? |
| `x >= y` | Is `x` greater than or equal to `y`? |
| `x` **`in`** `y` | Does `x` exist in `y`? (Where `y` is a compound data type, such as a list or string) |

Example, given the following variables:

```python
a = 4
b = 6
c = 5
```

These expressions evaluate to `True`:

```python
b >= a
a != c
a < c
b <= 10
```

These expressions evaluate to `False`:

```python
a >= 5
b <= a
b == c
```

**NOTE:** There is a difference between the `=` and `==` operators. The `=` operator is used to assign a value to a variable, while the `==` operator is used to compare two values.

Example:

```python
>>> weight = 64 # an assignment
>>> weight == 64 # an equality test
True
>>> 57 == weight # another equality test
False
>>> 57 = weight # an illegal assignment, will cause a SyntaxError
```

### Boolean Connectives

Boolean connectives are used to combine two or more boolean expressions. The following table shows some expressions using boolean connectives:

| Expression | Meaning |
| ---------- | ------- |
| `x` **`and`** `y` | Is `x` and `y` both `True`? |
| `x` **`or`** `y` | Is `x` or `y`, or both `True`? |
| **`not`** `x` | Is `x` `False`? |

Example, given the following variables:

```python
a = 4
b = 6
c = True
```

These expressions evaluate to `True`:

```python
a == 4 and b < 10
not (a == b)
b < 10 and a < 10
c or a == 9 # This one is tricky!
```

These expressions evaluate to `False`:

```python
a == 4 and b == 7
b > 10 or a > 10
not c
```

### Boolean operator precedence and ordering

The order in which boolean operators are evaluated is as follows:
- `not` is evaluated first
- `and` is evaluated next
- `or` is evaluated last
- If two operators have the same precedence, they are evaluated from left to right

**When in doubt, use parentheses to avoid ambiguity.**

Example:

```python
>>> weekend = False # it's not a weekend
>>> student = False # person is not a student
>>> senior = True # person is a senior
>>> # Should we give the person a concession?
>>> weekend and student or senior # Wrong!
False
>>> weekend and (student or senior) # Correct!
False
```

### Predicates (Boolean-valued functions)

A predicate is a function that returns a boolean value. For example, the function `is_even` below returns `True` if the argument is an even number, and `False` otherwise:

```python
def is_even(n):
    return n % 2 == 0
```

Example:

```python
>>> is_even(4)
True
>>> is_even(5)
False
```

## Text Input

Two functions are used to get keyboard: `input` and `eval`.
- `input` returns whatever the user types as a string. It takes an optional argument, which is a prompt that is displayed to the user.
- `eval` evaluates the string that is passed to it as a Python expression. It returns the value of the expression.

Example:

```python
# Get some input from the user
response = input("Please enter an expression: ")
# Echo it
print("You typed '" + response + "'")
# Display the result of evaluating the expression
print("Your expression equals", eval(response))
# Display the type of the result
print('Your expression is of type', type(eval(response)))
```

Usage:

```
Please enter an expression: 6 * 7.2
You typed '6 * 7.2'
Your expression equals 43.2
Your expression is of type <class 'float'>
```

## Condition Statements

A condition statement is used to execute a block of code only if a condition is `True`. There are a few ways to do this in Python:
- A single `if` statement
- A two-alternative `if`-`else` statement
- A multi-alternative `if`-`elif`-`else` statement

In all cases, the condition is a boolean expression. The block of code that is executed is called the **body** of the statement.

### Single `if` statement

The syntax of a single `if` statement is:

```python
if <condition>:
    <body>
```

For example, consider a program which calculates a person's pay. If they work for more than 40 hours, they get paid time-and-a-half for the extra hours.

```python
# Step 0: Get the number of hours worked and pay rate
hours_worked = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

# Step 1: Calculate the normal hourly rate
normal_pay = hours_worked * pay_rate
overtime_pay = 0

# Step 2: Optionally calculate the overtime pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5

# Step 3: Sum total payment
pay = normal_pay + overtime_pay
```

### Two-alternative `if`-`else` statement

The syntax of a two-alternative `if`-`else` statement is:

```python
if <condition>:
    <body_1>
else:
    <body_2>
```

For example, consider the Turtle program that draws a line segment that is red in the bottom half, and blue in the top half.

```python
goto(0, -100)
setheading(90)

for step in range(30):
    if ycor() >= 0:
        # We are in the top half
        pencolor('blue')
    else:
        # We are in the bottom half
        pencolor('red')
    # Either way, keep moving!
    forward(20)
```

In this example, the condition `ycor() >= 0` is used to guide the program's execution.
- If the condition is `True`, the body of the `if` statement is executed and the line segment is drawn in blue.
- Otherwise, the body of the `else` statement is executed and the line segment is drawn in red.

The `forward(20)` statement is executed in both cases, because it is not part of the `if`-`else` statement.

### Multi-alternative `if`-`elif`-`else` statement

The syntax of a multi-alternative `if`-`elif`-`else` statement is:

```python
if <condition_1>:
    <body_1> # This is executed if condition_1 is True
elif <condition_2>:
    <body_2> # This is executed if condition_1 is False and condition_2 is True
elif <condition_3>:
    <body_3> # This is executed if condition_1 and condition_2 are False and condition_3 is True
...
else:
    <body_n> # This is executed if all above conditions are False
```

For example, consider a program that gives directions to a driver based on their speed.

```python
speed = float(input("Enter the speed of the vehicle: "))

if speed < 5: # km/hr
    print("Hurry up!")
elif speed < 50:
    print("Go a bit quicker!")
elif speed < 90:
    print("That's fast enough!")
else:
    print("Slow down!")

print("Give me the wheel!")
```

In the above example, the `speed` variable is used to guide the program's execution.
- If `speed` is less than 5, the body of the `if` statement is executed and the program prints "Hurry up!".
- If `speed` is greater than or equal to 5 but less than 50, the body of the `elif` statement is executed and the program prints "Go a bit quicker!".
- If `speed` is greater than or equal to 50 but less than 90, the body of the `elif` statement is executed and the program prints "That's fast enough!".
- Otherwise (if `speed` is greater than or equal to 90), the body of the `else` statement is executed and the program prints "Slow down!".

The `print("Give me the wheel!")` statement is executed in all cases, because it is not part of the `if`-`elif`-`else` statement.

Note that even though `speed` = 4 is less than 5, the program prints "Hurry up!" instead of "Go a bit quicker!". This is because the first condition that is `True` is the one that is executed. The program does not check the other conditions.

### Nested condition statements

Condition statements can be nested to build complex decision trees. 

For example, consider a bank has a rule that before a person qualifies for a loan, they must earn at least $30,000 and have worked in their current job for at least 2 years:

```python
salary = float(input("Enter your salary: "))
years_in_job = float(input("Enter the number of years you have worked in your current job: "))

if salary >= 30000:
    if years_in_job >= 2:
        print("You qualify for a loan!")
    else:
        print("You must have worked in your current job for at least 2 years to qualify for a loan.")
else:
    print("You must earn at least $30,000 to qualify for a loan.")
```