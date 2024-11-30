import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        soldier = 100
        for i in range(100):
            soldier -= self.power
            print(f'{self.name} сражается {i + 1}(дня)..., осталось {soldier} воинов.')
            if soldier == 0:
                print(f'{self.name} одержал победу спустя {i + 1} дней(дня)')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
