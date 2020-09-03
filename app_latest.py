import streamlit as st
import pandas as pd
from PIL import Image
import logging
#Custom modulespip
#Module to PredictorFolder values
from PredictorFolder.predict import predictor as pt
#Module to get values from keys
from DescriptionCodes_Folder.get_value import reason_label as rl
from DescriptionCodes_Folder.get_value import desc_value as gv
#Module to retrain model with new data
from Train_Retrain_Folder.model_latest import train_retrain as ml

logging.basicConfig(filename='C:\\Users\\subra\\PycharmProjects\\Group4A_latest\\Logging\\test.log',level=logging.DEBUG)

def main():

    img=Image.open('DatasetFolder/Absentism_pic.png')
    st.image(img,width=700)


    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Predicting Absent Hours for Employees </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    
    #Option to user whether bulk upload data or Single Sample check
    st.subheader('Select a Data Input Options')
    Data_Option=st.selectbox('',['--Select an option--','Upload csv file for bulk data','Input single data via UI','Re-train Model'])
    #logging.debug('Options given to user successfully')
    if Data_Option =='Upload csv file for bulk data':
       #Data input via CSV                      
        st.subheader('Instructions')
        st.set_option('deprecation.showfileUploaderEncoding', False)
        st.write('Please upload a .CSV file')
        st.write('Please maintain the below columns in the exact same sequence in your file .')
        st.write('R_code,Transportation expense,Office Distance,Age,Body mass index')
        st.write('As of now we are` not handling empty cells')
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

        if uploaded_file is not None:
            
            try:
                uploaded_data=pd.read_csv(uploaded_file)
                if st.button('Predict Absent Hours'):
                    pred_hours=pt.predict(uploaded_data)
                    #st.write(type(pred_hours))
                    Pred_hours=pd.Series(pred_hours,name='Predicted_Absent_hours')
                    FinalData=pd.concat([uploaded_data,Pred_hours],axis=1)
                    st.subheader('Predictions')
                    st.write(FinalData)
            except:
                st.write('Please follow the instructions !!')
                 
    elif Data_Option =='Input single data via UI':

        #Input for Reason for Absence of the Employee
        r_l=gv(rl)
        reason=st.selectbox("Select Reason for Absense ", tuple(rl.keys()))
        st.write('You selected the reason as :',reason)
        v_reason=r_l.get_value(reason)
        st.write('Reason Code : ',v_reason)

        #Input for Office travel expenses

        Travel_Expense=st.number_input('Travel Expenses to Office in Dollars ',1.0,1000.0)
        st.write('Travel Expenses to Office as :',Travel_Expense)

        #Input for Employees Distance from Office
        Distance=st.number_input('Distance from Residence to Work in kms',1.0,100.0)
        st.write('You Selected Distance as :',Distance)


        #Input Employees Age
        Age=st.number_input('Enter Employee Age in Years',0.0, 100.0)
        st.write('You entered Employee Age as ', Age ,'years')


        #Input for Employess Body Mass Index
        BMI=st.number_input('Enter a BMI index',0.0,100000.0)
        st.write('You selected Body Mass Index as :',BMI)
        pred_hours=''

        #creating a dataframe to give input to the code
        columns=['R_code','Transportation expense','Office Distance','Age','Body mass index']
        df_test=pd.DataFrame({'R_code':[v_reason],'Transportation expense':[Travel_Expense],'Office Distance':[Distance],'Age':[Age], 'Body mass index':[BMI]},columns=columns)

        if st.button('Predict Absent Hours'):

            pred_hours=pt.predict(df_test)
            st.success('Prediction {}'.format(pred_hours[0]))

    elif Data_Option =='Re-train Model':
        st.subheader('Instructions')
        st.set_option('deprecation.showfileUploaderEncoding', False)
        st.write('Please upload a training file in .CSV format')
        st.write('Please maintain the below columns in the exact same sequence in your file .')
        st.write('R_code,Transportation expense,Office Distance,Age,Body mass index','Absnt_hr_estimate')
        st.write('As of now we are not handling empty cells')
        uploaded_file = st.file_uploader("Upload CSV file", type="csv")

        if uploaded_file is not None:

            try:
                uploaded_data = pd.read_csv(uploaded_file)
                if st.button('Re-Train Model'):
                    ReTrain_status = ml.re_train(uploaded_data)

                    st.success(ReTrain_status)
            except:
                st.write('Please follow the instructions !!')



    else :
        st.write('')
logging.debug('checking log')
if __name__=='__main__':
    main()
    


