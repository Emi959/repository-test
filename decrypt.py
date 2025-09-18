#imports the clock
from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# Extract the hour as an integer
current_hour = current_time.hour

# defines decrpyt_file used on line 26
def decrypt_file(input_path, output_path="decrypt.txt"):
    try:
        #opens and reads encrypted file
        with open(input_path, "r", encoding="utf-8") as infile:
            encrypted_data = infile.read()

        #defines decrypted as how to decrypt and creates a list
        decrypted = ''.join([chr(int(int(num) / 3 / current_hour)) for num in encrypted_data.split()])

        #creates ne file
        with open(output_path, "w", encoding="utf-8") as outfile:
        #decrypts in new file
            outfile.write(decrypted)
        # prints success message and links to decrypted file
        print(f"Decryption complete. Output written to '{output_path}'.")
    # prints error messagefor illegible decryption
    except ValueError:
        print("Decryption failed: Encrypted data is invalid or malformed.")
    # prints file error message
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
    # prints decryption failiure message
    except Exception as e:
        print("Decryption failed:", e)

# moves text from 'encrypted.txt' to the newly made 'deccrypted.txt' file
if __name__ == "__main__":
    decrypt_file("encrypted.txt")
