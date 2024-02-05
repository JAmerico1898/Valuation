import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#CABEÇALHO DO FORM
st.markdown("<h1 style='text-align: center;'>VALUATION DE UM CLUBE DE FUTEBOL</h1>", unsafe_allow_html=True)
#st.markdown("<h2 style='text-align: center;'>Método do Múltiplo de Receitas</h2>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>app by @JAmerico1898</h6>", unsafe_allow_html=True)
#st.markdown("---")

with st.form("captura"):

    st.markdown("<h4 style='text-align: center;'>Escolha o Valor dos Direitos de Transmissão da Série A</h4>", unsafe_allow_html=True)
    direitos_transmissão = st.slider(label="", min_value=0, max_value=300, step=1)
    st.markdown("<h6 style='text-align: center; color: grey'>Em 2023, a estimativa para o Vasco foi de 109M, nas seguintes parcelas:<br>igualitária: 31,8M; audiência:30,4M; colocação: 16.7M; PPV: 30M </h6>", unsafe_allow_html=True)
    st.markdown("---")    

    st.markdown("<h4 style='text-align: center;'>Escolha o Valor dos Direitos de Transmissão do Estadual</h4>", unsafe_allow_html=True)
    direitos_transmissão2 = st.slider("", min_value=0, max_value=24, step=1)
    st.markdown("<h6 style='text-align: center; color: grey'>Em 2023, a estimativa para o Vasco foi de 8M por não ter aderido à proposta da FERJ,<br>cujo valor máximo foi de 24M </h6>", unsafe_allow_html=True)
    st.markdown("---")    

    st.markdown("<h4 style='text-align: center;'>Escolha o Valor da Premiação da Copa do Brasil</h4>", unsafe_allow_html=True)
    cb = st.slider("", min_value=0, max_value=90, step=1)    
    st.markdown("<h6 style='text-align: center; color: grey'>Em 2024, a premiação será de: Oitavas: 9M; Quartas: 13, Semi: 22; Campeão: até 90M</h6>", unsafe_allow_html=True)
    st.markdown("---")    

    st.markdown("<h4 style='text-align: center;'>Escolha o Valor da Premiação da Sulamericana ou Libertadores</h4>", unsafe_allow_html=True)
    continental = st.slider("", min_value=0, max_value=145, step=1)    
    st.markdown("<h6 style='text-align: center; color: grey'>Em 2023, a premiação da Libertadores foi de:<br>Fase de Grupos: 20M; Oitavas: 27M; Semi: 39, Campeão: até 145M</h6>", unsafe_allow_html=True)
    st.markdown("---")    

    st.markdown("<h4 style='text-align: center;'>Escolha o Valor da Receita com bilheteria/Match Day</h4>", unsafe_allow_html=True)
    bilheteria = st.slider("", min_value=0, max_value=150, step=1)    
    st.markdown("<h6 style='text-align: center; color: grey'>Em 2023, a estimativa para o Vasco foi de 33M.<br>Com a reforma de SJ, a estimativa foi de 80M</h6>", unsafe_allow_html=True)
    st.markdown("---")    

    st.markdown("<h4 style='text-align: center;'>Escolha o Valor da Receita com Sócio-Torcedor</h4>", unsafe_allow_html=True)
    socio = st.slider("", min_value=0, max_value=120, step=1)    
    st.markdown("<h6 style='text-align: center; color: grey'>Em 2023, a estimativa para o Vasco foi de 30M<br>Com a reforma de SJ, a estimativa foi de 50M</h6>", unsafe_allow_html=True)
    st.markdown("---")    

    st.markdown("<h4 style='text-align: center;'>Escolha o Valor da Receita com Marketing + Comercial</h4>", unsafe_allow_html=True)
    mkt = st.slider("", min_value=0, max_value=200, step=1)
    st.markdown("<h6 style='text-align: center; color: grey'>Em 2023, a estimativa para o Vasco foi de 40M</h6>", unsafe_allow_html=True)
    st.markdown("---")    
    
    st.markdown("<h4 style='text-align: center;'>Escolha o Valor da Receita com Venda de Jogadores</h4>", unsafe_allow_html=True)
    jogadores = st.slider("", min_value=0, max_value=200, step=2)
    st.markdown("<h6 style='text-align: center; color: grey'>Em 2023, a estimativa para o Vasco foi de 84M</h6>", unsafe_allow_html=True)
    st.markdown("---")    

    st.markdown("<h4 style='text-align: center; color: green'>Escolha o Valor do Múltiplo da Receita Operacional Líquida para obter o Valor do Clube</h4>", unsafe_allow_html=True)
    multiplo = st.slider("", min_value=2.0, max_value=6.0, step=0.1)    
    st.markdown("<h6 style='text-align: center; color: green'>Antes da pandemia, os múltiplos giravam em torno<br>de 2, após a pandemia, entre 4 e 5.</h6>", unsafe_allow_html=True)
    st.markdown("---")    

    button = st.form_submit_button("**Calcule o Valor do CLUBE!**")
    

if button:
    renda_oper_liquida = 0.95*(direitos_transmissão + direitos_transmissão2 + cb + continental + bilheteria + socio + mkt) + jogadores
    valuation = multiplo*renda_oper_liquida


    fontsize = 25
    st.markdown("---")    
    st.markdown("<h4 style='text-align: center; color: blue'>Renda Operacional Líquida e Valor do Clube</b></h4>", unsafe_allow_html=True)
    markdown_amount = f"<div style='text-align:center; color: blue; font-size:{fontsize}px'>R$ {renda_oper_liquida:.0f} milhões</div>"
    markdown_amount_2 = f"<div style='text-align:center; color: blue; font-size:{fontsize}px'>R$ {valuation:.0f} milhões</div>"

    col3, col4 = st.columns(2)
    with col3:
        st.markdown(markdown_amount, unsafe_allow_html=True)
    with col4:
        st.markdown(markdown_amount_2, unsafe_allow_html=True)




