#!/usr/bin/python



''' Anagram notes from Lecture '''
# Given a word, return all anagrams of that word in the English Language

# Given a word, check each other word in the list, and return all that are anagrams

# How do we know if two words are anagrams of each other? 
# Same length
# all letters in the first word are present at the same frequency in second word 
def is_anagram(word1, word2):
  if sorted(word1) != sorted(word2):
    return False
  else:
    return True





import math

def recipe_batches(recipe, ingredients):
  min_ratio = math.inf

  for ingredient, amount in recipe.items():
    if ingredient not in ingredients:
      return 0
    ratio = math.floor(ingredients[ingredient] / amount)
    if ratio < min_ratio:
      min_ratio = ratio
  return min_ratio  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))