# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:55:15 2022

@author: akhil
"""

import streamlit as st
import pickle
import pandas as pd

new_df = pd.read_csv("final_data.csv")
scored_df = pd.read_csv("Scores_data.csv")

similarity = pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
    movie_index = new_df[new_df["title"] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x:x[1])[1:6]
    
    recommend_movies = []
    
    for i in movies_list:
        movie_id = i[0]
        recommend_movies.append((new_df.iloc[i[0]].title))
        
    return recommend_movies

st.title("Movie Recommender System")

options = st.selectbox("Which movie do you want to select", new_df["title"])
types=  st.selectbox("Do you want to be recommened based on popularity or based on content type", ["popularity","content based"])

if st.button("recommend"):
    if types == "popularity":
        recommendations = scored_df['original_title'].head(10)
        for i in recommendations:
            st.write(i)
    else:
        recommendations = recommend(options)
        for i in recommendations:
            st.write(i)
