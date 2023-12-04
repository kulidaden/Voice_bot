from sound import *
from importings import *
from functions import *
from slowars import *

recognizer = sr.Recognizer()

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
                    # IlistenYou()
                    def voice():
                        global result1
                        global search_results
                        with sr.Microphone() as source:
                            print("Скажіть що-небудь...")
                            audio = recognizer.listen(source)

                        try:
                            text = recognizer.recognize_google(audio, language="uk-UA")
                            print(f"Розпізнанний текст: {text.lower()}")
                            flag = 0
                            # це для ютуба
                            for command in search_youtube:
                                if command in text:
                                    open()
                                    result = text.replace(command, '')
                                    print(result)
                                    url = "https://www.youtube.com/results?search_query=" + '+' + result
                                    webbrowser.open(url)
                                    voice()
                            #це для гугла
                            for command in search_google:
                                if command in text:
                                    open()
                                    result1 = text.replace(command, '')
                                    print(result1)
                                    url = "https://www.google.com/search?q=" + '+' + result1
                                    search_results = list(search(url, num_results=10, lang='uk'))
                                    print(search_results)
                                    webbrowser.open(url)
                                    result1=result1
                                    print(result1)
                                    voice()


                            for command in search_google_0:
                                if command in text:
                                    print(result1)
                                    print(search_results)
                                    webbrowser.open(search_results[search_google_0[command]])

                            # для пошуку у ПК
                            for command in comp_slowar:
                                if command in text:
                                    open()
                                    result = text.replace(command, '')
                                    result=result.title()
                                    result=result.strip()
                                    print(result)
                                    open_item_on_desktop(result)
                                    voice()
                            #скріншот
                            for command in screenshot:
                                if command in text:
                                    screen()
                                    voice()
                            #чат ГПТ
                            for command in znach:
                                if command in text:
                                    open()
                                    url = "https://chat.openai.com/"
                                    webbrowser.open(url)
                                    voice()
                            #повертає назад вкладку в гуглі
                            for command in res_wkl_0:
                                if command in text:
                                    res_wkl()
                                    voice()
                            #закрийває вкладку
                            for command in close_wkl_0:
                                if command in text:
                                    close_wkl()
                                    voice()
                            #відкриває нову вкладку
                            for command in open_wkl_0:
                                if command in text:
                                    open_wkl()
                                    voice()
                            #закриває все(Alt+f4)
                            for command in close_0:
                                if command in text:
                                    close()
                                    voice()
                            #звертає поточну програму
                            for command in zverni_0:
                                if command in text:
                                    zverni()
                                    voice()
                            #вимокає/вмикає звук
                            for command in valume_on_off_0:
                                if command in text:
                                    valume_on_off()
                                    voice()
                            #запис відео
                            for command in scr_video:
                                if command in text:
                                    scr_videos()
                                    voice()
                            #вимокає/вмикає мікрофон
                            for command in micro_0:
                                if command in text:
                                    micro()
                                    voice()

                            for command in open_first_site:
                                if command in text:

                                    openFirstSite()
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
                            if 'Сплячий режим' in text or 'Спящий режим' in text or 'сплячий режим' in text or 'спящий режим' in text:
                                dont_listen()
                                voice()
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
