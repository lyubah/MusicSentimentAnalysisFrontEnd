from urllib import response
import requests
import streamlit as st



def send_request(song_title,artist_name):
    api_url = 'https://master-music-sentiment-analysis-lyubah.endpoint.ainize.ai/predict'
    files = {'song_title':(None, song_title) ,
    'artist_name':(None, artist_name), 
    }
    response = requests.post(api_url, files = files)
    status_code = response.status_code
    return status_code, response

st.title("Music Sentiment Analyzer")
st.header("Classify the general emotion of a song of your choosing")


song_title = st.text_input("Type Song", "Float On")
artist_name = st.text_input("Type artist", "Modest Mouse")

if st.button("Submit"):
     status_code, response = send_request(song_title,artist_name)
     if status_code == 200:
         prediction = response.json()
         st.success(prediction["prediction"])
     else:
         st.error(str(status_code) + " Error")

         







