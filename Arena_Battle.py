import random



# TEIL 1: DIE HELDEN (KLASSEN)


class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power

# __init__ ist der Konstruktor der Klasse.
# Es wird automatisch aufgerufen, wenn ein neues Objekt (z.B. ein Held) erstellt wird,
# um dessen Anfangswerte (Name, Lebenspunkte, Angriffskraft) festzulegen.
    def is_alive(self):
        return self.hp > 0


class Slayer(Hero):
    def __init__(self, name):
        super().__init__(name, hp=60, attack_power=18)

    # 'super()' stellt die Verbindung zur Elternklasse (Hero) her.
    # Damit rufen wir die __init__-Methode von 'Hero' auf, um die
    # Basiseigenschaften (wie den Namen) dort zentral zu verarbeiten.
    def special_move(self):
        damage = self.attack_power + random.randint(15, 25)
        self.hp -= self.max_hp*0.075
        return damage, "Deathblow (Hoher Schaden, kostet 5 HP)"


class Ironbreaker(Hero):
    def __init__(self, name):
        super().__init__(name, hp=90, attack_power=10)

    def special_move(self):
        damage = self.attack_power + 5
        self.hp += 10
        if self.hp > self.max_hp: self.hp = self.max_hp
        return damage, "Gromril Rüstung (Heilt +10 HP)"


class BrightWizard(Hero):
    def __init__(self, name):
        super().__init__(name, hp=40, attack_power=8)
        self.winds_of_magic = 60

    def special_move(self):
        if self.winds_of_magic >= 20:
            self.winds_of_magic -= 20
            damage = self.attack_power + random.randint(30, 45)
            return damage, "Aqshy's Feuerwind!"
        return 0, "Verpufft (Nicht genug Winde der Magie)"


class Engineer(Hero):
    #Der Engineer: Kann einen Turm rufen, der jede Runde automatisch feuert.

    def __init__(self, name):
        super().__init__(name, hp=70, attack_power=12)
        self.turret_rounds = 0

    def special_move(self):
        self.turret_rounds = 3
        return 0, "Geschützturm aufgebaut! (Feuert 3 Runden lang)"

    def turret_fire(self):
        if self.turret_rounds > 0:
            self.turret_rounds -= 1
            return 10  # Schaden pro Turm-Schuss
        return 0


def level_up(hero):
    hero.max_hp += 10
    hero.hp = hero.max_hp
    hero.attack_power += 4
    if hasattr(hero, 'winds_of_magic'):
        hero.winds_of_magic += 30
    print(f"\n[LEVEL UP] {hero.name} wird stärker! HP: {hero.max_hp}, ATK: {hero.attack_power}")



# TEIL 2: DIE MONSTER-DATENBANK (VOLLSTÄNDIG)


# GRUPPE EINFACH
def erstelle_goblin(): return {"Name": "Goblin", "HP": random.randint(20, 35), "Schaden": random.randint(0, 5),
                               "EP": random.randint(10, 20)}


def erstelle_zombie(): return {"Name": "Zombie", "HP": random.randint(30, 40), "Schaden": random.randint(0, 3),
                               "EP": random.randint(10, 20)}


def erstelle_Kaefer(): return {"Name": "Kaefer", "HP": random.randint(15, 25), "Schaden": random.randint(3, 10),
                               "EP": random.randint(10, 20)}


def erstelle_Teufelchen(): return {"Name": "Teufelchen", "HP": random.randint(20, 30), "Schaden": random.randint(2, 5),
                                   "EP": random.randint(10, 20)}


def erstelle_Schlaeger(): return {"Name": "Schlaeger", "HP": random.randint(35, 40), "Schaden": random.randint(4, 6),
                                  "EP": random.randint(10, 20)}


def erstelle_Steingolem(): return {"Name": "Steingolem", "HP": random.randint(40, 45), "Schaden": random.randint(0, 10),
                                   "EP": random.randint(10, 20)}


def erstelle_Riesenkroete(): return {"Name": "Riesenkroete", "HP": random.randint(20, 35),
                                     "Schaden": random.randint(2, 5), "EP": random.randint(10, 20)}


def erstelle_Varan(): return {"Name": "Varan", "HP": random.randint(30, 35), "Schaden": random.randint(4, 8),
                              "EP": random.randint(10, 20)}


