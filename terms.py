from tkinter import * # this imports everything related to TKinter
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import messagebox

window = Tk()
label =Label(window,text="I've read, understand and accept Terms and Conditions, privacy policy of this store")
label.place(x=0,y=425)
window.geometry("600x500")
window.title("Terms & Conditions")

icon = PhotoImage(file="C:\\Users\\Nick Looby\\PycharmProjects\\notion.py\\pictures\\microsoft_window.png")
window.iconphoto(True,icon)

def display():
    if (x.get()==1):
        print("you will receive promo material by email")
def display2():
    if (y.get()==1):
        print("you will receive promo material by sms")

def click():
    messagebox.showinfo(' terms & conditons',
    message="You have accepted the terms and conditons")
    close()

def click2():
    messagebox.showwarning(' terms & conditons',
    message="You did not accept the terms and conditons")
    close()

def close():
    window.quit()

x = IntVar()
y = IntVar()
sms_check = Checkbutton(window,
                        text="receive promotional material via sms",
                        variable = x,
                        onvalue=1,
                        offvalue=0,
                        command = display)
email_check = Checkbutton(window,
                        text= "receive promotional material via email",
                        variable=y,
                        onvalue=1,
                        offvalue=0,
                        command = display2)

sms_check.place(x=0,y=400)
email_check.place(x=0,y=375)

photo = PhotoImage(file='C:\\Users\\Nick Looby\\PycharmProjects\\notion.py\\pictures\\microsoft1.png')

photo_label = Label(window,
                    image=photo)
photo_label.place(x=0,y=50)

button = Button(window,
                text='Accept',
                command=click,
                font=30,
                fg='black',
                bg='grey',
                activeforeground='black',
                activebackground='grey'
                )
button.place(x=180,y=455)
button2 = Button(window,
                text='Do not Accept',
                command=click2,
                font=30,
                fg='black',
                bg='grey',
                activeforeground='black',
                activebackground='grey'
                )
button2.place(x=270,y=455)

ttk.Label(window, text="Our Terms and Conditions").grid(column=0,row=0)
scrolW=70
scrolH=10
scr=scrolledtext.ScrolledText(window, width=scrolW, height=scrolH, wrap=WORD)
long_text= """inuing to use the Services after being notified of a change to these Terms.
Your Privacy
1. Your Privacy. Your privacy is important to us. Please read the Microsoft Privacy Statement 
(https://go.microsoft.com/fwlink/?LinkId=521839) (the "Privacy Statement") as it describes the types of 
data we collect from you and your devices ("Data"), how we use your Data and the legal bases we have to
process your Data. The Privacy Statement also describes how Microsoft uses your content, which is your
communications with others; postings submitted by you to Microsoft via the Services; and the files, photos, 
documents, audio, digital works, livestreams and videos that you upload, store, broadcast or share through
the Services ("Your Content"). Where processing is based on consent and to the extent permitted by law, by 
agreeing to these Terms, you consent to Microsoft’s collection, use and disclosure of Your Content and Data 
as described in the Privacy Statement. In some cases, we will provide separate notice and request your consent
as referenced in the Privacy Statement."""
scr.insert(END,long_text)
scr.grid(column=0, columnspan=10)
scr.place(x=0,y=200)

window.mainloop()