
import tkinter as tk
import hashlib

DEFAULTING_PROGRESS = 1

root = tk.Tk()
root.configure(bg='#EFEEEE')

def killer(*args):
    global root, DEFAULTING_PROGRESS
    if DEFAULTING_PROGRESS < 5:
        DEFAULTING_PROGRESS += 1
        return
    elif DEFAULTING_PROGRESS == 5:
        root.destroy()
        quit()

root.wm_attributes('-fullscreen', True)  # Uncomment for production code.
root.wm_attributes('-topmost', True)     # Makes the widget always stay on top. KEEP COMMENTED UNLESS ABSOLUTELY SURE CODE IS WORKING!!!

letYouKnow = tk.Label(root, text='Sorry Renee, but you cannot get in.', font='Times 30 bold', bg='#EBECF0', foreground='darkred')
letYouKnow.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2) / 2
positionDown = int(root.winfo_screenheight() / 4 - windowHeight / 2) / 2

incorrectNotify = tk.Label(root, text='', font='Times 15 bold', foreground='darkred', bg='#EBECF0')
incorrectNotify.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

enter = tk.Entry(root, show='*', takefocus=True, font='Times 20 bold', relief=tk.SUNKEN, bg='#EBECF0', bd=2, foreground='darkred')
enter.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def check(*args):
    global enter, root
    what = enter.get()
    check = 'd5dc38ed9a841011cc70f4bdc82aae2c71ae154ba25da6d4f274677634553912'
    password = hashlib.sha256(what.encode()).hexdigest()

    if password == check:
        root.destroy()
    else:
        incorrectNotify['text'] = 'Incorrect password.'
        enter.delete(0, 'end')


submit = tk.Button(root, text='Enter', command=check, font='Times 20 bold', bg='#EBECF0', fg='darkred', activebackground='#EBECF0', activeforeground='darkred', relief='raised', bd=3)
submit.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.bind('<Return>', check)
root.mainloop()
#'''
