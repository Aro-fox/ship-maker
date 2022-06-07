import random

list = ["Julian ", "Aj ", "monkey man ", "rojam ", "Caitanya ", "Drew ", "Gracie ", "Gynx ", "Isaiah ", "Jacksie Wacksie ", "JONathan ", "Lamp <3 ", "Michael ", "Noah ", "Potu ", "Russell ", "Tay ", "Teddy ",]
wordGoal = "1234"
wordSize = 2
word = ""
finished = False




while True:
  for _ in range(wordSize):
      word = word + random.choice(list)
  print("--ship" + " " + word)
  if word == wordGoal:
      break
  word = ""
