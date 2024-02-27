from quote import quote
def quotemaker(query):
    line=quote(query,limit=1)
    token=f"Author👨‍🎓:\n\n{line[0]['author']}\n\nBook📖:\n\n{line[0]['book']}\n\nQuote✒:\n\n\"{line[0]['quote']}\""
    return token

