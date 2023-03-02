import streamlit as st
import streamlit_option_menu as option_menu
import base64
import car_price_data

def add_image(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_image('img5.jpg')

st.markdown(f'<h1 style="color:#FFFFFF;font-size:104px;">{"ACCU-RATE "}</h1>', unsafe_allow_html=True)

selectbox = st.sidebar.radio(
    "How would you like to be proceed?",
    ("Home","Contact Us","About")
    )
def input_car_name():
        Car_Name = st.text_input("Car Name")
def input_car_company():
        Company = st.text_input("Car Company Name")
def input_car_modelyear():
        model_year = st.text_input("Car Model Year")
def input_car_kmdriven():
        km_driven = st.text_input("Km Driven")
def input_car_fueltype():
        Fuel_type = st.text_input("Fuel Type")

if selectbox=="Home":
       carname = input_car_name()
       company = input_car_company()
       year = input_car_modelyear()
       kmdriven = input_car_kmdriven()
       fuel = input_car_fueltype()
       if st.button("Save Car Detail"):
        st.write("Car Detail save Sucessfully")
       if st.button("Predict Price"):
            price = car_price_data.input()
            st.write(price)
        # st.write(carname)
if selectbox == "Contact Us":
      st.write("""Office Address:
                                Near RKGIT ,Rajnagar Extension Ghaziabad
                
                
                
                
    Phone Number :7068787934,7088589151
    Email:vishal70687934@gmail.com""")
if selectbox=="About":
      st.write("Accu-Rate is a tool or model that uses various data and factors to estimate the price of a car. This tool can be useful for both car buyers and sellers, as it can help them determine a fair price for a vehicle.")