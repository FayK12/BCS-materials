#this code prints a random fact for the user
name = input("Please input your name and press \"enter\"" " or \"return\" key: ")
print("Welcome "+ name +". How old are you? ")
age = int(input ())
print("Wow! You've been on this earth for",age,"years! Here's a random thought:")
import random
myList = [
    "===> I thought I saw a pussycat.",
    "===> There's a robot chef that can cook meals and clean up. It'll be selling for $92k in 2018",
    "===> I'm smarter than Siri, and Cortana. I'm the new age technology bro.",
    "===> She sells seashells by the seashore.",
    "===> Thomas Alva Edison is one of the greatest inventors of the world. He was also identified as a mentally deficient child by his schoolteachers at a very young age."]
print(random.choice(myList))
print()
print("Press any key to exit")

