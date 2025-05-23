import streamlit as st
import datetime
import requests
'''
# TaxiFareModel fronttttt
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
date = st.date_input("Choose a date", value=datetime.date.today())
time = st.time_input("Choose a time", value=datetime.datetime.now().time())
dt = datetime.datetime.combine(date, time)
p_longtitude = st.number_input("Pickup longitude")
p_latitude = st.number_input("Pickup latitude")
d_longtitude = st.number_input("Dropoff longitude")
d_latitude = st.number_input("Dropoff latitude")
passenger_count = st.number_input("Passenger count", min_value=1, max_value=10, value=1)

st.markdown(f"Time: **{dt}**")
st.markdown(f"Pickedup place: **longtitude is {p_longtitude}**, latitude is {p_longtitude}**")
st.markdown(f"Droppedoff place: **longtitude is {d_longtitude}**, latitude is {d_longtitude}**")
st.markdown(f"Num of: {passenger_count}**")



# st.markdown(
# '''
# Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# ''')

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# st.markdown('''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# # Finally, we can display the prediction to the user
# ''')
params = {
    'pickup_datetime': dt,
    'pickup_longitude': p_longtitude,
    'pickup_latitude': p_latitude,
    'dropoff_longitude': d_longtitude,
    'dropoff_latitude': d_latitude,
    'passenger_count': passenger_count
}
response = requests.get(url, params=params)

st.markdown(f"{response.json()}")
