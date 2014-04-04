# encoding: utf-8
# Counting Sundays
# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
#  1 Jan 1900 was a Monday.
#  Thirty days has September,
#  April, June and November.
#  All the rest have thirty-one,
#  Saving February alone,
#  Which has twenty-eight, rain or shine.
#  And on leap years, twenty-nine.
#  A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# total days in each month
months = [
  31, # jan
  28, # feb
  31, # mar
  30, # apr
  31, # may
  30, # jun
  31, # jul
  31, # ago
  30, # sep
  31, # oct
  30, # nov
  31  # dec
]

# current values
year = 1900
month = 1
day = 1
weekday = 1 # monday

# total sundays
sundays = 0

def is_leap_year(year):
  return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

while year <= 2000:
  # go through the days of the month
  day += 1

  # handle february special case
  month_days = months[month - 1]
  if month == 2 and is_leap_year(year):
    month_days += 1

  # reset days and go to next month
  if day > month_days:
    # start new month
    day = 1
    month += 1

    if month > 12:
      # start next year
      month = 1
      year += 1


  # go through the days of the week
  weekday += 1
  if weekday > 7:
    # reset to monday
    weekday = 1

  if year > 1900 and weekday == 7 and day == 1:
    sundays += 1




print sundays
