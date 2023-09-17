# freeCodeCamp
My solutions for freeCodeCamp course projects required to complete their respective course and attain certification.

You can find respective courses on the https://www.freeCodeCamp.org website.

## Scientific Computing with Python

> **Note**
> The following projects require the newest version of pytest to run.

### Project 1 - Arithmetic Formatter

"Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed."

<details><summary>Instructions and functionality example</summary>

Instructions used to build this project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

Example function call:

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

</details>

### Project 2 - Time Calculator

"Write a function named add_time that takes in two required parameters and one optional parameter:

> - a start time in the 12-hour clock > > format (ending in AM or PM)
> - a duration time that indicates the number of hours and minutes
> - (optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result."

<details><summary>Instructions and functionality example</summary>

Instructions used to build this project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

Example function calls:

```python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

</details>
