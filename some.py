import streamlit as st
import pandas as pd
# my_form = st.form(key = "some")
# name = my_form.text_input(label = "Enter the model name")
# age = my_form.text_input(label = "Enter the age")
# submit = my_form.form_submit_button(label = "Submit this form")
import gspread
from oauth2client.service_account import ServiceAccountCredentials

hide_ststyle = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_ststyle, unsafe_allow_html=True)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("final.json", scope)
client = gspread.authorize(creds)
sheet = client.open("streamlink").sheet1


# header=st.container()
# dataset=st.container()
# features=modelTraining=st.container()
# with header:
    
# st.title("hello")
p=st.empty()
st.title("Event name")
# st.header("Select the number of participants")
sb=st.selectbox("Select the number of participants",options=["--Choose--","One","Two"],index=0)
if sb=="One":
    name=st.text_input('Name of participant:')
    rollno=st.text_input('Roll Number of participant: ')
    mail=st.text_input('Mail ID of participant: ')
    clg=st.text_input('College name of participant: ')
    year=st.selectbox("Year of study for participant: ",options=["--Choose--","I","II","III","IV","V"],index=0)
    ph=st.text_input('Mobile number of participant  ')
    pdf=st.file_uploader("College ID { in PDF format }",type=['PDF'])
    if pdf is not None:
            with open("/home/sarvesh/Documents/pdfs/("+name+ ")"+pdf.name,"wb") as f:
                f.write(pdf.getbuffer())
            st.success("Done")

    if st.button("Submit"):
        name_err=rollno_err=mail_err=clg_err=year_err=ph_err=pdf_err=0
        row=[name,rollno,mail,clg,year,ph]
        if name=="" or name==' ':
            st.error("Enter valid Name of participant")
        else:
            name_err=1
###
        if rollno=="" or rollno==' ':
            st.error("Enter valid Roll Number of participant")            
        else:
            rollno_err=1
###
        if mail=="" or mail==' ':
            st.error("Enter valid Mail ID of participant")
        else:
            mail_err=1
###
        if clg=="" or clg==' ':
            st.error("Enter valid College Name of participant")
        else:
            clg_err=1
###
        if year=="--Choose--":
            st.error("Enter year of study for participant")
        else:
            year_err=1
###
        if ph=="" or ph==' ' or not (ph[4:].isdigit()) or len(ph)<10:
            st.error("Enter valid paricipant phone number")
        else:
            ph_err=1
###
        if pdf is None:
            st.error("Upload College ID { in PDF format }")
        else:
            pdf_err=1
        if name_err==rollno_err==mail_err==clg_err==year_err==ph_err==pdf_err==1:
            print(row)
            data=sheet.get_all_values()
            sheet.insert_row(row,len(data)+1)
            st.markdown(f'<h1 style="color:#33ff33;font-size:25px;">{"Successfully registered"}</h1>', unsafe_allow_html=True)
            # st.button("Next",on_click=)
