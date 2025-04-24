#!/usr/bin/env python3

'''
Spanish version of wordle
'''


import re
import random
import sys

legalwordbank = []
solutionwordbank = []
MAXWORDS = 500
MAXGUESSES = 6
LENGTH_OF_WORDS = 6
legal_word_pattern = r"^" + (LENGTH_OF_WORDS * r"\w") + r"$"

green_letters = set()
yellow_letters = set()
gray_letters = set()

def check_guess(guess,solution):
  correct_characters = 0
  feedback = ""
  for i in range(LENGTH_OF_WORDS):
    if guess[i] == solution[i]:
      green_letters.add(guess[i])
      correct_characters += 1
      feedback = feedback + guess[i] + "+" + " "
    elif solution.count(guess[i]) > 0:
      yellow_letters.add(guess[i])
      feedback = feedback + guess[i] + "?" + " "
    else:
      gray_letters.add(guess[i])
      feedback = feedback + guess[i] + "-" + " "
  if correct_characters == LENGTH_OF_WORDS:
    return True, "todo correcto"
  else:
    return False, feedback
  
with open("CREA_total.TXT","r", encoding='iso-8859-1') as f:
  _ = f.readline() # waste header row
  i = 0
  for line in f:
    line = line.strip().split()
    if len(line[1]) != 6:
      continue
    if i <= MAXWORDS:
      solutionwordbank.append(line[1])
    legalwordbank.append(line[1])
    i += 1

solution = random.choice(solutionwordbank)
legalwordbank = set(legalwordbank)

if len(sys.argv) > 1 and sys.argv[1] == "c":
  print(f"---solution is '{solution}'")

nguesses = 0
guesses_so_far = set()
while nguesses < MAXGUESSES:
  while True:
    guess = input(f'Adivino nr. {nguesses+1} de {MAXGUESSES}: ')
    guess = guess.strip().lower()
    if guess in guesses_so_far:
      print(f"Ya adivinaste '{guess}', prueba otra vez")
      continue
    if re.search(legal_word_pattern,guess) is None:
      print(f"Lo siento, se puede usar solo {LENGTH_OF_WORDS} letras")
      continue
    if guess not in legalwordbank:
      print(f"No conozco la palabra '{guess}', prueba otra vez")
      continue
    if re.search(r"_",guess) is not None:
      print("Lo siento, no se puede usar _")
      continue
    solved, response = check_guess(guess,solution)
    if solved:
      print("Correcto, bien hecho")
      sys.exit(0)
    else:
      print(response)
    nguesses += 1
    guesses_so_far.add(guess)
    if nguesses == MAXGUESSES:
      print(f"Fallaste, la palabra fue '{solution}'")
      sys.exit(1)


