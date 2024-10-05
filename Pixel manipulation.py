from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Load the image
    image = Image.open(input_image_path)
    # Convert image to a numpy array
    image_array = np.array(image)

    # Ensure the key is large enough
    key = np.array(list(key), dtype=np.uint8)
    key_length = key.size
    if key_length < image_array.size:
        # Repeat the key as necessary
        key = np.resize(key, image_array.shape)

    # Encrypt the image using XOR operation
    encrypted_image_array = image_array ^ key
    # Convert back to an image
    encrypted_image = Image.fromarray(encrypted_image_array)
    # Save the encrypted image
    encrypted_image.save(output_image_path)
    print(f"Encrypted image saved as {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Load the encrypted image
    encrypted_image = Image.open(input_image_path)
    # Convert image to a numpy array
    encrypted_image_array = np.array(encrypted_image)

    # Ensure the key is large enough
    key = np.array(list(key), dtype=np.uint8)
    key_length = key.size
    if key_length < encrypted_image_array.size:
        # Repeat the key as necessary
        key = np.resize(key, encrypted_image_array.shape)

    # Decrypt the image using XOR operation
    decrypted_image_array = encrypted_image_array ^ key
    # Convert back to an image
    decrypted_image = Image.fromarray(decrypted_image_array)
    # Save the decrypted image
    decrypted_image.save(output_image_path)
    print(f"Decrypted image saved as {output_image_path}")

# Example usage
if __name__ == "__main__":
    key = b'secret'  # This key can be any byte string
    encrypt_image('input_image.png', 'encrypted_image.png', key)
    decrypt_image('encrypted_image.png', 'decrypted_image.png', key)
