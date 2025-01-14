"""
читает данные из канала в отдельном потоке выполнения и помещает их в очередь,
которая проверяется в цикле обработки событий от таймера; позволяет сценарию
отображать вывод программы, не вызывая блокирование графического интерфейса
между операциями вывода; со стороны дочерних программ не требуется выполнять
подключение или выталкивать буферы, но данное решение сложнее, чем подход на
основе сокетов
"""

import _thread as thread, queue, os
from tkinter import Tk
from PP4E.Gui.Tools.guiStreams import GuiOutput
stdoutQueue = queue.Queue()     # бесконечной длины


def producer(input):
    while True:
        line = input.readline()     # блокирование не страшно: дочерний поток
        stdoutQueue.put(line)       # пустая строка - конец файла
        if not line:
            break


def consumer(output, root, term='<end>'):
    try:
        line = stdoutQueue.get(block=False) # главный поток: проверять очередь
    except queue.Empty:                     # 4 раза в сек, это нормально,
        pass                                # если очередь пуста
    else:
        if not line:            # остановить цикл по достижении конца файла
            output.write(term)  # иначе отобразить следующую строку
            return
        output.write(line)
    root.after(250, lambda: consumer(output, root, term))


def redirectedGuiShellCmd(command, root):
    input = os.popen(command, 'r')              # запустить программу командной строки
    output = GuiOutput(root)
    thread.start_new_thread(producer, (input,)) # запустить поток чтения
    consumer(output, root)


if __name__ == '__main__':
    win = Tk()
    redirectedGuiShellCmd('python -u pipe-nongui.py', win)
    win.mainloop()
