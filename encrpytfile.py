#imports the clock
from datetime import datetime

# Get the current time
current_time = datetime.now()

# Extract the hour as an integer
current_hour = current_time.hour

#defines the encrypt_file used on line 25
def encrypt_file(input_path, output_path):
    try:
        #opens file
        with open(input_path, "r", encoding="utf-8") as infile:
            content = infile.read()

        #defines how it's encrypted
        encrypted = ' '.join([str(ord(char) * 3 * current_hour) for char in content])
        #creates new file
        with open(output_path, "w", encoding="utf-8") as outfile:
            #encrypts created file
            outfile.write(encrypted)
        #prints success response and send link to encrypted file
        print(f"Encryption complete. Encrypted output written to '{output_path}'.")
    # prints error message for files
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    # prints error message for encryption
    except Exception as e:
        print("Encryption failed:", e)

# moves text from 'input.txt' to the newly made 'encrypted.txt' file
if __name__ == "__main__":
    encrypt_file("input.txt", "encrypted.txt")
