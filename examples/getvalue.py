import jsonc

# Load the JSONC file
with open("examples/list_r.jsonc", 'r') as file:
    data = jsonc.load(file)

# Update the value associated with the key ".char[0]" to "gg"
data['char'][0] = 'gg'

# Save the updated data back to the file
with open('examples/list.jsonc', 'w') as file:
    jsonc.dump(data, file, indent=2)
