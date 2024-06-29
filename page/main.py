import streamlit as st
from .pages.cadastro import cadastro_extintor
from .pages.localizacao import localizar_page


def main_page():
    st.sidebar.header('MENU PRINCIPAL')
    st.sidebar.markdown('-----------')
    page = st.sidebar.selectbox(label='', options=['Cadastro Extintores', 'Localizar extintor'])

    if page == 'Cadastro Extintores':
        cadastro_extintor()
    if page == 'Localizar extintor':
        localizar_page()


