Observatório de Dados Públicos

Objetivo:
Criar uma aplicação capaz de:
- Consultar uma API pública através da biblioteca requests e interpretar JSON.
- Recolher informação de uma página HTML com BeautifulSoup.
- Organizar registos em listas e dicionários e exportar ficheiros CSV

Requisitos e Ferramentas:
- Spyder
- Git Bash e GitHub
- Microsoft Excel
- Bibliotecas Python necessárias:
  "requests" (para pedidos dados)
  "beautifulsoup4" (para ler HTML)

Instruções de Execução:
1. Abra o Spyder e defina a pasta "ObservatorioDadosPublicos" como diretório de trabalho atual.
2. Abra e execute o ficheiro "api_utilizadores.py" para recolher os dados da API e gerar o ficheiro "utilizadores.csv".
3. Abra e execute o ficheiro "scraping_citacoes.py" para recolher as citações da página Web e gerar o ficheiro "citacoes.csv".
4. Abra os ficheiros ".csv" no Excel para confirmar se a separação das colunas está correta (separador ";" e codificação "UTF-8-SIG").

Fontes de Dados:
- https://jsonplaceholder.typicode.com/users — serviço com dados fictícios para demonstração
- https://quotes.toscrape.com/ — página criada para exercícios de Web Scraping


PARTE B - DESAFIO AUTÓNOMO: Opção A - Filtro de utilizadores
Foi acrescentado um filtro de utilizadores, no final do script de "api_utilizadores.py". Após a recolha dos dados de utilizador e a criação do ficheiro CSV, o script solicita um nome ou parte do nome do utilizador que se procura, e apresenta o nome e o endereço de email correspondente. Caso não encontre, informa que nenhum utilizador foi encontrado.