# GRUPPE MITTEL
def erstelle_Ork(): return {"Name": "Ork", "HP": random.randint(50, 70), "Schaden": random.randint(10, 15),
                            "EP": random.randint(30, 50)}


def erstelle_Skelett(): return {"Name": "Skelett", "HP": random.randint(40, 65), "Schaden": random.randint(10, 13),
                                "EP": random.randint(30, 50)}


def erstelle_Wolf(): return {"Name": "Wolf", "HP": random.randint(40, 55), "Schaden": random.randint(5, 20),
                             "EP": random.randint(30, 50)}


def erstelle_Daemon(): return {"Name": "Daemon", "HP": random.randint(60, 70), "Schaden": random.randint(10, 15),
                               "EP": random.randint(30, 50)}


def erstelle_Bandit(): return {"Name": "Bandit", "HP": random.randint(50, 60), "Schaden": random.randint(10, 13),
                               "EP": random.randint(30, 50)}


def erstelle_Eisengolem(): return {"Name": "Eisengolem", "HP": random.randint(65, 70), "Schaden": random.randint(8, 12),
                                   "EP": random.randint(30, 50)}


def erstelle_Giftfrosch(): return {"Name": "Giftfrosch", "HP": random.randint(45, 60), "Schaden": random.randint(6, 13),
                                   "EP": random.randint(30, 50)}


def erstelle_Krokodil(): return {"Name": "Krokodil", "HP": random.randint(60, 70), "Schaden": random.randint(12, 14),
                                 "EP": random.randint(30, 50)}


# GRUPPE SCHWER
def erstelle_Oger(): return {"Name": "Oger", "HP": random.randint(75, 85), "Schaden": random.randint(15, 25),
                             "EP": random.randint(100, 120)}


def erstelle_Fleischkonstrukt(): return {"Name": "Fleischkonstrukt", "HP": random.randint(80, 85),
                                         "Schaden": random.randint(10, 20), "EP": random.randint(100, 120)}


def erstelle_Baer(): return {"Name": "Baer", "HP": random.randint(60, 80), "Schaden": random.randint(16, 25),
                             "EP": random.randint(100, 120)}


def erstelle_Erzdaemon(): return {"Name": "Erzdaemon", "HP": random.randint(60, 75), "Schaden": random.randint(17, 25),
                                  "EP": random.randint(100, 120)}


def erstelle_Assassine(): return {"Name": "Assassine", "HP": random.randint(65, 75), "Schaden": random.randint(15, 25),
                                  "EP": random.randint(100, 120)}


def erstelle_Diamantgolem(): return {"Name": "Diamantgolem", "HP": random.randint(85, 95),
                                     "Schaden": random.randint(13, 18), "EP": random.randint(100, 120)}


def erstelle_Teufelskroete(): return {"Name": "Teufelskroete", "HP": random.randint(70, 85),
                                      "Schaden": random.randint(15, 20), "EP": random.randint(100, 120)}


def erstelle_Raptor(): return {"Name": "Raptor", "HP": random.randint(65, 80), "Schaden": random.randint(17, 21),
                               "EP": random.randint(100, 120)}


# Listen befüllen
einfach = [erstelle_goblin, erstelle_zombie, erstelle_Kaefer, erstelle_Teufelchen, erstelle_Schlaeger,
           erstelle_Steingolem, erstelle_Riesenkroete, erstelle_Varan]
mittel = [erstelle_Ork, erstelle_Skelett, erstelle_Wolf, erstelle_Daemon, erstelle_Bandit, erstelle_Eisengolem,
          erstelle_Giftfrosch, erstelle_Krokodil]
schwer = [erstelle_Oger, erstelle_Fleischkonstrukt, erstelle_Baer, erstelle_Erzdaemon, erstelle_Assassine,
          erstelle_Diamantgolem, erstelle_Teufelskroete, erstelle_Raptor]



# TEIL 3: KAMPFLOGIK & SPIELABLAUF


#Ermittelt den Namen des ersten Monsters und die Anzahl aller Monster in der Welle,
# um eine passende Ankündigung für den Kampf auszugeben.

