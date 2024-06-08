from dotenv import load_dotenv
import os
import streamlit as st
#--IMPORT PATHS----------

load_dotenv()
IMAGES=os.getenv("IMAGES")
LOGO_IMAGE=os.getenv("LOGO_IMAGE")

def markdowns():
    #pages  
    st.markdown(f"""<style>[class="st-emotion-cache-10rjk4g eczjsme14"]{{display:none; }}</style>""",unsafe_allow_html=True)
    st.markdown(f"""<style>[class="st-emotion-cache-1mi2ry5 eczjsme6"]{{display:none; }}</style>""",unsafe_allow_html=True)
    #image expander 
    st.markdown(f"""<style>[class="st-emotion-cache-11qx4gg e1vs0wn31"]{{display:none; }}</style>""",unsafe_allow_html=True)
    # LINK ICON
    st.markdown(f"""<style>[class="st-emotion-cache-gi0tri e1nzilvr1"]{{display:none; margin-bottom:30px;}}</style>""",unsafe_allow_html=True)
    #SPACEBELOWTITLE
    #st.markdown(f"""<style>[class="st-emotion-cache-ocqkz7 e1f1d6gn5"]{{margin-bottom:25px;}}</style>""",unsafe_allow_html=True)
    # Sidebar hide
    st.markdown(f"""<style>[class="st-emotion-cache-6qob1r eczjsme8"]{{display:none;}}</style>""",unsafe_allow_html=True)
    
    st.markdown(f"""<style>[class="st-emotion-cache-1gv3huu eczjsme16"]{{display:none;}}</style>""",unsafe_allow_html=True)
#     st.sidebar.markdown(f"""<style>[class="st-emotion-cache-1gv3huu eczjsme16"]{{
#    background: linear-gradient(to bottom right, #053c47, #078a97);}}</style>""",unsafe_allow_html=True)
    #collapse button
    st.sidebar.markdown(f"""<style>[class="eyeqlp51 st-emotion-cache-1pbsqtx ex0cdmw0"]{{display: none;}}</style>""",unsafe_allow_html=True)