from abc import ABC, abstractmethod
from random import randint

"""

Kirjutasin teadlikult igale alamklassile eraldi funktsiooni on_elus abstractklassina

Nii saan ühe funktsiooniga iga klassi puhul kontrollida nii elude kui ka noolte/mana arvu
MÄNGU SAAB MÄNGIDA KUNI LÕPMATU ARV MÄNGIJATEGA - lihtsalt tüütu

"""


class character(ABC):
    def __init__(self, name):
        self._lives = 30
        self._name = name

    def __repr__(self):
        return f'{self._name}-l on alles {self._lives} elu'

    @abstractmethod
    def on_elus(self):
        """ABSTRACTMETHOD — kontrollib elusid JA ressursse (mana/nooled)"""
        pass

    def võta_kahju(self, damage):
        """KAPSELDAMINE"""
        if isinstance(damage, int):
            self._lives -= damage
        return False

    def runda(self, vastane, damage):
        vastane.võta_kahju(damage)
        print(f'{vastane._name}-t ründas {self._name} ja võttis {damage} elu! ({vastane.__repr__()})\n')


class Sõdalane(character):

    def __init__(self, name):
        """Pärilus"""
        super().__init__(name)

    def on_elus(self):
        return self._lives > 0

    def create_damage(self):
        """Polümorfism"""
        return randint(4, 15)


class Maag(character):

    def __init__(self, name):
        """Pärilus"""
        super().__init__(name)
        self._mana = 30

    def on_elus(self):
        return self._lives > 0 and self._mana > 0

    def create_damage(self):
        """Polümorfism"""
        protsent = randint(1, 5)
        self.eemalda_mana(protsent)
        return 10 if protsent == 5 else 1

    def eemalda_mana(self, number):
        self._mana -= number

    def __repr__(self):
        return super().__repr__() + f' ja {self._mana} mana!'


class Vibukütt(character):

    def __init__(self, name):
        """Pärilus"""
        super().__init__(name)
        self._nooled = 20

    def on_elus(self):
        return self._lives > 0 and self._nooled > 0

    def create_damage(self):
        """Polümorfism"""
        protsent = randint(1, 2)
        self.eemalda_nooled()
        return 6 if protsent == 2 else 1

    def eemalda_nooled(self):
        self._nooled -= 3

    def __repr__(self):
        return super().__repr__() + f' ja {self._nooled} noolt!'


def loo_tegelased(indeks):
    indeks += 1
    while True:
        name = input(f"Palun sisesta {indeks}. karakteri nimi: ")
        tegelane = input(f"Palun sisesta {indeks}. karakteri tüüp (Maag, Sõdalane või Vibukütt): ")
        if tegelane.lower() == "maag":
            return Maag(name)
        elif tegelane.lower() == "sõdalane":
            return Sõdalane(name)
        elif tegelane.lower() == "vibukütt":
            return Vibukütt(name)
        else:
            print("Tegemist ei ole valitava karakteriga!")


def lahing(mängijad: list):
    print("\nAlgab lahing: ...\n")
    print("Algseis:", ' | '.join(str(t) for t in mängijad))

    kord = 1
    while True:
        print(f"\nKÄIK {kord}")

        for ründaja in mängijad:
            if not ründaja.on_elus():
                continue

            # Vaenlased = elus (ainult elud, mitte ressursid)
            elus_vaenlased = [t for t in mängijad if t != ründaja and t.on_elus()]
            if not elus_vaenlased:
                print(f"{ründaja._name} võitis!")
                return

            print(f"Elus vaenlased: {[t._name for t in elus_vaenlased]}")
            keda_rünnata = input(f"{ründaja._name} | {ründaja._lives}, keda soovid rünnata: ")

            sihtmärk = next((t for t in elus_vaenlased if t._name == keda_rünnata), None)
            if sihtmärk is None:
                print("Sellist vaenlast pole! Käik vahele jäetud.")
                continue

            damage = ründaja.create_damage()
            ründaja.runda(sihtmärk, damage)

            if not sihtmärk.on_elus():
                print(f"{sihtmärk._name} on langenud!")

            if not ründaja.on_elus():
                print(f"{ründaja._name} on langenud! (ressursid said otsa)")

        # Mängus on ainult eluga tegelased
        elus = [t for t in mängijad if t.on_elus()]
        if len(elus) == 1:
            print(f"\n{elus[0]._name} võitis lahingu!")
            return False

        kord += 1


if __name__ == '__main__':
    mängijad = []
    mängijate_arv = input("Mitu mängijat mängib? ")
    for i in range(int(mängijate_arv)):
        mängijad.append(loo_tegelased(i))

    if len(mängijad) > 1:
        lahing(mängijad)
    else:
        print("Üksi on ju igav mängida :(")
        exit()
