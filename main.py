from PIL import Image
import numpy as np

def encode_message(image_path, message, output_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Add a delimiter to the end of the message
    message += '%%%'

    # Convert the message to binary
    binary_message = ''.join([format(ord(c), '08b') for c in message])

    # Check if the message is too long for the image
    if len(binary_message) > img_array.size * 3:
        raise ValueError("Message is too long for this image")

    # Put the message in the least significant bits
    data_index = 0
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3): # For each RGB channel (ignore alpha if present)
                if data_index < len(binary_message):
                    # Replace LSB with message bit
                    img_array[i][j][k] = img_array[i][j][k] & ~1 | int(binary_message[data_index])
                    data_index += 1

    # Save the edited image
    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_path)
    print(f"Message successfully hidden in {output_path}")

def decode_message(image_path):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    binary_message = ''
    message = ''

    # Extract the least significant bits
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3): # For each RGB channel
                binary_message += str(img_array[i][j][k] & 1)

    # Check if we found the delimiter
            if len(binary_message) >= 8 and len(binary_message) % 8 == 0:
                byte = binary_message[-8:]
                char = chr(int(byte, 2))
                if message.endswith('%%%'):
                    return message[:-3]
                message += char

    return message

# Usage example
if __name__ == "__main__":
    # Encode a message
    encode_message("original.png", "This is a secret message!", "modified_image.png")

    # Decode the message
    secret_message = decode_message("modified_image.png")
    print("Extracted message:", secret_message)