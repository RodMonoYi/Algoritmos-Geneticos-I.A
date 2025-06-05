# Resolução das Questões propostas na disciplina de I.A

Segue a resolução para as questões do arquivo "Questões.pdf" para a disciplina de I.A utilizando as bibliotecas `NumPy`, `Matplotlib` e `SciPy`. 
Cada questão está em um arquivo `.py` separado.

## Estrutura do Projeto

A estrutura de arquivos do projeto é a seguinte:
Cada arquivo `questaoX.py` contém o código para resolver o problema correspondente, incluindo a definição da função objetivo, restrições e a chamada do otimizador.

## Como Rodar os Scripts

Você tem duas opções para executar esses scripts:

1.  **Com Python Instalado (Recomendado se você já tem ou quer instalar Python)**
2.  **Com Docker (Se você não quer instalar Python e suas dependências diretamente no seu sistema)**

### Opção 1: Rodar com Python Instalado no seu Sistema

Se você já tem o Python (versão 3.x) instalado você pode rodar os scripts diretamente.

1.  **Clone o Repositório:**
    ```bash
    git clone git@github.com:RodMonoYi/Algoritmos-Geneticos-I.A.git
    cd Algoritmos-Geneticos-I.A
    ```

2.  **Instale as Dependências:**
    Certifique-se de ter as bibliotecas necessárias instaladas. Elas estão listadas no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute um Script:**
    Para executar qualquer questão, use o comando `python` seguido do nome do arquivo:
    ```bash
    python questao1.py
    # ou
    python questao2.py
    # ... e assim por diante para as outras questões
    ```

### Opção 2: Rodar com Docker (Ambiente Isolado)

Se você não quer instalar o Python e as dependências diretamente no seu sistema operacional, ou se prefere um ambiente isolado e reproduzível utilize via Docker.

**Pré-requisitos:**
* **Docker Desktop** (para Windows/macOS) ou **Docker Engine** (para Linux) instalado na sua máquina.

1.  **Clone o Repositório:**
    ```bash
    git clone git@github.com:RodMonoYi/Algoritmos-Geneticos-I.A.git
    cd Algoritmos-Geneticos-I.A
    ```

2.  **Construa a Imagem Docker:**
    O `Dockerfile` no diretório raiz define o ambiente necessário. Este comando construirá uma imagem Docker que contém Python e todas as bibliotecas necessárias.
    ```bash
    docker build -t atividade-ia-python .
    ```
    (O `.` no final indica que o Docker deve procurar o `Dockerfile` no diretório atual.)

3.  **Execute um Script em um Contêiner Docker:**
    Após a imagem ser construída, você pode executar qualquer um dos scripts dentro de um contêiner Docker.

    ```bash
    # Para executar questao1.py:
    docker run -v $(pwd):/app atividade-ia-python python questao1.py

    # Para executar questao2.py:
    docker run -v $(pwd):/app atividade-ia-python python questao2.py

    # ... e assim por diante para as outras questões (substitua 'questaoX.py' pelo nome desejado)
    ```
    * `docker run`: Comando para iniciar um novo contêiner.
    * `-v $(pwd):/app`: Monta o diretório atual do seu computador (`$(pwd)` no Linux/macOS, use `%cd%` no PowerShell do Windows ou o caminho completo no CMD) dentro do contêiner no caminho `/app`. Isso permite que o contêiner acesse seus arquivos de script e salve os gráficos gerados no seu diretório local.
    * `atividade-ia-python`: O nome da imagem Docker que você construiu.
    * `python questaoX.py`: O comando que será executado dentro do contêiner.

## Visualização de Gráficos (`matplotlib.pyplot.show()`)

Os scripts utilizam a biblioteca `matplotlib.pyplot` para gerar gráficos. Por padrão, no `Dockerfile` e na execução local, eu configurei os scripts para **salvar os gráficos como arquivos PNG** (ex: `questao1_grafico.png`). Isso garante que os resultados visuais estejam sempre disponíveis no seu diretório, independentemente do ambiente.

Se você deseja que as janelas dos gráficos **apareçam interativamente (`plt.show()`)** ao invés de serem salvas como arquivos, siga as instruções abaixo, dependendo do seu sistema operacional e método de execução:

### A. Se você está rodando com Python Nativo no Windows ou macOS:

