#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # This is a good example of how we used list comprehension 
    squared_list = [num ** 2 for num in int_list]
    return squared_list

def fizzbuzz():
    num = 1
    while num <= 100:
        if (num%3 == 0 and num%5 == 0):
            print("FizzBuzz")
        elif (num%3 == 0):
            print("Fizz")
        elif (num%5 == 0):
            print("Buzz")
        else:
            print(num)
        num += 1
