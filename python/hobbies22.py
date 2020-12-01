#!/bin/bash

hobbies = ["rock climbing", "bug collecting", "cooking", "knitting", "writting"]

for hobby in hobbies:
    print(hobby)
print("------------------")

for x in range(2,5):
    print(x)
print("------------------")

for index, hobby in enumerate(hobbies):
    print(hobby + " is my #" + str(index) + " hobby")

for index, hobby in enumerate(hobbies, start=1):
    print(hobby + " is my #" + str(index) + " hobby")
