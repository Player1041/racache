import json

# Load the JSON file
with open('25049-Notes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Open a new file to write the formatted output
with open('formatted_notes.txt', 'w', encoding='utf-8') as f_out:
    for idx, entry in enumerate(data):
        address = entry.get("Address", "")
        note = entry.get("Note", "")
        # Preserve literal \n and \r in the string
        note_escaped = note.replace('\\', '\\\\') \
                           .replace('\n', '\\n') \
                           .replace('\r', '\\r') \
                           .replace('"', '\\"')
        f_out.write(f'N0:{address}:"{note_escaped}"\n')

print("Formatted notes written to formatted_notes.txt with literal \\r and \\n preserved")