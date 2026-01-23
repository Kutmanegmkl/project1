import requests
from bs4 import BeautifulSoup
import json

# URL сайта для парсинга
url = "http://books.toscrape.com/" # Это тестовый сайт 

# Делаем запрос к сайту
print("Загружаем страницу...")
response = requests.get(url)

# Проверяем что запрос успешный
if response.status_code == 200:
    print("✓ Страница загружена успешно!")
else:
    print(f"✗ Ошибка: {response.status_code}")
    exit()

# Создаем объект BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Список для хранения всех книг
books = []

# Ищем все карточки книг на странице
book_cards = soup.find_all('article', class_='product_pod')

print(f"\nНайдено книг: {len(book_cards)}")
print("\nПарсим данные...\n")

# Проходим по каждой карточке
for card in book_cards:
    # Создаем словарь для одной книги
    book = {}
    
    # Название книги
    title = card.find('h3').find('a')
    book['название'] = title['title']
    
    # Цена
    price = card.find('p', class_='price_color')
    book['цена'] = price.text
    
    # Наличие
    availability = card.find('p', class_='instock availability')
    book['в_наличии'] = availability.text.strip()
    
    # Рейтинг (в виде звезд)
    rating = card.find('p', class_='star-rating')
    book['рейтинг'] = rating['class'][1]  # One, Two, Three, Four, Five
    
    # Ссылка на книгу
    link = card.find('h3').find('a')['href']
    book['ссылка'] = url + link
    
    # Изображение
    img = card.find('img')
    book['изображение'] = url + img['src']
    
    # Добавляем книгу в список
    books.append(book)
    
    # Выводим информацию
    print(f"📖 {book['название']}")
    print(f"   Цена: {book['цена']}")
    print(f"   Рейтинг: {book['рейтинг']}")
    print(f"   {book['в_наличии']}")
    print()

# Сохраняем в JSON файл
filename = 'books.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=2)

print("="*60)
print(f"✓ Парсинг завершен!")
print(f"✓ Всего книг: {len(books)}")
print(f"✓ Данные сохранены в файл: {filename}")
print("="*60)

# Выводим пример первой книги
print("\nПример данных (первая книга):")
print(json.dumps(books[0], ensure_ascii=False, indent=2))


