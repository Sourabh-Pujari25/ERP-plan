import streamlit as st
from import option_menu

# Function to handle form submission
def handle_form_submission():
    # Fetch user inputs
    work_name = st.text_input("Name of Work")
    date = st.date_input("Date")
    # Example of different input fields, you can add more
    vardhaman_material = st.text_input("Vardhaman Material")
    mmc_material = st.text_input("MMC Material")
    excavation_quantity = st.number_input("Excavation Quantity")
    excavation_length = st.number_input("Excavation Length", value=1)
    excavation_width = st.number_input("Excavation Width", value=1)
    excavation_depth = st.number_input("Excavation Depth", value=1)
    excavation_default = st.checkbox("Default Excavation")
    excavation_material = st.selectbox("Excavation Material", ["Material 1", "Material 2"])
    start_time_jcb_bucket = st.number_input("Start Time for JCB Bucket")
    stop_time_jcb_bucket = st.number_input("Stop Time for JCB Bucket")
    start_time_jcb_breaker = st.number_input("Start Time for JCB Breaker")
    stop_time_jcb_breaker = st.number_input("Stop Time for JCB Breaker")
    labour = st.number_input("Labour")
    site_photos = st.file_uploader("Site Photo Upload", accept_multiple_files=True)
    drawing_upload = st.file_uploader("Drawing Upload", accept_multiple_files=True)
    labour_names = st.multiselect("Labour Names", ["Labour 1", "Labour 2", "Labour 3"])
    additional_notes = st.text_area("Additional Notes")

    # You can add further processing logic here

# Main function to run the Streamlit app
def main():
    st.title("ADD WORK")

    with st.sidebar:
        projectname=option_menu(menu_title=None,options=[f"Project: {project_name_display}"],icons=["folder"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "white"},})


if __name__ == "__main__":
    main()
