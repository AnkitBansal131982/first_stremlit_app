
import streamlit

streamlit.title('My New Healthy Breakfast')
streamlit.header('🥑 Avacado')
streamlit.text('🎂 Omega3 and Almonds Kavish')
streamlit.text('😎,Guava and Banana')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)
