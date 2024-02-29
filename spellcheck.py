from spellchecker import SpellChecker
def bee(input):
    root=SpellChecker()
    list=input.split()
    token=[]
    tok=""
    wrong=root.unknown(list)
    for i in wrong:
      correct=root.correction(i)
      for j in list:
         if i==j:
            ind=list.index(j) 
            list[ind]=correct
         else:
            pass
    for k in list:
       tok+=str(k)+" "
    return tok.capitalize()