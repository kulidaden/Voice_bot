
def search_query(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


# def listen_and_search():
#     recognizer = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         print("Скажіть, що ви хочете знайти:")
#         audio = recognizer.listen(source)
#
#     try:
#         query = recognizer.recognize_google(audio, language="uk-UA")
#         print(f"Ви сказали: {query}")
#         search_query(query)
#     except sr.UnknownValueError:
#         print("Не вдалося розпізнати мову")
#     except sr.RequestError as e:
#         print(f"Помилка при запросі до Google Speech Recognition: {e}")
#
# if __name__ == "__main__":
#     listen_and_search()