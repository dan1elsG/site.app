import pandas as pd
import streamlit as st


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
                if len(partes) >= 7:
                    extintores_localizados.append({
                        'ID': partes[1].strip(),
                        'Selo Inmetro': partes[2].strip(),
                        'Tipo': partes[3].strip(),
                        'Capacidade': partes[4].strip(),
                        'Data de Validade': partes[5].strip(),
                        'Endereço': partes[6].strip()
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
        df_extintores_localizados = pd.DataFrame(extintores_localizados,
                                                columns=['ID', 'Selo Inmetro', 'Tipo', 'Capacidade', 'Data de Validade', 'Endereço'])
        st.write("Extintores Localizados:")
        st.dataframe(df_extintores_localizados)
    else:
        st.info("Não há extintores localizados.")

