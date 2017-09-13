"""Code IBAN."""

IBAN = input('Entrez un code IBAN > ')
IBAN = IBAN.replace(" ", "")
IBAN = IBAN.replace("-", "")

element = IBAN[0] + IBAN[1] + IBAN[2] + IBAN[3]
IBAN = IBAN[4:]
IBAN = IBAN + element

IBAN = IBAN.replace("A", "10")
IBAN = IBAN.replace("B", "11")
IBAN = IBAN.replace("C", "12")
IBAN = IBAN.replace("D", "13")
IBAN = IBAN.replace("E", "14")
IBAN = IBAN.replace("F", "15")
IBAN = IBAN.replace("G", "16")
IBAN = IBAN.replace("H", "17")
IBAN = IBAN.replace("I", "18")
IBAN = IBAN.replace("J", "19")
IBAN = IBAN.replace("K", "20")
IBAN = IBAN.replace("L", "21")
IBAN = IBAN.replace("M", "22")
IBAN = IBAN.replace("N", "23")
IBAN = IBAN.replace("O", "24")
IBAN = IBAN.replace("P", "25")
IBAN = IBAN.replace("Q", "26")
IBAN = IBAN.replace("R", "27")
IBAN = IBAN.replace("S", "28")
IBAN = IBAN.replace("T", "29")
IBAN = IBAN.replace("U", "30")
IBAN = IBAN.replace("V", "31")
IBAN = IBAN.replace("W", "32")
IBAN = IBAN.replace("X", "33")
IBAN = IBAN.replace("Y", "34")
IBAN = IBAN.replace("Z", "35")

IBAN = int(IBAN)

reste = IBAN % 97

if reste == 1:
    print("Le code IBAN est correct")
else:
    print("Le code IBAN est incorrect")
