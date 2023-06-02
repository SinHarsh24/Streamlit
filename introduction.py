import streamlit as st 

#Set Title
st.title("First Work")

#add Image

from PIL import Image

st.subheader('This ia a sub header')

image=Image.open("C:/Users/sinha/Downloads/image27_frqkzv.png")
st.image(image,use_column_width=True)

st.write('Writing a text here')

st.markdown('This is a markdown')

st.success('Congrats we run the app successfully')

st.info('This is a information')

st.warning("Be cautious")

st.error("Oops you run into an error,you need to rerun your app again ")

st.help(range)


#####################################################

import numpy as np 
import pandas as pd
import seaborn as sns

dataframe=np.random.rand(10,20)
st.dataframe(dataframe)

st.text("---"*100)

df=pd.DataFrame(np.random.rand(10,20),columns=('col %d' % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=1))

st.text("---"*100)

#Display chart

chart_data=pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.line_chart(chart_data)

st.text("---"*100)

st.area_chart(chart_data)

chart_data=pd.DataFrame(np.random.randn(50,3), columns=['a','b','c'])
st.bar_chart(chart_data)

import matplotlib.pyplot as plt

arr=np.random.normal(1,1,size=100)
plt.hist(arr,bins=20)
st.pyplot()

st.text("---"*100)

import plotly
import plotly.figure_factory as ff

#adding histogram

x1=np.random.randn(200)-2
x2=np.random.randn(200)
x3=np.random.randn(200)-2

hist_data=(x1,x2,x3)
group_lbaels=['Group1','Group2','Group3']

fig=ff.create_distplot(hist_data,group_lbaels,bin_size=[.2,.25,.5])
st.plotly_chart(fig,use_container_width=True)

st.text("---"*100)

df=pd.DataFrame(np.random.randn(100,2)/[50,50]+[37.76,-122.4],columns=['lat','lon'])
st.map(df)

st.text("---"*100)

##Creating Buttons

if st.button("Say Hello"):
	st.write("Hello is here")
else:
	st.write("Why are u here")

st.text("---"*100)

genre=st.radio("What is your favorite genre?",('Comedy','Drama','Documentry'))

if genre== 'Comedy':
	st.write("Oh you like comedy")
elif genre == 'Drama':
	st.write("Yeah drama is good")
else:
    st.write("I see!")  

#Select Buttons

option=st.selectbox("How was your day?",('fantastic','Good','Not good'))
st.write("You said your day was ",option)

st.text("---"*100)

option=st.multiselect("How was your day?",('fantastic','Good','Not good'))
st.write("You said your day was ",option)

st.text("---"*100)

age=st.slider("How old are you",0,150,10)
st.write("Your age is ",age)

values=st.slider('select a range of values',0,200,(15,80))
st.write("You selected a range between",values)

number=st.number_input('Imput some numbers')
st.write("The number you imputed is:",number)


st.text("---"*100)
st.text("---"*100)


#File Uploader

upload_file=st.file_uploader("Choose a csv file",type='csv')
if upload_file is not None:
	data=pd.read_csv(upload_file)
	st.write(data)
	st.success("Successfully Uploaded")
else:
	st.markdown("Please upload a csv file")

#Color Picker

color=st.sidebar.color_picker("pick your preferred color",'#00f900')
st.write("This is your color",color)

st.text("---"*100)

#SideBar

add_sidebar=st.sidebar.selectbox("What is your favorite game?",('Cricket','Football','Others'))


#pogress bar

import time

my_bar=st.progress(0)
for percent_complete in range(100):
	time.sleep(0.1)
	my_bar.progress(percent_complete+1)

#OR

with st.spinner('Wait for it'):
	time.sleep(5)
st.success("successfull")
st.balloons()


st.text("---"*100)
