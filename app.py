import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# load test data for seeing current image
test_data = pickle.load(open('test_data.pkl','rb'))
test_data_ = pd.DataFrame(test_data)

# load train data for seeing recommendations
train_data = pickle.load(open('img_data.pkl','rb'))
train_data_ = pd.DataFrame(train_data)

# load model;
knn = pickle.load(open('model_recommend.pkl','rb'))

# tfidf for text:
X_test = pickle.load(open('test_array.pkl','rb'))

st.title("Fashion Recommendation system")

st.header('About Recommendation model:')
st.markdown("The model used here is 'Nearest Neighbours'. For a given data point it gives "
            "us similar points within the neighbourhood. Here, for a given women wear we get 10 more recommendations. "
            "Also this model depends heavily on the 'title' of the product but also takes into "
            "consideration the color and brand of the same.")

title_current = st.selectbox('Search for the product you want here:',
                    list(test_data_['title']))
product = test_data_[(test_data_['title'] == title_current)]
s1 = product.index[0]
captions = [test_data_['brand'].values[s1],test_data_['formatted_price'].values[s1]]
c1,c2,c3 = st.columns(3)
with c1:
    st.image(test_data_['medium_image_url'].values[s1])
with c2:
    st.text('Brand--->')
    st.text('Color--->')
    st.text('Price in $--->')
with c3:
    st.text(test_data_['brand'].values[s1])
    st.text(test_data_['color'].values[s1])
    st.text(test_data_['formatted_price'].values[s1])

distances, indices = knn.kneighbors([X_test.toarray()[s1]])
result1 = list(indices.flatten())[:5]
result2 = list(indices.flatten())[5:]

if st.button('Click here to get recommendations'):
    st.success('Hope you like the below recommendations :)')
    col1,col2,col3,col4,col5 = st.columns(5)
    lst1 = [col1,col2,col3,col4,col5]
    for i,j in zip(lst1,result1):
        with i:
            st.text(train_data_['brand'].values[j])
            st.text(train_data_['color'].values[j])
            st.image(train_data_['medium_image_url'].values[j])

    col6, col7, col8, col9, col10 = st.columns(5)
    lst2 = [col6, col7, col8, col9, col10]
    for k,l in zip(lst2,result2):
        with k:
            st.text(train_data_['brand'].values[l])
            st.text(train_data_['color'].values[l])
            st.image(train_data_['medium_image_url'].values[l])

    st.success('Thank You for Shopping, Stay Classy!!')

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer: {
	content:Made by Bairagi Saurabh :);
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


