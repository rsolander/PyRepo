import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy as np
import json
import requests
import pandas as pd
import timeit
import math
import datetime
import os
import time
import csv
import plotly.express as px
import streamlit as st
from datetime import datetime, timedelta
import pytz

def main():
    st.title('Test Emails sent from ec2 Instance')
    def sendEm():
        testemail = MIMEMultipart()
        sender_email = "hotjarreports@gmail.com"
        pw = "Rockwell4058"
        target_email = "rsolande@ra.rockwell.com"
        testemail["From"] = sender_email
        testemail["To"] = target_email
        testemail["Subject"] = "Test Subject"

        testemail.attach(MIMEText("Test String, Hello.", "html",'utf-8'))

        session = smtplib.SMTP('smtp.gmail.com', 587, None, 30)
        session.starttls()
        session.login(sender_email, pw)
        #session.set_debuglevel(1)
        text = testemail.as_string()
        session.sendmail(sender_email, target_email, text)
        session.quit()
    if st.button('Send email'):
        sendEm()
if __name__ == "__main__":
    main()
