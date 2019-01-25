from Player import Player


class Quiz(Player):
    players = []

    def __init__(self, num_c):
        for i in range(num_c):
            self.players.append(Player())

    def PrintGameStatus(self):
        for _Player in self.players:
            print(_Player)
        return

    def WhoAnswers(self):
        ok = False
        while 1:
            for _Player in self.players:
                if _Player._Buzz.Premuto():
                    print(_Player.Name)
                    self.ValidateAnswer(_Player)
                    ok = True
                    break
            if ok:
                break
        return

    def ValidateAnswer(self, __Player):
        if str(input("Is the answer correct? [y/n]: ")) == "y":
            __Player.RightAnswer()
            print("Right answer...")
        else:
            print("Wrong answer...")
        __Player._Buzz.NextQuestion()
        return
