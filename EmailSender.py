# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:16:23 2020

@author: saimi
"""

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

type(conn) #Check

conn.ehlo()
conn.starttls()
conn.login('username', 'password')
conn.sendmail('from-id', 'to-id', 'Subject: So long..\n\nDear Sai\n, Hello')
conn.quit()