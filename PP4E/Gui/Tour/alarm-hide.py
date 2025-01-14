# стирает и отображает кнопку в обработчике, устанавливаемом методом after()

from tkinter import *
import alarm


class Alarm(alarm.Alarm):               # измените обработчик таймера
    def __init__(self, msecs=1000):     # по умолчанию = 1 секунда
        self.shown = False
        alarm.Alarm.__init__(self, msecs)

    def repeater(self): # каждые N миллисекунд
        self.bell()             # подать сигнал
        if self.shown:
            self.stopper.pack_forget()  # скрыть кнопку
        else:                       # или изменить цвет, мигнуть...
            self.stopper.pack()
            self.shown = not self.shown # изменить до следующего раза
            self.after(self.msecs, self.repeater)   # переустановить обработчик


if __name__ == '__main__':
    Alarm(msecs=500).mainloop()
