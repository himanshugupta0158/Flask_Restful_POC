import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.post(BASE + "helloworld")

# name = str(input("Enter name : "))
# response = requests.get(BASE + "helloworld/" + name)

# data = [{'likes':10 , 'name':'How to make Restful api with flask' , 'views':17556},
#         {'likes':23 , 'name':'kale' , 'views':50000},
#         {'likes':104 , 'name':'Mac' , 'views':45000},]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/"+str(i), data[i] )
#     print(response.json())

# response = requests.delete(BASE + "video/0")
# print(response)
# input()

# response = requests.get(BASE + "video/12" )

# response = requests.patch(BASE + "video/2" , {'views':99 , 'likes':101} )
# response = requests.patch(BASE + "video/2" , {} )

# response = requests.delete(BASE + "video/1")

# print(response.json())