import os
import sqlite3

from importings import *

#
# def open_program_in_directories(program_name, directories=["E:\\", "D:\\", "C:\\", os.path.expanduser("~")]):
#     # Лічильник перевірених файлів
#     checked_files = 0
#
#     for directory in directories:
#         print(f"\nПеревірка директорії: {directory}")
#
#         for root, dirs, files in os.walk(directory):
#             # print(f"Шлях: {root}")
#             # print(f"Файли: {files}")
#
#             if program_name in files:
#                 program_path = os.path.join(root, program_name)
#                 try:
#                     subprocess.Popen([program_path])
#                     checked_files += 1
#                     print(
#                         f"Запущено програму '{program_name}' за шляхом: {program_path} ({checked_files} файлів перевірено)")
#                     # Тут ви можете використовувати program_path, якщо потрібно зробити щось з шляхом
#                     return  # Зупинити пошук після знаходження програми
#                 except Exception as e:
#                     print(f"Помилка: {e}")
#
#     if checked_files == 0:
#         print(f"Програма '{program_name}' не знайдена в жодній директорії. ({checked_files} файлів перевірено)")

def search_query(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)



conn=sqlite3.connect('DataBase_V/test.db')


def open_item_on_desktop(item_name):
    item_name=item_name.title()
    cursor = conn.cursor()
    cmd_way = f'SELECT way FROM test WHERE words="{item_name}"'
    cursor.execute(cmd_way)
    result = cursor.fetchone()
    if result:
        program_path = result[0]  # Отримання шляху з результату запиту
        zak = ['.lnk', '.exe', '.xlsx', '.txt', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp3', '.mp4', '.docx']

        file_path = None
        for i in zak:
            current_path = f'{program_path}\\{item_name}{i}'
            if os.path.exists(current_path):
                file_path = current_path
                break  # Вийти з циклу, якщо знайдено файл
            else:
                current_path=f"{program_path}\\{item_name}"
                if os.path.exists(current_path):
                    file_path=current_path
                    break

        if file_path:
            try:
                os.startfile(file_path)
                print(f"Відкрито програму: {file_path}")
            except Exception as e:
                print(f"Помилка при відкритті програми: {e}")
        else:
            print("Файл не знайдено")
    else:
        print("НЕ ЗНАЙШОВ У БД")
        item_name = item_name.strip().title()
        taskbar_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Internet Explorer', 'Quick Launch', 'User Pinned', 'TaskBar')
        main_desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        public_desktop_path = os.path.join(os.path.join(os.environ['PUBLIC']), "Desktop")
        desktop_paths = [main_desktop_path, public_desktop_path, taskbar_path, 'D:\\', 'C:\\']
        for desktop_path in desktop_paths:
            if os.path.exists(desktop_path):
                for root, dirs, files in os.walk(desktop_path):
                    for current_item_name in files + dirs:
                        current_item_path = os.path.join(root, current_item_name)
                        try:
                            current_item_name_without_extension, current_item_extension = os.path.splitext(current_item_name.strip())
                            if current_item_name_without_extension.lower() == item_name.lower():
                                if current_item_extension.lower() == '.lnk':
                                    shell = win32com.client.Dispatch("WScript.Shell")
                                    shortcut = shell.CreateShortCut(current_item_path)
                                    item_to_open = shortcut.Targetpath
                                else:
                                    item_to_open = current_item_path
                                if os.path.isdir(item_to_open) or current_item_extension.lower() in (
                                        '.lnk', '.exe', '.xlsx', '.txt', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mp3', '.mp4', '.docx'):
                                    os.startfile(item_to_open)
                                    # Вставляйте в базу даних лише в разі успішного відкриття
                                    cmd1 = f'''INSERT INTO test (words, way) VALUES ('{item_name}','{root}')'''
                                    conn.execute(cmd1)
                                    conn.commit()
                                    print(f"Відкрито {item_name} з робочого столу.")
                                    return
                                elif os.path.isdir(item_to_open) or current_item_extension.lower():
                                    os.startfile(item_to_open)
                                    cmd1 = f'''INSERT INTO test (words, way) VALUES ('{item_name}','{root}')'''
                                    conn.execute(cmd1)
                                    conn.commit()
                                    print(f"Відкрито {item_name} з робочого столу.")
                                    return
                                else:
                                    print(f"Не вдається визначити тип {item_name}.")
                                    return
                        except Exception as e:
                            print(f"Помилка відкриття {item_name}: {e}")
        print(f"{item_name} не знайдено на робочому столі або в директоріях C або D.")
