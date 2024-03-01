import time
from tkinter import *
import jobscrape
import sendMail

# -----------Constants---------------
BLUE = "#49b8f3"
GREY = "#2c2c2c"
FONT_NAME = "Courier"
# -----------------------------------


def search():
    # print(f"{job_search1.get()},{job_search2.get()},{job_search3.get()}")
    n = jobscrape.BackendWork()
    n.t1 = job_search1.get()
    n.t2 = job_search2.get()
    n.t3 = job_search3.get()
    n.login()


def mail_service():
    mail = sendMail.Mail()
    mail.receiver_email = email.get()
    mail.name = name.get()
    mail.send_mail()


window = Tk()
window.title("JOBScraper")
window.config(background=GREY, padx=10, pady=10)
window.minsize(width=900, height=600)

# Canvas window
canvas = Canvas(width=560, height=202, bg=GREY, highlightthickness=0)
img = PhotoImage(file="img.png")  # to convert to PhotoImage type
canvas.create_image(383, 140, image=img)
canvas.place(x=100, y=200)

# Label
l1 = Label(text="Name:", bg=GREY, font=FONT_NAME, fg=BLUE, pady=20)
l1.place(x=80, y=60)
l2 = Label(text="E-mail:", bg=GREY, font=FONT_NAME, fg=BLUE)
l2.place(x=80, y=120)

# Entry
name = Entry(width=20, borderwidth=2)
name.place(x=160, y=80)
email = Entry(width=20, borderwidth=2)
email.place(x=160, y=120)
# Header1
job_search1 = Entry(width=15, borderwidth=2)
job_search1.place(x=80, y=10)
time.sleep(3)
# Header2
job_search2 = Entry(width=15, borderwidth=2)
job_search2.place(x=180, y=10)
time.sleep(3)
# Header3
job_search3 = Entry(width=15, borderwidth=2)
job_search3.place(x=280, y=10)
time.sleep(3)

# Button
b1 = Button(text="Search", width=18, height=1, command=search)
b1.place(x=280, y=40)
b2 = Button(text="Send Mail", width=18, height=1, command=mail_service)
b2.place(x=160, y=160)

window.mainloop()
