import requests
import json
import time

api_key = "5bbc31768fcf156ae7203eb2bc9784e1"

while True:
    cidade = input("Digite o nome da cidade e o país onde ele se localiza (ex: London,uk): ")

    url_base = "http://api.openweathermap.org/data/2.5/weather"

    parametros = {
        'q': cidade,
        'appid': api_key,
        'lang': 'pt_br',
        'units': 'metric'
    }


    print (f"Buscando dados do sistema para a cidade de {cidade}...")
    time.sleep(1)
    response = requests.get(url_base, params=parametros)

    if response.status_code == 200:
        dados_clima = response.json()

        temp_atual = dados_clima['main']['temp']
        temp_sensacao = dados_clima['main']['feels_like']
        temp_min = dados_clima['main']['temp_min']
        temp_max = dados_clima['main']['temp_max']

        decricao = dados_clima['weather'][0]['description']

        print ("-------------------------------------------")
        print (f"Clima em {cidade}: {decricacao}")
        print (f"Temperatura atual: {temp_atual}°C")
        print (f"Sensação térmica: {temp_sensacao}°C")
        print (f"temperatura mínima: {temp_min}°C")
        print (f"Temperatira maxima: {temp_max}°C")
        print ("-------------------------------------------")

    elif response.status_code == 404:
        print (f"Cidade {cidade} não encontrada. Verifique o nome e tente novamente.")
    elif response.status_code == 401:
        print ("Chave de API inválida. Verifique sua chave e tente novamente.")
    else:
        print (f"Opa, algo deu errado! Código de status: {response.status_code} ")
        print (response.json())

    sair = input("Deseja sair do programa? (s/n): ")
    if sair.lower() == 's':
        print("Encerrando o programa. Até mais!")
        break
    else:
        continue
