from abc import ABC, abstractmethod
from random import randint

class character(ABC):
    def __init__(self,name):
        self._lives = 20
        self._name = name

    def __str__(self):
        return f'{self._lives, self._name}'

    @abstractmethod
    def on_elus(self):
        pass

    def võta_kahju(self, damage):
        if isinstance(damage, int):
            self._lives -= damage
        return False

    def runda(self, vastane, damage):
        vastane.võta_kahju(damage)
        print(f'{self._name} ründas {vastane._name} (elus järgi: {vastane._lives})')

class Sõdalane(character):
    def __init__(self, name):
        super().__init__(name)

    def on_elus(self):
        if self._lives > 0:
            return True
        return False

    def create_damage(self):
        """Abifunktsioon random damage jaoks vahemiks 10-20"""
        return randint(10,20)


class Maag(character):
    def __init__(self, name):
        super().__init__(name)
        self._mana = 20

    def on_elus(self):
        if self._lives > 0:
            if self._mana > 0:
                return True
        return False

    def create_damage(self):
        """Abifunktsioon random damage jaoks vahemiks 5-10"""
        return randint(5,10)



class Vibukütt(character):
    def __init__(self, name):
        super().__init__(name)
        self._nooled = 10

    def on_elus(self):
        if self._lives > 0:
            if self._nooled > 0:
                return True
        return False

    def create_damage(self):
        """Abifunktsioon random damage jaoks vahemiks 10-20"""
        return randint(7,14)



def loo_tegelased(indeks):
    name = input(f"Palun sisesta {indeks}. karakteri nimi:")
    tegelane = input(f"Palun sisesta {indeks}. karakteri tüüp (Maag, Sõdalane või Vibukütt):")
    if tegelane.lower() == "maag":
        t1 = Maag(name)
    elif tegelane.lower() == "sõdalane":
        t1 = Sõdalane(name)
    elif tegelane.lower() == "vibukütt":
        t1 = Vibukütt(name)
    else:
        print("Tegemist ei ole valitava karakterina")
        return False
    return t1

def lahing(t1, t2):
    while True:
        print(f"Mängus on {t1._name} (Elusid alles: {t2._lives}) ja {t1._name} (Elusid alles: {t2._lives})")

        keda_rünnata = input(f"{t1._name}, keda soovid rünnata: ")
        damage = t1.create_damage()
        """Vaja lisada listist objekt nime järgi"""
        t1.runda(t2, damage)
        if not t2.on_elus():
            print(f"{t1._name} võitis!")
            return False

        keda_rünnata = input(f"{t2._name}, keda soovid rünnata: ")
        damage = t2.create_damage()
        """Vaja lisada listist objekt nime järgi"""
        t2.runda(t1, damage)
        if not t1.on_elus():
            print(f"{t2._name} võitis!")
            return False

def main():
    tegelased = []
    for i in range(1,3):
        j = loo_tegelased(i)
        tegelased.append(j)

    lahing(tegelased[0], tegelased[1])



if __name__ == '__main__':
    main()