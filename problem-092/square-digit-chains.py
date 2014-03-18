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

will_arrive_at_1 = set()
will_arrive_at_89 = set()

def next_number_in_chain(number):
  return sum( map(lambda x: x * x, map(int, list(str(number))) ) )

def last_digit_chain(number):
  if number == 1 or number in will_arrive_at_1:
    return 1
  if number == 89 or number in will_arrive_at_89:
    return 89

  next = next_number_in_chain(number)
  last_digit = last_digit_chain(next)

  if last_digit == 1:
    will_arrive_at_1.add(number)

  if last_digit == 89:
    will_arrive_at_89.add(number)

  return last_digit

total = 0
for i in range(1, 10000000):
  if last_digit_chain(i) == 89:
    total += 1

print total
