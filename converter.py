import streamlit as st

st.title("Unit Converter")
st.markdown("#### Length, Weight, And Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real time.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to miles":
            return value * 0.621371
        elif unit == "Miles to kilometer":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilogram to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilogram":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hour":
            return value / 60
        elif unit == "Hour to Minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

if category == "Length":
    unit = st.selectbox("Select Conversion", ["Kilometer to miles", "Miles to kilometer"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilogram to pounds", "Pounds to kilogram"])
elif category == "Time":
    unit = st.selectbox("Select Conversion", [
        "Seconds to minutes", "Minutes to seconds", "Minutes to hour",
        "Hour to Minutes", "Hours to days", "Days to hours"
    ])

value = st.number_input("Enter the value to convert", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Conversion could not be performed. Please check your inputs.")
