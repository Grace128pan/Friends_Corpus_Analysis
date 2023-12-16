import os

# File paths
input_file_path = r'C:\Users\grace\Desktop\Analysis\season1_friends.txt'
output_folder_path = r'C:\Users\grace\Desktop\Analysis\Character_Lines'

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)


# Function to extract character lines and save to a new file
def extract_and_save_character_lines(character_name, input_path, output_folder):
    with open(input_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
        character_lines = [line.strip() for line in lines if line.startswith(f'{character_name}:')]

    output_file_path = os.path.join(output_folder, f'{character_name}_lines.txt')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(character_lines))


# List of characters
characters = ['Chandler', 'Ross', 'Joey', 'Phoebe', 'Monica', 'Rachel']

# Extract lines for each character and save to separate files
for character in characters:
    extract_and_save_character_lines(character, input_file_path, output_folder_path)
