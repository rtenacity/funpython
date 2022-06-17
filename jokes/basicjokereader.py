#uses jokes.txt
from random import randint

randJokeNumber = randint(0,15)

sciencejokelist = []

def fileReader(fileName, topicList):
  topicList = []
  my_file = open(fileName, "r")
  content = my_file.read()
  topicList = content.split("/")
  my_file.close()
  return topicList

sciencejokefunc = fileReader("jokes.txt", sciencejokelist)
print(sciencejokefunc[randJokeNumber])
