import sys

def replace_words_in_gcode(input_file, output_file, replacements):
    with open(input_file, 'r') as file:
        file_contents = file.read()

    # Perform replacements
    for old_word, new_word in replacements.items():
        # Replace old_word with new_word, case-sensitive
        file_contents = file_contents.replace(old_word, new_word)

    # Write the modified contents to the output file
    with open(output_file, 'w') as file:
        file.write(file_contents)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Kullanım: python xy_gcode_par.py <input_file.gcode> <output_file.gcode>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Define the replacements dictionary
    replacements = {
    'G92': ';G92',
    'E': ';E',
    'M107': ';M107',
    'M105': ';M105',
    'M109': ';M109',
    'M82': ';M82',
    'Z0.2': 'Z0.0',
    'Z1.2': 'Z1.0'
    }

    # Call the function to replace words
    replace_words_in_gcode(input_file, output_file, replacements)

    print(f"Kelime değiştirme işlemi tamamlandı. Yeni dosya: {output_file}")
