import streamlit
import pandas
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🧉 Kale, Spinach and Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')
streamlit.text('🍞🥑 Avocado Toast')
streamlit.header('🍌🍓  Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a picklist here so they can pick the fruits they want in the smoothie
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Avocados','Strawberry'])

# display the table on the page
streamlit.dataframe(my_fruit_list)

