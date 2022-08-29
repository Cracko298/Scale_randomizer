while True:
 import random


 set = input("What Set of scales would you like? Major or minor?\n")

 if set == "Major" or "major":
   scale =  random.randint(1, 12)
 elif set == "Minor" or "minor":
   scale =  random.randint(13, 24)
 else:
   print("please enter scale set again")



 if scale == 1:
    print("C major")
 elif scale == 2:
  print("Db major")
 elif scale == 3:
   print("D major")
 elif scale == 4:
  print("Eb major")
 elif scale == 5:
  print("E major")
 elif scale == 6:
  print("F major")
 elif scale == 7:
  print("F# major")
 elif scale == 8:
  print("G major")
 elif scale == 9:
  print("Ab major")
 elif scale == 10:
  print("A major")
 elif scale == 11:
  print("Bb major")
 elif scale == 12:
  print("B major")
 elif scale == 13:
  print("C minor")
 elif scale == 14:
  print("C# minor")
#hehe c# hehe
 elif scale == 15:
  print("D minor")
 elif scale == 16:
  print("Eb minor")
 elif scale == 17:
  print("E minor")
 elif scale == 18:
  print("F minor")
 elif scale == 19:
  print("F# minor")
 elif scale == 20:
  print("G minor")
 elif scale == 21:
  print("G# minor")
 elif scale == 22:
  print("A minor")
 elif scale == 23:
  print("Bb minor")
 elif scale == 24:
  print("B minor")
 else:
  print("Error:Unexpected integer")

 restart = input("Again? Y/n \n")
 if restart == "Y" or "y":
    continue    
 elif restart == "n" or "N":
  exit()
 else:
  print("?")
