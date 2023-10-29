def fib():
  a, b = 0, 1
  n = int(input('Enter a value to print Fibonacci series:'))
  while a < n:
    print(a, end='')
    a, b = b, a + b


print('1.Fibonacci series using function and control flow statements')
print('2.string manipulations')
ch = int(input('Enter a option value'))
if ch == 1:
  fib()
elif ch == 2:
  str1 = input(
      'Enter a string to find length of string and change capitalize=')
  print('Given string length is=', len(str1))
  print('Given string first letter is capital=', str1.capitalize())
  str2 = "Hello"
  str3 = input("Enter a string (your name to append a string=")
  str2 += str3
  print("Append string is=", str2)
else:
  print("wrong option")
