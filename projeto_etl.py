import pandas as pd
import requests

api_url = 'https://api.apify.com/v2/key-value-stores/TyToNta7jGKkpszMZ/records/LATEST?disableRedirect=true'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
else:
    print(f'Erro ao acessar a API. Código de status: {response.status_code}')
    data = []

if data:
    df = pd.DataFrame(data)
    
    df['nova_coluna'] = df['coluna_existente'] * 2

    df.to_csv('dados_transformados.csv', index=False)
    print('Dados transformados foram salvos em dados_transformados.csv')
else:
    print('Nenhum dado para processar.')

