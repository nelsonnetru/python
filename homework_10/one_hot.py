'''
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит 
всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это 
сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

'''

import random, pprint

lst = ['robot'] * 5
lst += ['human'] * 5
lst += ['animal'] * 5
random.shuffle(lst)

data = {'whoAmI' : lst}
pprint.pprint(data['whoAmI'])
print() 

cat = set(data['whoAmI'])
pprint.pprint(cat)
print()

onehot_encode = [{z: 0 for z in cat} for x in range(len(data['whoAmI']))]

for item in enumerate(data['whoAmI']):
	onehot_encode[item[0]][item[1]] = 1

pprint.pprint (onehot_encode)
