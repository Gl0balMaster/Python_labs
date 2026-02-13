"""
написать класс птички
наследники виды птиц
продемоонстрировать наследование, переопрееделение и свое исключение
несколько своих методов, несколько общих, несколько переопределять
обязательно польз ввод и свое исключение
методы
полет
гнездо
петь
"""


from abc import ABC, abstractmethod

def colorInput():
    color = list()
    print("Введите цвет в формате RGB\n")
    for _ in range(3):
        char = int(input(f"Введите {_ + 1} цвет\n"))
        color.append(char)
    return color

class ColorException(Exception):
    pass

class InputException(Exception):
    pass

class Birds(ABC):
    BIRD_COLOR = tuple()
    can_fly = bool
    can_build = bool
    can_sing = bool


    def __init__(self, bird_color):
        try:
            for _ in bird_color:
                if not 0 < _ < 255:
                    raise ColorException
        except ColorException as ex:
            print(f"обработано исключение {ex, type(ex)}")


        except ValueError as e:
            print(f"обработано исключение {e, type(e)}")


    def canBuildNest(self):
        if self.can_build:
            print(f"{type(self)} строит гнезда")
        else:
            print(f"{type(self)} не строит гнезда")


    def canSing(self):
        if self.can_sing:
            print(f"{type(self)} умеет петь")
        else:
            print(f"{type(self)} не умеет петь")


    def canFly(self):
        if self.can_fly:
            print(f"{type(self)} умеет летать")
        else:
            print(f"{type(self)} не умеет летать")

    def birdType(self):
        print(type(self))
        return type(self)

    def birdColor(self):
        print(f"RGB цвет: {self.birdColor}")
        return Birds.BIRD_COLOR

    @abstractmethod
    def useAll(self):
        self.canFly()
        self.canBuildNest()
        self.canSing()

class Parrot(Birds):

    BIRD_COLOR = tuple()
    can_fly = True
    can_build = True
    can_sing = True

    def __init__(self, bird_color):
        super(Parrot,self).__init__(bird_color)
        self.birdColor = bird_color

    def unique_colors(self):
        print(f"{(type(self))} имеют много разных окрасов")

    def useAll(self):
        super(Parrot,self).useAll()
        self.unique_colors()

class Chicken(Birds):
    BIRD_COLOR = tuple()
    can_fly = False
    can_build = True
    can_sing = False


    def __init__(self, bird_color):
        super(Chicken,self).__init__(bird_color)

    def used_in_farms(self):
        print(f"{type(self)} выращивают на фермах")

    def eatableEggs(self):
        print(f"яйца {type(self)} едят")

    def useAll(self):
        super(Chicken,self).useAll()
        self.eatableEggs()
        self.used_in_farms()

class Pigeon(Birds):

    can_fly = True
    can_build = True
    can_sing = False

    def __init__(self,bird_color):
        super(Pigeon,self).__init__(bird_color)

    def stays_at_home(self):
        print(f"{type(self)} не улетает на зиму")

    def useAll(self):
        super(Pigeon,self).useAll()
        self.stays_at_home()

# RGB = (255,255,256)




select = int()
while True:
    try:
        select = int(input("Какую птицу создать?\n"
                           "1. Попугай\n"
                           "2. Курица\n"
                           "3. Голубь\n"
                           "4. Выход\n"))
        if select == 1:
            bird = Parrot(colorInput())
            bird.useAll()
        elif select == 2:
            bird = Chicken(colorInput())
            bird.useAll()
        elif select == 3:
            bird = Pigeon(colorInput())
            bird.useAll()
        elif select == 4:
            break
        else:
            raise InputException
    except InputException as e:
        print(f"{e,type(e)}")
        break
    input("Нажмите любую клавишу чтобы продолжить...")







