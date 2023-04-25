import streamlit as st 
#from googleapiclient.discovery import build, Resource
#from google_auth_oauthlib.flow import Flow
#import os
#import asyncio

#from httpx_oauth.clients.google import GoogleOAuth2
#client = GoogleOAuth2("1023844332180-26u1j2e19ppqkco37kfu61h3ijqf8e6o.apps.googleusercontent.com", "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")

#async def write_access_token(client,
#                             redirect_uri,
#                             code):
#    token = await client.get_access_token(code, redirect_uri)
#    return token



#try:
#    code = st.experimental_get_query_params()['code'][0]
#    st.write(code)
#    token = asyncio.run(
#    write_access_token(client=client,
#                       redirect_uri="https://partial-hooman-st-auth-tewst-main-rfcit3.streamlit.app/",
#                       code=code))
#    API_SERVICE_NAME = "webmasters"
#    API_VERSION = "v3"
#    st.write(token)
#    service = build(API_SERVICE_NAME, API_VERSION, credentials=token)
#    st.write(service.sites().list().execute())
#except Exception as e:
#    st.write(e)
#
#    flow = Flow.from_client_secrets_file(
#                 "client_secret_1023844332180-26u1j2e19ppqkco37kfu61h3ijqf8e6o.apps.googleusercontent.com.json",
#                 scopes=['https://www.googleapis.com/auth/webmasters.readonly'],
#                 redirect_uri='https://partial-hooman-st-auth-tewst-main-rfcit3.streamlit.app/')


#    auth_uri = flow.authorization_url()

#    st.header("please authorize using the follow:")

#    link = f'[AUTHORIZE]({auth_uri[0]})'
#    st.markdown(link, unsafe_allow_html=True)

button = st.file_uploader("gaming")

st.write(type(button))
