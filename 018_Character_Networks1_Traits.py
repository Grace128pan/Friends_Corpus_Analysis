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
output_file_path = 'C:\\Users\\grace\\Desktop\\Analysis\\Character_Traits_Evidence.txt'

# Initialize lines for evidence
evidence_lines = []

# Define personal traits keywords for each character
traits_keywords = {
    'Rachel': ['fashion', 'stylish', 'shopping'],
    'Monica': ['clean', 'organized', 'chef'],
    'Phoebe': ['quirky', 'eccentric', 'music'],
    'Ross': ['science', 'paleontology', 'academic'],
    'Chandler': ['sarcasm', 'jokes', 'IT'],
    'Joey': ['acting', 'food', 'women']
}

# Extract lines showing each character's personal traits
for character, path in characters_lines_paths.items():
    with open(path, 'r', encoding='utf-8') as character_lines_file:
        lines = character_lines_file.readlines()

        evidence_lines.append(f"\nEvidence for {character}'s personal traits:")
        for trait, keywords in traits_keywords.items():
            trait_lines = [line.strip() for line in lines if any(re.search(rf'\b{keyword}\b', line, flags=re.IGNORECASE) for keyword in keywords)]
            evidence_lines.extend([f"- {line}" for line in trait_lines[:5]])

# Save the evidence lines to a text file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(evidence_lines))

print(f"Evidence saved to: {output_file_path}")















