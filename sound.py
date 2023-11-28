from importings import *

def hello():
    pygame.init()
    sound = pygame.mixer.Sound("звук/привіт!.mp3")
    sound.play()
    duration_seconds = 3
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

def open():
    pygame.init()
    sound = pygame.mixer.Sound("звук/окей_вмикаю.mp3")
    sound.play()
    duration_seconds = 3
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

def see_you():
    pygame.init()
    sound = pygame.mixer.Sound("звук/хай_щастить!.mp3")
    sound.play()
    duration_seconds = 3
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

def music(adres):
    pygame.init()
    sound = pygame.mixer.Sound(adres)
    sound.play()
    duration_seconds = 5
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

def dontUnderstedebl():
    pygame.init()
    sound = pygame.mixer.Sound("звук/не_зрозумів.mp3")
    sound.play()
    duration_seconds = 5
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

def EnterPassword():
    pygame.init()
    sound = pygame.mixer.Sound("звук/для_користування_програмою_нада_пароль.mp3")
    sound.play()
    duration_seconds = 5
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

def IlistenYou():
    pygame.init()
    sound = pygame.mixer.Sound("звук/я-вас-слухаю.mp3")
    sound.play()
    duration_seconds = 5
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

# def WichPassword():
#     pygame.init()
#     sound = pygame.mixer.Sound("звук/який-пароль-встановити.mp3")
#     sound.play()
#     duration_seconds = 5
#     duration_milliseconds = duration_seconds * 1000
#     pygame.time.wait(duration_milliseconds)
#     pygame.quit()

def InvalidPassword():
    pygame.init()
    sound = pygame.mixer.Sound("звук/пароль-не-правильний.mp3")
    sound.play()
    duration_seconds = 5
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

def UnknownComand():
    pygame.init()
    sound = pygame.mixer.Sound("звук/не-знаю-команду.mp3")
    sound.play()
    duration_seconds = 5
    duration_milliseconds = duration_seconds * 1000
    pygame.time.wait(duration_milliseconds)
    pygame.quit()

