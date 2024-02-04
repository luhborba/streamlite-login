# Utilizando o Streamlit-Authenticator

## Leve em consideração que esta sendo usando Linux, com Pyenv e Poetry:
Você pode seguir esse guia que utilizei para utilização no WSL, assim você pode começar a partir da instalação do `PyEnv`: [GitHub que pode ser usado como guia](https://github.com/luhborba/Wsl-Pyenv-Poetry)

1. Clone o repositório:
```bash
git clone https://github.com/luhborba/streamlite-login.git
cd streamlite-login
```

2. Configure a versão correta do Python com `pyenv`, caso não tenha instalado a versão do python utilize o `pyenv install`, caso já tenha instalado ou após a instalação utilize o `pyenv local`
```bash
pyenv install 3.11.7
pyenv local 3.11.7
```

3. Ativando Poetry
```bash
poetry shell
```
4. Instalando Dependencias
```bash
poetry install
```

5. Testando projeto
```bash
streamlit run app.py
```