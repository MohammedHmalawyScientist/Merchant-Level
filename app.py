import streamlit as st
import time
import sklearn
import pandas
import numpy

df = pandas.read_csv('Merchant Level (Deployment).csv')

st.title("Merchant Level")
st.write("This is a web app to recommend the best category and merchant for a customer.")

if st.button('Generate Samples'):
    samples = df['User_Id'].sample(5).tolist()
    st.write(samples)

# Create virtual tester to recommend the top category and merchant based on mean of Trx_Vlu
def recommend_mean(user_id):
    cluster = df[df['User_Id'] == user_id]['Cluster'].iloc[0]

    if cluster == 0:
        st.write(f'User {user_id} informations are:')
        st.write('User Cluster is High Spenders with Top Category: Electronics and Second Category: Fashion')
        st.write('User Cluster is High Spenders with Top Merchant in 1st Category: 25')
        st.write('User Cluster is High Spenders with Top Merchant in 2nd Category: 47')
    elif cluster == 1:
        st.write(f'User {user_id} informations are:')
        st.write('User Cluster is High Spenders with Top Category: Fashion and Second Category: Other')
        st.write('User Cluster is High Spenders with Top Merchant in 1st Category: 11')
        st.write('User Cluster is High Spenders with Top Merchant in 2nd Category: 19')
    elif cluster == 2:
        st.write(f'User {user_id} informations are:')
        st.write('User Cluster is High Spenders with Top Category: Electronics and Second Category: Fashion')
        st.write('User Cluster is High Spenders with Top Merchant in 1st Category: 28')
        st.write('User Cluster is High Spenders with Top Merchant in 2nd Category: 47')
    elif cluster == 3:
        st.write(f'User {user_id} informations are:')
        st.write('User Cluster is High Spenders with Top Category: Electronics and Second Category: Grocery')
        st.write('User Cluster is High Spenders with Top Merchant in 1st Category: 28')
        st.write('User Cluster is High Spenders with Top Merchant in 2nd Category: 8')

# Create virtual tester to recommend the top category and merchant based on count of Trx_Rank
def recommend_count(user_id):
    cluster = df[df['User_Id'] == user_id]['Cluster'].iloc[0]

    if cluster == 0:
        st.write(f'User {user_id} informations are:')
        st.write('User Cluster is Frequent Purchasers with Top Category: Grocery and Second Category: F&B')
        st.write('User Cluster is Frequent Purchasers with Top Merchant in 1st Category: 36')
        st.write('User Cluster is Frequent Purchasers with Top Merchant in 2nd Category: 53')
    elif cluster == 1:
        st.write(f'User {user_id} informations are:')
        st.write('User Cluster is Frequent Purchasers with Top Category: Grocery and Second Category: F&B')
        st.write('User Cluster is Frequent Purchasers with Top Merchant in 1st Category: 8')
        st.write('User Cluster is Frequent Purchasers with Top Merchant in 2nd Category: 1')
    elif cluster == 2:
        st.write(f'User {user_id} informations are:')
        st.write('User Cluster is Frequent Purchasers with Top Category: Grocery and Second Category: F&B')
        st.write('User Cluster is Frequent Purchasers with Top Merchant in 1st Category: 31')
        st.write('User Cluster is Frequent Purchasers with Top Merchant in 2nd Category: 20')
    elif cluster == 3:
        st.write(f'User {user_id} informations are:')
        st.write('User Cluster is Frequent Purchasers with Top Category: Grocery and Second Category: Fashion')
        st.write('User Cluster is Frequent Purchasers with Top Merchant in 1st Category: 8')
        st.write('User Cluster is Frequent Purchasers with Top Merchant in 2nd Category: 47')

# Switch between recommendation methods based on user selection
method = st.selectbox('Select Recommendation Method', ('Mean of Trx_Vlu', 'Count of Trx_Rank'))
user_id = st.number_input('Enter User Id', min_value=0)

if st.button('Recommend'):
    with st.spinner('Wait for it...'):
        time.sleep(1)
    
    if method == 'Mean of Trx_Vlu':
        recommend_mean(user_id)
    elif method == 'Count of Trx_Rank':
        recommend_count(user_id)