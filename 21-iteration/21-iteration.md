# Chapter 21 – Iteration

## Learning Goals

- Master iteration techniques for all collection types.
- Learn safe modification during iteration.
- Understand time complexity of operations.
- Apply comprehensions and generator expressions.

## Iteration Patterns

### Basic Iteration

```python
# List
for item in my_list:
    print(item)

# Dictionary (keys)
for key in my_dict:
    print(key)

# Dictionary (key-value)
for k, v in my_dict.items():
    print(f"{k}: {v}")

# Tuple
for item in my_tuple:
    print(item)
```

### Index-Based Iteration

```python
# Using enumerate
for index, item in enumerate(my_list):
    print(f"{index}: {item}")

# Using while loop
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
```

### Reverse Iteration

```python
for item in reversed(my_list):
    print(item)
```

## Safe Modification

### Lists

```python
# Iterate over copy
for item in my_list[:]:
    if condition:
        my_list.remove(item)
```

### Dictionaries

```python
# Iterate over list of keys
for key in list(my_dict.keys()):
    if condition:
        del my_dict[key]
```

## Time Complexity

| Operation | List | Dict | Tuple |
| --- | --- | --- | --- |
| Iteration | O(n) | O(n) | O(n) |
| Membership test | O(n) | O(1) | O(n) |
| Access by index | O(1) | N/A | O(1) |
| Access by key | N/A | O(1) | N/A |

## Best Practices

- Use `for item in collection` for clean iteration
- Use `enumerate()` when index is needed
- Never modify collection while iterating directly
- Use `items()` for dictionary key-value pairs
- Use generator expressions for memory efficiency

## Common Mistakes

- Modifying list while iterating over it
- Using `for key in dict.values()` when you need keys too
- Forgetting that dictionary order is guaranteed only in Python 3.7+