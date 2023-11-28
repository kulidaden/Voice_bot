import os
import win32com.client
import sqlite3

conn = sqlite3.connect('DataBase/test.db')

def open_item_on_desktop(item_name):
    # item_name=item_name.title()
    cursor = conn.cursor()
    cmd_way = f'SELECT way FROM test WHERE words="{item_name}"'
    cursor.execute(cmd_way)
    result = cursor.fetchone()
    if result:
        program_path = result[0]  # Отримання шляху з результату запиту
        os.startfile(program_path+f'\\{item_name}')
        print(f"Запущено програму за шляхом: {program_path}")
    else:
        print(32)
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
                                else:
                                    print(f"Не вдається визначити тип {item_name}.")
                                    return
                        except Exception as e:
                            print(f"Помилка відкриття {item_name}: {e}")
        print(f"{item_name} не знайдено на робочому столі або в директоріях C або D.")


open_item_on_desktop("деградація")