A função `plt.show()` funcionará automaticamente, abrindo as janelas dos gráficos. Certifique-se apenas de que a linha `plt.show()` não esteja comentada e que `plt.savefig()` esteja comentada, se você preferir a exibição interativa.

### B. Se você está rodando com Docker (especialmente no Windows via WSL2 ou Linux):

Para que `plt.show()` funcione dentro de um contêiner Docker e exiba a janela gráfica na sua máquina host (Windows, macOS ou Linux), você precisa configurar o **reencaminhamento X11**.

#### No Windows (com WSL2 e Docker Desktop):

1.  **Instale um Servidor X no Windows:**
    O mais comum e recomendado é o **VcXsrv Windows X Server**.
    * Baixe e instale-o a partir de [SourceForge: VcXsrv Windows X Server](https://sourceforge.net/projects/vcxsrv/).
    * Após a instalação, inicie o **XLaunch** (procure no menu Iniciar).
    * Siga o assistente:
        * Escolha **"Multiple windows"**.
        * Escolha **"Start no client"**.
        * Na tela de "Extra settings", **marque "Disable access control"**.
        * Clique em "Finish". Um ícone do VcXsrv aparecerá na sua bandeja do sistema.

2.  **Modifique seus Scripts Python:**
    Certifique-se de que a linha `plt.show()` esteja **descomentada** e a linha `plt.savefig(...)` esteja **comentada** em seus arquivos `questaoN.py`.

3.  **Execute o Contêiner Docker com Variáveis de Ambiente:**
    Abra seu terminal **WSL2** (onde você roda os comandos Docker) e execute o seguinte comando:

    ```bash
    # Primeiro, obtenha o IP do host Windows para a variável DISPLAY
    export DISPLAY=$(grep -m 1 nameserver /etc/resolv.conf | awk '{print $2}'):0.0

    # Agora, execute o contêiner com as variáveis de DISPLAY e montando o soquete X11
    docker run \
      -e DISPLAY=$DISPLAY \
      -v /tmp/.X11-unix:/tmp/.X11-unix \
      -v $(pwd):/app \
      atividade-ia-python \
      python questaoX.py # Substitua X pelo número da questão
    ```
    Isso permitirá que as janelas dos gráficos apareçam no seu desktop Windows.

#### No Linux (com Docker):

Você geralmente já tem um servidor X rodando. Basta configurar as variáveis de ambiente e montar o soquete X11.

1.  **Modifique seus Scripts Python:**
    Certifique-se de que a linha `plt.show()` esteja **descomentada** e a linha `plt.savefig(...)` esteja **comentada** em seus arquivos `questaoN.py`.

2.  **Execute o Contêiner Docker:**
    ```bash
    docker run \
      -e DISPLAY=$DISPLAY \
      -v /tmp/.X11-unix:/tmp/.X11-unix \
      -v $(pwd):/app \
      atividade-ia-python \
      python questaoX.py # Substitua X pelo número da questão
    ```

#### No macOS (com Docker Desktop):

O Docker Desktop para macOS geralmente lida com o reencaminhamento X11 de forma mais integrada se você tiver um servidor X como o XQuartz instalado.

1.  **Instale o XQuartz:**
    Baixe e instale a partir de [XQuartz](https://www.xquartz.org/). Inicie-o.
2.  **Modifique seus Scripts Python:**
    Certifique-se de que a linha `plt.show()` esteja **descomentada** e a linha `plt.savefig(...)` esteja **comentada** em seus arquivos `questaoN.py`.
3.  **Execute o Contêiner Docker:**
    ```bash
    docker run \
      -e DISPLAY=host.docker.internal:0 \
      -v $(pwd):/app \
      atividade-ia-python \
      python questaoX.py # Substitua X pelo número da questão
    ```

---

**Observação:** No momento estou rodando os arquivos de forma local sem um servidor X configurado estão os gráficos são salvos como PNGs no seu diretório. Se a exibição interativa não for necessária, mantenha as configurações padrões. é a maneira mais simples de garantir que os resultados visuais sejam gerados. Caso contrário siga as instruções acima de acordo com seu sistema operaciona, descomente nos arquivos desejados a linha `# plt.show()` e comente a linha `plt.savefig('questaoX.png')`
