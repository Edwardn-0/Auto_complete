import tkinter as tk
from collections import Counter

window = tk.Tk()
window.title("auto maker")
window.geometry("290x300+100+100")

rv = tk.IntVar()

def load_text(name):
    with open(name, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    return lines

def clear_text(lst):
    return list(set(lst))

def path_setting(data):
    global database
    global loaded_text
    global cleared_text
    database = data
    loaded_text = load_text(database)
    cleared_text = clear_text(loaded_text) #리스트
    listbox.delete(0, len(cleared_text)+100)

def write_text(text):
    cleared_text.append(text)
    str = '\n'.join(cleared_text)
    file = open(database, 'w')
    file.write(str)
    file.close()

def searching():
    listbox.delete(0, len(cleared_text))
    find_data = searcher.get()
    for word in cleared_text:
        if word.startswith(find_data):
            listbox.insert(0, word)

def saving():
    find_data = searcher.get()
    write_text(find_data)

searcher = tk.Entry(window)
check = tk.Button(window, text='searching' ,command=searching)
save = tk.Button(window, text='save', command=saving)
listbox = tk.Listbox(window, selectmode='extended', height=14)


def set_up():
    set = setting.get()
    text = 'D:/system\문서\code\Database\\'+set+'.txt'
    path_setting(text)

setting = tk.Entry(window)
setting_confirm = tk.Button(window, text='confirm', command=set_up)

searcher.place(x=50, y=35)
check.place(x=200, y=35)
save.place(x=200, y=65)
listbox.place(x=50, y=60)

setting.place(x=50, y=0)
setting_confirm.place(x=200, y=0)



window.mainloop()