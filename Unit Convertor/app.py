import streamlit as st

#For Distance
def distance_convertor (from_unit , to_unit , value):
    units = {
        'Meters': 1,
        'Kilometers': 1000,
        'Feet': 0.3048,
        'Miles': 1609.34
    }
    result = units[from_unit] * value / units[to_unit]
    return result
#For Temperature
def temperature_convertor (from_unit , to_unit , value):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        result = (value * 9/5) + 32
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        result = value + 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        result = (value - 32) * 5/9
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        result = (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        result = value - 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        result = (value - 273.15) * 9/5 + 32
    else:
        result = value
    return result
#For Weight
def weight_convertor (from_unit , to_unit , value):
    units = {
        'Kilograms': 1,
        'Grams': 0.001,
        'Pounds': 0.453592,
        'Ounces': 0.0283495
    }
    result = units[from_unit] * value / units[to_unit]
    return result
#For Pressure
def pressure_convertor (from_unit , to_unit , value):
    units = {
        'Pascal': 1,
        'Bar': 100000,
        'Atmosphere': 101325,
        'Torr': 133.322
    }
    result = units[from_unit] * value / units[to_unit]
    return result

#UI
st.title('Unit Converter')

category = st.selectbox("Select Category", ['Distance','Tamperature','Weight','Pressure'])

if category == 'Distance':
    from_unit = st.selectbox("From",['Meters','Kilometers', 'Feet' ,'Miles'])
    to_unit = st.selectbox("To",['Meters','Kilometers', 'Feet' ,'Miles'])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
     result = distance_convertor(from_unit, to_unit, value)
     st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
elif category == 'Tamperature':
    from_unit = st.selectbox("From",['Celsius','Fahrenheit', 'Kelvin'])
    to_unit = st.selectbox("To",['Fahrenheit', 'Celsius', 'Kelvin'])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
     result = temperature_convertor(from_unit, to_unit, value)
     st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
elif category == 'Weight':
    from_unit = st.selectbox("From",['Kilograms','Grams', 'Pounds' ,'Ounces'])
    to_unit = st.selectbox("To",['Grams','Kilograms', 'Pounds' ,'Ounces'])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
     result = weight_convertor(from_unit, to_unit, value)
     st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
elif category == 'Pressure':
    from_unit = st.selectbox("From",['Pascal','Bar', 'Atmosphere' ,'Torr'])
    to_unit = st.selectbox("To",['Atmosphere','Bar', 'Pascal' ,'Torr'])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
     result = pressure_convertor(from_unit, to_unit, value)
     st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")