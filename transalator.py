from deep_translator import GoogleTranslator
def gtranslator(text,dest):
  root=GoogleTranslator(source="auto",target=dest)
  result=root.translate(text)
  return result