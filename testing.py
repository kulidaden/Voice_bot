# import webbrowser
# from googlesearch import search
#
#
# def open_first_search_result(query,num_site):
#     try:
#         # Використовуємо бібліотеку googlesearch для отримання результатів пошуку
#         search_results = list(search(query, num_results=1, lang='en'))
#
#         # Відкриваємо перший результат у браузері
#         if search_results:
#             webbrowser.open(search_results[num_site])
#         else:
#             print("Пошук не дав результатів.")
#     except Exception as e:
#         print(f"Помилка: {e}")
#
#
# # Приклад виклику функції

# text = "відкрий перший сайт"
#
# for command in search_google:
#     if command in text:
#         # Видаляємо команду з тексту
#         result = text.replace(command, '').strip()
#
#         # Викликаємо функцію для відкриття першого сайту
#         open_first_search_result(result,text)
#         break


import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import webbrowser
from googlesearch import search

# Отримання HTML-коду сторінки
url = "https://www.google.com/search?q=танки"
response = requests.get(url)
html_content = response.text

# Витягнення текстового вмісту з HTML-коду
soup = BeautifulSoup(html_content, 'html.parser')
text_content = soup.get_text()

# Розпізнавання мови
recognizer = sr.Recognizer()

def get_voice_command():
    with sr.Microphone() as source:
        print("Скажіть що-небудь...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="uk-UA").lower()
        return command
    except sr.UnknownValueError:
        print("Не розпізнано команду.")
        get_voice_command()
    except sr.RequestError as e:
        print(f"Помилка при розпізнаванні мови: {e}")
        get_voice_command()

# Відкриття першого сайту з результатів пошуку
def open_first_search_result(query,rt=0):
    search_results = list(search(query, num_results=10, lang='uk'))
    print(search_results)
    if search_results:
        webbrowser.open(search_results[rt])
        return True
    else:
        print("Пошук не дав результатів.")
        return False



# Виклик функції обробки команд
open_first_search_result('танки',5)