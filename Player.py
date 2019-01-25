from Quiz_Buzz import Buzz


class Player(Buzz):
    Points = 0

    def __init__(self):
        self.Name = input("Insert player's name : ")
        Pin1 = int(input("Insert button pin: "))
        Pin2 = int(input("Insert LED pin: "))
        self._Buzz = Buzz(Pin1, Pin2)

    def RightAnswer(self):
        self.Points = self.Points+1
        return

    def __str__(self):
        return str(self.Name)+" "+str(self.Points)
