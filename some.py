import streamlit as st
import pandas as pd
import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from streamlit.components.v1 import iframe
from github import Github
import random
import smtplib
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# my_form = st.form(key = "some")
# name = my_form.text_input(label = "Enter the model name")
# age = my_form.text_input(label = "Enter the age")
# submit = my_form.form_submit_button(label = "Submit this form")
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# img=Image.open("Untitled design.png")
st.set_page_config(page_title="TZ23 General Registration",page_icon="Untitled design.png")
# c1,c2,c3=st.columns([6,9,1])
# with c3:
#             st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
#               st.markdown('<form> <button style="height:58px;width:120px" font-size:100px>Click to quit registration</button></form>', unsafe_allow_html=True)
# st.write("dd")
hide_ststyle = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_ststyle, unsafe_allow_html=True)
i_=0
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("final.json", scope)
client = gspread.authorize(creds)
sheet = client.open("registration").sheet1

# f=open("ID.txt","r")
# d=f.read()
# print(d)
# f.close()
# f1=open("ID.txt","w")
# f1.write("14")
# f1.close()

# header=st.container()
# dataset=st.container()
# features=modelTraining=st.container()
# with header:
# st.beta_set_page_config(page_title='Event 1')
# PAGE_CONFIG={"page_title":"Event 1"}

# st.title("hello")
p=st.empty()
st.title("TZ23 General registration ")
# st.write("Each")
# st.header("Select the number of participants")
# sb=st.selectbox("Select the number of participants",options=["--Choose--","One","Two"],index=0)
# if sb=="One":
name=st.text_input('Enter your full name:')
rollno=st.text_input('Enter your roll number: ')
mail=st.text_input('Enter your mail ID: ')
clg=st.text_input('Enter your college name: ')
year=st.selectbox("Year of study: ",options=["--Choose--","I","II","III","IV","V"],index=0)
ph=st.text_input('Your mobile number (follow this format - without country code: 935xxxxxxx): ')
# pdf=st.file_uploader("College ID { in PDF format }",type=['PDF'])
# if pdf is not None:
#         with open(pdf.name,"wb") as f:
#             f.write(pdf.getbuffer())
#         st.success("Done")
def fun2():
            st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
def fun():
#             try:
                        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                        server.login("21i252@psgtech.ac.in","A1.2.3.4.5.6")
                        text=f"Hello {name}! \nGet ready to enroll for the electrifying events of Technotronz'23.\nYour login credentials are :\nRegistration ID: TZ23{str(int(r[4:])+1)}\nName: {name}\nContact number: {ph}\n\nNOTE: This mail along with the Registeration pdf be used as verification.\n\nBest regards,\nTeam Technotronz."
                        message='Subject: {}\n\n{}'.format("Technotronz Registration Completed!",text )
                        server.sendmail("21i252@psgtech.ac.in",mail,message)
                        server.quit()
                        st.write("(A mail has been sent your registered mail id)")
#             except:
#                         st.write("Invalid Mail ID is entered, no registration info will be sent.")
def check(email):
            if not (re.fullmatch(regex, email)):
                        return 1
            return 0
def valid(name):
    name=name.replace(" ","").replace(".","")
    return name.isalpha()
def valid2(name):
    return name.replace(" ","").isalpha()
