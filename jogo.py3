weapon = False

def strangeCreature():
  actions = ["lutar","correr"]
  global weapon
  print("Uma estranha criatura humanóide apareceu. Você pode correr ou lutar. O que você gostaria de fazer?")
  userInput = ""
  while userInput not in actions:
    print("opções: lutar/correr")
    userInput = input()
    if userInput == "lutar":
      if weapon:
        print("Você mata a criatura com a faca que encontrou anteriormente. Depois de seguir em frente, você encontra uma das saídas. Parabéns!")
      else:
        print("A criatura te matou.")
        quit()
    elif userInput == "correr":
      showSkeletons()
    else:
      print("por favor, digite uma opção valida.")

def showSkeletons():
  directions = ["trás","frente"]
  global weapon
  print("Você vê uma parede de esqueletos quando entra na sala. Alguém está observando você. Onde você gostaria de ir?")
  userInput = ""
  while userInput not in directions:
    print("opções: esquerda/trás/frente")
    userInput = "" 
    if userInput == "esquerda":
      print("Você descobre que esta porta se abre para uma parede. Você abre parte do drywall para descobrir uma faca.") 
      weapon = True
    elif userInput == "trás":
      introScene()
    elif userInput == "frente":
      strangeCreature()
    else:
      print("por favor, digite uma opção valida.")

def hauntedRoom():
  directions = ["direita","esquerda","trás"]
  print("Você ouve vozes estranhas. Você acha que acordou alguns dos mortos. Onde você gostaria de ir?")
  userInput = ""
  while userInput not in directions:
    print("opções: direita/esquerda/trás")
    userInput = input()
    if userInput == "direita":
      print("Várias criaturas semelhantes a humanóides começam a surgir quando você entra na sala. Você está morto.")
      quit()
    elif userInput == "trás":
      introScene()
    else:
      print("por favor, digite uma opção valida.")

def cameraScene():
  directions = ["frente","trás"]
  print("Você vê uma câmera que caiu no chão. Alguém esteve aqui recentemente. Onde você gostaria de ir?")
  userInput = ""
  while userInput not in directions:
    print("opções: frente/trás")
    userInput = input()
    if userInput == "frente":
      print("Você conseguiu! Você encontrou uma saída.")
    elif userInput == "trás":
      showShadowFigure()
    else:
      print("por favor, digite uma opção valida.")

def showShadowFigure():
  directions = ["direita","trás"]
  print("Você vê uma figura sombria e escura aparecer à distância. Você está assustado. Onde você gostaria de ir?")
  userInput = ""
  while userInput not in  directions:
    print("opções: direita/esquerda/trás")
    userInput = input()
    if userInput == "direita":
      cameraScene()
    elif userInput == "esquerda":
      print("essa porta dá de cara com a parede..")
    elif userInput == "trás":
      introScene()
    else:
      print("por favor, digite uma opção valida.")

def introScene():
  directions = ["left","right","forward"]
  print("Você está em uma encruzilhada, e pode escolher ir para qualquer uma das 4 direções. Pra onde você vai?")
  userInput = ""
  while userInput not in directions:
      print("Opções: esquerda/direita/trás/frente")
      userInput = input()
      if userInput == "esquerda":
        showShadowFigure()
      elif userInput == "direita":
        showSkeletons()
      elif userInput == "frente":
        hauntedRoom()
      elif userInput == "trás":
        print("está porta dá de cara com uma parede..")
      else:
        print("por favor, digite uma opção válida.")


if __name__ == "__main__":
  while True:
    print("bem vindo ao level 1!")
    print("Você decide viajar para paris (durante suas ferias), é vai fazer uma visita as famosas catacumbas.")
    print("entretanto, durante sua exploração, você se perde.")
    print("você pode andar em varias direções para achar uma saida.")
    print("vamos começar pelo seu nome: ")
    name = input()
    print("Boa sorte, " +name+ ".")
    introScene()
