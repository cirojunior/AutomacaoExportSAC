# AutomacaoExportSAC

Automação para exportar arquivos do SAP Analytics Cloud utilizando Python.

Vamos criar um robo que automaticamente acessa uma análise criada no SAP Analytics Cloud, faz a intereção necessária na análise e exporta os arquivos.

## Deixa eu exemplificar a situação:
- Você tem uma lista de vendedores com a venda e a meta.
- Você precisa todos os dias acessar a sua análise, filtrar vendedor por vendedor, exportar e enviar para cada um deles a informação de quanto já atingiu da sua meta.
- Se você tem uns 20 vendedores, acredito que em 1 hora mais ou menos você faz esse trabalho.
- Se você tem 200 vendedores, quando termina de gerar os arquivos do dia está na hora de ir embora.

Nesse cenário a empresa está gastando um dinheiro desnecessário e você que está fazendo essa operação está se impedindo de crescer, de fazer algo relevante, de ganhar um aumento, visibilidade dentro da empresa.

**Será o cara que faz manual algo que é automatizável.**

Aqui quero mostrar como fazer essa automatização e ir para outro nível.

E se está com medo de fazer porque pode perder o teu trabalho, alguem vai fazer e você vai perder igual.

## Seja você quem faz a diferença na tua empresa.

Esse exemplo de automação pode e deve ser aplicado em vários outros trabalhos manuais e repetitivos.

Vamos estudar jundo o código que foi criado.

[Acesse o arquivo sac.py para ter acesso ao código fonte](sac.py)

O que vamos precisar?

1. Python.
2. Ambiente virtual - Virtualenv "opcional" 
3. Pacotes do python "time, os e selenium"
4. Driver do navegador preferido.

**Detalhando os itens acima.**

1. Python.
    - Vem instalado em todos sistemas operacionais, exceto o windows.
    - Para instalar no windows, [clique aqui e veja como](https://python.org.br/instalacao-windows/)
2. Ambiente virtual.
    - Instalar, [clique e veja como](https://virtualenv.pypa.io/en/latest/installation.html#via-pip)
    - Para criar a máquina virtual "virtualenv nome_da_virtualenv"
    - Para acessar "source nome_da_virtualenv/bin/activate"
3. Pacotes do Python.
    - pip install selenium
    - Os outros vem com a instalação padrão do python, não precisa adicionar.
4. Driver do navegador.
    - [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) - https://sites.google.com/a/chromium.org/chromedriver/downloads
    - [Firefox](https://github.com/mozilla/geckodriver/releases) - https://github.com/mozilla/geckodriver/releases
    - [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    - [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/) - https://webkit.org/blog/6900/webdriver-support-in-safari-10/

Todo ambiente pronto agora é mão no código.

Calma que vamos analisar linha por linha calmamente.

