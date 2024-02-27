from PyDictionary import PyDictionary
root = PyDictionary()
def dict(word):
  meaning=root.meaning(word)
  for i in meaning:
    x=f"🌟{i}:\n\n\"{meaning[i][0]}\""
    return x