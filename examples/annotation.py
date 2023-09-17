


name = "Braun"
age = 21
amount = 20.00
print ("My name is: %s I am %d years old, I have %.2f dollars in my pocket\n" % (name, age, amount))


print ("My name is {0} my age is {1} I have {:.2f 2} in my pocket".format(name,age,amount))


print (f"My name is {name} my age is {age} I have {amount} in my pocket.")


# Use type annotations!
def square(x: int)-> int:
    return x ** 2


