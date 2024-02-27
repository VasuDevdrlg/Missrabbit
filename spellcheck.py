from spellchecker import SpellChecker
def bee(input):
    root=SpellChecker()
    list=[]
    list.append(input)
    token=""
    wrong=root.unknown(list)
    for i in wrong:
      correct=root.candidates(i)
    for j in correct:
     token+="👉 "+j+"\n"
    return token