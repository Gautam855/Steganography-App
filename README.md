# Steganography Application

Steganography Application is a Python-based tool that allows users to hide secret text messages within image files using steganography techniques. It provides options for encrypting and decrypting messages, as well as saving the manipulated images and text content.

## Features

- **Image Encryption:** Hide secret text messages within image files (.png, .jpg).
- **Text Decryption:** Reveal hidden text messages from encrypted images.
- **Support for Various File Formats:** Supports text files (.txt) and Word documents (.docx) for input and output.
- **User-friendly Interface:** Easy-to-use graphical user interface built with Tkinter.
- **Save Manipulated Data:** Save manipulated images and text content to local storage.
- **Help and About Sections:** Provides user guides and information about the application.


## Prerequisites

  ### Python:
  - Make sure you have python installed on your system. You can download and install it from the [official website](https://www.python.org/downloads/).
  ### IDE (Optional):
  - If you prefer using an Integrated Development Environment (IDE) like VS Code, IDLE, or Jupyter, you can import the project into your IDE and run it from there.


## Installation Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Gautam855/Steganography-App.git
    ```

    Replace `Gautam855` with your actual GitHub username.

2. **Navigate to the Cloned Repository:**

    ```bash
    cd Steganography-App
    ```

3. **Install Python Dependencies:**

    Install the required dependencies using pip:

    ```bash
    pip install Pillow==8.4.0 stegano==0.9.10 python-docx==0.8.11
    ```

4. **Run the Application:**

    ```bash
    python SteganoApp.py
    ```

    Follow the on-screen instructions to encrypt, decrypt, and manipulate images with hidden messages.



## Usage

- **Encrypt Image:** Select an image file and a text message, then click "Encrypt" to hide the message within the image.
- **Decrypt Image:** Choose an encrypted image file and click "Decrypt" to reveal the hidden text message.
- **Browse:** Use the "Browse" button to select image files for encryption or decryption.
- **Save:** After encryption or decryption, use the "Save" option to save the manipulated image or revealed text.
- **Help:** Access the user guide for detailed instructions on using the application.

  

## Contributing

Contributions are welcome! Please feel free to submit bug reports, feature requests, or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- **Gautam Verma** - _Initial work_ - [GitHub](https://github.com/Gautam855)


