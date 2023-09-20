import math

# Custom base64 characters
BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
PADDING_CHAR = "=" # dont forget to add padding characters or else it dont work

def main():
    print("Welcome to the custom base64 encoder/decoder")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")
    choice = input("Enter your choice: ") #get the user's choice
    if choice == "1":
        encode()
    elif choice == "2":
        decode()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        print("\n")
        main()

def encode(): #encode function
    string = input("\nEnter the string to encode: ")
    encoded = custom_base64_encode(string) #encode the string
    print("\nEncoded Output:")
    print(encoded) #print the encoded string
    print("\n")
    main()

def custom_base64_encode(input_string): #encode function
    result = "" # Initialize result string, makes sure its empty
    input_bytes = input_string.encode()
    padding = (3 - len(input_bytes) % 3) % 3  # Calculate padding size

    # Add padding characters to the input bytes
    input_bytes += bytes([0] * padding)

    for i in range(0, len(input_bytes), 3): # Iterate over input bytes
        chunk = int.from_bytes(input_bytes[i:i + 3], byteorder='big') # Convert 3 input bytes into a 24 bit number
        result += BASE64_CHARS[(chunk >> 18) & 63] # Get 1st 6 bits and convert to base64
        result += BASE64_CHARS[(chunk >> 12) & 63] # Get next 6 bits and convert to base64
        result += BASE64_CHARS[(chunk >> 6) & 63]  # Get next 6 bits and convert to base64
        result += BASE64_CHARS[chunk & 63]         # Get last 6 bits and convert to base64

    # Replace the padding characters
    result = result[:-padding] + PADDING_CHAR * padding

    return result # I think you know what this does

def decode():
    string = input("\nEnter the string to decode: ")
    #using try and except to catch errors is way faster than checking if the string is valid
    try: #try to decode the string
        decoded = custom_base64_decode(string) #decode the string
        print("\nDecoded Output:")
        print(decoded)
    except ValueError: #if the string is not valid
        print("Invalid input for decoding.")
    print("\n")
    main()

def custom_base64_decode(encoded_string): #decode function
    # Remove padding characters
    encoded_string = encoded_string.rstrip(PADDING_CHAR)
    input_bytes = bytearray()

    for i in range(0, len(encoded_string), 4): # Iterate over the input string
        chunk = 0
        for j in range(4): # Iterate over each character in the group
            chunk <<= 6
            if i + j < len(encoded_string): # Skip padding characters
                chunk += BASE64_CHARS.index(encoded_string[i + j])
            else: # Replace padding characters with 0
                chunk += 0  # Padding character
        input_bytes.extend(chunk.to_bytes(3, byteorder='big')) # Add decoded chunk to the input bytes

    return input_bytes.decode() # Return the decoded bytes as a string

main()

#Arclamp was here :D 2023