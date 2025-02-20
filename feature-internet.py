import requests
import re
from bs4 import BeautifulSoup

#source: https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
results={}

def get_link(href):
    #turn //duckduckgo.com/l/?uddg=https%3A%2F%2Fwww.britannica.com%2Fanimal%2Fpenguin%2FNatural%2Dhistory&rut=94bee35c66e5b6ffd71fc3a69b7a90a69bf6263acb774cfc8be0a4495d01b86f into regular link
    link="https://"
    href=re.search(r"%3A%2F%2F([^&]+)", href).group(1)
    link=link+href
    link=link.replace("%2F","/").replace("%2D","-")
    return link

def visit_site():
    id_input=input("Which site would you like to visit? (1-10)\n")
    try:
        id_input=int(id_input)
    except ValueError:
        print("Integer not entered")
        return
    if(id_input >=1 and id_input<=10):
        link=results[id_input][1]
        headers = {"User-Agent": "Mozilla/5.0"}
        response=requests.get(link,headers=headers)
        if response.status_code==200:
            soup=BeautifulSoup(response.text,'html.parser')
            description=soup.find("meta",attrs={"name":"description"})
            if(description is None):
                paragraphs=soup.find_all("p")
                paragraphs=[p.text.strip() for p in paragraphs]
                for i in range(3):
                    print(paragraphs[i])
            else:
                print(description.get("content"))
        else:
            print(f"Request failed. Status code is {response.status_code}")
    else:
        print("Input not between 1 and 10.")

def retrieve_link():
    id_input=input("Which site would you like to visit? (1-10)\n")
    try:
        id_input=int(id_input)
    except ValueError:
        print("Integer not entered")
        return
    if(id_input >=1 and id_input<=10):
        link=results[id_input][1]
        print(f"The link you have requested is: \n{link}")
    else:
        print("Input not between 1 and 10.")    

def duckduckgo_search():
    search_input=input("What would you like to search? ")
    url=f"https://lite.duckduckgo.com/lite/?q={search_input}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
        counter=1
        for result in soup.find_all("a",class_="result-link"):
            title=result.text.strip()
            link=get_link(result["href"])
            results[counter]=[title,link]
            counter+=1
        for key,value in results.items():
            print(f"{key}. {value[0]}")
            pass
    else:
        print(f"Request failed. Status code is {response.status_code}")

def feature_internet():
    def menu():
        menu_input=input("""
---------------
Internet Search
---------------
1. Visit a website
2. Get link
3. Exit
""")
        if menu_input=="1":
            duckduckgo_search()
            visit_site()
        elif menu_input=="2":
            duckduckgo_search()
            retrieve_link()
        elif menu_input=="3":
            return "Exiting internet search app"
        else:
            raise Exception("Invalid input")
        menu()
    menu()

feature_internet()