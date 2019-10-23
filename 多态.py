#! /usr/bin/env python
#coding:utf-8


class Bob:
    def bow(self):
        print("thank you")
    def drive(self):
        print("beep")
    def speak(self):
        print("hello")
class Cat:
    def speak(self):
        print("moni")
class Dog:
    def speak(self):
        print("ncdsk")
def command(pet):
    pet.speak()
pets=[Cat(),Dog(),Bob()]

for pet in pets:
    command(pet)




