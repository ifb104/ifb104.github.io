---
layout: default
title: Week 3 - How to Create Reusable Functions
nav_order: 4
permalink: /weekly-content/week-3
---

# Week 3 - How to Create Reusable Functions
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

<!-- [Do the Practical](../practicals/week-3){: .btn .btn-blue .fs-5 .mb-4 .mb-md-0 .mr-2 } -->

---

## Code Reuse via Functions

### Function Definition

A function is a *named, parameterised* sequence of statements. A function definition consists of the following:

- The keyword `def`
- The function name
- A list of parameters in parentheses. A function can have zero or more parameters. Even if there are no parameters, the parentheses are required.
- A colon
- A sequence of statements, indented
- Optionally, a `return` statement to return a value

The syntax for a function definition is as follows:

```python
def function_name(parameter1, parameter2, ...):
    statement1
    statement2
    ...
    value = expression # calculate a value before outputting it
    return value
```

For example, consider a function to get a person's initials from their full name:

```python
## Return someone's initials from their full name
def get_initials(full_name):
    # Get the initial char of the person's first name
    first_initial = full_name[0]
    # Find the space before the person's last name
    pos_last_space = full_name.rfind(" ")
    # Get the initial char of the person's last name
    second_initial = full_name[pos_last_space + 1]
    # Return the initials
    return first_initial + second_initial
```

### Function Call

A function call is a statement that causes a function to be executed. A function call consists of the following:
- The function name
- A list of arguments in parentheses. A function call can have zero or more arguments. Even if there are no arguments, the parentheses are required.

The syntax for a function call is as follows:

```python
function_name(argument1, argument2, ...)
```

For example, consider the function `get_initials` defined above. We can call the function as follows:

```python
>>> get_initials("John Smith")
JS
>>> get_initials("Ching Ling Foo")
CF
```

### Default Parameter Values

A function can have default values for its parameters. If a parameter is not specified when the function is called, the default value is used instead.

For example, consider a power function that raises a number to a power. The power is 2 by default:

```python
## Raise the base to the given exponent, or square by default
def power(base, exponent=2):
    return base ** exponent
```

Usage:

```python
>>> power(4)
16
>>> power(4, 3)
64
```

### Named Parameters

A function can have named parameters. When a function is called, the arguments can be specified in any order, as long as the parameter names are specified.

For example, consider a power function that raises a number to a power. The base is 10 by default, and the exponent is 2 by default:

```python
## Raise the base (default: 10) to the given exponent, or square by default
def power(base=10, exponent=2):
    return base ** exponent
```

Usage:

```python
>>> power(4) # In this case, base is 4 and exponent is defaulted to 2
16
>>> power(exponent=4) # In this case, base is defaulted to 10 and exponent is 4
10000
>>> power(exponent=4, base=2) # In this case, base is 2 and exponent is 4. Note the different order of the arguments
16
```

### Local Variables and Scope

A variable defined inside a function is a *local variable*. It is only visible inside the function.

Local variables and parameters are created when the function is called and are not accessible outside the function. We say that they have *local scope*.

To *assign* to a global variable from inside a function, we need to use the `global` keyword. For example:

```python
base = 10

def power(exponent=2):
    global base
    return base ** exponent
```

In this case, the `base` variable was made global by using the `global` keyword.

## Testing Functions - Unit Testing

Assume we want to test the following function:

```python
def square(base):
    return base ** 2
```

We will need to define a suite of test cases that show how the function is intended to work. In python, the convention is to document the test cases in a docstring (`"""..."""`).

For example:

```python
"""
Test 1: Zero case:
>>> square(0)
0

Test 2: Positive case:
>>> square(1)
1

Test 3: Positive case:
>>> square(10)
100

Test 4: Negative case:
>>> square(-5)
25
"""
```

We can then use the `doctest` module to run the tests:

```python
from doctest import testmod
testmod(verbose=True)
```

Combine it all together:

```python
def square(base):
    return base ** 2

"""
Test 1: Zero case:
>>> square(0)
0

Test 2: Positive case:
>>> square(1)
1

Test 3: Positive case:
>>> square(10)
100

Test 4: Negative case:
>>> square(-5)
25
"""

from doctest import testmod
testmod(verbose=True)
```