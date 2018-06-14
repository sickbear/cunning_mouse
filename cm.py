# -*- coding: utf-8 -*-
import time
import sys
from unix import PyMouse

if __name__ == '__main__':
    
    def startScript(minutes):
        print('--- Скрипт запущен на %s минут ---' % minutes)
        mouse = PyMouse()
        for i in range(1, minutes + 1):
            mouse.click(600, 600, 1)
            time.sleep(15)
            mouse.click(600, 800, 1)
            time.sleep(15)
            mouse.click(800, 800, 1)
            time.sleep(15)
            mouse.click(800, 600, 1)
            time.sleep(15)
            print('Прошло %s минут' % i)
        print('--- Конец ---')
    
    def checkParam(param):
        try: 
            int(param)
            return True
        except ValueError:
            return False 
        
    status = True
    
    if len(sys.argv) > 1:
        if checkParam(sys.argv[1]):
            work_time = int(sys.argv[1])
        else:
            print('Введён неверный тип параметра')
            status = False
    else:
        work_time = 1

    if status:
        startScript(work_time)