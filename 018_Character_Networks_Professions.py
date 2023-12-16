import re
import os

# File paths
full_text_path = 'C:\\Users\\grace\\Desktop\\Analysis\\season1_friends.txt'
characters_lines_paths = {
    'Rachel': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Rachel_lines.txt',
    'Monica': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Monica_lines.txt',
    'Phoebe': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Phoebe_lines.txt',
    'Ross': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Ross_lines.txt',
    'Chandler': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Chandler_lines.txt',
    'Joey': 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Lines\\Joey_lines.txt',
}

# Output file path
output_file_path = 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Professions_Evidence.txt'

# Initialize lines for evidence
evidence_lines = []

# Define profession keywords for each character
profession_keywords = {
    'Rachel': ['fashion', 'buyer', 'sales'],
    'Monica': ['chef', 'restaurant', 'catering'],
    'Phoebe': ['music', 'singer', 'massage'],
    'Ross': ['paleontologist', 'museum', 'academic'],
    'Chandler': ['IT', 'office', 'jokes'],
    'Joey': ['actor', 'audition', 'soap opera']
}

# Extract lines showing each character's professions
for character, path in characters_lines_paths.items():
    with open(path, 'r', encoding='utf-8') as character_lines_file:
        lines = character_lines_file.readlines()

        evidence_lines.append(f"\nEvidence for {character}'s professions:")
        for profession, keywords in profession_keywords.items():
            profession_lines = [line.strip() for line in lines if any(re.search(rf'\b{keyword}\b', line, flags=re.IGNORECASE) for keyword in keywords)]
            evidence_lines.extend([f"- {line}" for line in profession_lines[:5]])

# Save the evidence lines to a text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(evidence_lines))

print(f"Evidence saved to: {output_file_path}")
