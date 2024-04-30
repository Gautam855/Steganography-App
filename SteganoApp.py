import tkinter as tk
from tkinter import filedialog, messagebox, Menu, PhotoImage, Label
from PIL import Image, ImageTk
from stegano import lsb
import os
import customtkinter
from docx import Document



def read_text_file(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            text_content = file.read()
        return text_content
    except UnicodeDecodeError as e:
        messagebox.showerror("Error", f"Error decoding text file: {str(e)}")
        return None

def read_docx_file(filename):
    try:
        doc = Document(filename)
        text_content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        return text_content
    except Exception as e:
        messagebox.showerror("Error", f"Error reading docx file: {str(e)}")
        return None

def showimage():
    global filename, img, text6, lbl_frame1

    try:
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                              filetype=(("PNG file", "*.png"), ("JPG file", "*.jpg"),
                                                        ("Text file", "*.txt"), ("Docs file", "*.docx"), ("All file", "*.*")))

        if filename.lower().endswith(('.png', '.jpg')):
            # If it's an image file
            img = Image.open(filename)
            img = ImageTk.PhotoImage(img)

            # Check if lbl_frame1 exists and destroy it if it does
            if lbl_frame1:
                lbl_frame1.destroy()

            lbl_frame1 = tk.Label(f, image=img, width=400, height=270)
            lbl_frame1.pack()

            directory_label_text = f"{os.path.dirname(filename)}/{os.path.basename(filename)}"
            text6.delete(1.0, tk.END)
            text6.insert(tk.INSERT, directory_label_text)
        else:
            raise ValueError("Invalid file type. Please select a valid image, text, or docx file.")
    except Exception as e:
        messagebox.showerror("Error", f"Error loading file: {str(e)}")

def showtext():
    global fi, text5, text1

    try:
        fi = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                        filetype=(("Text file", "*.txt"), ("Docs file", "*.docx"), ("All file", "*.*")))

        if fi.lower().endswith('.txt'):
            # If it's a text file
            text_content = read_text_file(fi)
            if text_content is not None:
                text1.delete(1.0, tk.END)
                text1.insert(tk.INSERT, text_content)
            directory_label_text = f"{os.path.dirname(fi)}/{os.path.basename(fi)}"
            #text5.delete(1.0, tk.END)
            text5.insert(tk.INSERT, directory_label_text)
        elif fi.lower().endswith('.docx'):
            # If it's a docx file
            text_content = read_docx_file(fi)
            if text_content is not None:
                text1.delete(1.0, tk.END)
                text1.insert(tk.INSERT, text_content)
            directory_label_text = f"{os.path.dirname(fi)}/{os.path.basename(fi)}"
            text5.delete(1.0, tk.END)
            text5.insert(tk.INSERT, directory_label_text)
        else:
            raise ValueError("Invalid file type. Please select a valid image, text, or docx file.")
    except Exception as e:
        messagebox.showerror("Error", f"Error loading file: {str(e)}")

# ... (Rest of your code)



def show_help():
    messagebox.showinfo("Help",
                        "Steganography Application Help\n\n"
                        "1. Open an image file using the 'Browse' button.\n"
                        "2. Enter your secret message in the provided text box.\n"
                        "3. Click 'Hide Data' to hide the message in the image.\n"
                        "4. To reveal the hidden message, click 'Show Data'.\n"
                        "5. You can also save the manipulated image or text content using the 'Save' options.\n\n"
                        "Note: Make sure to save your data before exiting the application.")


def Hide():
    global filename, secret, text1

    # Get the message from the text widget
    message = text1.get(1.0, "end-1c").strip()

    # Check if the message is not empty
    try:
        if message and filename:
            secret = lsb.hide(filename, message)
            messagebox.showinfo("Hide Success", "Data Hide successfully.")
        else:
        # Show an error message or handle the case where the message is empty
            messagebox.showerror("Error", "Please enter a non-empty message to hide.")
    except:
        messagebox.showerror("Error", "Message is too long please reduce length of message.")
    

def Show():
    try:
        global filename
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, tk.END)
        text1.insert(tk.INSERT, clear_message)
    except Exception as e:
        messagebox.showerror("Error", "There is no hidden data")

def save_text_to_file():
    global text1

    # Get the content from the text widget
    text_content = text1.get(1.0, tk.END)

    # Prompt the user for the file path to save the text
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    # Check if the user canceled the save dialog
    if not save_path:
        return

    try:
        # Open the file in write mode and save the text content
        with open(save_path, 'w') as file:
            file.write(text_content)

        # Optionally, show a success message
        messagebox.showinfo("Save Success", "Text content saved successfully.")
    except Exception as e:
        # Show an error message if there is an issue saving the file
        messagebox.showerror("Error", f"Error saving text content: {str(e)}")




def save():
    global secret

    if secret:
        # Prompt the user for the directory and file name to save
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

        # Check if the user canceled the save dialog
        if not save_path:
            return

        # Save the photo to the specified path
        secret.save(save_path)
        messagebox.showinfo("Save Success", "Image saved successfully.")

def on_exit():
    global secret

    if secret:
        # Prompt the user before exiting if the image is not saved
        response = messagebox.askyesno("Exit Confirmation", "Do you want to exit without saving the image?")
        if response:
            root.destroy()

    else:
        root.destroy()

