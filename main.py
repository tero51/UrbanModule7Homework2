def custom_write(file_name, strings):
    string_position = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            byte_position = file.tell()
            file.write(string + '\n')
            string_position[(line_number, byte_position)] = string
    return string_position

if __name__ == "__main__":
    info = [
        'Text для tell.',
        'Use кодировку utf-8.',
        'Потому что there are 2 languages!',
        'Спасибо sweetie!'
    ]

    result = custom_write('text.txt', info)
    for elem in result.items():
        print(elem)