import requests
from bs4 import BeautifulSoup
url=input("BULMAK ISTEDIGINIZ SAYFANIN URLSINI GIRINIZ ==>")
tag=input("SAYFADA ARADIGINIZ TAG(a,script,class)")
response=requests.get(url)
icerik=response.content
soup=BeautifulSoup(icerik,"html.parser")
script=soup.find_all(tag)
for i in script:
    print(i)
    print("-------")