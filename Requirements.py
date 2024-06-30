import subprocess


def criar_requirements():
    try:
        # Executa o comando pip freeze e redireciona a saída para requirements.txt
        subprocess.check_call(['pip', 'freeze', '>', 'requirements.txt'], shell=True)
        print("Arquivo requirements.txt criado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o arquivo requirements.txt: {e}")


def instalar_dependencias():
    try:
        # Instala as dependências listadas em requirements.txt
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
        print("Dependências instaladas com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar as dependências: {e}")


if __name__ == '__main__':
    criar_requirements()
    instalar_dependencias()
