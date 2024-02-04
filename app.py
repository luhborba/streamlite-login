import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Bem Vindo *{st.session_state["name"]}*')
    st.title('Página de Sistema')
elif st.session_state["authentication_status"] is False:
    st.error('Usuário/Senha is inválido')
elif st.session_state["authentication_status"] is None:
    st.warning('Por Favor, utilize seu usuário e senha!')