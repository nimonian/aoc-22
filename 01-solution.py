# I saved the input.txt locally, and then this is how to open a file in python
# The 'r' means I'm opening the file in read only mode
with open('01-input.txt', 'r') as f:
  # Save the input in a variable called elves
  # .read() gets the text from the file
  # .strip() removes any unwanted whitespace from beginning and end of the file
  # .split('\n\n') will break the text into a list of individual elves (so at blank lines)
  elves = f.read().strip().split('\n\n') # e.g. ['100\n200\n300', '200\n400', ...] <-- elves

# Each elf is currently a string - we want to break them up so each elf is a list
elves = [elf.strip().split('\n') for elf in elves]
# So elves now looks like
# [
#   ['100', '200', '300'],
#   ['200', '400'],
#   ...
# ]

# We step through the list of elves and calculate the sum of each elf
elves = [sum([int(x) for x in elf]) for elf in elves]
# the int(x) turns e.g. the string '100' into the number 100

# Then we print the answer for (a)!
print(max(elves))

# For part (b), we'll simply sort all the elves and find the largest 3
elves.sort()
print(sum(elves[-3:]))
# This elves[-3:] is called a "slice" in python - it just returns the last 3 items in the list
# Since the list has been sorted in ascending order it will give us the biggest 3
