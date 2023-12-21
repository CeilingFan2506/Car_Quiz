import requests
import json
import streamlit as st



def get_prediction(data={"sentence":"Hello"}):
  #copy paste your aiservice link here
  url = 'https://askai.aiclub.world/5c639127-bc1a-4891-9efa-b83136f034ee'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  return response

#creating the web app
#setting the title
st.title("Car_Quiz")#change the title as your web app

#setting up the sub title
st.subheader("Guess the car brand")#change the subheader as your web app

#text input
text = st.text_input("Give the correct answer")

#settin the data
input_data = {"sentence":text}
#getting the respoense
prediction = get_prediction(input_data)
country = json.loads(json.loads(prediction)['body'])['prediction']


