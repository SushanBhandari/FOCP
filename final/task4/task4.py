def decrypt(encrypted_text, key):
  # Shift each character in the text by the key value
  decrypted_text = ""
  for c in encrypted_text:
    decrypted_text += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
  return decrypted_text

def is_english(text):
  # Check if the text contains mostly English letters and spaces
  letters = 0
  spaces = 0
  for c in text:
    if c.isalpha():
      letters += 1
    elif c.isspace():
      spaces += 1
  return letters > spaces

# Read the encrypted message from the file
filename = "message.txt"
try:
  with open(filename) as f:
    encrypted_text = f.read()
except FileNotFoundError:
  print(f"Cannot open {filename!r}. Sorry about that.")
  exit(1)

# Try all possible key values and print the first decrypted message that makes sense
for key in range(26):
  decrypted_text = decrypt(encrypted_text, key)
  if is_english(decrypted_text):
    print(decrypted_text)
    break
else:
  print("Cannot decrypt. Most likely not a Caesar Cypher at work here.")