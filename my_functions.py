def greet(name, time_of_day):
    return f"Good {time_of_day}, {name.title()}"


greeting = greet("Euan", "afternoon")
print(greeting)
