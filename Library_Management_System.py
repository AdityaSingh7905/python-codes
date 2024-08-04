"""----------------------------------LIBRARY MANAGEMENT SYSTEM------------------------------"""
class Library:
    dict={}
    def __init__(self,list_of_books,library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name

    def displaybook(self):
        return self.list_of_books

    def lendbook(self,user_name,book_name):
        for keys in self.dict:
            if keys==book_name:
              print(f"This book is not present in the library as this is being lended by {self.dict.get(keys)} now.."
                  f"Sorry for inconvenience!!")
              return

        self.dict.update({f"{book_name}":f"{user_name}"})
        print(lib1.dict)
        print("Book is issued to you.Thanks!! Please come again!!")
        # print(self.dict)

    def addbook(self,book_name):
        self.list_of_books.append(book_name)

    def returnbook(self,user_name,book_name):
        for keys in self.dict:
            if keys==book_name:
                self.dict.pop(keys)
                break

lib1=Library(["NCERTPhysics","NCERTChemistry","NCERTMathematics","NCERTBiology","NCERTEnglish",
                       "NCERTHindi"],"B R Ambedkar Library")
# print(lib1.displaybook())
# lib1.addbook("NCERTComputer_Science")
# print(lib1.displaybook())
# lib1.lendbook("Aditya Singh","NCERTMathematics")
# lib1.lendbook("Anshuman Singh","NCERTPhysics")
# lib1.lendbook("Riya Singh","NCERTChemistry")
# print(lib1.dict)
# lib1.lendbook("Aditya Singh","NCERTChemistry")
# lib1.returnbook("Aditya Singh","NCERTMathematics")
# print(lib1.dict)
while(1):
    print("Hello!You are in B R Ambedakar National Library.How can I help you??")
    a=int(input("Press 1 for 'displaybook',2 for 'addbook',3 for 'lendbook',4 for 'returnbook':"))
    if a==1:
        print(lib1.displaybook())
    elif a==2:
        print("For lending a book to you,we need some information about you.")
        b=input("Enter user name:")
        c=input("Enter Book name you want to lend:")
        lib1.lendbook(b,c)

    elif a==3:
        d=input("Enter the book you want to add:")
        lib1.addbook(d)
        print(lib1.displaybook())
        print("From the B R Ambedakar National Library,we thanks for your support to the library..")
    else:
        e=input("Enter the book you want to return to the library:")
        f=input("Enter user name:")
        lib1.returnbook(f,e)
        print(lib1.dict)
        print("Thanks for returning our book in good condition.. ")
