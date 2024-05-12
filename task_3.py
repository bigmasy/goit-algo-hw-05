import timeit


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено




def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    # Створюємо таблицю зсувів для патерну (підрядка)
    shift_table = build_shift_table(pattern)
    i = 0  # Ініціалізуємо початковий індекс для основного тексту

    # Проходимо по основному тексту, порівнюючи з підрядком
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # Починаємо з кінця підрядка

        # Порівнюємо символи від кінця підрядка до його початку
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Зсуваємось до початку підрядка

        # Якщо весь підрядок збігається, повертаємо його позицію в тексті
        if j < 0:
            return i  # Підрядок знайдено

        # Зсуваємо індекс i на основі таблиці зсувів
        # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    # Якщо підрядок не знайдено, повертаємо -1
    return -1



def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Базове число для хешування та модуль
    base = 256 
    modulus = 101  
    
    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


with open('article_1.txt', 'r') as file:
    article_1_text = file.read()


with open('article_2.txt', 'r') as file:
    article_2_text = file.read()



existing_pattern_article_1 = 'позиції для відомого елемента'
existing_pattern_article_2 = 'Бінарні діаграми рішень'
fake_pattern = 'вигаданий рядок ййй'

print('Стаття 1:')
print('Боєра-Мура (існуючий підрядок):', timeit.timeit(lambda: boyer_moore_search(article_1_text, existing_pattern_article_1), number=1000))
print('Боєра-Мура (вигаданий підрядок):', timeit.timeit(lambda: boyer_moore_search(article_1_text, fake_pattern), number=1000))

print('Кнута-Морріса-Пратта (існуючий підрядок):', timeit.timeit(lambda: kmp_search(article_1_text, existing_pattern_article_1), number=1000))
print('Кнута-Морріса-Пратта (вигаданий підрядок):', timeit.timeit(lambda: kmp_search(article_1_text, fake_pattern), number=1000))

print('Рабіна-Карпа (існуючий підрядок):', timeit.timeit(lambda: rabin_karp_search(article_1_text, existing_pattern_article_1), number=1000))
print('Рабіна-Карпа (вигаданий підрядок):', timeit.timeit(lambda: rabin_karp_search(article_1_text, fake_pattern), number=1000))


print('Стаття 2:')
print('Боєра-Мура (існуючий підрядок):', timeit.timeit(lambda: boyer_moore_search(article_2_text, existing_pattern_article_2), number=1000))
print('Боєра-Мура (вигаданий підрядок):', timeit.timeit(lambda: boyer_moore_search(article_2_text, fake_pattern), number=1000))

print('Кнута-Морріса-Пратта (існуючий підрядок):', timeit.timeit(lambda: kmp_search(article_2_text, existing_pattern_article_2), number=1000))
print('Кнута-Морріса-Пратта (вигаданий підрядок):', timeit.timeit(lambda: kmp_search(article_2_text, fake_pattern), number=1000))

print('Рабіна-Карпа (існуючий підрядок):', timeit.timeit(lambda: rabin_karp_search(article_2_text, existing_pattern_article_2), number=1000))
print('Рабіна-Карпа (вигаданий підрядок):', timeit.timeit(lambda: rabin_karp_search(article_2_text, fake_pattern), number=1000))
