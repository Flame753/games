types = ["Fire", "Water", "Wind", "Earth", "Ice", "Darkness", "Light", "Electric", "Poison", "Acid"]


def get_element_damage():
    damage = {}
    for element in types:
        damage[f"{element}_damage"] = 0
    return damage


def get_element_resistance():
    resistance = {}
    for element in types:
        resistance[f"{element}_resistance"] = 0
    return resistance

