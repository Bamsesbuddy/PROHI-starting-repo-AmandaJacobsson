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
    Mushroom season is on the way! 
    Our community has collected data on how many mushrooms had been picked :star:
    The areas are split into Area 0 to 9.
    Mushrooms are identified as number 0-20.
    
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

on = st.toggle("Press for statistics")

if on:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total picked Mushroom nr 10", "1679", "+ 58%")
    col2.metric("Types found in Area 0", "18", "+ 24%")
    col3.metric("Mushrooms picked", "18754", "+ 211%")

"""

## Thanks!
Hope you enjoyed looking at my statistics! I wish you a great mushroom season before winter starts :snowflake:

"""

button2 = st.button("Press if ready for wintertime", type="secondary")
if button2: 
    st.snow()

