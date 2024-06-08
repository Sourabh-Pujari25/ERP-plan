import streamlit as st
from app_utils import *
#from dotenv import load_dotenv
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Oliots ERP', page_icon='images/logo.ico')
#078a97

def main():
    image_path = f"{IMAGES}{LOGO_IMAGE}"
    
    st.markdown(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Visibility</title>
    <style>
        /* Default style: hide the image */
        .mobile-only {{
            display: none;
        }}

        /* Media query for screens with max-width 768px (typical for mobile devices) */
        @media only screen and (max-width: 768px) {{
            .mobile-only {{
                display: block; /* Show the image */
            }}
        }}
    </style>
</head>
<body>
<a href="https://github.com/Sourabh-Pujari25/ERP-plan/blob/main/images">

    <img class="mobile-only" src="/logo.png" alt="Mobile-only image">
             </a>   
</body>
</html>

    
''',unsafe_allow_html=True)
    

    # Sidebar 
    st.sidebar.markdown(f"""<style>[class="st-emotion-cache-1gv3huu eczjsme16"]{{
   background: linear-gradient(to bottom right, #053c47, #078a97);}}</style>""",unsafe_allow_html=True)
    #collapse button
    st.sidebar.markdown(f"""<style>[class="eyeqlp51 st-emotion-cache-1pbsqtx ex0cdmw0"]{{display: none;}}</style>""",unsafe_allow_html=True)
    image_path = f"{IMAGES}{LOGO_IMAGE}"
    st.sidebar.markdown("""<div style="
    height: 170px;
"></div>""",unsafe_allow_html=True)
    st.sidebar.image(image_path) 
    #containers
    st.sidebar.markdown(f"""<style>[class="st-emotion-cache-r421ms e1f1d6gn0"]{{padding: 50px;}}</style>""",unsafe_allow_html=True)

    
    
    
    space1,logo_space,space2=st.columns([20,60,20])
    with logo_space:
        st.markdown("""<h1 style="
    color: teal;
">Sign in to Workspace</h1>""",unsafe_allow_html=True)
    with st.container(border=True):  
        username_inp=st.text_input("Username")
        password_inp=st.text_input("Password")
        login_butt=st.button("Login",use_container_width=True,type="primary")
    




if __name__=="__main__":
    main()