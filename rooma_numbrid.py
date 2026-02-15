
def validate_number(number : int) -> bool:
    """Valideerime, et tegemist on numbriga ja vahemikus 1-1000"""
    if not isinstance(number, int):
        return False
    if number < 1 or number > 1000:
        return False

    """Return True kui passib kõik checkid"""
    return True

def write_roman(number):
    """Kirjutame välja, kõik võimalikud varjandid 0-9"""

    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    """Saaksime lisada tuhandid ka juurde, aga tagastame, kui on 1000 - ül kirjeldus"""
    if number == 1000:
        return 'M'

    """Leiame arvu jäägid ja jagame vastavalt arvule"""
    sajad = c[(number % 1000)//100]
    kümnesed = x[(number % 100)//10]
    ühesed = i[number % 10]

    return ''.join(sajad + kümnesed + ühesed)


def main():
    starting_number = 888
    """Valideerime numbri"""
    if validate_number(starting_number):

        """Kui valideeritud, siis muudame rooma numbriks"""
        print(write_roman(starting_number))

        """Kui ei valideeri, siis prindime error lause"""
    else:
        print("Tegemist ei ole lubatud arvuga")

if __name__ == '__main__':
    main()