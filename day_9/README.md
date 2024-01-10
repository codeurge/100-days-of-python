# Python Dictionaries

Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
*As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:
```python
{
  key1: value1,
  key2: value2,
  key3: value3,
}
```

## Dictionary Items

Dictionary items are ordered, changeable, and does not allow duplicates.
Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

```python
dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

dictionary["model"]
dictionary["color"] = "red" # add a new key:value pair
dictionary["year"] = 1967 # change the value of an existing key

for thing in dictionary:
  print(thing) # prints the keys
  print(dictionary[thing]) # prints the values
```

## Nested Dictionaries

A dictionary can contain dictionaries, this is called nested dictionaries.

```python
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
  },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
  },
}

my_family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
```

Nesting a dictionary in a list
```python
travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
  },
]
```