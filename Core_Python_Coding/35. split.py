"""
split: converts a string into the list.
"""

a = "Hello world this is python"
words = a.split()
print(words)
# output: ['Hello', 'world', 'this', 'is', 'python']

a = "Hello-world-this-is-python"
words = a.split("-")
print(words)
