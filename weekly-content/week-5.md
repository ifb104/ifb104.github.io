---
layout: default
title: Week 5 - How To Repeat Actions
nav_order: 5
permalink: /weekly-content/week-5
---

# Week 5 - How To Repeat Actions
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## Fixed Iterations

Using the `for` loop and the built in `range` function, we can repeat a block of code a fixed number of times. 

```python
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

### Accessing sequence values using for-each loop

We can also use a `for` loop to iterate over the values in a sequence. This is called a `for-each` loop. 

```python
# Do a different action for each
# letter in a character string
for letter in "WHAM":
    print('.oO', letter, 'Oo.')
# Output:
# .oO W Oo.
# .oO H Oo.
# .oO A Oo.
# .oO M Oo.
```

### Accessing sequence values using a `range` loop

The `range` function can be used in a `for` loop to iterate over the values in a sequence, using their position (or **index**). 

```python
palindrome = 'Rats live on no evil star!'

# Print just the second half of the palindrome
midpoint = len(palindrome) // 2
for index in range(midpoint, len(palindrome)):
    print(palindrome[index], end='')
# Output:
# no evil star!
```

Note than when given two arguments, the `range` function returns a sequence of numbers starting at the first argument and ending at the second argument minus one. 

### Exiting a loop early

There are two ways to exit a loop early.

- `return` terminates a function immediately, exiting the loop
- `break` terminates a loop immediately

```python
palindrome = 'Rats live on no evil star!'

# Print letters until we reach a space
for letter in palindrome:
    if letter == ' ':
        break
    else:
        print(letter)
# Output:
# R
# a
# t
# s
```

## Condition-controlled iterations

In some situations, we may not know how many times we want to repeat a block of code. In these situations, we can use a `while` loop. 

In the example below, we use a `while` loop to calculate and print a series of sales commissions. The loop will continue until the user enters a value other than `yes` for the `keep_going` variable.

```python
# Set up a variable to control the loop
keep_going = 'yes'

# Calculate and print a series of sales commissions
while keep_going == 'yes':
    # Get salesperson's sales and commission rate
    sales = input('Enter number of sales: ')
    comm_rate = input('Enter commission rate: ')
    
    # Calculate and display the commission
    commission = sales * comm_rate
    print('Your commission is', commission)

    # See if the user wants to continue
    keep_going = input('More (yes/no)? ')
```

## Recursive functions

Another way to perform actions repeatedly is to use a **recursive function**. A recursive function is a function that calls itself. 

```python
def countdown(time):
    if time <= 0:
        print('Lift off!')
    else:
        print(time)
        countdown(time - 1)

>>> countdown(5)
5
4
3
2
1
Lift off!
```

### Base case and recursive case

A recursive function must have a **base case** and a **recursive case**.

- The **base case** returns an answer straight away, without calling the function again.
- The **recursive case** does one step of the calculation and then calls the function again (usually passing a simpler version of the original problem).

There can be more than one base case or recursive case.

```python
def identify_letter(word):
    if word == '': # Base case
        print('Finished!')
    elif word[0] in 'aeiou': # Recursive case
        print('Found a vowel...')
        identify_letter(word[1:])
    else: # Another recursive case
        print('Found a consonant...')
        identify_letter(word[1:])

>>> identify_letter('recur')
Found a consonant...
Found a vowel...
Found a consonant...
Found a vowel...
Found a consonant...
Finished!
```

### Danger: Infinite recursion

To ensure that a recursive function will eventually terminate, every recursive call must make the problem smaller, bringing it closer to the base case.

If the base case is not reached, the function will call itself again and again, (until the program crashes!). This is called **infinite recursion**.

```python
# Don't call this function!
def never_ending_story():
    print('Once upon a time...')
    never_ending_story()

>>> never_ending_story()
Once upon a time...
Once upon a time...
Once upon a time...
...
```