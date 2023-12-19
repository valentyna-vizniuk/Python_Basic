# Ваше завдання написати функцію, яка прочитає заданий файл,
# очистить текст від html-тегів і запише цей текст в інший файл.
# html-тег завжди починається з "<" і закінчується на ">" тобто
# потрібно видалити ці символи та все, що між ними.
# Функція отримує на вхід два параметри – ім'я файлу,
# який потрібно очистити, та ім'я файлу, куди потрібно записати очищений текст.
# Ім'я файлу, куди потрібно писати, можна задати за замовчуванням.
# Приклади файлів у вкладенні – файл який потрібно очистити (draft.html)
# та приклад файлу, який може вийти на виході з очищеним текстом.
# Файл draft.html необхідно скачати і покласти поряд з файлом, де буде вирішення цієї домашки.

import codecs

def delete_html_tags(html_file,result_file):
    with codecs.open(html_file,'r','utf-8') as file:
        text = file.read()
        cleaned_text = ''

        inside_tag = False
        for i in text:
            if i == '<':
                inside_tag = True
            elif i == '>':
                inside_tag= False
            elif not inside_tag:
                cleaned_text += i
        with open(result_file, 'w') as out_file:
            out_file.write(cleaned_text)
        print(f'Очищено з файлу {html_file} та збежено у файлі {result_file} ')

file_HW31 = open('HW31.txt', 'w')
delete_html_tags('draft.html', 'HW31.txt')
