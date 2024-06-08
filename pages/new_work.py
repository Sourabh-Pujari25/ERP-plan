import streamlit as st
from app_utils import *
# page_congig()

def main():
    
    work_name=st.text_input("Add Project Name")
    work_date=st.date_input("Select Project Date")

if __name__=="__main__":
    main()