import threading 
import time

class NumberPrintingThread(threading.Thread):
    def __init__(self, n ,sleeptime):
        threading.Thread.__init__(self)
        self.__n= n
        self.__sleeptime= sleeptime
    
    def run(self):
        for i in range(1, self.__n):
            print(f"Number: " + str(i))
            time.sleep(self.__sleeptime)

class CharacterPrintingThread(threading.Thread):
    def __init__(self, n ,sleeptime):
        threading.Thread.__init__(self)
        self.__n= n
        self.__sleeptime= sleeptime
    
    def run(self):
        start_char= "A"
        for i in range(1, self.__n):
            print(f"Letter: " + chr(ord(start_char)+i))
            time.sleep(self.__sleeptime)


if __name__ == "__main__":
    #create instances
    thread_numbers= NumberPrintingThread(n=7, sleeptime=1)
    thread_chars=  CharacterPrintingThread(n=10, sleeptime=1)
    
    thread_numbers.start()
    thread_chars.start()
    thread_numbers.join() #terminate 
    thread_chars.join() 


#2 printing tasks with delay between each print