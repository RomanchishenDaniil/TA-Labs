import math

WORDS = ["ЛЮДИНА", "БЕЗ", "РІДНОГО", "КРАЮ", "ЯК", "СОЛОВЕЙ", "ГНІЗДА"]
A_CONST = (math.sqrt(5) - 1) / 2

ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
LETTER_POSITIONS = {char: idx + 1 for idx, char in enumerate(ALPHABET)}

def get_key(word: str) -> int:
	return sum(LETTER_POSITIONS.get(char, 0) for char in word.upper())

def hash_division(key: int, m: int) -> int:
	return key % m

def hash_multiplication(key: int, m: int) -> int:
	return math.floor(m * ((key * A_CONST) % 1))

def build_closed_hash_table(words: list, m: int, hash_func) -> list:
	hash_table = [None] * m
	
	for word in words:
		key = get_key(word)
		start_address = hash_func(key, m)
		
		for i in range(m):
			address = (start_address + i) % m
			if hash_table[address] is None:
				hash_table[address] = word
				break
		else:
			print(f"Помилка: Таблиця заповнена. Не вдалося додати слово: {word}")
			
	return hash_table

def display_closed_hash_table(table: list, method_name: str):
	print(f"\n--- Хеш-таблиця (Відкрита адресація, {method_name}, M={len(table)}) ---")
	print("Індекс | Слово")
	print("-" * 20)
	for i, item in enumerate(table):
		value = item if item is not None else "(NULL)"
		print(f"{i:02d}     | {value}")

hash_table_div_closed = build_closed_hash_table(WORDS, 13, hash_division)
display_closed_hash_table(hash_table_div_closed, "Метод ділення")

hash_table_mul_closed = build_closed_hash_table(WORDS, 16, hash_multiplication)
display_closed_hash_table(hash_table_mul_closed, "Метод множення")
