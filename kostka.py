#!/usr/bin/env python3
#pecina

import random

class Kostka:

    def __init__(self, steny=6):
        self.__pocet_sten = steny

    def __str__(self):
        return f'Kostka s {self.__pocet_sten} stenami.'

    def hod(self):
        return random.randint(1,self.__pocet_sten)

    def getPocetSten(self):
        return self.__pocet_sten
k1 = Kostka(220)
print(k1)
print(k1.getPocetSten()+10)
print(k1.hod())
k2 = Kostka()
print(k2.hod())




















