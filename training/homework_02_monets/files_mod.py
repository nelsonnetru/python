def WriteToFile(data):
	file = open('data.txt', 'a')
	if type(data) is list:
		file.writelines(data)
	else:
		file.write(data)
	file.close()

def ReadFromFile():
	with open('data.txt', 'r') as file:
		for line in file:
			print (line.strip())

def ReadFromFileMonets():
	with open('data.txt', 'r') as file:
		print ('Данные из файла:')
		i = 1
		for line in file:
			print('\n\n' + '-'*10 + f' набор {i} ' + '-'*10)
			monetsStringList = line.strip()[1:-1].split(', ')
			monetsIntList = [int(i) for i in monetsStringList]
			monets.ReadMonets(monetsIntList)
			i += 1


if __name__ == '__main__':
	#WriteToFile('строка 2\n')
	#ReadFromFile()
	import monets
	ReadFromFileMonets()

	
