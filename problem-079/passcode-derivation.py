# Passcode derivation
# Problem 79
# A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# 
# The text file, keylog.txt, contains fifty successful login attempts.
# 
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
import itertools

# Generate list of all attempts as a list of lists of integers
attempts = [line.rstrip('\n') for line in open('keylog.txt')]
attempts = [map((lambda x: int(x)), list(digits)) for digits in attempts]

# check all attempts for a given passcode and return whether it's valid
def is_valid_passcode(passcode):
  for attempt in attempts:
    if len(set(attempt).intersection(set(passcode))) == 3:
      d0Index = passcode.index(attempt[0])
      d1Index = passcode.index(attempt[1])
      d2Index = passcode.index(attempt[2])
      if not (d0Index < d1Index and d1Index < d2Index):
        return False
    else:
      return False

  return True
  
perms = 0
min_passcode_length = 11
secret = []
for perm in itertools.permutations(range(0, 10)):
  perms += 1
  # just try to find a better solution
  perm_size = min_passcode_length - 1

  while is_valid_passcode(perm[:perm_size]):
    secret = perm[:perm_size]
    min_passcode_length = perm_size
    perm_size -= 1

print ''.join(map(lambda x: str(x), secret))

