'''
Создайте файл "test_file.txt" с тестовым текстом:

"It's a text for task Найти везде,
Используйте его для самопроверки.
Успехов в решении задачи!
text text text"
'''

class WordsFinder:                                              # Напишите класс WordsFinder
    def __init__(self, *file_names):                            # *file_names: Неограниченное количество названий файлов.
        self.file_names = file_names                            # Сохраняем названия файлов в атрибуте класса

    def get_all_words(self):                                    # подготовительный метод
        all_words = {}                                          # Создаем пустой словарь для хранения результатов
        for file_name in self.file_names:                       # перебираем названия файлов
            with open(file_name, 'r', encoding='utf-8') as file:# Открываем файл с помощью оператора 'with' (автоматическое закрытие файла)
                words = []                                      # Список для хранения слов из текущего файла
                for line in file:                               # Читаем файл построчно
                    line = line.lower()                         # Приводим строку к нижнему регистру
                    punctuation = [',', '.', '=', '!', '?', ';', ':']# Убираем пунктуацию
                    for i in punctuation:
                        line = line.replace(i, '')
                    line = line.replace(' - ', ' ')
                    words += line.split()                       # Разбиваем эту строку на элементы списка методом split()
                all_words[file_name] = words
        return all_words                                        # Возвращаем полученный словарь

    def find(self, word):
        word = word.lower()                                     # Приводим искомое слово к нижнему регистру
        result = {}                                             # Создаем словарь для хранения результатов
        all_words = self.get_all_words()                        # Получаем все слова из файлов
        for file_name, words in all_words.items():              # Проходим по словарю all_words
            if word in words:                                   # Проверяем, есть ли слово в списке
                result[file_name] = words.index(word) + 1       # Записываем позицию (1-индексация)
        return result                                           # Возвращаем словарь с результатами

    def count(self, word):
        word = word.lower()                                     # Приводим искомое слово к нижнему регистру
        result = {}                                             # Создаем словарь для хранения результатов
        all_words = self.get_all_words()                        # Получаем все слова из файлов
        for file_name, words in all_words.items():              # Проходим по словарю all_words
            count = words.count(word)                           # Считаем количество вхождений слова
            if count > 0:                                       # Если слово встречается в файле
                result[file_name] = count                       # Записываем количество в словарь
        return result                                           # Возвращаем словарь с результатами

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())                                  # Вывод всех слов
print(finder2.find('TEXT'))                                     # Поиск позиции слова 'text'
print(finder2.count('teXT'))                                    # Подсчет количества слова 'text'