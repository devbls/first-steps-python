class Television:
    def __init__(self, channel, min, max):
        self.channel = channel
        self.min = min
        self.max = max

    def change_channel_down(self):
        if self.channel - 1 >= self.min:
            self.channel -= 1
        else:
            self.channel = self.max

    def change_channel_up(self):
        if self.channel + 1 <= self.max:
            self.channel += 1
        else:
            self.channel = self.min

tv1 = Television(2, 2, 10)
print(tv1.channel)
for x in range(1, 20):
    tv1.change_channel_up()
    print(tv1.channel)

tv2 = Television(10, 2, 10)
print(tv2.channel)
for x in range(1, 20):
    tv2.change_channel_down()
    print(tv2.channel)