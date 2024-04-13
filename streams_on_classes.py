import threading
import time


# Создаем класс профессионального рыцаря, наследуемый от класса threading.Thread
class Knight(threading.Thread):
    def __init__(self, name, skill):
        threading.Thread.__init__(self)
        self.name = name
        self.skill = skill

    def run(self):
        print(self.name + ", на нас напали!")
        count = 100
        day = 1

        while count > 0:
            print(self.name + ", сражается " + str(day) + " день(дня)..., осталось " + str(count) + " воинов.")
            count -= self.skill
            day += 1
            time.sleep(1)

        print(self.name + " одержал победу спустя " + str(day - 1) + " дней!")


if __name__ == "__main__":
    # Создаем двух рыцарей с разными навыками
    knight1 = Knight("sir lancelot", 10)
    knight2 = Knight("sir galahad", 20)

    # Запускаем каждого рыцаря в отдельном потоке
    knight1.start()
    knight2.start()

    # Ожидаем завершения каждого потока перед выводом сообщения
    knight1.join()
    knight2.join()

    # Все битвы закончились
    print("все битвы закончились!")
