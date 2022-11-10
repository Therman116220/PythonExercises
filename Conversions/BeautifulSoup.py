import requests
from bs4 import BeautifulSoup as toolOfChoice

print("Input youtube extension")
extension = input("")
print("Input element such as link,body,img & footer")
element = input("")
url = 'https://youtube.com/' + extension
req = requests.get(url)
beautsoop = toolOfChoice(req.content, 'html.parser')

'''Find from within the html document (this tag)'''
data = beautsoop.find(element)
print(data)




    
