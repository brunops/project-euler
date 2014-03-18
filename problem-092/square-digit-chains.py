# Square digit chains
# Problem 92
# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
# For example,
#
# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?


ARRAY_SIZE = 568
# maximum number after calculating the next number is 567
# that is for 9^2 * 7 = 567, for number 9999999
last_number = [0] * ARRAY_SIZE

# base cases
last_number[1] = 1
last_number[89] = 89

def next_number_in_chain(number):
  return sum( map(lambda x: x * x, map(int, list(str(number))) ) )

def last_number_chain(number):
  if number < ARRAY_SIZE and last_number[number] != 0:
    return last_number[number]
  else:
    last = last_number_chain(next_number_in_chain(number))
    if number < ARRAY_SIZE:
      last_number[number] = last
    return last


total = 0
i = 1
while i < 10000000:
  if last_number_chain(i) == 89:
    total += 1
  i += 1

print total
