# from tkinter import *
# from tkinter import filedialog
# from tkinter import messagebox
# from algorithms.LSB import LSB
# from algorithms.PhaseCoding import PhaseCoding

# root = Tk()
# root.geometry("1440x1024")
# root.title("Audio Steganography")

# global encode_screen
# global encode_window


# def encode():
#     root.withdraw()
#     global encode_screen
#     global encode_window
#     encode_window = Toplevel()
#     encode_screen = Encode_screen(encode_window)
#     encode_window.protocol("WM_DELETE_WINDOW", lambda: exit_to_main(encode_window))
#     encode_window.mainloop()


# def exit_to_main(screen):
#     confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=screen)
#     if confirm:
#         screen.destroy()
#         root.deiconify()


# global decode_screen
# global decode_window


# def decode():
#     root.withdraw()
#     global decode_screen
#     global decode_window
#     decode_window = Toplevel()
#     decode_screen = Decode_screen(decode_window)
#     decode_window.protocol("WM_DELETE_WINDOW", lambda: exit_to_main(decode_window))
#     decode_window.mainloop()


# def exit_program():
#     confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
#     if confirm:
#         root.destroy()
#         exit()


# root.protocol("WM_DELETE_WINDOW", exit_program)


# class Main_screen:
#     def __init__(self, parent=None):
#         self.parent = parent
#         self.parent.geometry("1440x1024")
#         self.parent.resizable(0, 0)
#         self.parent.title("Audio Steganography")

#         self.background_image = Label(root)
#         self.background_image.place(relx=0, rely=0, width=1440, height=1024)
#         self.main_screen_image = PhotoImage(file="images/main.png")
#         self.background_image.configure(image=self.main_screen_image)

#         self.encode_button = Button(root, relief="flat", overrelief="flat", cursor="hand2", text="Encode",
#                                     font="Roboto 35 bold", bg="#ffffff", fg="#575757", borderwidth="0",
#                                     activebackground="#ffffff", activeforeground="#575757", command=encode)
#         self.encode_button.place(relx=0.19, rely=0.6, width=297, height=100)

#         self.decode_button = Button(root, relief="flat", overrelief="flat", cursor="hand2", text="Decode",
#                                     font="Roboto 35 bold", bg="#ffffff", fg="#575757", borderwidth="0",
#                                     activebackground="#ffffff", activeforeground="#575757", command=decode)
#         self.decode_button.place(relx=0.602, rely=0.6, width=297, height=100)


# class Encode_screen:
#     def __init__(self, parent=None):
#         self.parent = parent
#         self.parent.geometry("1440x1024")
#         self.parent.resizable(0, 0)
#         self.parent.title("Encode")

#         self.background_image = Label(encode_window)
#         self.background_image.place(relx=0, rely=0, width=1440, height=1024)
#         self.encode_screen_image = PhotoImage(file="images/encode.png")
#         self.background_image.configure(image=self.encode_screen_image)

#         self.file_var = StringVar()
#         self.file_entry = Entry(encode_window, textvariable=self.file_var, relief="flat", font="Roboto 20",
#                                 bg="#ffffff", fg="#575757")
#         self.file_entry.place(relx=0.078, rely=0.3, width=990, height=32)

#         self.algo_option_list = [23 * " " + "Least Significant Bit" + 23 * " ", 27 * " " + "Phase Coding" + 31 * " "]
#         self.algo_option_var = StringVar()
#         self.algo_option_var.set("Least Significant Bit")
#         self.algo_options = OptionMenu(encode_window, self.algo_option_var, *self.algo_option_list)
#         self.algo_options.config(font=('Roboto', 30), bg='#ffffff', fg='#575757', width=40, height=1,
#                                  activeforeground='#575757', borderwidth='1')
#         self.algo_options['menu'].config(font=('Roboto', 30), bg='#ffffff', fg='#575757')
#         self.algo_options.place(relx=0.078, rely=0.47)

#         self.secret_text = Text(encode_window, font=('Roboto', 20), width=62, height=7, bg='#ffffff', fg='#575757',
#                                 wrap=WORD, relief='flat')
#         self.secret_text.place(relx=0.098, rely=0.67)

