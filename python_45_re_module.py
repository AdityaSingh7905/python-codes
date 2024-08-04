#Regular Expressions are sequence of characters that are used for searching a  pattern in a strings or a list of strings...
import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiii'''

# findall,search,sub,split,finditer
# patt=re.compile(r'fass')
# patt=re.compile(r'.adm ')
# patt=re.compile(r'^Tata')
# patt=re.compile(r'aiin$')
# patt=re.compile(r'a*i*')
# patt=re.compile(r'a+i+')
# patt=re.compile(r'a?i+')
# patt=re.compile(r'a?i?')
# patt=re.compile(r'ai{3}')
# patt=re.compile(r'(ai){2}')
# patt=re.compile(r'(ai)|t')
# patt=re.compile(r'(ai)|Fax')
# patt=re.compile(r'[abc]')
#Special Sequences
# patt=re.compile(r'\ATata')
# patt=re.compile(r'\Afax')
# patt=re.compile(r' Fax\b')
# patt=re.compile(r'\d{5}-\d{4}')
# patt=re.compile(r'\d{4}\b')
patt=re.compile(r'\W')
matches=patt.finditer(mystr)
# print(matches)

for match in matches:
    print(match)

#Task
string='''+91-9956723865
          +91-9956723866
          +91-9956723867
          +91-9956723868
          +91-9956723869
          +91-9956723870
          +91-9956723871
          +91-9956723877'''
# pattern=re.compile(r'\d{2}-\d{10}')
# list=re.search(r'\d{2}-\d{10}',string)
list=re.findall(r'\d{2}-\d{10}',string)
print(list)

# for item in list:
#     print(item)