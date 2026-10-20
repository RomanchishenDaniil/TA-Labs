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

def build_open_hash_table(words: list, m: int, hash_func) -> list:
	hash_table = [[] for _ in range(m)]
	for word in words:
		key = get_key(word)
		address = hash_func(key, m)
		hash_table[address].append(word)
	return hash_table

def display_hash_table(table: list, method_name: str):
	print(f"\n--- Результат хешування ({method_name}, M={len(table)}) ---")
	for i, chain in enumerate(table):
		print(f"Індекс {i:02d}: {chain}")

hash_table_div = build_open_hash_table(WORDS, 13, hash_division)
display_hash_table(hash_table_div, "Метод ділення")

hash_table_mul = build_open_hash_table(WORDS, 16, hash_multiplication)
display_hash_table(hash_table_mul, "Метод множення")
