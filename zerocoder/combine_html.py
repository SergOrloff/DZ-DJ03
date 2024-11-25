# Список ваших HTML-файлов
html_files = ['about.html', 'base.html', 'contact.html', 'footer.html', 'home.html', 'menu.html', 'services.html', 'add_news.html', 'news.html', 'news_detail.html']

# Имя результирующего текстового файла
output_file = 'combined.txt'

# Открываем результирующий файл для записи
with open(output_file, 'w', encoding='utf-8') as outfile:
    for fname in html_files:
        with open(fname, 'r', encoding='utf-8') as infile:
            # Читаем содержимое текущего HTML-файла и записываем в результирующий файл
            outfile.write(infile.read())
            outfile.write("\n")  # Добавляем перевод строки между файлами

print(f"Объединение завершено. Результат сохранен в {output_file}.")