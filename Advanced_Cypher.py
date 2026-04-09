import base64

def encode(message):
    encoded_bytes = base64.b64encode(message.encode())
    return encoded_bytes.decode()

def decode(encoded_message):
    decoded_bytes = base64.b64decode(encoded_message.encode())
    return decoded_bytes.decode()

def main():
    while True:
        user_input = input("Enter a message to encode or decode (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the program. Goodbye!")
            break

        choice = input("Choose an option (encode/decode): ").lower()
        if choice == "encode":
            encoded_result = encode(user_input)
            print("Encoded:", encoded_result)
        elif choice == "decode":
            decoded_result = decode(user_input)
            print("Decoded:", decoded_result)
        else:
            print("Invalid choice. Please choose 'encode', 'decode', or 'exit'.")

if __name__ == "__main__":
    main()
