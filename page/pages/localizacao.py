import streamlit as st
from page.pages.enderecos import endereco_page
from page.pages.busca import buscar


def busca_page():
    st.sidebar.markdown('-------')
    st.sidebar.header('MENU  BUSCA')
    opcao = st.sidebar.selectbox('Selecione uma opcao', options=['LOCALIZAR', 'NOVO ENDEREÇO'])

    if opcao == 'LOCALIZAR':
        buscar()
    if opcao == 'NOVO ENDEREÇO':
        endereco_page()

