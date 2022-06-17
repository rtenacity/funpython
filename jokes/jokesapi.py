import pyjokes
x = True
while True:
  while x:
    joke = input("Do you want to hear a joke? Type y/n: ")
    if joke == "n" or joke == "y":
      if joke == "n": quit()
      if joke == "y":
        lang = input("Language: ")
        if lang == "en" or lang == "es" or lang == "it" or lang == "de":
          categ = input("Category: "  )
          if categ == "neutral" or categ == "all":
            My_joke = pyjokes.get_joke(language=lang, category=categ)
            print(My_joke)
            x = False
            break
          else:
            print("Error! Restarting")
            x = False
            break
        else:
          print("Error! Restarting")
          x = False
          break
    else:
      print("Error! Restarting")
      x = False
      break
  x = True
