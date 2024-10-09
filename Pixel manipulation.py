import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

class ImageEncryptorDecryptor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor/Decryptor")
        

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Key Entry Section
        key_frame = tk.Frame(self.root)
        key_frame.pack(pady=50)

        key_label = tk.Label(key_frame, text="Enter Encryption Key:" , font=("Arial",12))
        key_label.pack()

        self.key_entry = tk.Entry(key_frame, show='' , font=("Arial",12))  # Hide key input
        self.key_entry.pack(pady=5)

        # Encrypt Section
        encrypt_frame = tk.Frame(self.root)
        encrypt_frame.pack(pady=10)

        encrypt_label = tk.Label(encrypt_frame, text="Encrypt Image", font=("Arial",12))
        encrypt_label.pack()

        self.encrypt_button = tk.Button(encrypt_frame, text="Choose Image to Encrypt", font=("Arial",12), command=self.choose_image_to_encrypt)
        self.encrypt_button.pack(pady=5)

        self.encrypted_image_path_label = tk.Label(encrypt_frame, text="", font=("Arial",10))
        self.encrypted_image_path_label.pack()

        self.save_encrypted_button = tk.Button(encrypt_frame, text="Save Encrypted Image", font=("Arial",12), command=self.save_encrypted_image, state=tk.DISABLED)
        self.save_encrypted_button.pack(pady=5)

        # Decrypt Section
        decrypt_frame = tk.Frame(self.root)
        decrypt_frame.pack(pady=10)

        decrypt_label = tk.Label(decrypt_frame, text="Decrypt Image", font=("Arial",12))
        decrypt_label.pack()

        self.decrypt_button = tk.Button(decrypt_frame, text="Choose Image to Decrypt", font=("Arial",12), command=self.choose_image_to_decrypt)
        self.decrypt_button.pack(pady=5)

        self.decrypted_image_path_label = tk.Label(decrypt_frame, text="", font=("Arial",10))
        self.decrypted_image_path_label.pack()

        self.save_decrypted_button = tk.Button(decrypt_frame, text="Save Decrypted Image", font=("Arial",12), command=self.save_decrypted_image, state=tk.DISABLED)
        self.save_decrypted_button.pack(pady=5)

    def choose_image_to_encrypt(self):
        self.input_image_path = filedialog.askopenfilename(title="Select Image to Encrypt",
                                                           filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if self.input_image_path:
            self.encrypted_image_path_label.config(text=self.input_image_path)
            self.save_encrypted_button.config(state=tk.NORMAL)

    def choose_image_to_decrypt(self):
        self.encrypted_image_path = filedialog.askopenfilename(title="Select Encrypted Image to Decrypt",
                                                                filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if self.encrypted_image_path:
            self.decrypted_image_path_label.config(text=self.encrypted_image_path)
            self.save_decrypted_button.config(state=tk.NORMAL)

    def save_encrypted_image(self):
        key = self.key_entry.get().encode('utf-8')  # Get the user-provided key
        if not key:
            messagebox.showerror("Error", "Please enter a valid key.")
            return

        output_image_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                            filetypes=[("PNG files", "*.png")])
        if output_image_path:
            self.encrypt_image(self.input_image_path, output_image_path, key)
            messagebox.showinfo("Success", f"Encrypted image saved as {output_image_path}")

    def save_decrypted_image(self):
        key = self.key_entry.get().encode('utf-8')  # Get the user-provided key
        if not key:
            messagebox.showerror("Error", "Please enter a valid key.")
            return

        output_image_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                            filetypes=[("PNG files", "*.png")])
        if output_image_path:
            self.decrypt_image(self.encrypted_image_path, output_image_path, key)
            messagebox.showinfo("Success", f"Decrypted image saved as {output_image_path}")

    def encrypt_image(self, input_image_path, output_image_path, key):
        image = Image.open(input_image_path)
        image_array = np.array(image)

        key = np.array(list(key), dtype=np.uint8)
        if key.size < image_array.size:
            key = np.resize(key, image_array.shape)

        encrypted_image_array = image_array ^ key
        encrypted_image = Image.fromarray(encrypted_image_array)
        encrypted_image.save(output_image_path)

    def decrypt_image(self, input_image_path, output_image_path, key):
        encrypted_image = Image.open(input_image_path)
        encrypted_image_array = np.array(encrypted_image)

        key = np.array(list(key), dtype=np.uint8)
        if key.size < encrypted_image_array.size:
            key = np.resize(key, encrypted_image_array.shape)

        decrypted_image_array = encrypted_image_array ^ key
        decrypted_image = Image.fromarray(decrypted_image_array)
        decrypted_image.save(output_image_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorDecryptor(root)
    root.mainloop()
