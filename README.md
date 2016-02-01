# Assignment 6

We talked about conditionals/flow control and recursion in class on Tuesday.  We also talked a little bit about taking input from the user and doing something with it.  We're going to expand a little bit on those topics for the tasks below.  As with the previous assignment, fork and clone this repository. Then create a directory equivalent to your username in the `answers` directory.  Within your `answers/username` directory, write a program to complete each task, below. Name each of the programs you are writing, according to the "task" (e.g. task1.py). Commit those programs, push them up to your cloned repository, and make a pull request.

## Task 1

Write your own program that demonstrates the use of chained conditionals within a function to accomplish a (relatively simple) task.  You choose what the task is.  Write the program to include a `main()` function and the `ifmain` statement.

## Task 2

Write a program that uses a recursive function to compute the sum of the integers from 0 to 1000 (inclusive).  Return the sum of these numbers to the main loop and print the result. Write the program to include a `main()` function and the `ifmain` statement.

## Task 3

In [task-4](https://github.com/biolprogramming/assignment-5#task-4) of Assignment-5, I asked you to write a function that computed [Euler's](https://en.wikipedia.org/wiki/Leonhard_Euler) number, return that value to the main loop of the program, and print that out.

This time, I want you to compute [Euler's](https://en.wikipedia.org/wiki/Leonhard_Euler) number using recursion - that is, use a function that calls itself to compute Euler's number, then return that value to the main loop and print the value you have returned to the screen.  You cannot use the `sum()` function.  Return the sum of these numbers (the value of `e`) to the main loop and print the result. Write the program to include a `main()` function and the `ifmain` statement.

## Task 4

Modify the program you created in [Task 3](task-3), above, to accept user input where the user input is the maximum value of the range over which you compute `e` (you initially limited this to some value less than 1000). You cannot use the `sum()` function.  Return the sum of these numbers (the value of `e`) to the main loop and print the result. Write the program to include a `main()` function and the `ifmain` statement.

## Task 5

Modify the program you created in [Task 4](task-4), above, to accept input from the user using the `argparse` module.  You'll need to looks at the [argparse documentation](https://docs.python.org/3/library/argparse.html) to learn how the module works.  Group the use of `argparse` into its own function.  As before, you cannot use the `sum()` function.  Return the sum of these numbers (the value of `e`) to the main loop and print the result. Write the program to include a `main()` function and the `ifmain` statement.
