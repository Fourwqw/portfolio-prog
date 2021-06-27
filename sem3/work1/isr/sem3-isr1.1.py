"""
		Кузнецов Антон Денисович 
		ИВТ 1.1, 2 курс
		Задание: Вывод таблицы истинности для не A  
"""
header = "- A -- not A -"
tmpLen =  len(" not A ")
dot = "-"
A = [1, 0]
print(dot * len(header) +"\n" + header + 
     "\n" + dot * len(header))
print(dot + " " + str(A[0]) + " " + dot*2 +
	 tmpLen // 2 * " " + str(int(not A[0])) + tmpLen // 2 * " " + dot +
	 "\n" + dot * len(header) +"\n" +
	 dot + " " + str(A[1]) + " " + dot*2 +
	 tmpLen // 2 * " " + str(int(not A[1])) + tmpLen // 2 * " " + dot 
	 + "\n" + dot * len(header) +"\n")
input()  