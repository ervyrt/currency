import requests


def exchange():
    print("Welcome to exchance program...\nYou can exchange money on latest currency or historical currency.")
    date=input("if you want to use latest, currerncy write 'today'\nif you a specific date, enter date as YYYY-MM-DD:")
    if date== 'today':
       response= requests.get("http://data.fixer.io/api/latest?access_key=e50ee7633eed91d2c46ddae5b39a7a03")
       response=response.json() 
    else:
       response= requests.get("http://data.fixer.io/api/{}?access_key=e50ee7633eed91d2c46ddae5b39a7a03&format=1".format(date))
       response=response.json()
    a=input("From which currency:")
    b=input("To which currency:")
    miktar=int(input("How much money:"))
    try:
        sonuç=(miktar/response["rates"].get(a))*response["rates"].get(b)
        print(sonuç)
    except:
        print("please write symbol of currency or date correctly.")
    again()
def again():
    answer=input("If you want to continue press 'a', if not then press 'n':")
    if answer=="a":
        exchange()
    if answer=="n":
        exit()
exchange()



