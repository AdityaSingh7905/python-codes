#String FORMATTING and F-String
import math
me="Harry is a good boy"
ne="Aditya"
oe="Anshuman"
pe="Akash"
qe="Akhil"
# a="This is %s"%me
# a="This is %s %s %s %s"%(ne,oe,pe,qe)
# a="This is {1} {0}"
# b=a.format(ne,oe)
# print(b)
#F-String is a fast string
a=f"This is {me} {ne} {oe} {pe} {qe} {math.cos(90)}"
print(a)