#         self.browse_button = Button(encode_window, relief="flat", overrelief="flat", cursor="hand2", text="Browse",
#                                     font="Roboto 26", bg="#3DBBF1", fg="#ffffff", borderwidth="0",
#                                     activebackground="#3DBBF1", activeforeground="#ffffff", command=self.browse)
#         self.browse_button.place(x=1170, y=284, width=159, height=54)

#         self.encode_button = Button(encode_window, relief="flat", overrelief="flat", cursor="hand2", text="Encode",
#                                     font="Roboto 26", bg="#3DBBF1", fg="#ffffff", borderwidth="0",
#                                     activebackground="#3DBBF1", activeforeground="#ffffff", command=self.encode)
#         self.encode_button.place(x=1170, y=786, width=159, height=54)

#         self.file_name = ""

#     def browse(self):
#         self.file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
#                                                     filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3"),
#                                                                ("all files", "*.*")))
#         self.file_var.set(self.file_name)

#     def encode(self):
#         algorithm = self.algo_option_var.get().strip()
#         if algorithm == "Least Significant Bit":
#             algo = LSB()
#         else:
#             algo = PhaseCoding()
#         encoded_file_address = algo.encode(self.file_name, self.secret_text.get("1.0", END))
#         messagebox.showinfo("Success!", "Successfully encoded! \n\nEncoded file was saved to " + encoded_file_address)
#         self.exit_encode_screen()

#     def exit_encode_screen(self):
#         self.parent.destroy()
#         root.deiconify()


# class Decode_screen:
#     def __init__(self, parent=None):
#         self.parent = parent
#         self.parent.geometry("1440x1024")
#         self.parent.resizable(0, 0)
#         self.parent.title("Encode")

#         self.background_image = Label(decode_window)
#         self.background_image.place(relx=0, rely=0, width=1440, height=1024)
#         self.decode_screen_image = PhotoImage(file="images/decode.png")
#         self.background_image.configure(image=self.decode_screen_image)

#         self.file_var = StringVar()
#         self.file_entry = Entry(decode_window, textvariable=self.file_var, relief="flat", font="Roboto 20",
#                                 bg="#ffffff", fg="#575757")
#         self.file_entry.place(relx=0.078, rely=0.3, width=990, height=32)

#         self.algo_option_list = [23 * " " + "Least Significant Bit" + 23 * " ", 27 * " " + "Phase Coding" + 31 * " "]
#         self.algo_option_var = StringVar()
#         self.algo_option_var.set("Least Significant Bit")
#         self.algo_options = OptionMenu(decode_window, self.algo_option_var, *self.algo_option_list)
#         self.algo_options.config(font=('Roboto', 30), bg='#ffffff', fg='#575757', width=40, height=1,
#                                  activeforeground='#575757', borderwidth='1')
#         self.algo_options['menu'].config(font=('Roboto', 30), bg='#ffffff', fg='#575757')
#         self.algo_options.place(relx=0.078, rely=0.47)

#         self.secret_text = Text(decode_window, font=('Roboto', 20), width=62, height=7, bg='#ffffff', fg='#575757',
#                                 wrap=WORD, relief='flat')
#         self.secret_text.place(relx=0.098, rely=0.67)

#         self.browse_button = Button(decode_window, relief="flat", overrelief="flat", cursor="hand2", text="Browse",
#                                     font="Roboto 26", bg="#3DBBF1", fg="#ffffff", borderwidth="0",
#                                     activebackground="#3DBBF1", activeforeground="#ffffff", command=self.browse)
#         self.browse_button.place(x=1170, y=284, width=159, height=54)

#         self.decode_button = Button(decode_window, relief="flat", overrelief="flat", cursor="hand2", text="Decode",
#                                     font="Roboto 26", bg="#3DBBF1", fg="#ffffff", borderwidth="0",
#                                     activebackground="#3DBBF1", activeforeground="#ffffff", command=self.decode)
#         self.decode_button.place(x=1170, y=786, width=159, height=54)

#         self.file_name = ""

#     def browse(self):
#         self.file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
#                                                     filetypes=(("wav files", "*.wav"), ("all files", "*.*")))
#         self.file_var.set(self.file_name)

