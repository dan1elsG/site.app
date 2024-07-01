import pandas as pd
import streamlit as st
from datetime import datetime


# Função para ler os dados de extintores localizados
def ler_extintores_localizados():
    try:
        with open('localizado.txt', 'r') as file:
            linhas = file.readlines()

            # Lista para armazenar os dados dos extintores localizados
            extintores_localizados = []

            # Iterar sobre as linhas e extrair os dados dos extintores localizados
            for linha in linhas:
                partes = linha.strip().split(',')
                if len(partes) >= 6:
                    data_validade = partes[4].strip()
                    try:
                        # Verifica se a data de validade é uma data válida
                        validade = datetime.strptime(data_validade, '%Y-%m-%d')
                        hoje = datetime.now()
                        if validade < hoje:
                            status = 'Vencido'
                        else:
                            status = 'Dentro do Prazo'
                    except ValueError:
                        status = 'Data Inválida'

                    extintores_localizados.append({
                        'ID': partes[0].strip(),
                        'Selo Inmetro': partes[1].strip(),
                        'Tipo': partes[2].strip(),
                        'Capacidade': partes[3].strip(),
                        'Data de Validade': partes[4].strip(),
                        'Endereço': partes[5].strip(),
                        'Status': status
                    })

            return extintores_localizados

    except FileNotFoundError:
        st.error("Arquivo 'localizado.txt' não encontrado.")
        return []
    except Exception as e:
        st.error(f"Ocorreu um erro ao ler o arquivo de extintores localizados: {e}")
        return []


# Função para exibir os extintores localizados em uma tabela
def exibir_extintores_localizados():
    st.title('EXTINTORES LOCALIZADOS')

    # Chama a função para ler os extintores localizados
    extintores_localizados = ler_extintores_localizados()

    # Verifica se há extintores localizados para exibir
    if extintores_localizados:
        st.write(f"Número de extintores localizados: {len(extintores_localizados)}")
        df_extintores_localizados = pd.DataFrame(extintores_localizados,
                                                 columns=['ID', 'Selo Inmetro', 'Tipo', 'Capacidade',
                                                          'Data de Validade', 'Endereço', 'Status'])
        st.write("Extintores Localizados:")
        st.dataframe(df_extintores_localizados)
    else:
        st.info("Não há extintores localizados.")
