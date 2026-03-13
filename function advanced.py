### 1. Keyword Arguments:
def display(name,age):
    print(f"Name:{name},Age:{age}")
display(age=18,name="Anu")

### 2. Variable-Length Arguments:

# You can use args and kwargs to accept a variable number of arguments in a function.

#### Example: Using 'args'
```python
def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4))

#### Example: Using 'kwargs'
def student_info(**details):
    for key, value in details.items():
        print(f"{key}
        
### 3. lambda functions:        
cube=lambda x:x*3
print(cube(2))

#### lambda function that multiplies two numbers:
multiple=lambda a,b :a*b
print(multiple(10,20))

### 4.function that accepts any number of arguments and returns their averag:
def variable(*numbers):
    return sum(numbers)/2
print(variable(10,20,30,40))

### 5. Nested Functions:
def outer_function(name):
    def inner_function(name):
        print(f"Hello, {name}!")
    inner_function("Anusha")

outer_function("Anu")
        
