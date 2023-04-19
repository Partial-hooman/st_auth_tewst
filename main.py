import streamlit as st 

from google_auth_oauthlib.flow import Flow
import os
import asyncio

from session_state import get
from httpx_oauth.clients.google import GoogleOAuth2
client = GoogleOAuth2(client_id, client_secret)

async def write_access_token(client,
                             redirect_uri,
                             code):
    token = await client.get_access_token(code, redirect_uri)
    return token



try:
    code = st.experimental_get_query_params()['code'][0]
    st.write(code)
    token = asyncio.run(
    write_access_token(client=client,
                       redirect_uri=redirect_uri,
                       code=code))
    session_state.token = token
    st.write(session_state.token)
except:
    

    flow = Flow.from_client_secrets_file(
                 "client_secret_1023844332180-26u1j2e19ppqkco37kfu61h3ijqf8e6o.apps.googleusercontent.com.json",
                 scopes=['https://www.googleapis.com/auth/webmasters.readonly'],
                 redirect_uri='https://partial-hooman-st-auth-tewst-main-rfcit3.streamlit.app/')


    auth_uri = flow.authorization_url()

    st.header("please authorize using the follow:")

    link = f'[AUTHORIZE]({auth_uri[0]})'
    st.markdown(link, unsafe_allow_html=True)

