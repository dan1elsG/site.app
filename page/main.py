import streamlit as st
from .pages.cadastro import cadastro_extintor
from .pages.localizacao import busca_page
from page.TABELA_EXTINTORES import exibir_extintores_localizados


def main_page():
    st.sidebar.header('MENU PRINCIPAL')
    st.sidebar.markdown('-----------')
    page = st.sidebar.selectbox(label='', options=['CADASTRAR EXTINTORES', 'BUSCAR EXTINTORES', 'TABELA EXTINTORES'])

    if page == 'CADASTRAR EXTINTORES':
        cadastro_extintor()
    if page == 'BUSCAR EXTINTORES':
        busca_page()
    if page == 'TABELA EXTINTORES':
        exibir_extintores_localizados()


