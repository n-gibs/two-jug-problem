# Water Jug Problem

## Overview:
You are given two jugs, J1 and J2, with capacities C1 and C2. There are no markings on jugs, i.e., we cannot measure a partially filled jug directly. The objective is to measure a target, T units, of water by taking sequence of actions, where the sequence of actions available are:
* Fill up J1 completely
* Fill up J2 completely
* Empty J1 completely
* Empty J2 completely
* Transfer water from J1 to J2
* Transfer water from J2 to J1
The solution must return either
    1) the sequence of actions required to achieve the target
    2) 2) that achieving the target is not achievable.

## Algorithm Overview:
* Input: C1, C2, T
* Output:
  * If target achievable:
    * “Fill J1 -> Pour J1 to J2 -> ...”, (x1, x2) where x1 is amount of water in J1, x1 + x2 = T
  * Else:
    * “not achievable”

## Run Locally

run the file in the terminal with three inputs as arguments
first two inputs are the jug capacities and the last is the target
ex.

```
two_jugs.py 10 6 8
```

If there is a solution it will print the shortest to the console. If not it will print `not achieveable`

## Solution

First step is to find if this is solvable.

ax + by = c is solvable if gcd(a, b) divides by c

Lets take the example above: `10x + 6y = 8 `

GCD of 10 and 6 is 2. 8 is also divisible by 2 so we will have a solution

The algorithm runs twice, switching which jug gets filled first. There is a source jug (filled first) and a destination jug.

The `while` loop keeps running as long as the target is not hit by either jug.

At the beginning of each run of the loop, the destination jug is filled by the source jug. That amount depends on if the destination jug is empty or not. We can get that number by finding the minimum between the amount in the amount in the source jug and difference between the capacity of the source jug and the amount in the destination jug. Once the transfer is complete we have 4 options depending on the state of the jugs.

1. source jug hits target, dump destination jug and return
2. destination jug hits target, dump source jug and return
3. when source jug is empty, fill it up
4. when destination jug is full, empty it

As we go through these steps, they are added to an array.
When both options are completed, we return the smaller array of the two and print the array to the console.
