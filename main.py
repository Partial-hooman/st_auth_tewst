import streamlit as st 

from google_auth_oauthlib.flow import Flow






flow = Flow.from_client_secrets_file(
    "client_secret_1023844332180-knicf5jgjp1d286076t71tp9ntjlbcr5.apps.googleusercontent.com.json",
    scopes=['https://www.googleapis.com/auth/webmasters.readonly'],
    redirect_uri='https://partial-hooman-fiverr-google-console-api-main-qxl9lf.streamlit.app/authentication')


auth_uri = flow.authorization_url()

link = f'[GitHub]({auth_uri[0]})'
st.markdown(link, unsafe_allow_html=True)




