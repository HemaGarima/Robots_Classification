import streamlit as st
from joblib import load

st.title("Classification of Robots from their conversation")

model = load('C:\Users\HP\Desktop\Data Science\Development - streamlit\Robots\Robots.joblib')

numbers = []

for i in range(1, 11):
    num = st.number_input(f"Enter number {i} (between 0 and 10103494901760)", min_value=0, max_value=10103494901760, key=f'num_{i}')
    numbers.append(num)

clicked = st.button("Find Robot")

if(clicked == True):
    st.write("You have entered the following numbers:")
    st.write(numbers)
    pred = model.predict([numbers])
    print(pred[0])

    st.header(f"Robot {pred[0]} have said these numbers")