import shelve
import pickle
import anagrams_sets as anagram

def main():
  store_anagrams('worlds.txt', )

def store_anagrams(filename, file_map):
  db = shelve.open(filename, 'c')
  
  for word, word_anagrams in file_map.itens():
    db[word] = word_anagrams
  
  db.close()


def read_anagrams():
  pass


if __name__ == "__main__":
  main()    