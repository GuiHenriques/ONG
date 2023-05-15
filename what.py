class Animal:

    def sleep(self):
        return "This animal is sleeping"

class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")
        print(self.sleep())


rab = Rabbit()
rab.run()