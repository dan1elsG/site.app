import pandas as pd
import streamlit as st
from page.pages.enderecos import mostrar_enderecos_disponiveis
from page.pages.localizar import combinar_dados


def ler_dados_extintores():
    try:
        with open('dados.txt', 'r') as file:
            linhas = file.readlines()
            return [linha.strip().split(',') for linha in linhas]
    except FileNotFoundError:
        st.error("Arquivo 'dados.txt' não encontrado.")
        return []


def ler_extintor_por_id(id_extintor):
    try:
        with open('dados.txt', 'r') as file:
            for linha in file:
                partes = linha.strip().split(',')
                if len(partes) >= 1 and int(partes[0].strip()) == id_extintor:
                    return {
                        'ID': int(partes[0].strip()),
                        'Selo Inmetro': partes[1].strip(),
                        'Tipo': partes[2].strip(),
                        'Capacidade': partes[3].strip(),
                        'Data de Carga': partes[4].strip()
                    }
        return None  # Retorna None se não encontrar o extintor com o ID especificado

    except FileNotFoundError:
        st.error("Arquivo 'dados.txt' não encontrado.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo de dados: {e}")
        return None


def localizar_extintor_por_tipo(tipo_extintor):
    extintores_encontrados = []
    # Ler dados dos extintores
    dados_extintores = ler_dados_extintores()

    # Iterar sobre os dados dos extintores
    for dados_extintor in dados_extintores:
        # Verificar se o tipo do extintor na linha corresponde ao tipo desejado
        if len(dados_extintor) >= 3 and dados_extintor[2].strip() == tipo_extintor:
            extintores_encontrados.append(dados_extintor)

    # Verificar se foram encontrados extintores do tipo especificado
    if extintores_encontrados:
        df = pd.DataFrame(extintores_encontrados,
                          columns=['ID', 'Selo Inmetro', 'Tipo', 'Capacidade', 'Data de Validade'])
        st.write("Extintores Encontrados:")
        st.dataframe(df)
        return extintores_encontrados
    else:
        st.warning(f"Nenhum extintor do tipo '{tipo_extintor}' encontrado.")
        return []


def buscar():
    st.title('BUSCA DE EXTINTORES')
    # Interface para localizar extintores pelo tipo
    tipo_extintor = st.selectbox('Selecione o tipo de extintor:', ['-', 'AP', 'BC', 'ABC', 'CO2'])

    if st.button('BUSCAR') and tipo_extintor != '-':
        localizar_extintor_por_tipo(tipo_extintor)
        mostrar_enderecos_disponiveis(tipo_extintor)
    else:
        st.warning('Por favor, selecione um tipo de extintor.')

    combinar_dados()