st.write("Note: Once you have submitted the detials, save the Technotronz'23 ID PDF for participation in events!")
col1,col2,col3=st.columns([2,1,2])
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(255, 255, 255);
    height:1.5em;
    width: 3em; 
    font-size: 29px;
    color: black;
}
</style>""", unsafe_allow_html=True)
with col2:
            d=st.button("Submit")
if d:
#   with col1:
        name_err=rollno_err=mail_err=clg_err=year_err=ph_err=pdf_err=0
        row=[name,rollno,mail,clg,year,ph]
        if not valid(name):
            st.error("Enter valid Name of participant")
        else:
            name_err=1
    ###
        if rollno=="" or rollno==' ':
            st.error("Enter valid Roll Number of participant")            
        else:
            rollno_err=1
    ###     
        if check(mail):
            st.error("Enter valid Mail ID of participant")
        else:
            mail_err=1
    ###
        if not valid2(clg):
            st.error("Enter valid College Name of participant")
        else:
            clg_err=1
    ###
        if year=="--Choose--":
            st.error("Enter year of study for participant")
        else:
            year_err=1
    ###
        if ph=="" or ph==' ' or not (ph[4:].isdigit()) or len(ph)<10 or len(ph)>10:
            st.error("Enter valid paricipant phone number")
        else:
            ph_err=1

    ###
        # if pdf is None:
        #     st.error("Upload College ID { in PDF format }")
        # else:
        #     pdf_err=1
        # if name_err==rollno_err==mail_err==clg_err==year_err==ph_err==pdf_err==1:
        if name_err==rollno_err==mail_err==clg_err==year_err==ph_err==1:
            print(row)
            data=sheet.get_all_values()

            # st.markdown(f'<h1 style="color:#33ff33;font-size:25px;font-family: Verdana, Geneva, Tahoma, sans-serif">{"Successfully registered"}</h1>', unsafe_allow_html=True)

    #         g = Github("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")
    #         repo=g.get_repo("Saru2003/id")
    #         file = repo.get_contents("ID.txt")

    #         g=Github("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")
    #         repo=g.get_repo("Saru2003/id")
    #         file = repo.get_contents("ID.txt")
    #         content = int(file.decoded_content.decode())
    #         repo.update_file(file.path, "commit message", str(content+1), file.sha)

            env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
            template = env.get_template("index (1).html")
    #         f=open("ID.txt","r")
    #         r=f.read()
    #         ran_num=str(random.randint(1, 100))
    #         ran_letter = chr(random.randint(ord('A'), ord('Z')))
    # #         print(ran_letter+ran_num)
    #         r=ran_letter+ran_num
            r=sheet.cell(len(data),1).value
            html = template.render(reg="TZ23"+str(int(r[4:])+1),name=name,mail=mail,ph=ph)
    #         f.close()        
    #         repo.update_file(file.path, "commit message", str(int(r)+1), file.sha)
#             pdf = pdfkit.from_string(html, False)
            pdf = pdfkit.from_string(html,False)
            st.success("Your Registration ID is generated!")

    #         server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    #         server.login("21i252@psgtech.ac.in","A1.2.3.4.5.6")
    #         text=f"Hello {name}! You now can register for upcoming Technotonz events\nYour login credentials:\nRegistration ID: {r}\nName: {name}\nContact number: {ph}\n\nNote: You can use this mail as verification if the registration pdf went missing."
    #         message='Subject: {}\n\n{}'.format("Technotronz Registration Completed!",text )
    # #         server.sendmail("21i252@psgtech.ac.in",mail,message)

    #         server.quit()
    #         st.write("(A mail has been sent your registered mail id)")
            st.download_button("⬇️ Download PDF for particpating in Technotronz events", data=pdf,file_name="technotronz'23_ID.pdf", mime="application/octet-stream",)
#             st.download_button("⬇️ Download PDF for particpating in Technotronz events", data=pdf, mime="application/octet-stream",)
            sheet.insert_row(["TZ23"+str(int(r[4:])+1)]+row,len(data)+1)
            fun() 
#         fun2()
#             st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
#         st.markdown('<form> <button class="w3-button w3-green">Click to complete registration</button></form>', unsafe_allow_html=True)
#         if name_err==rollno_err==mail_err==clg_err==year_err==ph_err==1:

# def fun():
#             server=smtplib.SMTP_SSL("smtp.gmail.com",465)
#             server.login("21i252@psgtech.ac.in","A1.2.3.4.5.6")
#             text=f"Hello {name}! You now can register for upcoming Technotonz events\nYour login credentials:\nRegistration ID: {r}\nName: {name}\nContact number: {ph}\n\nNote: You can use this mail as verification if the registration pdf went missing."
#             message='Subject: {}\n\n{}'.format("Technotronz Registration Completed!",text )
#             server.sendmail("21i252@psgtech.ac.in",mail,message)
#             server.quit()
#             st.markdown('<form> <button class="w3-button w3-green">Click to complete/quit registration</button></form>', unsafe_allow_html=True)
# if sb=="Two":
#     st.header("Particpant 1")
#     name1=st.text_input('Name of participant 1:')
#     rollno1=st.text_input('Roll Number of participant 1: ')
#     mail1=st.text_input('Mail ID of participant 1: ')
#     clg1=st.text_input('College name of participant 1: ')
#     year1=st.selectbox("Year of study for participant 1: ",options=["--Choose--","I","II","III","IV","V"],index=0)
#     ph1=st.text_input('Mobile number of participant 1 (follow this format: 935xxxxxxx):')
#     pdf1=st.file_uploader("College ID of paticipant 1 { in PDF format }",type=['PDF'])
#     if pdf1 is not None:
#             with open(pdf1.name,"wb") as f:
#                 f.write(pdf1.getbuffer())
#             st.success("Done")
    
#     st.header("Particpant 2")
#     name2=st.text_input('Name of participant 2:')
#     rollno2=st.text_input('Roll Number of participant 2: ')
#     mail2=st.text_input('Mail ID of participant 2: ')
#     clg2=st.text_input('College name of participant 2: ')
#     year2=st.selectbox("Year of study for participant 2: ",options=["--Choose--","I","II","III","IV","V"],index=0)
#     ph2=st.text_input('Mobile number of participant 2 (follow this format: 935xxxxxxx):')
#     pdf2=st.file_uploader("College ID of paticipant 2 { in PDF format }",type=['PDF'])
#     if pdf2 is not None:
#             with open(pdf2.name,"wb") as f:
#                 f.write(pdf2.getbuffer())
#             st.success("Done")
#     if st.button("Submit"):
#         name_err1=rollno_err1=mail_err1=clg_err1=year_err1=ph_err1=pdf_err1=0
#         name_err2=rollno_err2=mail_err2=clg_err2=year_err2=ph_err2=pdf_err2=0
#         row1=[name1,rollno1,mail1,clg1,year1,ph1]
#         row2=[name2,rollno2,mail2,clg2,year2,ph2]
# ## 1
#         if name1=="" or name1==' ':
#             st.error("Enter valid Name of participant 1")
#         else:
#             name_err1=1
# ###
#         if rollno1=="" or rollno1==' ':
#             st.error("Enter valid Roll Number of participant 1")            
#         else:
#             rollno_err1=1
# ###
#         if mail1=="" or mail1==' ':
#             st.error("Enter valid Mail ID of participant 1")
#         else:
#             mail_err=1
# ###
#         if clg1=="" or clg1==' ':
#             st.error("Enter valid College Name of participant 1")
#         else:
#             clg_err1=1
# ###
#         if year1=="--Choose--":
#             st.error("Enter year of study for participant 1")
#         else:
#             year_err1=1
# ###
#         if ph1=="" or ph1==' ' or not (ph1[4:].isdigit()) or len(ph1)<10:
#             st.error("Enter valid paricipant 1 phone number")
#         else:
#             ph_err1=1
# ###
#         if pdf1 is None:
#             st.error("Upload College ID { in PDF format } for participant 1")
#         else:
#             pdf_err1=1
        

# ## 2
#         if name2=="" or name2==' ':
#             st.error("Enter valid Name of participant 2")
#         else:
#             name_err2=1
# ###
#         if rollno2=="" or rollno2==' ':
#             st.error("Enter valid Roll Number of participant 2")            
#         else:
#             rollno_err2=1
# ###
#         if mail2=="" or mail2==' ':
#             st.error("Enter valid Mail ID of participant 2")
#         else:
#             mail_err2=1
# ###
#         if clg2=="" or clg2==' ':
#             st.error("Enter valid College Name of participant 2")
#         else:
#             clg_err2=1
# ###
#         if year2=="--Choose--":
#             st.error("Enter year of study for participant 2")
#         else:
#             year_err2=1
# ###
#         if ph2=="" or ph2==' ' or not (ph2[4:].isdigit()) or len(ph2)<10:
#             st.error("Enter valid paricipant 2 phone number")
#         else:
#             ph_err2=1
# ###
#         if pdf2 is None:
#             st.error("Upload College ID { in PDF format } for particpant 2")
#         else:
#             pdf_err2=1
#         if (name_err1 and rollno_err1 and mail_err1 and clg_err1 and year_err1 and ph_err1 and pdf_err1 and name_err2 and rollno_err2 and mail_err2 and clg_err2 and year_err2) or (ph_err2 and pdf_err2):
#             data=sheet.get_all_values()
#             sheet.insert_row(["Two"]+row1+["Second"]+row2,len(data)+1)
#             # st.markdown(f'<h1 style="color:#33ff33;font-size:25px;">{"Successfully registered"}</h1>', unsafe_allow_html=True)
#             # st.button("Next",on_click=)
#             st.markdown(f'<h1 style="color:#33ff33;font-size:25px;font-family: Verdana, Geneva, Tahoma, sans-serif">{"Successfully registered"}</h1>', unsafe_allow_html=True)
#             st.markdown('<form> <button class="w3-button w3-green">Click to complete registration</button></form>', unsafe_allow_html=True)x
