import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to Task 2 of showing my skills 👋")

st.markdown(
"""    
    ## My commits made to this project:
    
    1. Explored buttons, made them clickable with a result showing
    2. Had extreme problems with finding out why my code wouldn't run, found out i wasn'nt in the environment but managed to commit anyway? It didn't have a title since i was stressed. Thanks for your understanding. 

""")

result = st.button("Click me", type="secondary")
if result: 
    st.write(":material/thumb_up:")
# You can also add text right into the web as long comments (""")

"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# # DATAFRAME MANAGEMENT
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# # Add a slider to the sidebar:
add_slider = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0)
 )
