# pesquisa-aplicada
# bebeti

Guia Rápido: Como Instalar e Executar a Dashboard com Streamlit
Para corrermos a nossa dashboard interativa da PRF e INMET, precisamos de instalar o Streamlit e executá-la corretamente através do terminal. Segue os passos abaixo:

1. Instalar as dependências
Abre o terminal na pasta do projeto e executa o comando para instalar as bibliotecas necessárias (Pandas, Streamlit e Plotly):

Bash
pip install pandas streamlit plotly
2. Executar a Dashboard
Como o atalho direto do Streamlit pode não estar configurado no PATH do teu sistema, a forma mais segura e universal de correr o projeto é através do Python com o argumento -m.

Executa o seguinte comando no terminal (substituindo editor.py pelo nome do teu ficheiro de código, caso seja diferente):

Bash
python -m streamlit run editor.py


Nota na primeira execução: Poderá aparecer uma mensagem de boas-vindas do Streamlit a pedir o teu e-mail para novidades e promoções. Podes simplesmente deixar em branco e carregar em Enter para avançar, ou introduzir o teu e-mail se preferires.