#     def decode(self):
#         algorithm = self.algo_option_var.get().strip()
#         if algorithm == "Least Significant Bit":
#             algo = LSB()
#         else:
#             algo = PhaseCoding()
#         secret_text = algo.decode(self.file_name)
#         self.secret_text.delete("1.0", END)
#         self.secret_text.insert("1.0", secret_text)


# if __name__ == '__main__':
#     main_screen = Main_screen(root)
#     root.mainloop()


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from algorithms.LSB import LSB
from algorithms.PhaseCoding import PhaseCoding

root = Tk()
root.geometry("900x600")
root.title("Audio Steganography")

global encode_screen
global encode_window


def encode():
    root.withdraw()
    global encode_screen
    global encode_window
    encode_window = Toplevel()
    encode_screen = Encode_screen(encode_window)
    encode_window.protocol("WM_DELETE_WINDOW", lambda: exit_to_main(encode_window))
    encode_window.mainloop()


def exit_to_main(screen):
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=screen)
    if confirm:
        screen.destroy()
        root.deiconify()


global decode_screen
global decode_window


def decode():
    root.withdraw()
    global decode_screen
    global decode_window
    decode_window = Toplevel()
    decode_screen = Decode_screen(decode_window)
    decode_window.protocol("WM_DELETE_WINDOW", lambda: exit_to_main(decode_window))
    decode_window.mainloop()


def exit_program():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=root)
    if confirm:
        root.destroy()
        exit()


root.protocol("WM_DELETE_WINDOW", exit_program)


class Main_screen:
    def __init__(self, parent=None):
        self.parent = parent
        self.parent.geometry("900x600")
        self.parent.resizable(0, 0)
        self.parent.title("Audio Steganography")

        self.background_image = Label(root)
        self.background_image.place(relx=0, rely=0, width=900, height=600)
        self.main_screen_image = PhotoImage(file="images/main.png")
        self.background_image.configure(image=self.main_screen_image)

        self.encode_button = Button(root, relief="flat", overrelief="flat", cursor="hand2", text="Encode",
                                    font="Roboto 35 bold", bg="#ffffff", fg="#575757", borderwidth="0",
                                    activebackground="#ffffff", activeforeground="#575757", command=encode)
        self.encode_button.place(relx=0.19, rely=0.6, width=297, height=100)

        self.decode_button = Button(root, relief="flat", overrelief="flat", cursor="hand2", text="Decode",
                                    font="Roboto 35 bold", bg="#ffffff", fg="#575757", borderwidth="0",
                                    activebackground="#ffffff", activeforeground="#575757", command=decode)
        self.decode_button.place(relx=0.602, rely=0.6, width=297, height=100)


class Encode_screen:
    def __init__(self, parent=None):
        self.parent = parent
        self.parent.geometry("900x600")
        self.parent.resizable(0, 0)
        self.parent.title("Encode")

        self.background_image = Label(encode_window)
        self.background_image.place(relx=0, rely=0, width=900, height=600)
        self.encode_screen_image = PhotoImage(file="images/encode.png")
        self.background_image.configure(image=self.encode_screen_image)

        self.file_var = StringVar()
        self.file_entry = Entry(encode_window, textvariable=self.file_var, relief="flat", font="Roboto 20",
                                bg="#ffffff", fg="#575757")
        self.file_entry.place(relx=0.078, rely=0.3, width=600, height=32)

        self.algo_option_list = [23 * " " + "Least Significant Bit" + 23 * " ", 27 * " " + "Phase Coding" + 31 * " "]
        self.algo_option_var = StringVar()
        self.algo_option_var.set("Least Significant Bit")
        self.algo_options = OptionMenu(encode_window, self.algo_option_var, *self.algo_option_list)
        self.algo_options.config(font=('Roboto', 20), bg='#ffffff', fg='#575757', width=30, height=1,
                                 activeforeground='#575757', borderwidth='1')
        self.algo_options['menu'].config(font=('Roboto', 20), bg='#ffffff', fg='#575757')
        self.algo_options.place(relx=0.078, rely=0.47)

        self.secret_text = Text(encode_window, font=('Roboto', 16), width=50, height=5, bg='#ffffff', fg='#575757',
                                wrap=WORD, relief='flat')
        self.secret_text.place(relx=0.098, rely=0.67)

        self.browse_button = Button(encode_window, relief="flat", overrelief="flat", cursor="hand2", text="Browse",
                                    font="Roboto 20", bg="#3DBBF1", fg="#ffffff", borderwidth="0",
                                    activebackground="#3DBBF1", activeforeground="#ffffff", command=self.browse)
        self.browse_button.place(x=720, y=175, width=130, height=45)

        self.encode_button = Button(encode_window, relief="flat", overrelief="flat", cursor="hand2", text="Encode",
                                    font="Roboto 20", bg="#3DBBF1", fg="#ffffff", borderwidth="0",
                                    activebackground="#3DBBF1", activeforeground="#ffffff", command=self.encode)
        self.encode_button.place(x=720, y=480, width=130, height=45)

        self.file_name = ""

    def browse(self):
        self.file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3"),
                                                               ("all files", "*.*")))
        self.file_var.set(self.file_name)

    def encode(self):
        algorithm = self.algo_option_var.get().strip()
        if algorithm == "Least Significant Bit":
            algo = LSB()
        else:
            algo = PhaseCoding()
        encoded_file_address = algo.encode(self.file_name, self.secret_text.get("1.0", END))
        messagebox.showinfo("Success!", "Successfully encoded! \n\nEncoded file was saved to " + encoded_file_address)
        self.exit_encode_screen()

    def exit_encode_screen(self):
        self.parent.destroy()
        root.deiconify()


