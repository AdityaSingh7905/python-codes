def Searcher():
    import time
    # Some 4 seconds time consuming task
    book="This is Aditya Singh studying in School of Engineering " \
         ",Jawaharlal Nehru University."
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Text is in the book.")
        else:
            print("Text is not present in the book.")

search = Searcher()
print("Search Started...")
search.__next__()
print("Next method run...")
search.send("Aditya")

search.close()
search.send("Aditya Singh")

