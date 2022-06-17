from random import randint
import quantumrandom

x = True
randJokeNum = int(quantumrandom.randint(0, 15))
scienceJokeList = []
mathJokeList = []

def fileReader(fileName, topicList):
  topicList = []
  my_file = open(fileName, "r")
  content = my_file.read()
  topicList = content.split("/")
  my_file.close()
  return topicList
def jokeReader(listName, fileName):
  listName = fileReader(fileName, listName)
  randJokeNum = int(quantumrandom.randint(0, 15))
  print(listName[randJokeNum])

while True:
  while x:
    joke = input("Do you want to hear a joke? Type y/n: ")
    if joke == "n" or joke == "y":
      if joke == "n": quit()
      if joke == "y":
        categ = input("Category (math or science): ")
        if categ == "science":
          jokeReader(scienceJokeList, "sciencejokes.txt")
        elif categ == "math":
          jokeReader(mathJokeList, "mathjokes.txt")
        else:
          print("Error! Restarting")
          x = False
          break
    else:
      print("Error! Restarting")
      x = False
      break
  x = True
  

