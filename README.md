# freeCodeCamp
My solutions for freeCodeCamp course projects required to complete their respective course and attain certification.

You can find respective courses on the https://www.freeCodeCamp.org website.

## Scientific Computing with Python

> **Note**
> The following projects require the newest version of pytest to run.

### Project 1 - Arithmetic Formatter

"Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed."

<details><summary>Functionality example</summary>

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

<details><summary>Functionality example</summary>

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

### Project 3 - Budget App

"Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list."

<details><summary>Functionality example</summary>

Instructions used to build this project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app

Example output:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Generated chart:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

</details>

### Project 4 - Polygon Area Calculator

"Use object-oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit methods and attributes."

<details><summary>Functionality example</summary>

Instructions used to build this project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

Usage example:

```
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

This code should return:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

</details>

### Project 5 - Probability Calculator

"Suppose there is a hat containing 5 blue balls, 4 red balls, and 2 green balls. What is the probability that a random draw of 4 balls will contain at least 1 red ball and 2 green balls? While it would be possible to calculate the probability using advanced mathematics, an easier way is to write a program to perform a large number of experiments to estimate an approximate probability.

For this project, write a program to determine the approximate probability of drawing certain balls randomly from a hat."

<details><summary>Functionality example</summary>

Instructions used to build this project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator

Usage example:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

</details>
