def extract_lines(char1, char2, full_text_path, output_path):
    with open(full_text_path, 'r', encoding='utf-8') as full_text_file:
        lines = full_text_file.readlines()

    relevant_lines = []

    for line in lines:
        if char1 in line and char2 in line:
            relevant_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(relevant_lines)

if __name__ == "__main__":
    full_text_path = 'C:\\Users\\grace\\Desktop\\Analysis\\season1_friends.txt'
    characters_lines_paths = {
        'Rachel': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt',
        'Monica': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt',
        'Phoebe': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt',
        'Ross': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt',
        'Chandler': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt',
        'Joey': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt',
    }

    # Define character pairs and their respective output paths
    character_pairs = [('Ross', 'Rachel'), ('Ross', 'Monica'), ('Ross', 'Phoebe'),
                       ('Ross', 'Chandler'), ('Ross', 'Joey')]

    # Extract and save lines for each character pair
    for char1, char2 in character_pairs:
        output_path = f'C:\\Users\\grace\\Desktop\\Analysis\\{char1}_and_{char2}_lines.txt'
        extract_lines(char1, char2, full_text_path, output_path)
        print(f"Lines between {char1} and {char2} saved to {output_path}")





