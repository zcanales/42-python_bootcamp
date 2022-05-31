import time
from random import randint

def log(func):
    def aux(*args, **kwarg):
    #    with open("machine.log", "a") as file:
        file = open("machine.log", "a")
        begin = time.time()
        if not callable(func):
            print("Not callable")
            return False
        return_value = func(*args, **kwarg)
        exec_time = time.time() - begin
        unit= "s"
        if exec_time < 0.5:
            exec_time *= 1000
            unit = "ms"
        s = func.__name__
        s = s.replace("_", " ")
        file.write(f"(cmaxime)Running: {s.title()}      [exec-time = {exec_time:.3f} {unit}\n")
        file.close()
            #file.close() si ponemo with no hay que cerrar se asegurel de cerrar
            #print(f"Return value-> {return_value}")
            #devolver el valor de la function
        return return_value
    return aux

class CoffeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    @log 
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):  
                time.sleep(0.1)
                self.water_level -= 1
        print(self.boil_water())
        print("Coffe is ready!")
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)