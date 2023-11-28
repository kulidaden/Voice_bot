from sound import *
from functions import *
from importings import *

recognizer = sr.Recognizer()

search_google=["Найди в інтернеті","Найди у інтернеті","Найди в google","Найди у Google","Найди в Google","Найди у google",
               "Найди в chrome","Найди у chrome","Найди в Chrome","Найди у Chrome",
               "Погугли", "Пошукай у гуглі","Пошукай в гуглі",
                "Пошукай у google","Пошукай в Google","Пошукай у Google","Пошукай в google",
               "Пошукай у chrome","Пошукай в chrome","Пошукай у Chrome","Пошукай в Chrome",
               "Забий у google","Забий у Google","Забий в google","Забий в Google",
                "Забий у google","Забий у Google","Забий в google","Забий в Google",
                "Забий у Гуглі","Забий у гуглі","Забий в гуглі","Забий в Гуглі",
               "Знайди у гуглі","Знайди у Гуглі","Знайди в гуглі","Знайди в Гуглі",
                "Знайди у Google","Знайди у google","Знайди в Google","Знайди в google",
                "найди в інтернеті","найди у інтернеті","найди в google","найди у Google","найди в Google","найди у google",
               "найди в chrome","найди у chrome","найди в Chrome","найди у Chrome",
               "погугли", "пошукай у Гуглі","пошукай в Гуглі","пошукай у інтернеті","пошукай в інтернеті",
                "пошукай у google","пошукай в Google","пошукай у Google","пошукай в google",
               "пошукай у chrome","пошукай в chrome","пошукай у Chrome","пошукай в Chrome",
               "забий у google","забий у Google","забий в google","забий в Google",
                "забий у google","забий у Google","забий в google","забий в Google",
                "забий у Гуглі","забий у гуглі","забий в гуглі","забий в Гуглі",
               "знайди у гуглі","знайди у Гуглі","знайди в гуглі","знайди в Гуглі",
                "знайди у Google","знайди у google","знайди в Google","знайди в google"
                "найди", "погугли", "пошукай", "забий",'знайти', "знайди","google", "гуглі","chrome"
                "Найди", "Погугли","Пошукай", "Забий", 'Знайти', "Знайди", "Google", "Гуглі", "Chrome"
               ]

search_youtube=['Пошукай в Ютубі ','Пошукай у Ютубі ','Знайди в Ютубі ','Знайди у Ютубі ',
                'Забий в Ютубі ','Забий у Ютубі ','Найди в Ютубі ','Найди у Ютубі ',
                'У Ютубі пошукай ','В Ютубі пошукай ','У Ютубі знайди ','В Ютубі знайди ',
                'У Ютубі забий ','В Ютубі забий ','У Ютубі найди ','В Ютубі найди ',
                "У Ютубі ", "В Ютубі ",'пошукай в Ютубі ','пошукай у Ютубі ','знайди в Ютубі ','знайди у Ютубі ',
                'забий в Ютубі ','забий у Ютубі ','найди в Ютубі ','найди у Ютубі ',
                'у Ютубі пошукай ','в Ютубі пошукай ','у Ютубі знайди ','в Ютубі знайди ',
                'у Ютубі забий ','в Ютубі забий ','у Ютубі найди ','в Ютубі найди ',
                "у Ютубі ", "в Ютубі "]

comp_slowar=["Запусти мені","Включи мені","Відкрий мені","Открий мені","Запусти","Включи","Відкрий","Открий",
             "запусти мені","включи мені","відкрий мені","открий мені","запусти","включи","відкрий","открий"]

password = (1,2,3)

def mu():
    while True:
        # EnterPassword()
        # with sr.Microphone() as source:
        #     print("Скажіть пароль!")
        #     audio = recognizer.listen(source)
        # try:
        #     text = recognizer.recognize_google(audio, language="uk-UA")
        #     text = text.lower()
        #     print(f"Розпізнанний текст: {text}")
        #     if text == '1 2 3':
                while True:
                    IlistenYou()

                    def voice():
                        with sr.Microphone() as source:
                            print("Скажіть що-небудь...")
                            audio = recognizer.listen(source)
                        try:
                            text = recognizer.recognize_google(audio, language="uk-UA")
                            print(f"Розпізнанний текст: {text}")
                            flag = 0
                            # це для ютуба
                            for command in search_youtube:
                                if command in text:
                                    open()
                                    for i in search_youtube:
                                        if i in text:
                                            result = text.replace(i, '')
                                            print(result)
                                            break
                                    url = "https://www.youtube.com/results?search_query=" + '+' + result
                                    webbrowser.open(url)
                                    voice()
                            #це для гугла
                            for command in search_google:
                                if command in text:
                                    open()
                                    for i in search_google:
                                        if i in text:
                                            result = text.replace(i, '')
                                            print(result)
                                            break
                                    url = "https://www.google.com/search?q=" + '+' + result
                                    webbrowser.open(url)
                                    voice()
                            for command in comp_slowar:
                                if command in text:
                                    open()
                                    for i in comp_slowar:
                                        if i in text:
                                            result = text.replace(i, '')
                                            break
                                    result=result.title()
                                    result=result.strip()
                                    print(result)
                                    open_item_on_desktop(result)
                                    voice()
                            #це для готових команд
                            # for word in text.split():
                            #     if word in slowar:
                            #         open()
                            #         slowar[word][0](slowar[word][1])
                            #         flag = 1
                            #         voice()
                            if "Припини роботу" in text:
                                flag = 2
                                see_you()
                                sys.exit()
                            if flag == 0:
                                UnknownComand()
                            voice()

                        except sr.UnknownValueError:
                            dontUnderstedebl()
                            voice()
                        except sr.RequestError as e:
                            print(f"Ошибка при запросе к Google Web Speech API: {e}")

                    voice()
            # else:
            #     InvalidPassword()
        # except sr.UnknownValueError:
        #         dontUnderstedebl()


hello()
mu()
