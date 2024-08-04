# Creating a dictionary
dict={
       "append":"concatenate",
       "comment":"pieces of code ignored by the python or any computer language interpreter",
       "distinct":"differently",
       "mutable":"changeable",
       "nonmutable":"nonchangeable"
      }
print("Enter the word whose meaning you want to know:" )
word=input()
print("You entered:",word)
print("Meaning of the word is:",dict[word])