"""
Открывает три новых окна со стилями
метод destroy() закрывает одно окно, метод quit() закрывает все окна и завершает
приложение (прерывает работу функции mainloop);
окна верхнего уровня имеют заголовки, значки, могут сворачиваться
и восстанавливаться и поддерживают протокол событий wm;
приложение всегда имеет корневое окно, создаваемое по умолчанию или явно,
вызовом конструктора Tk(); все окна верхнего уровня являются контейнерами,
но они никогда не размещаются с помощью менеджера компоновки; объект Toplevel
напоминает фрейм Frame, но в действительности является новым окном и может иметь
собственное меню;
"""

from tkinter import *

root = Tk()  # explicit root

trees = [('The Larch!', 'light blue'),
            ('The Pine!', 'light green'),
            ('The Giant Redwood!', 'red')]
for (tree, color) in trees:                         # новое окно
    win = Toplevel(root)                            # установка границ
    win.title('Sing...')                            # игнорировать закрытие
    win.protocol('WM_DELETE_WINDOW', lambda: None)  #  вместо значка Tk
    win.iconbitmap('py-blue-trans-out.ico')
    msg = Button(win, text=tree, command=win.destroy) # закрывает одно окно
    msg.pack(expand=YES, fill=BOTH)
    msg.config(padx=10, pady=10, bd=10, relief=RAISED)
    msg.config(bg='black', fg=color, font=('times', 30, 'bold italic'))

root.title('Lumberjack demo')
Label(root, text='Main window', width=30).pack()
Button(root, text='Quit All', command=root.quit).pack()     # завершает программу
root.mainloop()
