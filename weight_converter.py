try:
	user_weight = int(input("Weight: "))
	user_input = input("(L)bs or (K)g: ")
	if user_input == "K":
		conversion = user_weight * 2.205
		print(f'your weight in pounds is {conversion}lb')
	else:
		conversion = user_weight // 2.205
		print(f'your weight in kilograms is {conversion}kg')
except ValueError:
	print("Sorry you made an invalid input")
