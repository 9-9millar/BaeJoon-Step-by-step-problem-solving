Leap_Year = int(input())

if (Leap_Year % 4 == 0 and Leap_Year % 100 != 0) or Leap_Year % 400 == 0:
    print('1')
else:
    print('0')
    