class Decode_screen:
    def __init__(self, parent=None):
        self.parent = parent
        self.parent.geometry("900x600")
        self.parent.resizable(0, 0)
        self.parent.title("Encode")

        self.background_image = Label(decode_window)
        self.background_image.place(relx=0, rely=0, width=900, height=600)
        self.decode_screen_image = PhotoImage(file="images/decode.png")
        self.background_image.configure(image=self.decode_screen_image)

        self.file_var = StringVar()
        self.file_entry = Entry(decode_window, textvariable=self.file_var, relief="flat", font="Roboto 20",
                                bg="#ffffff", fg="#575757")
        self.file_entry.place(relx=0.078, rely=0.3, width=600, height=32)

        self.algo_option_list = [23 * " " + "Least Significant Bit" + 23 * " ", 27 * " " + "Phase Coding" + 31 * " "]
        self.algo_option_var = StringVar()
        self.algo_option_var.set("Least Significant Bit")
        self.algo_options = OptionMenu(decode_window, self.algo_option_var, *self.algo_option_list)
        self.algo_options.config(font=('Roboto', 20), bg='#ffffff', fg='#575757', width=30, height=1,
                                 activeforeground='#575757', borderwidth='1')
        self.algo_options['menu'].config(font=('Roboto', 20), bg='#ffffff', fg='#575757')
        self.algo_options.place(relx=0.078, rely=0.47)

        self.secret_text = Text(decode_window, font=('Roboto', 16), width=50, height=5, bg='#ffffff', fg='#575757',
                                wrap=WORD, relief='flat')
        self.secret_text.place(relx=0.098, rely=0.67)

        self.browse_button = Button(decode_window, relief="flat", overrelief="flat", cursor="hand2", text="Browse",
                                    font="Roboto 20", bg="#3DBBF1", fg="#ffffff", borderwidth="0",
                                    activebackground="#3DBBF1", activeforeground="#ffffff", command=self.browse)
        self.browse_button.place(x=720, y=175, width=130, height=45)

        self.decode_button = Button(decode_window, relief="flat", overrelief="flat", cursor="hand2", text="Decode",
                                    font="Roboto 20", bg="#3DBBF1", fg="#ffffff", borderwidth="0",
                                    activebackground="#3DBBF1", activeforeground="#ffffff", command=self.decode)
        self.decode_button.place(x=720, y=480, width=130, height=45)

        self.file_name = ""

    def browse(self):
        self.file_name = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                    filetypes=(("wav files", "*.wav"), ("all files", "*.*")))
        self.file_var.set(self.file_name)

    def decode(self):
        algorithm = self.algo_option_var.get().strip()
        if algorithm == "Least Significant Bit":
            algo = LSB()
        else:
            algo = PhaseCoding()
        secret_text = algo.decode(self.file_name)
        self.secret_text.delete("1.0", END)
        self.secret_text.insert("1.0", secret_text)


if __name__ == '__main__':
    main_screen = Main_screen(root)
    root.mainloop()
