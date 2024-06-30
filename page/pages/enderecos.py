import streamlit as st
import pandas as pd


def ler_ultimo_id():
    try:
        with open('enderecos.txt', 'r') as file:
            linhas = file.readlines()
            if linhas:
                ultimo_id = int(linhas[-1].strip().split(',')[0])  # Lê o último ID utilizado
            else:
                ultimo_id = 0
    except FileNotFoundError:
        ultimo_id = 0
    return ultimo_id


def mostrar_enderecos_disponiveis(tipo_extintor):
    try:
        # Abrir o arquivo 'enderecos.txt' para leitura
        with open('enderecos.txt', 'r') as file:
            linhas = file.readlines()

            # Filtrar as linhas pelo tipo de extintor especificado
            dados = []
            for linha in linhas:
                ID, endereco, tipo = linha.strip().split(',')
                if tipo.strip() == tipo_extintor:
                    dados.append({'ID': ID.strip(), 'Endereço': endereco.strip(), 'Tipo de Extintor': tipo.strip()})

            # Exibir a tabela de endereços disponíveis para o tipo de extintor especificado
            if dados:
                st.text(f"Endereços disponíveis para extintores do tipo '{tipo_extintor}':")
                df = pd.DataFrame(dados)
                st.dataframe(df)
            else:
                st.info(f"Não há endereços cadastrados para o tipo de extintor '{tipo_extintor}'.")

    except FileNotFoundError:
        st.error("Arquivo 'enderecos.txt' não encontrado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo de endereços: {e}")


def endereco_page():
    st.title('Enderecos')
    with st.form(key='enderecos_extintor'):
        id_ultimo = ler_ultimo_id()
        ID = id_ultimo + 1
        endereco = st.text_input(label='Digite o endereco do extintor')
        tipo = st.selectbox('Selecione o tipo do extintor', options=['-', 'AP', 'BC', 'ABC', 'CO2'])
        if st.form_submit_button(label='Criar endereco'):
            if tipo != '-':
                with open('enderecos.txt', 'a') as file:
                    file.write(f'{ID}, {endereco}, {tipo}\n')
                    st.success('Endereco criado com sucesso!')
            else:
                st.warning('Selecione o tipo do extintor')






