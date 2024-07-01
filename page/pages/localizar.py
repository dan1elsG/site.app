import streamlit as st

# Função para ler o arquivo dados.txt e armazenar os dados em um dicionário
def ler_dados():
    dados = {}
    with open('dados.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            partes = linha.split(',')
            id = partes[0]
            selo_inmetro = partes[1]
            tipo = partes[2]
            capacidade = partes[3]
            data_validade = partes[4]
            dados[id] = {
                'selo_inmetro': selo_inmetro,
                'tipo': tipo,
                'capacidade': capacidade,
                'data_validade': data_validade
            }
    return dados

# Função para ler o arquivo enderecos.txt e armazenar os endereços em um dicionário
def ler_enderecos():
    enderecos = {}
    with open('enderecos.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            partes = linha.split(',')
            id = partes[0]
            endereco = partes[1]
            tipo = partes[2]
            enderecos[id] = {
                'endereco': endereco,
                'tipo': tipo
            }
    return enderecos

# Função para remover o extintor localizado dos arquivos dados.txt e enderecos.txt
def remover_extintor(extintor_id, endereco_id):
    try:
        # Remover extintor de dados.txt
        with open('dados.txt', 'r') as file:
            linhas = file.readlines()
        with open('dados.txt', 'w') as file:
            for linha in linhas:
                if linha.startswith(f"{extintor_id},"):
                    continue
                file.write(linha)

        # Remover endereço de enderecos.txt
        with open('enderecos.txt', 'r') as file:
            linhas = file.readlines()
        with open('enderecos.txt', 'w') as file:
            for linha in linhas:
                if linha.startswith(f"{endereco_id},"):
                    continue
                file.write(linha)
    except FileNotFoundError:
        st.warning('Arquivos dados.txt ou enderecos.txt não encontrados.')

# Função para combinar os dados e escrever no arquivo localizado.txt
def combinar_dados():
    dados = ler_dados()
    enderecos = ler_enderecos()

    st.subheader('LOCALIZAR EXTINTORES AO ENDEREÇO')
    extintor_id = st.number_input('Digite o ID do extintor:', step=1)
    endereco_id = st.number_input('Digite o ID do endereço:', step=1)

    if st.button('LOCALIZAR EXTINTOR'):
        if dados.get(str(extintor_id)) and enderecos.get(str(endereco_id)):
            # Gerar novo ID para o extintor localizado
            with open('localizado.txt', 'a+') as arquivo:  # Modo 'a+' para ler e adicionar no final do arquivo
                arquivo.seek(0)
                linhas = arquivo.readlines()
                if linhas:
                    ultimo_id = int(linhas[-1].split(',')[0])
                    novo_id = ultimo_id + 1
                else:
                    novo_id = 1

                linha = (f"{novo_id},{dados[str(extintor_id)]['selo_inmetro']},"
                         f"{dados[str(extintor_id)]['tipo']},{dados[str(extintor_id)]['capacidade']},"
                         f"{dados[str(extintor_id)]['data_validade']},{enderecos[str(endereco_id)]['endereco']}\n")
                arquivo.write(linha)
                st.success('EXTINTOR LOCALIZADO COM SUCESSO!')
                remover_extintor(extintor_id, endereco_id)
        else:
            st.warning('IDs de extintor ou endereço não encontrados.')

