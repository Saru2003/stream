import streamlit as st
import pandas as pd
# my_form = st.form(key = "some")
# name = my_form.text_input(label = "Enter the model name")
# age = my_form.text_input(label = "Enter the age")
# submit = my_form.form_submit_button(label = "Submit this form")
import gspread
from oauth2client.service_account import ServiceAccountCredentials
st.set_page_config(page_title="Event 1")
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
sheet = client.open("Event 1").sheet1


# header=st.container()
# dataset=st.container()
# features=modelTraining=st.container()
# with header:
# st.beta_set_page_config(page_title='Event 1')
# PAGE_CONFIG={"page_title":"Event 1"}

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
            with open(pdf.name,"wb") as f:
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
            sheet.insert_row(["One"]+row,len(data)+1)
            st.markdown(f'<h1 style="color:#33ff33;font-size:19px;">{"Successfully registered"}</h1>', unsafe_allow_html=True)
            # st.button("Next",on_click=)
            st.markdown('<form> <button class="w3-button w3-green">Click to complete registration</button></form>', unsafe_allow_html=True)

if sb=="Two":
    st.header("Particpant 1")
    name1=st.text_input('Name of participant 1:')
    rollno1=st.text_input('Roll Number of participant 1: ')
    mail1=st.text_input('Mail ID of participant 1: ')
    clg1=st.text_input('College name of participant 1: ')
    year1=st.selectbox("Year of study for participant 1: ",options=["--Choose--","I","II","III","IV","V"],index=0)
    ph1=st.text_input('Mobile number of participant 1:')
    pdf1=st.file_uploader("College ID of paticipant 1 { in PDF format }",type=['PDF'])
    if pdf1 is not None:
            with open(pdf1.name,"wb") as f:
                f.write(pdf1.getbuffer())
            st.success("Done")
    
    st.header("Particpant 2")
    name2=st.text_input('Name of participant 2:')
    rollno2=st.text_input('Roll Number of participant 2: ')
    mail2=st.text_input('Mail ID of participant 2: ')
    clg2=st.text_input('College name of participant 2: ')
    year2=st.selectbox("Year of study for participant 2: ",options=["--Choose--","I","II","III","IV","V"],index=0)
    ph2=st.text_input('Mobile number of participant 2:')
    pdf2=st.file_uploader("College ID of paticipant 2 { in PDF format }",type=['PDF'])
    if pdf2 is not None:
            with open(pdf2.name,"wb") as f:
                f.write(pdf2.getbuffer())
            st.success("Done")
    if st.button("Submit"):
        name_err1=rollno_err1=mail_err1=clg_err1=year_err1=ph_err1=pdf_err1=0
        name_err2=rollno_err2=mail_err2=clg_err2=year_err2=ph_err2=pdf_err2=0
        row1=[name1,rollno1,mail1,clg1,year1,ph1]
        row2=[name2,rollno2,mail2,clg2,year2,ph2]
## 1
        if name1=="" or name1==' ':
            st.error("Enter valid Name of participant 1")
        else:
            name_err1=1
###
        if rollno1=="" or rollno1==' ':
            st.error("Enter valid Roll Number of participant 1")            
        else:
            rollno_err1=1
###
        if mail1=="" or mail1==' ':
            st.error("Enter valid Mail ID of participant 1")
        else:
            mail_err=1
###
        if clg1=="" or clg1==' ':
            st.error("Enter valid College Name of participant 1")
        else:
            clg_err1=1
###
        if year1=="--Choose--":
            st.error("Enter year of study for participant 1")
        else:
            year_err1=1
###
        if ph1=="" or ph1==' ' or not (ph1[4:].isdigit()) or len(ph1)<10:
            st.error("Enter valid paricipant 1 phone number")
        else:
            ph_err1=1
###
        if pdf1 is None:
            st.error("Upload College ID { in PDF format } for participant 1")
        else:
            pdf_err1=1
        

## 2
        if name2=="" or name2==' ':
            st.error("Enter valid Name of participant 2")
        else:
            name_err2=1
###
        if rollno2=="" or rollno2==' ':
            st.error("Enter valid Roll Number of participant 2")            
        else:
            rollno_err2=1
###
        if mail2=="" or mail2==' ':
            st.error("Enter valid Mail ID of participant 2")
        else:
            mail_err2=1
###
        if clg2=="" or clg2==' ':
            st.error("Enter valid College Name of participant 2")
        else:
            clg_err2=1
###
        if year2=="--Choose--":
            st.error("Enter year of study for participant 2")
        else:
            year_err2=1
###
        if ph2=="" or ph2==' ' or not (ph2[4:].isdigit()) or len(ph2)<10:
            st.error("Enter valid paricipant 2 phone number")
        else:
            ph_err2=1
###
        if pdf2 is None:
            st.error("Upload College ID { in PDF format } for particpant 2")
        else:
            pdf_err2=1
        if (name_err1 and rollno_err1 and mail_err1 and clg_err1 and year_err1 and ph_err1 and pdf_err1 and name_err2 and rollno_err2 and mail_err2 and clg_err2 and year_err2) or (ph_err2 and pdf_err2):
            data=sheet.get_all_values()
            sheet.insert_row(["Two"]+row1+["Second"]+row2,len(data)+1)
            # st.markdown(f'<h1 style="color:#33ff33;font-size:25px;">{"Successfully registered"}</h1>', unsafe_allow_html=True)
            # st.button("Next",on_click=)
            st.markdown('<form> <button class="w3-button w3-green">Click to complete registration</button></form>', unsafe_allow_html=True)
