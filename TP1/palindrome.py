"""Palindrome."""

phrase = input('Entrez une phrase > ')
reverse = ''.join(reversed(phrase))

phraseLower = phrase.lower()
reverseLower = reverse.lower()

phraseLower = phraseLower.replace(" ", "")
reverseLower = reverseLower.replace(" ", "")

if phraseLower == reverseLower:
    print(phrase, "est un palindrome.")
else:
    print(phrase, "n'est pas un palindrome.")
