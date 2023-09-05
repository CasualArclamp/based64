#a simple program that encodes and decodes base64 using the console

import base64

print("Welcome to the base64 encoder/decoder")

def main(): #main function
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
    encoded = base64.b64encode(string.encode()) #encode the string to bytes
    print("\nEncoded Output:")
    print(encoded.decode())
    print("\n")
    main()

def decode(): #decode function
    string = input("\nEnter the string to decode: ")
    decoded = base64.b64decode(string.encode()) #encode the string to bytes
    print("\nDecoded Output:")
    print(decoded.decode())
    print("\n")
    main()

main() #call the main function
