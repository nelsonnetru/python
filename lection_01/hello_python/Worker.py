class Worker:
	id: int
	full_name: str
	salary: int
	age: int
	dep_id: str

def __init__(self, id: int, full_name: str, salary: int, age: int, dep_id: str) -> None:
	self.id = id;
	self.full_name = full_name
	self.salary = salary
	self.age = age
	self.dep_id = dep_id

def __repr__(self) -> str:
	return f'id: {self.id}, full_name: {self.full_name}, salary: {self.salary}, age: {self.age}, dep_id{self.dep_id}'
