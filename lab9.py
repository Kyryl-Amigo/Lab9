def create_file(filename, lines):
    """Функція для створення текстового файлу з заданими рядками."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
    except IOError:
        print("Помилка при створенні файлу.")


def process_file(input_file, output_file):
    """Функція для читання, видалення цифр та запису по 10 символів у рядок."""
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = ''.join(filter(lambda x: not x.isdigit(), content))
        
        with open(output_file, 'w', encoding='utf-8') as file:
            for i in range(0, len(content), 10):
                file.write(content[i:i+10] + '\n')
                
    except IOError:
        print("Помилка при обробці файлу.")


def read_and_print_file(filename):
    """Функція для читання та виведення вмісту файлу по рядках."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    except IOError:
        print("Помилка при читанні файлу.")


lines = ["Це перший рядок123", "Другий рядок456", "Третій рядок7890 з текстом"]
create_file("TF10_1.txt", lines)
process_file("TF10_1.txt", "TF10_2.txt")
print("Вміст файла TF10_2:")
read_and_print_file("TF10_2.txt")
