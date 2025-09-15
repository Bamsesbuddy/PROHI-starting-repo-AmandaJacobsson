import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Mushroom season :mushroom:")

st.markdown(
"""    
    Mushroom season is on the way! Lets see some statistics of how many eatable mushrooms we have picked so far :star:
    
""")
import numpy as np

dataframe = np.random.rand(10, 20)*200
st.bar_chart(dataframe)

result = st.button("Click me for some encouragement along the way", type="secondary")
if result: 
    st.write(":material/thumb_up:")

# You can also add text right into the web as long comments (""")

"""
## Wohooo!
Looks like we are reaching a recordbreaking season in finding mushrooms. 
Lets see some statistics for how we are doing compared to the same time last year :fallen_leaf: 

"""

col1, col2, col3 = st.columns(3)
col1.metric("Muchroom nr 10", "1679", "+ 58%")
col2.metric("Area 0", "18 types", "+ 24%")
col3.metric("Overall", "18754 mushrooms", "+ 211%")


# # Add a slider to the sidebar:
# add_slider = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

