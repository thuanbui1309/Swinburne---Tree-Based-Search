def modify_dict(**kwargs):
    # kwargs is a dictionary that collects keyword arguments
    kwargs["new_key"] = "new_value"
    print(kwargs)

my_dict = {"key1": "value1", "key2": "value2"}

# Using ** to unpack the dictionary as keyword arguments
modify_dict(**my_dict)

# Original dictionary remains unchanged
print(my_dict)
