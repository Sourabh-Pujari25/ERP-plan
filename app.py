import streamlit as st
from app_utils import *
#from dotenv import load_dotenv
from streamlit_option_menu import option_menu
import base64
st.set_page_config(page_title='Oliots ERP', page_icon='images/logo.ico',layout="wide")
#078a97
#@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img =get_img_as_base64("images/background.png")

st.markdown(f"""<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}</style>""",unsafe_allow_html=True)

#st.set_page_config(page_title='Oliots ERP', page_icon='images/logo.ico',layout="wide")
def main():
    st.markdown(f"""<style>[class="st-emotion-cache-12fmjuu ezrtsby2"]{{display:none;}}</style>""",unsafe_allow_html=True)
    
    markdowns()
    image_path = f"{IMAGES}{LOGO_IMAGE}"
    col1,space,col2=st.columns([30,10,60])
    with col1:
        st.markdown("""<div style="height: 120px;"></div>""",unsafe_allow_html=True)
        st.image(image_path,use_column_width=True) 
    with col2:

    
   
    #st.sidebar.markdown("""<div style="height: 250px;"></div>""",unsafe_allow_html=True)
    
        space1,logo_space,space2=st.columns([20,60,20])
        with logo_space:
            st.markdown("""<center><h1 style="color: teal;">Sign in to Workspace</h1></center>""",unsafe_allow_html=True)
        with st.container(border=True):
            pad_left,content,pad_right=st.columns([10,80,10])
            with content:
                st.markdown("""<div style="height: 20px;"></div>""",unsafe_allow_html=True)
                username_inp=st.text_input("Username")
                password_inp=st.text_input("Password")
                login_butt=st.button("Login",use_container_width=True,type="primary")
                st.markdown("""<div style="height: 20px;"></div>""",unsafe_allow_html=True)
    
    




if __name__=="__main__":
    main()