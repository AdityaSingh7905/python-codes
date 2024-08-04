import requests
r=requests.get("https://catfact.ninja/fact")   # Free API
print(r.text)
print(r.status_code)

# url="https://catfact.ninja/fact"
# data={"email":"aditya***singh1901@gamil.com","password":"A***u@13"}
# r=requests.post(url=url,data=data)
# print(r.text)