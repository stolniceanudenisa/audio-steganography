import os.path
import wave


class LSB:
    def __init__(self):
        self.audio = None

    def convert_into_byte_array(self, audio_file):
        """Convert an audio into a byte array"""

        # Open the audio file and read it
        self.audio = wave.open(audio_file, "rb")

        # Get the number of audio frames
        number_of_audio_frames = self.audio.getnframes()

        # Read and return a list of audio frames as byte objects
        audio_frames = list(self.audio.readframes(number_of_audio_frames))

        # Create a byte array represents the audio based on the list created above
        audio_in_byte_array = bytearray(audio_frames)

        # Return the audio in byte array
        return audio_in_byte_array

    def encode(self, audio_address, secret_text):
        """Embed a secret text into an audio file"""

        # Convert the audio into a byte array
        audio_byte_array = self.convert_into_byte_array(audio_address)

        # Calculate the number of audio bytes
        number_of_audio_bytes = int(len(audio_byte_array) / 8)

        # Calculate the number of secret text bits
        number_of_secret_text_bits = len(secret_text) * 8

        # Construct the text to be encoded by padding the secret text with "#" so that it has the same size as the audio
        encoding_text = secret_text + int(number_of_audio_bytes - number_of_secret_text_bits) * '#'

        # Create an array to store bytes and an array to store bits
        byte_array = []
        bits = []

        # Convert each character in the encoding text to bytes
        for char in encoding_text:
            # Convert the character to ASCII Value
            char_ascii = ord(char)

            # Convert the character in ASCII to binary value
            binary_char_ascii = bin(char_ascii).lstrip('0b')

            # Left padding the binary value of the character with 0s to make a complete byte
            binary_char_ascii_in_byte = binary_char_ascii.rjust(8, '0')

            # Store the byte character in the byte array
            byte_array.append(binary_char_ascii_in_byte)

        # Construct the whole encoding text in bytes
        encoding_text_in_bytes = ''.join(byte_array)

        # Store each bit of the encoding text in the bit array
        for bit in encoding_text_in_bytes:
            bits.append(int(bit))

        # Applying Least Significant Bit method
        for i in range(len(bits)):
            # Replacing the last bits (the Least Significant Bits) of the audio byte array by the bits of the secret text
            audio_byte_array[i] = (audio_byte_array[i] & 254) | bits[i]

        # Convert the audio byte array into the encoded audio
        encoded_audio = bytes(audio_byte_array)

        # Save the encoded audio in the same directory as the original carrier audio
        return self.save_encoded_audio(encoded_audio, audio_address)

    def save_encoded_audio(self, encoded_audio, address):
        """Save a stego audio file to a location"""

        # Get the directory of the audio
        addr = os.path.dirname(address)

        # Get the file name of the audio
        ori_file_name = os.path.basename(address).rstrip('.wav')

        # Set the address for the encoded audio
        new_audio_file_address = addr + '/' + ori_file_name + '-stego-lsb.wav'

        # Create a new audio file which is the encoded audio file with the name specified above
        new_audio_file = wave.open(new_audio_file_address, 'wb')

        # Set parameters for the new audio file
        new_audio_file.setparams(self.audio.getparams())

        # Write audio frames for the new audio file
        new_audio_file.writeframes(encoded_audio)

        # Close the new audio file and return its location
        new_audio_file.close()
        self.audio.close()
        return new_audio_file_address

    def decode(self, audio_address):
        """Decode a stego audio file to get the secret message"""

        # Convert the audio into a byte array
        audio_byte_array = self.convert_into_byte_array(audio_address)

        # Create a list to store bits of the secret text
        bits = []
        for byte in audio_byte_array:
            bits.append(byte & 1)
        self.audio.close()

        # Store the letters of the secret text in a list
        secret_letters = []
        for i in range(0, len(bits), 8):

            # Take every 8 bits and convert them to string data type
            letter_in_bits = map(str, bits[i:i + 8])

            # Group them together to make a byte
            letter_in_byte = ''.join(letter_in_bits)

            # Convert the byte from binary to decimal value to get the ascii value of the letter
            letter_in_ascii = int(letter_in_byte, 2)

            # Convert the ascii value of the letter to the actual letter
            real_letter = chr(letter_in_ascii)

            # Store the letter inside the list created above
            secret_letters.append(real_letter)

        # Group the letters together to construct a whole text
        padded_secret_text = ''.join(secret_letters)

        # Provide the original secret text by getting rid of the part that contains "###" which we used to pad the secret text
        original_secret_text = padded_secret_text.split('###')[0]

        # Return the original secret text
        return original_secret_text
