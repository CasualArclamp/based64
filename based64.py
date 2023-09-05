#a simple program that encodes and decodes base64 using the console

import base64

def main(): #main function
    print("Welcome to the base64 encoder/decoder")
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
        main()

def encode(): #encode function
    string = input("Enter the string to encode: ")
    encoded = base64.b64encode(string.encode()) #encode the string to bytes
    print(encoded.decode())
    main()

def decode(): #decode function
    string = input("Enter the string to decode: ")
    decoded = base64.b64decode(string.encode()) #encode the string to bytes
    print(decoded.decode())
    main()

main() #call the main function