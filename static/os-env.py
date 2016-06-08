import os
print os.environ['HOME']

# using get will return `None` if a key is not present rather than raise a `KeyError`
print os.environ.get('KEY_THAT_MIGHT_EXIST')

# os.getenv is equivalent, and can also give a default value instead of `None`
print os.getenv('KEY_THAT_MIGHT_EXIST')

