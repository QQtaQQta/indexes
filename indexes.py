string = input("Введите строку: ")

third_char = string[2]
print("Третий символ:", third_char)

penultimate_char = string[-2]
print("Предпоследний символ:", penultimate_char)

first_five_chars = string[:5]
print("Первые пять символов:", first_five_chars)

without_last_two_chars = string[:-2]
print("Строка без последних двух символов:", without_last_two_chars)

even_index_chars = string[::2]
print("Символы с четными индексами:", even_index_chars)

odd_index_chars = string[1::2]
print("Символы с нечетными индексами:", odd_index_chars)

reverse_string = string[::-1]
print("Символы в обратном порядке:", reverse_string)

reverse_every_other_char = string[::-2]
print("Символы через один в обратном порядке:", reverse_every_other_char)

string_length = len(string)
print("Длина строки:", string_length)