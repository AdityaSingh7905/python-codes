import json

# data = '{"var1":"harry","var2":56}'
# # print(data["var2"])
# print(data)
#
# parsed=json.loads(data)
# print(parsed["var2"])
#
# data2={"channel_name":"CodeWithHarry",
#        "cars":['bmw','audi a8','ferrari'],
#        "fridge":('roti','dal','chaval'),
#        "isbad":False
#        }
#
# l=json.dumps(data2)
# print(l)

#Creating the JSON file
data= {
       "name":"'Aditya Singh'",
       "place":"Allahabad",
       "skills":["Raspberry pi","Machine Learning",
                 "Web Development"],
       "email":"xyz@gamil.com",
       "projects":["Python Data Mining",
                   "Python Data Science"
                   ]

}
with open("data_file.json","w") as f:
       json.dump(data,f)
#After creating JSON file , let's use json.load()
with open("data_file.json") as f1:
    print(json.load(f1))
