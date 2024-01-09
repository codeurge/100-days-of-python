# Functions with Arguments

## Positional Arguments

```python
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

# Calling greet_with() with Positional Arguments
# The order of the arguments matters
greet_with("Jack Bauer", "Nowhere")
```

## Keyword Arguments

```python
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

# Calling greet_with() with Keyword Arguments
# The order of the arguments does not matter
greet_with(location="Nowhere", name="Jack Bauer")
greet_with("Jack Bauer", "Nowhere")
```