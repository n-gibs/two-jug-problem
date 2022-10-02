# Water Jug Problem

## Overview:
You are given two jugs, J1 and J2, with capacities C1 and C2. There are no markings on jugs, i.e., we cannot measure a partially filled jug directly. The objective is to measure a target, T units, of water by taking sequence of actions, where the sequence of actions available are:
• Fill up J1 completely
• Fill up J2 completely
• Empty J1 completely
• Empty J2 completely
• Transfer water from J1 to J2
• Transfer water from J2 to J1
The solution must return either
    1) the sequence of actions required to achieve the target
    2) 2) that achieving the target is not achievable.

## Algorithm Overview:
• Input: C1, C2, T
• Output:
o If target achievable:
▪ “Fill J1 -> Pour J1 to J2 -> ...”, (x1, x2) where x1 is amount of water in J1, x1 + x2
= T
o Else:
▪ “not achievable”

## Run Locally

run the file in the terminal with three inputs as arguments
first two inputs are the jug capacities and the last is the target
ex.

```
two_jugs.py 10 6 8
```

If there is a solution it will print the shortest to the console. If not it will print `not achieveable`

## Solution

This Solution uses the Euclidian algorithm. This is based on the principle that the greatest common divisor (GCD) of two numbers does not change if the larger value of the two is replaced by the difference between both numbers. Given two or more numbers the GCD is the greatest number that will divide by all of them.

For example
GCD(2322 and 654) = 6 -> 2322 - 654 = 1668

GCD(1668, 654) = 6 -> 1668 - 654 = 1014

GCD(1014, 654) = 6 -> 1014 - 654 = 360

GCD(360, 654) = 6 -> 654 - 360 = 294

GCD(360, 294) = 6 ... and so on
