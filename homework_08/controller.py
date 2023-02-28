﻿import model

def InputData(input_map: list):
	result_list = []
	for key in input_map.keys():
		if 'auto' in input_map[key][1]: continue

		item = input(f'Введите {input_map[key][0]}: ')

		if 'notEmpty' in input_map[key][1] and item == '':
			print(f'Значение поля \"{input_map[key][0]}\" не может быть пустым!')
			return False

		elif 'numeric' in input_map[key][1] and not item.isdigit():
			print(f'Значение поля \"{input_map[key][0]}\" должно содержать только цифры!')
			return False

		else:
			result_list.append(item.strip())

	return result_list


def AddContact(input_map: list, DB_filename: str):
	item_ID = model.SolveID(DB_filename)
	item = [item_ID]

	input_data = InputData(input_map)
	
	if type(input_data) is list: 
		item += input_data

		if model.AddItemToDB(item, DB_filename): 
			return True
	return False


def ReadContacts(headers: dict, DB_filename: str):
	result = model.ReadItemsFromDB(DB_filename)
	if result:
		print(model.PrintByTemplateMainMap(headers)+"\n")
		for res in result:
			print(model.PrintByTemplateItem(res))
		return True

	else:
		return False


def DeleteContact(DB_filename: str):
	try:
		id_del = int(input("\n\nВведите [id] контакта для удаления: "))
		return model.DeleteByID(DB_filename, id_del)
	except:
		return False


def SearchContacts(headers: dict, DB_filename: str):
	search_map = {'query': ['значение для поиска', 'notEmpty', 'не должно быть пустым']} 
	input_data = InputData(search_map)
	
	if type(input_data) is list: 
		result = model.FindInDB(DB_filename, input_data[0])

		if type(result) is list:
			print(f"Найдено {len(result)} записей.")
			print("\n\n" + model.PrintByTemplateMainMap(headers)+"\n")

			for item in result:
				print(model.PrintByTemplateItem(item))
		else:
			print("Ничего не найдено")

		return True
	return False


def EditContact(input_map: list, DB_filename: str):
	try:
		id_edit = int(input("\n\nВведите [id] контакта для редактирования: "))
		item = model.ReadOneItem(DB_filename, id_edit)
		if item:
			print(model.PrintByTemplateItem(item))
			print("Редактирование: ")

			edited_item = [id_edit]
			input_data = InputData(input_map)

			if type(input_data) is list: 
				edited_item += input_data
				if model.DeleteByID(DB_filename, id_edit):
					if model.AddItemToDB(edited_item, DB_filename): 
						return True
		return False

	except:
		return False