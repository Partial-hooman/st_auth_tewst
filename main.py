import streamlit as st 

from google_auth_oauthlib.flow import Flow






try:
    st.write(st.experimental_get_query_params()['code'])
    
except:
    

    flow = Flow.from_client_secrets_file(
                 "client_secret_1023844332180-26u1j2e19ppqkco37kfu61h3ijqf8e6o.apps.googleusercontent.com.json",
                 scopes=['https://www.googleapis.com/auth/webmasters.readonly'],
                 redirect_uri='https://partial-hooman-st-auth-tewst-main-rfcit3.streamlit.app/')


    auth_uri = flow.authorization_url()

    st.header("please authorize using the follow:")

    link = f'[AUTHORIZE]({auth_uri[0]})'
    st.markdown(link, unsafe_allow_html=True)

