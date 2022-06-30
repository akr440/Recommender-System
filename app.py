from turtle import left
from urllib import response
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests

# fetching data about the movie from the api
def fetch_poster(id):
    data=requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    data=data.json()
    poster_data="https://image.tmdb.org/t/p/w500/"+data['poster_path']
    return poster_data



# page configuration
st.set_page_config(page_title="Recommender",layout='wide')
st.title('Movie Recommendation System')

# getting data from pickle file
newdata = pickle.load(open('new_movie_data.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
newdata=pd.DataFrame(newdata)

# recommendation function
def recommend(movie):
    movie_index=newdata[newdata['title']==movie].index[0]
    similar = similarity[movie_index]
    lst=sorted(list(enumerate(similar)),reverse=True,key = lambda x:x[1])
    l=[] 
    poster=[]
    for i in lst[0:11]:
        movie_names=newdata.iloc[i[0]].title
        idd=newdata.iloc[i[0]].id
        poster.append(fetch_poster(idd))
        l.append(newdata.iloc[i[0]].title)
    return l,poster


# selection box
selected_movie=st.selectbox(
    'Select your movie',
    newdata['title'].values
)


# button 
if st.button('Recommend'):
    names, poster= recommend(selected_movie)
    x=0
    for i in range(0, 2):
        cols = st.columns(5)
        cols[0].text(names[0+x])
        cols[0].image(poster[0+x])
        cols[1].text(names[1+x])
        cols[1].image(poster[1+x])
        cols[2].text(names[2+x])
        cols[2].image(poster[2+x])
        cols[3].text(names[3+x])
        cols[3].image(poster[3+x])
        cols[4].text(names[4+x])
        cols[4].image(poster[4+x])
        x=5
        '\n'


    