def main():
    global f, text1, text6, text5

    f = tk.Frame(root, bd=3, bg="black", width=400, height=280, relief=tk.GROOVE)
    f.place(x=10, y=80)


    # Second Frame
    frame2 = tk.Frame(root, bd=3, width=520, height=260, bg="white", relief=tk.GROOVE)
    frame2.place(x=470, y=80)

    text1 = customtkinter.CTkTextbox(frame2, width=400, height=270)

    # Configure the font size directly on the widget using 'configure'
    text1.configure(font=("Helvetica", 20))
    text1.pack()

    text6 = tk.Text(root, bd=3, height=1,width=36, bg="white", relief=tk.GROOVE)
    text6.place(x=10, y=365)

    text5 = tk.Text(root, bd=3, height=1,width=36, bg="white", relief=tk.GROOVE)
    text5.place(x=480, y=365)

    # Bind the on_exit function to the window closing event
    root.protocol("WM_DELETE_WINDOW", on_exit)

def encrypt():
    main()

    btn_browse = customtkinter.CTkButton(master=root,
                                         fg_color=("lightgrey"),  # <- tuple color for light and dark theme
                                         text="Browse", width=100,
                                         height=25, text_color="black",
                                         command=showimage)
    btn_browse.place(x=310, y=365)



    btn_browse_txt = customtkinter.CTkButton(master=root,
                                         fg_color=("lightgrey"),bg_color=("lightblue"),  # <- tuple color for light and dark theme
                                         text="Browse", width=100,
                                         height=25, text_color="black",
                                         command=showtext)
    btn_browse_txt.place(x=780, y=365)



    

    btn_save_image = customtkinter.CTkButton(master=root,
                                             fg_color=("lightgrey"),  # <- tuple color for light and dark theme
                                             text="Save Image", width=120,
                                             height=35, text_color="black",
                                             command=save)
    btn_save_image.place(x=330, y=450)

    btn_hide_image = customtkinter.CTkButton(master=root,
                                             fg_color=("lightgrey"),  # <- tuple color for light and dark theme
                                             text="Hide Data", width=120,
                                             height=35, text_color="black",
                                             command=Hide)
    btn_hide_image.place(x=480, y=450)

    btn_browse.mainloop()

def decrypt():
    main()
    
    # Check if btn_browse is not None before trying to place_forget

    btn_save_image = customtkinter.CTkButton(master=root,
                                             fg_color=("black", "lightgrey"),
                                             text="Save in txt", width=120,
                                             height=35, text_color="black",
                                             command=save_text_to_file)
    btn_save_image.place(x=330, y=450)

    btn_show_data = customtkinter.CTkButton(master=root,
                                            fg_color=("black", "White"),
                                            text="Show Data", width=120,
                                            height=35, text_color="black",
                                            command=Show)
    btn_show_data.place(x=480, y=450)


if __name__ == "__main__":

    filename = None
    img = None
    secret = None
    f = None
    fi = None
    text1 = None
    text6 = None
    text5 = None
    new_root = None
    lbl_frame1 = None
    btn_browse_txt=None
    root = tk.Tk()
    root.title("Steganography - Hide a Secret Text Message in an Image")
    root.geometry("900x600+150+100")
    root.resizable(False, False)

    bg = PhotoImage(file="qq.png")
    bg = bg.subsample(int(bg.width() / 850), int(bg.height() / 600))

    canvas1 = tk.Canvas(root, width=900, height=600)
    canvas1.pack(fill="both", expand=False)
    canvas1.create_image(0, 0, image=bg, anchor="nw")

    menubar = Menu(root, background='blue', fg='white')

    # Declare file and edit for showing in menubar
    Encrypt = Menu( tearoff=False, background='White')
    Decrypt = Menu( tearoff=False, background='White')
    About = Menu( tearoff=False, background='White')
    Help = Menu( tearoff=False, background='White')
    Exit = Menu( tearoff=False, background='White')

    # Add commands in in file menu
    Exit.add_command(label="Exit", command=on_exit)
    Encrypt.add_command(label="Encrypt", command=encrypt)
    Decrypt.add_command(label="Decrypt", command=decrypt)
    About.add_command(label="About", command=lambda: messagebox.showinfo("About",
                 "Steganography - Hide a Secret Text Message in an Image\n"
                 "Version 1.0\n\n"
                 "This application allows you to hide a secret text message within an image using steganography. "
                 "It provides options for encrypting and decrypting messages, as well as saving the manipulated images and text content.\n\n"
                 "Developed by G.N.D Group"))
    Help.add_command(label="User Guide", command=show_help)

# Add the 'Help' menu to the menubar



    # Add commands in edit menu

    # Display the file and edit declared in previous step
    menubar.add_cascade(label="Encrypt", menu=Encrypt)
    menubar.add_cascade(label="Decrypt", menu=Decrypt)
    menubar.add_cascade(label="About", menu=About)
    menubar.add_cascade(label="Help", menu=Help)
    menubar.add_cascade(label="Exit", menu=Exit)

    # Displaying of menubar in the app
    root.config(menu=menubar)
    encrypt()

    root.mainloop()
