while True:
	ans = input('用除法請按1，用乘法請按2，求平方請按3，求開根號請按4，用加法請按5，用減法請按6，離開請按7。')
	if ans == '1':
		number1 = float(input('請輸入被除數：'))
		number2 = float(input('請輸入除數：'))
		anser = number1/number2
		print('答案是',anser)

	if ans == '2':
		number1 = float(input('請輸入被乘數：'))
		number2 = float(input('請輸入乘數：'))
		anser = number1*number2
		print('答案是',anser)

	if ans == '3':
		number = int(input('請輸入數字：'))
		anser = number*number
		print(number,'的平方是',anser)
	if ans == '4':	
		import math
		try:
			number = float(input('請輸入數字：'))
			if number <= 0:
				print('請輸入正數。')
			else:
				answer = math.sqrt(number)
				print(f'{number}的平方根是{answer}。')
		except ValueError:
			print('錯誤：請輸入有效的數字')		

	if ans == '5':
		try:
			number = int(input('請輸入x＋y的x。'))
			number2 = int(input('請輸入y。'))
			answer = number+number2
			print(f'答案是{answer}。')

		except ValueError:
			print('錯誤：請輸入有效的數字')





	if ans == '6':
		try:
			number1 = int(input('請輸入x-y的x。'))
			number2 = int(input('請輸入y。'))
			answer = number1 - number2
			print(f'答案是{answer}。')
		except ValueError:
			print('錯誤：請輸入有效的數字')



	if ans == '7':
		break
	
