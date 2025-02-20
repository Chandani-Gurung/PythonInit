class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} Menu is available from {self.start_time} to {self.end_time}."

    def calculate_bill(self, purchased_items):
        self.purchased_items = []
        return sum(self.items[item] for item in purchased_items if item in self.items)

# Creating a brunch menu
brunch_items = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}
brunch = Menu("Brunch", brunch_items, 1100, 1600)
print(brunch)
print(brunch.name)
print("Menu:", brunch.items)

# Breakfast Menu order
breakfast_order = ['pancakes', 'home fries', 'coffee']
bill_total = brunch.calculate_bill(breakfast_order)
print(f"Total for breakfast order: ${bill_total:.2f}\n")

# Creating early bird menu
early_bird_items = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00,
}
early_bird = Menu("Early Bird", early_bird_items, 1500, 1800)
print(early_bird)
print(early_bird.name)
print("Menu:", early_bird.items)

# Early bird order
early_bird_order = ['salumeria plate', 'vegan mushroom ravioli']
bill_total = early_bird.calculate_bill(early_bird_order)
print(f"Total for early bird order: ${bill_total:.2f}\n")

# Creating dinner menu
dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00,
}
dinner = Menu("Dinner", dinner_items, 1700, 2300)
print(dinner)
print(dinner.name)
print("Menu:", dinner.items, "\n")

# Creating kids menu
kids_items = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}
kids = Menu("Kids Menu", kids_items, 1100, 2100)
print(kids)
print(kids.name)
print("Menu:", kids.items, "\n")

# Creating the Franchises
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"Franchise is located at {self.address}."

    def available_menu(self, time):
        return [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]

menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store)
print(flagship_store.available_menu(1200))
print(flagship_store.available_menu(1700), "\n")
print(new_installment)
print(new_installment.available_menu(1200))
print(new_installment.available_menu(1700), "\n")

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
print("First Business name is:", basta.name)
print(basta.franchises, "\n")

# Creating new business
arepa_menu_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Arepa", arepa_menu_items, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", arepa_menu_items)
arepas = Business("Take a' Arepa", arepas_place)
print("Second Business name is:", arepas.name)
print(arepas_place)
print(arepas_menu)