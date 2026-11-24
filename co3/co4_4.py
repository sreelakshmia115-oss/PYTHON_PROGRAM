class time:
    def __init__(self, hr, min, sec):
        self.__hour = hr
        self.__minute = min
        self.__second = sec

    def __add__(self, other):
        sec = self.__second + other.__second
        minute = self.__minute + other.__minute
        hour = self.__hour + other.__hour

        if sec >= 60:
            minute += 1
            sec -= 60

        if minute >= 60:
            hour += 1
            minute -= 60

        return time(hour, minute, sec)

    def display(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)


t1 = time(2, 45, 50)
t2 = time(3, 30, 25)

t3 = t1 + t2

print("Sum of two times:")
t3.display()