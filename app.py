import streamlit as st

st.header('HOLA GIANCARLOS CARDENAS')


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
