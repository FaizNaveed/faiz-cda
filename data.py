import pandas as pd
import streamlit as st


#path = r'C:\Users\arsen\Downloads\Data analysis\class 2/'
#filename= 'Billionaire.csv'
#filepath= path+filename
#data=pd.read_csv(filepath)
#for github we will add the file name directly
data=pd.read_csv('Billionaire.csv')
data['NetWorth'] = data['NetWorth'].apply(lambda x: float(x.replace('$','').replace('B' , '')))
st.header('Billionaire')



#columns scnee
all_country = sorted(data['Country'].unique())
col1,col2= st.columns(2)

#display on streamlit
selected_country=col1.selectbox('Select Country',all_country)
#subset on selected country
subset_country=data[data['Country']==selected_country]

#get unique sources from selected country
source= sorted(subset_country['Source'].unique())

#display multiselect option
selected_source = col1.multiselect('select source',source)

#subset on selected source
subset_source=subset_country[subset_country['Source'].isin(selected_source)]

#Column2
mainstring = '{}-Billionaures'.format(selected_country)
#main.string =selected_country+ '-Billionaire'
col2.header(mainstring)
col2.dataframe(subset_country)
col2.header('Source wise info')
col2.dataframe(subset_source)




#interacivity 
#allCountry = data['Country'].unique()
#selection = st.selectbox('Select country',allCountry)
#subset=data[data['Country']==selection]
#st.table(subset)
#st.dataframe(subset)


#find count of billionaires by country
#bill= data.groupby('Country')['Name'].count().sort_values(ascending=False).head(10)
#st.bar_chart(bill)



#bill= data.groupby('Country')['Name'].count().sort_values(ascending=False).tail(50)
#st.bar_chart(bill)

#find the most popular source of income
#newdata = data.groupby('Source')['Name'].count().sort_values(ascending=False)
#newdata.head(1)

#get cumilative wealth of billionair belonging to US

#UsBill = data[data['Country']== 'United States' ]
#total = UsBill['NetWorth'].cumsum().max()
