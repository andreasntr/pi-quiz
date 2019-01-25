from gpiozero import Button, LED


class Buzz:
    def __init__(self, BtnPin, LedPin):
        self.Btn = Button(BtnPin)
        self.Led = LED(LedPin)

    def Premuto(self):
        if self.Btn.is_pressed:
            self.Led.on()
            return True
        return False

    def NextQuestion(self):
        self.Led.off()
        return