def kampf_gegen_welle(spieler, welle):
    monster_art = welle[0]['Name']
    print(f"\n>>> Eine Gruppe von {len(welle)} {monster_art}en greift an! <<<")

    while len(welle) > 0 and spieler.is_alive():
        # --- 1. TURRET SCHUSS (Engineer) ---
        if hasattr(spieler, 'turret_fire'):
            t_dmg = spieler.turret_fire()
            if t_dmg > 0 and len(welle) > 0:
                welle[0]['HP'] -= t_dmg
                print(f"[TURRET] Das Geschütz feuert! {t_dmg} Schaden an {welle[0]['Name']}.")
                if welle[0]['HP'] <= 0:
                    print(f"  {welle[0]['Name']} durch Turm zerstört!")
                    welle.pop(0)

        if len(welle) == 0: break

        # --- 2. SPIELER AKTION ---
        print(f"\n[{spieler.name}: {spieler.hp}/{spieler.max_hp} HP] vs [{len(welle)}x {monster_art}]")
        wahl = input("Aktion: (1) Angriff (2) Spezialfähigkeit: ")

        # Schaden berechnen
        if wahl == "2":
            dmg, info = spieler.special_move()
            print(f"-> {info} für {dmg} Schaden.")
        else:
            dmg = spieler.attack_power + random.randint(-2, 5)
            print(f"-> Normaler Angriff: {dmg} Schaden.")

        # Schaden auf das erste Monster anwenden
        if len(welle) > 0:
            welle[0]['HP'] -= dmg
            if welle[0]['HP'] <= 0:
                print(f"--- {welle[0]['Name']} wurde besiegt! ---")
                welle.pop(0)

        # --- 3. ALLE ÜBERLEBENDEN MONSTER GREIFEN AN ---
        if len(welle) > 0:
            gesamt_schaden = 0
            for monster in welle:
                schaden_wurf = random.randint(0, monster['Schaden'])
                gesamt_schaden += schaden_wurf

            spieler.hp -= gesamt_schaden
            print(f"< Die {len(welle)} {monster_art}(en) verursachen insgesamt {gesamt_schaden} Schaden!")

    if spieler.is_alive():
        level_up(spieler)
        return True
    return False


def main():
    print("--- WARHAMMER BATTLE SIMULATOR ---")
    print("Heldenwahl: (1) Slayer (2) Ironbreaker (3) Bright Wizard (4) Engineer")
    c_wahl = input("Deine Wahl: ")
    name = input("Name deines Helden: ")

    if c_wahl == "1":
        spieler = Slayer(name)
    elif c_wahl == "2":
        spieler = Ironbreaker(name)
    elif c_wahl == "3":
        spieler = BrightWizard(name)
    else:
        spieler = Engineer(name)

    # Rundenaufbau: Eine Art pro Runde via pop()
    # Wir nehmen einen Bauplan und erstellen daraus X Monster
    # --- RUNDEN-GENERIERUNG ---

    # 1. Auswahl des Bauplans:
    # 'pop()' nimmt eine Monster-Funktion (z.B. erstelle_goblin) zufällig aus der Liste.
    # Der Vorteil von pop: Dieses Monster wird aus der Liste gelöscht und kann in
    # dieser Spielsession nicht noch einmal als 'Bauplan' für eine andere Runde gewählt werden.
    plan1 = einfach.pop(random.randint(0, len(einfach) - 1))
    r1 = [plan1() for _ in range(3)]

    plan2 = einfach.pop(random.randint(0, len(einfach) - 1))
    r2 = [plan2() for _ in range(4)]

    plan3 = mittel.pop(random.randint(0, len(mittel) - 1))
    r3 = [plan3() for _ in range(2)]

    plan4 = schwer.pop(random.randint(0, len(schwer) - 1))
    r4 = [plan4() for _ in range(1)]


# 2. Erstellung der Monster-Liste:
# Die ausgewählte Funktion (plan1) wird nun x-mal aufgerufen, um echte Monster-Objekte
# (Dictionaries mit HP, Schaden etc.) zu erzeugen.
# 'range(3)' bedeutet: In Runde 1 treten 3 Monster desselben Typs an.
    wellen = [r1, r2, r3, r4]

# "enumerate" nummeriert die Elemente einer Liste automatisch durch,
# sodass man gleichzeitig die Position (Index) und den Inhalt erhält.
    for i, welle in enumerate(wellen, 1):
        if not kampf_gegen_welle(spieler, welle):
            print(f"\n{spieler.name} ist glorreich im Kampf gefallen.")
            break
    else:
        print(f"\nSIEG! {spieler.name} hat das Schlachtfeld gesäubert!")


if __name__ == "__main__":
    main()

