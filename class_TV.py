class TV:
    def __init__(self):
        self.state = Switch_off(self)
        self.chanel = '1+1'
    def switch_on(self):
        self.state.switch_on()
    def switch_off(self):
        self.state.switch_off()

    def change_channel(self, channel):
        self.state.change_channel(channel)

class State:
    def switch_on(self):
        print("Cannot switch on TV")
    def switch_off(self):
        print('Cannot switch off TV')
    def change_channel(self, channel):
        print('Cannot change channel')

class Switch_off(State):
    def __init__(self, tv):
        self.tv = tv

    def switch_on(self):
        self.tv.state = Switch_on(self.tv)

class Switch_on(State):
    def __init__(self, tv):
        self.tv = tv

    def switch_off(self):
        self.tv.state = Switch_off(self.tv)

    def change_channel(self, channel):
        self.tv.chanel = channel

def main():
    tv = TV()
    tv.switch_off()
    tv.change_channel('Inter')
    tv.switch_on()
    tv.change_channel('S')

main()