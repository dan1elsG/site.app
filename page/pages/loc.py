import streamlit as st
import pandas as pd
from page.pages.enderecos import endereco_page, mostrar_enderecos_disponiveis


def localizar_extintor_por_tipo(tipo_extintor):
    try:
        # Abrir o arquivo dados.txt para leitura
        with open('dados.txt', 'r') as file:
            # Inicializa uma lista para armazenar os dados dos extintores encontrados
            extintores_encontrados = []

            # Ler todas as linhas do arquivo
            linhas = file.readlines()

            # Iterar sobre cada linha do arquivo
            for linha in linhas:
                dados_extintor = linha.strip().split(',')

                # Verificar se o tipo do extintor na linha corresponde ao tipo desejado
                if len(dados_extintor) >= 2 and dados_extintor[1].strip() == tipo_extintor:
                    extintores_encontrados.append(dados_extintor)

            # Verificar se foram encontrados extintores do tipo especificado
            if extintores_encontrados:
                df = pd.DataFrame(extintores_encontrados,
                                  columns=['Selo Inmetro', 'Tipo', 'Capacidade', 'Data de Carga'])
                st.write("Extintores Encontrados:")
                st.dataframe(df)
            else:
                st.warning(f"Nenhum extintor do tipo '{tipo_extintor}' encontrado.")

    except FileNotFoundError:
        st.error("Arquivo 'dados.txt' não encontrado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo: {e}")


def localizar():
    st.title('Localizar extintores')

    # Interface para localizar extintores pelo tipo
    tipo_extintor = st.selectbox('Selecione o tipo de extintor:', ['AP', 'BC', 'ABC', 'CO2'])

    if st.button('Localizar'):
        if tipo_extintor:
            localizar_extintor_por_tipo(tipo_extintor)
            st.text('Enderecos disponiveis para localizar extintores')
            mostrar_enderecos_disponiveis(tipo_extintor)

        else:
            st.warning('Por favor, selecione um tipo de extintor.')




