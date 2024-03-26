from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext


class ChatApplication:
    def __init__(self,root):
        self.root = root
        self.root.title("Chat Application")

        self.chat_display = scrolledtext.ScrolledText(root,width=40,height=15)
        self.chat_display.pack(padx=10,pady=10)

        self.message_entry =tk.Entry(root,width=30,font=("Arial",12))
        self.message_entry.pack(padx=10,pady=5)



        send_button = tk.Button(root,text ="Send",command=self.send_message,width=10,height=5)
        send_button.pack(pady=10)

        send2_button = tk.Button(root,text="Reply",command=self.response,width=10,height=5)
        send2_button.pack(pady=10)
    def send_message(self):
        message= self.message_entry.get()
        if message:
            self.chat_display.insert(tk.END,f"you:{message}\n")
            self.message_entry.delete(0,tk.END)
        else:
            tk.messagebox.showwarning("Warning","please enter  a message.")


    def response (self):

        self.window = tk.Toplevel(self.root)
        self.response_entry = tk.Entry(self.window, width=30, font=("Arial", 12))
        self.response_entry.pack(padx=10, pady=5)

        send3_button = tk.Button(self.window, text="send", command=self.reply_message, width=10, height=5)
        send3_button.pack(pady=10)

    def reply_message(self):
        reply = self.response_entry.get()
        if reply:
            self.chat_display.insert(tk.END, f"them:{reply}\n")
            self.response_entry.delete(0, tk.END)

        else:
            tk.messagebox.showwarning("Warning", "please enter  a message.")


if __name__ == "__main__":

     root =tk.Tk()
     app = ChatApplication(root)

     root.mainloop()