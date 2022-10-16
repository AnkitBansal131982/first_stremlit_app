
import streamlit

streamlit.title('My New Healthy Breakfast')
streamlit.header('🥑 Avacado')
streamlit.text('🎂 Omega3 and Almonds Kavish')
streamlit.text('😎,Guava and Banana')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
