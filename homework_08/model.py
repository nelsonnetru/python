def AddItemToDB(item: list, DB_name: str):
	with open(DB_name, 'a', encoding='UTF-8') as file:
		if type(item) is list:
			file.writelines(str(item)[1:-1] + "\n")
			return True
	return False


def SolveID(DB_name: str):
	try:
		with open(DB_name, 'r', encoding='UTF-8') as file:
			for line in file:
				pass
			a = line.split(", ")
			new_id = int(a[0]) + 1
			return new_id
	except:
		return 0


def FindInDB(DB_name: str, query: str):
	try:
		res_list = []
		with open(DB_name, 'r', encoding='UTF-8') as file:
			for line in file:
				if query.lower() in line.lower(): 
					res_list.append(line)
		if len(res_list) > 0:
			return res_list
		else:
			return False
	except:
		return False


def CountContacts(DB_name: str):
	try:
		count = 0
		with open(DB_name, 'r', encoding='UTF-8') as file:
			for line in file:
				count += 1
			return count
	except:
		return 0


def PrintByTemplateMain(main_dict):
	output_string = ''
	for key in main_dict.keys():
		output_string += key + ": " + main_dict[key] + "\n"
	return output_string


def PrintByTemplateItem(item_str: str):
	item = item_str.replace("\n", "").split(", ")
	return(f'[{item[0]}]: {item[1][1:-1]} {item[2][1:-1]}: {item[3][1:-1]}')


def PrintByTemplateMainMap(input_map: dict):
	output_string = ''
	for key in input_map.keys():
		if key == "id": output_string += "[" + input_map[key][0] + "]: "
		elif key == "phone": output_string += ": " + input_map[key][0] + " "
		else:
			output_string += input_map[key][0] + " "
	return output_string + "\n"


def ReadItemsFromDB(DB_name: str):
	try:
		with open(DB_name, 'r', encoding='UTF-8') as file:
			data = file.readlines()
		return data
	except:
		return False

def ReadOneItem(DB_name: str, ID: int):
	items = ReadItemsFromDB(DB_name)
	if items:
		for item in items:
			a = item.split(", ")
			if int(a[0]) == ID:
				return item
	else:
		return False

def DeleteByID(DB_name: str, ID: int):
	items = ReadItemsFromDB(DB_name)
	if items:
		try:
			with open(DB_name, 'w', encoding='UTF-8') as file:
				for item in items:
					a = item.split(", ")
					if int(a[0]) != ID:
						file.write(item)
			return True	
		except:
			return False
