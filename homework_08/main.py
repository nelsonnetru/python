import controller, model
import sys 

DB_filename = 'database.txt'

main_map = 	{	'1': 'Добавить запись',
				'2': 'Просмотр справочника',
				'3': 'Поиск',
				'4': 'Изменить запись',
				'5': 'Удалить запись',
				'0': 'Выход'
			}

input_map = 	{	'id': 			['ID', 'auto'], 
					'name': 		['Имя', 'notEmpty', 'не должно быть пустым'], 
					'second_name':	['Отчество', ''],
					'phone':		['Номер телефона', 'notEmpty numeric', "должно быть числом"]
				}


if __name__ == "__main__":
	while True:
		print("="*10 + " ТЕЛЕФОННЫЙ СПРАВОЧНИК " + "="*10 + "\n")
		items_count = model.CountContacts(DB_filename)
		print(f"Записей в справочнике: {items_count}\n\n")

		print(model.PrintByTemplateMain(main_map))
		setDo = input("\n\nВыберите действие: ")

		if setDo == '1':
			print("-"*10 + " " + main_map[setDo] + " " + "-"*10 + "\n")
			result = controller.AddContact(input_map, DB_filename)

			if result: print ("Запись успешно добавлена в телефонный справочник")
			else: print ("Ошибка! Не удалось добавить запись в файл")

		elif setDo == '2':
			print("-"*10 + " " + main_map[setDo] + " " + "-"*10 + "\n")
			if not controller.ReadContacts(input_map, DB_filename):
				print ("Ошибка! Невозможно вывести список")

		elif setDo == '3':
			print("-"*10 + " " + main_map[setDo] + " " + "-"*10 + "\n")
			if not controller.SearchContacts(input_map, DB_filename):
				print ("Ошибка! Невозможно осуществить поиск")

		elif setDo == '4':
			print("-"*10 + " " + main_map[setDo] + " " + "-"*10 + "\n")
			result = controller.EditContact(input_map, DB_filename)

			if result: print ("Запись изменена")
			else: print ("Ошибка! Невозможно изменить запись")

		elif setDo == '5':
			print("-"*10 + " " + main_map[setDo] + " " + "-"*10 + "\n")
			result = controller.DeleteContact(DB_filename)
			
			if result: print ("Запись удалена")
			else: print ("Ошибка! Невозможно удалить запись")

		elif setDo == '0' or setDo == '':
			sys.exit()

		input('\nнажмите Enter...')