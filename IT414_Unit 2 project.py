def add_numbers(number1, number2):
  return number1 + number2

def input_gather():
	number1 = float(input("Enter the first number: "))
	number2 = float(input("Enter the second number: "))
	result = add_numbers(number1, number2)
	print("The sum of the two numbers is:", result)

def test_add_numbers():
  assert add_numbers(1, 6) == 7
  assert add_numbers(2, 5) == 7
  assert add_numbers(7, 5) == 12
  print ("Number verification passed!")
  
input_gather()
test_add_numbers()