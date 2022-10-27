from random import randint
from time import sleep
from os import system

list0 = ['Major', 'major', 'MAJOR']
list1 = ['Minor', 'minor', 'MINOR']
listY = ['Yes', 'yes', 'y', 'Y']
listN = ['No', 'no', 'n', 'N']


def MusicNotes():
  question = input("What Scale Would You Like? ('Major' or 'Minor'): ")
  print(" ")

  if question in list0:  # Major Scales Below
    major1 = randint(0, 12)
    if major1 == 1:
      print("C Major")
    if major1 == 2:
      print("Db Major")
    if major1 == 3:
      print("D Major")
    if major1 == 4:
      print("Eb Major")
    if major1 == 5:
      print("E Major")
    if major1 == 6:
      print("F Major")
    if major1 == 7:
      print("F# Major")
    if major1 == 8:
      print("G Major")
    if major1 == 9:
      print("Ab Major")
    if major1 == 10:
      print("A Major")
    if major1 == 11:
      print("Bb Major")
    if major1 == 12:
      print("B Major")

  if question in list1:  # Minor Scales Below
    minor1 = randint(13, 24)
    if minor1 == 13:
      print("C Minor")
    if minor1 == 14:
      print("C# Minor")
    if minor1 == 15:
      print("D Minor")
    if minor1 == 16:
      print("Eb Minor")
    if minor1 == 17:
      print("E Minor")
    if minor1 == 18:
      print("F Minor")
    if minor1 == 19:
      print("F# Minor")
    if minor1 == 20:
      print("G Minor")
    if minor1 == 21:
      print("G# Minor")
    if minor1 == 22:
      print("A Minor")
    if minor1 == 23:
      print("Bb Minor")
    if minor1 == 24:
      print("B Minor")
  if question not in list0:
    if question not in list1:
      print("Invalid Response To Privided Question.")
      sleep(2)
      system('clear')
      MusicNotes()

  sleep(2)
  print(" ")
  yesorno = input("Would Your Like to Restart? ('Yes' or 'No'): ")

  if yesorno in listN:
    sleep(1)
    exit()
  if yesorno in listY:
    sleep(1)
    system('clear')
    MusicNotes()


MusicNotes()
