class Fruit:
    def __init__(self, color='绿色'):
        Fruit.color = color

    def harvest(self, color):
        print("水果是:", color, "的!")
        print("水果已经收获......")
        print("水果原来是:", Fruit.color, '的!')


class Apple(Fruit):
    color = '红色'

    def __init__(self):
        print("窝是苹果")
        super().__init__()


class Aapodilla(Fruit):
    def __init__(self, color):
        print("\n窝是人参果")
        super().__init__(color)

    def harvest(self, color):
        print("人参果是:", color, "的!")
        print("人参果已经收获......")
        print("人参果原来是:", Fruit.color, '的!')


apple = Apple()
apple.harvest(apple.color)
sapodilla = Aapodilla('白色')
sapodilla.harvest('金黄色带紫色条纹')
