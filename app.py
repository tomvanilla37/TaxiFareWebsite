import streamlit as st
import datetime
import requests

'''
# Flo's TaxiFareModel
'''

st.markdown('''
Welcome to the convenient NY taxi fare estimator.
Please input the ride information and submit by clicking the button.
''')

st.markdown('''
Please input the ride information and submit by clicking the button.
''')

ride_date = st.date_input(
    "Date of Ride",
    datetime.datetime(2012, 10, 6, 12, 10, 20))
#st.write('Your birthday is:', d)

ride_time = st.time_input('Time of Ride', datetime.datetime(2012, 10, 6, 12, 10, 20))

#st.write('Alarm is set for', t)

st.write(f'Your ride will be on {ride_date} at {ride_time}.' )

lon_input = st.number_input(
    "Insert pickup longitude",
    value=float(40.7614327),
    step=1e-6,
    format="%.7f")

lat_input = st.number_input(
    'Insert pickup latitude',
    value=float(-73.9798156),
    step=1e-6,
    format="%.7f")

drop_lon_input = st.number_input(
    'Insert drop-off longitude',
    value=float(40.6513111),
    step=1e-6,
    format="%.7f")


drop_lat_input = st.number_input(
    'Insert drop-off latitude',
    value=float(-73.8803331),
    step=1e-6,
    format="%.7f")


num_passenger = st.slider('Select number of passengers', 1, 8, 1)

st.write(ride_time)

if st.button('predict ride fare'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.write('predicting...')


    pickupdatetime =  f"{ride_date} {ride_time}"


    url = 'https://taxifare.lewagon.ai/predict'

    response = requests.get(url,
        params={'pickup_datetime': pickupdatetime,
                'pickup_longitude': str(lon_input),
                'pickup_latitude': str(lat_input),
                'dropoff_longitude': str(drop_lon_input),
                'dropoff_latitude': str(drop_lat_input),
                'passenger_count': str(num_passenger)
                })

    #st.write("correct request url format should be:")
    #st.write("https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2")
    #st.write(response.request.url)
    fare = {response.json()["fare"]}

    st.metric("The estimated fare is:", "$437.8")

else:
    st.write('I was not clicked 😞')

###conneect to API###
