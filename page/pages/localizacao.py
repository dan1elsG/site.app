import streamlit as st
from page.pages.enderecos import endereco_page
from page.pages.loc import localizar


def localizar_page():
    st.sidebar.markdown('-------')
    st.sidebar.header('MENU LOCALIZACAO')
    opcao = st.sidebar.selectbox('Selecione uma opcao', options=['Localizacao', 'Criar endereco'])
    if opcao == 'Localizacao':
        localizar()
    if opcao == 'Criar endereco':
        endereco_page()
