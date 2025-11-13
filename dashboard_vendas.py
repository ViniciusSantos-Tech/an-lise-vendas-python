#𝐅𝐞𝐢𝐭𝐨 𝐩𝐨𝐫 𝐕𝐢𝐧𝐢𝐜𝐢𝐮𝐬 𝐒𝐚𝐧𝐭𝐨𝐬-𝐓𝐞𝐜𝐡

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
service = Service(ChromeDriverManager().install())
Preço1atual = 5899
Preço2atual = 4169
Preço3atual = 1619
Preço1limpo = 0
Preço2limpo = 0
Preço3limpo = 0
Loja1 = ''
Loja2 = ''
Loja3 = ''
Preço1 = ''
preço2 = ''
preço3 = ''

def menuzinho():
    print("--VALORES---")
    print(f"Loja {Loja1}: R${Preço1} ")
    print(f"Loja {Loja2}: R${preço2}")
    print(f"Loja {Loja3}: R${preço3}")

def Alarme():
    global Preço1atual, Preço2atual, Preço3atual
    preços = [Preço1limpo, Preço2limpo, Preço3limpo]
    if preços[0] < Preço1atual:
        print(f"Preço abaixou! De R${Preço1atual}, Para {Preço1limpo}")
        Preço1atual = Preço1limpo
    if preços[1] < Preço2atual:
        print(f"Preço abaixou! De R${Preço2atual}, Para {Preço2limpo}")
        Preço2atual = Preço2limpo
    if preços[2] < Preço3atual:
        print(f"Preço abaixou! De R${Preço3atual}, Para {Preço3limpo}")
        Preço3atual = Preço3limpo
    menuzinho()

def verificar_todos_sites():
    driver = webdriver.Chrome(service=service)
    
    global Preço1limpo, Preço2limpo, Preço3limpo, Preço1, preço2, preço3, Loja1, Loja2, Loja3
    
    while True:
        try:
            driver.get("https://www.amazon.com.br/Geladeira-Brastemp-French-Frost-Bro85ak/dp/B0BLQXH6NM")
            sleep(1)
            Loja1 = 'Amazon'
            Preço1 = driver.find_element(By.CSS_SELECTOR, ".a-price-whole").text
            Preço1 = Preço1.replace(".", "").replace("R$ ", "")
            Preço1limpo = int(Preço1)
            break
        except:
            print("Error site1")

    while True:
        try:
            driver.get("https://www.mercadolivre.com.br/geladeira-brastemp-frost-free-duplex-375-litros-cor-inox/p/MLB11101734")
            sleep(1)
            Loja2 = 'Mercado Livre'
            preço2 = driver.find_element(By.CSS_SELECTOR, ".andes-money-amount__fraction").text
            preço2 = preço2.replace(".", "").replace("R$ ", "") 
            Preço2limpo = int(preço2)
            break
        except:
            print("Error site2")

    while True:
        try:
            driver.get("https://www.americanas.com.br/geladeira-refrigerador-compacto-hq-defrost-140-litros-preto-inox-hq-140rdf-7514478991/p?idsku=3790963")
            sleep(1)
            Loja3 = 'Americanas'
            preço3 = driver.find_element(By.CSS_SELECTOR, '.ProductPrice_productPrice__vpgdo').text
            preço3 = preço3.replace("R$ ", "").replace(".", "").split(",")[0]
            Preço3limpo = int(preço3)
            break
        except:
            print("Error site3")
    
    driver.quit() 
    Alarme()

verificar_todos_sites()
