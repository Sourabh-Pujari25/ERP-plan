import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Oliots ERP', page_icon='images/logo.ico', layout='wide')
image = "images/oliots.png"
with st.sidebar:
    with st.container(border=True):
         st.image(image,use_column_width=True)


    

    # You can add further processing logic here

# Main function to run the Streamlit app
def main():
    st.markdown('''<style>

[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

    #st.title("Your Company Name")

    with st.sidebar:
        projectname=option_menu(menu_title=None,options=[f"Project : Oliots"],icons=["folder"],styles={"container": {"padding": "0!important", "background-color": "#fafafa","border":" 2px inset rgba(0,204,241,0.55)"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "25px","font-weight":"normal","color":"black", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "white"},})

    with st.sidebar:
        #st.markdown("Select an App")


        selected_app = option_menu(
            menu_title="Select Option",menu_icon="plugin",
            options = ["Add Work","Labour Attendance","Add Drawing","Stock List","Expense Account","Labour Advance"],
            icons = ["","bi bi-person-add","easel","bi bi-card-checklist","cash-coin","tools"],styles={"container": {"border":" 2px inset rgba(0,204,241,0.55)"}},key="trial",
            # options = ["Test Strategy","Test Design", "Code Expert", "Smart Data","Data Migration","Document Conversation","Execution History"],
            # icons = ["","person-fill-gear","robot","database-check","rocket-takeoff","receipt","clock-history"],styles={"container": {"border":" 2px inset rgba(0,204,241,0.55)"}},key="trial",


        )

    with st.container(border=True):
        st.subheader("Create a Work")
        col1,col2,submit_work_col=st.columns([40,40,20])
        with col1:
            work_name = st.text_input("Name of Work")
        with col2:
            date = st.date_input("Date")
        with submit_work_col:
            st.markdown(' <div style="height: 27px; visibility: hidden;"></div>',unsafe_allow_html=True)
            st.button("Save",use_container_width=True,type="primary")
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


if __name__ == "__main__":
    main()
