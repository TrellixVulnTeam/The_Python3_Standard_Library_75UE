# сценарий командной строки: действует как обычно, не требует выполнения
# дополнительных операций
import time
while True:                 # реализация сценария командной строки
    print(time.asctime())   # отправить процессу GUI
    time.sleep(2.0)         # выталкивать буфер здесь не требуется