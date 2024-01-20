"""
class Animal:
    def __init__(self, birthType="Unknowm", appearance="Unknown", blooded="Unknown"):
        self.birthType = birthType
        self.appearance = appearance
        self.blooded = blooded

    @property
    def birthType(self):
        return self.__birthType

    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__, self.birthType, self.appearance, self.blooded)

class Mammal(Animal):
    def __init__(self, birthType="Born Alive", appearance="hair or fur", blooded="warm blooded", nurseYoung=True):
        Animal.__init__(self, birthType, appearance, blooded)
        self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__() + " and it is {} they nurse" "there young".format(self.nurseYoung)
    
class Reptile(Animal):
    def __init__(self, birthType="born in an egg or born alive", appearance="dry scales", blooded="cold blooded"):
        Animal.__init__(self, birthType, appearance, blooded)

    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i

        return sum
    
def main():
    Animal1 = Animal("born Alive")
    print(Animal1.birthType)

    print(Animal1)
    print()

    Mammal1 = Mammal()

    print(Mammal1.birthType)
    print(Mammal1.appearance)
    print(Mammal1.blooded)
    print(Mammal1.nurseYoung)
    print(Mammal1)
    print()

    reptile1 = Reptile()

    print(reptile1.birthType)
    print(reptile1)
    print("Sum : {}".format(reptile1.sumAll(1,2,3,4,5)))

main()
"""


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)
    
    def __add__(self, other_time):
        new_time = Time()

        # Add the seconds and correct if sum > 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second - other_time.second

        # Add the minutes and correct if sum is > 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.miute) - 60
        else:
            new_time.minute = self.minute - other_time.minute

        # Add the hours and correct if sum is > 24
        if (self.hour + other_time.hour) > 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour
        return new_time
def main():
    time1 = Time(1, 20, 30)
    print(time1)
    
main()