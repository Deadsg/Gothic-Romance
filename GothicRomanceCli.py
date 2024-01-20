import random

class Player:
    def __init__(self, name, race, level=1, attack=10, defense=10, experience=0, max_health=100, max_attack=10, max_defense=10, inventory=None, health=100):
        self.name = name
        self.health = 100
        self.gold = 100
        self.race = race
        self.attack = attack
        self.defense = defense
        self.current_city = "Bloodhaven"  # Starting city
        self.inventory = inventory if inventory is not None else {}
        self.level = level
        self.experience = experience
        self.max_health = max_health
        self.max_attack = max_attack
        self.max_defense = max_defense
        self.health = self.max_health
        self.health=health

    def complete_quest(self, quest):
        print(f"Congratulations! You completed the quest: {quest['name']} - {quest['description']}")
        quest_experience = quest.get('experience', 0)
        quest_gold = quest.get('gold', 0)

        # Gain experience and gold for completing the quest
        self.gain_experience(quest_experience)
        self.gold += quest_gold

        print(f"You gained {quest_experience} experience and {quest_gold} gold!")

    def gain_experience(self, experience_points):
        self.experience += experience_points
        print(f"You gained {experience_points} experience points!")

        # Level up if enough experience is earned
        while self.experience >= self.calculate_experience_required():
            self.level_up()

        if self.experience >= self.level * 100:
            self.level_up()

    def calculate_experience_required(self):
        # You can customize the experience curve based on your game's design
        return 50 * self.level

    def level_up(self):
        print(f"Congratulations! You leveled up to level {self.level + 1}!")

        # Increase player stats on level up
        self.level += 1
        self.max_health += 10
        self.max_attack += 2
        self.max_defense += 2
        self.health = self.max_health  # Heal to full health on level up

        print(f"New Stats - Health: {self.max_health}, Attack: {self.max_attack}, Defense: {self.max_defense}")

    def take_damage(self, damage):
        # Subtract damage from health, ensuring it doesn't go below 0
        self.health = max(self.health - damage, 0)
        print(f"You took {damage} damage. Current Health: {self.health}")

    def heal(self, healing_points):
        # Heal the player, ensuring health doesn't exceed the maximum
        self.health = min(self.health + healing_points, self.max_health)
        print(f"You healed for {healing_points} points. Current Health: {self.health}")

    def view_stats(self):
        print(f"Level: {self.level}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.max_attack}")
        print(f"Defense: {self.max_defense}")
        print(f"Experience: {self.experience}/{self.calculate_experience_required()}")

    def get_race(self):
        return self.race

    def use_health_potion(self):
        self.health += 30
        if self.health > 100:
            self.health = 100

    def use_silver_dagger(self, enemy):
        damage = max(20 - enemy.defense, 0)
        enemy.health -= damage

    def use_iron_shield(self):
        self.defense += 10

    def view_inventory(self):
        print("Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

class Vampire(Player):
    def __init__(self, name, attack=10, defense=10, inventory=None):
        super().__init__(name, "Vampire", attack, defense, inventory)
        self.blood_points = 100

    def bite(self, target):
        if self.blood_points >= 10:
            self.blood_points -= 10
            target.health -= 20
            return f"{self.name} bites {target.name} and drains their blood!"
        else:
            return "Not enough blood points to bite."

    def use_vampire_blood_elixir(self):
        if self.blood_points < 100:
            self.blood_points += 30
            print(f"{self.name} used a Vampire Blood Elixir and gained 30 blood points.")
        else:
            print("Your blood points are already at maximum.")

class Human(Player):
    def __init__(self, name, attack=10, defense=10, inventory=None):
        super().__init__(name, "Human", attack, defense, inventory)
        self.arrows = 5

    def shoot_arrow(self, target):
        if self.arrows > 0:
            self.arrows -= 1
            target.health -= 15
            return f"{self.name} shoots an arrow at {target.name}!"
        else:
            return "Out of arrows."

class Merchant:
    def __init__(self):
        self.items_for_sale = {
            "Health Potion": 20,
            "Silver Dagger": 30,
            "Iron Shield": 50,
            "Vampire Blood Elixir": 100,
        }

    def display_items_for_sale(self):
        print("Items for Sale:")
        for item, cost in self.items_for_sale.items():
            print(f"{item}: {cost} gold")

    def sell_item(self, player, item_name):
        if item_name in self.items_for_sale:
            cost = self.items_for_sale[item_name]
            if player.gold >= cost:
                player.gold -= cost
                player.add_to_inventory(item_name)
                print(f"You bought {item_name} for {cost} gold.")
            else:
                print("Not enough gold to purchase.")
        else:
            print("Invalid item.")

class NPC:
    def __init__(self, name, race, dialog):
        self.name = name
        self.race = race
        self.dialog = dialog

    def talk(self):
        print(f"{self.name}: {self.dialog}")

class VampireNPC(NPC):
    def __init__(self, name, dialog):
        super().__init__(name, "Vampire", dialog)

class HumanNPC(NPC):
    def __init__(self, name, dialog):
        super().__init__(name, "Human", dialog)

def talk_to_npc():
    print("You engage in a conversation with a mysterious figure...")
    print("NPC: Welcome to our cursed town. Beware of the creatures that roam the night.")

def explore_command(player, merchant, npc):
    print(f"You decide to explore the surroundings of {player.current_city}.")

    # Implement a chance of finding gold
    found_gold = random.choice([True, False])
    if found_gold:
        gold_found = random.randint(5, 15)
        player.gold += gold_found
        print(f"You found {gold_found} gold!")

    # Implement a chance of encountering an enemy
    encounter_enemy = random.choice([True, False])
    if encounter_enemy:
        enemy = get_random_enemy()
        print(f"You encountered a {enemy['name']} while exploring!")

        while player.health > 0 and enemy.health > 0:
            player_damage, enemy_damage = battle_round(player, enemy)
            print_battle_status(player, enemy, player_damage, enemy_damage)

            if enemy.health <= 0:
                player.gold += random.randint(10, 20)
                print(f"You defeated the {enemy['name']} and gained {player.gold} gold!")
                break

            enemy_attack_damage = random.randint(8, 12)
            player.health -= enemy_attack_damage

            if player.health <= 0:
                print(f"You were defeated by the {enemy['name']}! Game over.")
                break

    # Print updated player stats
    print(f"Health: {player.health}\nGold: {player.gold}")

def quest_options(quests):
    print("Available Quests:")
    for idx, quest in enumerate(quests, start=1):
        print(f"{idx}. {quest['name']} - {quest['description']}")

def undertake_quest(player, quests):
    quest_options(quests)
    selected_quest_idx = input("Enter the quest number you want to undertake (or 'back' to choose another town): ")

    if selected_quest_idx.lower() == 'back':
        return None

    try:
        selected_quest_idx = int(selected_quest_idx) - 1
        if 0 <= selected_quest_idx < len(quests):
            selected_quest = quests[selected_quest_idx]
            print(f"You have accepted the quest: {selected_quest['name']} - {selected_quest['description']}")
            return selected_quest
        else:
            print("Invalid quest index.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid quest index.")
        return None

def get_random_enemy():
    enemy_data = random.choice(enemies)
    enemy_race = random.choice(["Vampire", "Human"])
    return Player(name=enemy_data['name'], race=enemy_race, attack=enemy_data['attack'], defense=enemy_data.get('defense', 0), health=enemy_data['health'])

def simulate_quest(player, quest):
    if quest is None:
        return

    enemy = get_random_enemy()
    print(f"You encountered a {enemy.get('name')} while on your quest!")

    while player.health > 0 and enemy.get('health') > 0:
        # Player's turn to attack
        player_damage, enemy_damage = battle_round(player, enemy)
        print_battle_status(player, enemy, player_damage, enemy_damage)

        # Check if enemy is defeated
        if enemy.get('health') <= 0:
            player.gold += random.randint(10, 20)
            print(f"You defeated the {enemy.get('name')} and gained {player.gold} gold!")
            player.complete_quest(quest)
            break

        # Enemy's turn to attack
        enemy_attack_damage = random.randint(8, 12)
        player.health -= enemy_attack_damage

        # Check if player is defeated
        if player.health <= 0:
            print(f"You were defeated by the {enemy.get('name')}! Quest failed.")
            break

    print(f"Health: {player.health}\nGold: {player.gold}")

    while player.health > 0 and enemy['health'] > 0:
        # Player's turn to attack
        player_damage, enemy_damage = battle_round(player, enemy)
        print_battle_status(player, enemy, player_damage, enemy_damage)

        # Check if enemy is defeated
        if enemy['health'] <= 0:
            player.gold += random.randint(10, 20)
            print(f"You defeated the {enemy['name']} and gained {player.gold} gold!")
            player.complete_quest(quest)
            break

        # Enemy's turn to attack
        enemy_attack_damage = random.randint(8, 12)
        player.health -= enemy_attack_damage

        # Check if player is defeated
        if player.health <= 0:
            print(f"You were defeated by the {enemy['name']}! Quest failed.")
            break

    print(f"Health: {player.health}\nGold: {player.gold}")

def get_random_enemy():
    enemy_data = random.choice(enemies)
    return Player(name=enemy_data['name'], attack=enemy_data['attack'], defense=enemy_data.get('defense', 0), health=enemy_data['health'])

def battle_round(player, enemy):
    # Player attacks enemy
    player_damage = calculate_damage(player, enemy)
    enemy.health -= player_damage

    # Enemy counterattacks
    enemy_damage = calculate_damage(enemy, player)
    player.health -= enemy_damage

    return player_damage, enemy_damage

def calculate_damage(attacker, defender):
    if hasattr(defender, 'defense'):
        damage = max(attacker.attack - defender.defense, 0)
    else:
        print("'defense' attribute not found in defender!")
        damage = attacker.attack
    return damage

def print_battle_status(player, enemy, player_damage, enemy_damage):
    print(f"Player health: {player.health}, Enemy health: {enemy.health}")
    print(f"Player dealt {player_damage} damage, Enemy dealt {enemy_damage} damage")

def town_options():
    print("Available Towns:")
    for town_name in towns:
        print(f"- {town_name}")

def quest_options(quests):
    print("Available Quests:")
    for idx, quest in enumerate(quests, start=1):
        print(f"{idx}. {quest['name']} - {quest['description']}")

def merchant_interaction(player, merchant):
    print("Welcome to the Gothic Market!")
    merchant.display_items_for_sale()

    while True:
        action = input("Do you want to buy something? (yes/no): ").lower()
        if action == 'yes':
            item_name = input("Enter the name of the item you want to buy: ")
            merchant.sell_item(player, item_name)
        elif action == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Define towns and quests
towns = ["Bloodhaven", "Shadowmere", "Ravenhollow", "Ebonkeep", "Crimsonkeep", "Darkshire"]
bloodhaven_npcs = [
    VampireNPC("Vladimir", "Beware, traveler. The night is dark and full of terrors."),
    VampireNPC("Isabella", "Welcome to Bloodhaven, where shadows whisper secrets."),
]

shadowmere_npcs = [
    VampireNPC("Countess Carmilla", "Greetings, mortal. Seek not what is hidden in the shadows."),
    HumanNPC("Sir Roland", "The dark cultists must be eradicated. Their presence taints Shadowmere."),
]

ravenhollow_npcs = [
    VampireNPC("Lilith", "The phantom beast is a guardian of these lands. Approach with caution."),
    HumanNPC("Eleanor", "The lost grimoire holds the key to ancient powers."),
]

town_npcs = {
    "Bloodhaven": bloodhaven_npcs,
    "Shadowmere": shadowmere_npcs,
    "Ravenhollow": ravenhollow_npcs,
    # ... (add NPCs for other towns)
}

def interact_with_npcs(player):
    current_town_npcs = town_npcs.get(player.current_city, [])
    if not current_town_npcs:
        print("No NPCs to interact with in this town.")
        return

    print("Available NPCs:")
    for npc in current_town_npcs:
        print(f"- {npc.name}")

    npc_name = input("Enter the name of the NPC you want to talk to (or 'back' to return): ")
    if npc_name.lower() == 'back':
        return

    selected_npc = next((npc for npc in current_town_npcs if npc.name.lower() == npc_name.lower()), None)
    if selected_npc:
        selected_npc.talk()
    else:
        print("Invalid NPC name. Please try again.")

city_quests = {
    "Bloodhaven": [
        {"name": "Learn the Dark Arts", "description": "Visit the local necromancer and learn the dark arts of combat."},
        {"name": "Harvest Nightshade", "description": "Collect the rare Nightshade herb in the haunted forest."},
    ],
    "Shadowmere": [
        {"name": "Defeat Dark Cultists", "description": "Clear out the dark cultists near Shadowmere."},
        {"name": "Deliver Cursed Artifacts", "description": "Deliver cursed artifacts to a mysterious figure in the shadows."},
    ],
    "Ravenhollow": [
        {"name": "Slay the Phantom Beast", "description": "Hunt down a phantom beast that haunts Raven's Hollow."},
        {"name": "Find the Lost Grimoire", "description": "Search for a lost grimoire in the haunted catacombs."},
    ],
    "Ebonkeep": [
        {"name": "Rescue the Sorceress", "description": "Rescue the sorceress captured by a group of dark knights."},
        {"name": "Investigate Eerie Whispers", "description": "Explore reports of eerie whispers in Ebon Keep."},
    ],
    "Crimsonkeep": [
        {"name": "Purge the Unholy Creatures", "description": "Eliminate unholy creatures infesting the town's crypt."},
        {"name": "Retrieve Blood Relics", "description": "Recover stolen blood relics from a band of vampires."},
    ],
    "Darkshire": [
        {"name": "Exorcise Malevolent Spirits", "description": "Help the town exorcise malevolent spirits haunting Darkshire."},
        {"name": "Seek Dark Alchemist's Advice", "description": "Consult with a renowned dark alchemist for advice."},
    ],
}

bloodhaven_npcs = [
    VampireNPC("Vladimir", "Beware, traveler. The night is dark and full of terrors."),
    VampireNPC("Isabella", "Welcome to Bloodhaven, where shadows whisper secrets."),
]

shadowmere_npcs = [
    VampireNPC("Countess Carmilla", "Greetings, mortal. Seek not what is hidden in the shadows."),
    HumanNPC("Sir Roland", "The dark cultists must be eradicated. Their presence taints Shadowmere."),
]

ravenhollow_npcs = [
    VampireNPC("Lilith", "The phantom beast is a guardian of these lands. Approach with caution."),
    HumanNPC("Eleanor", "The lost grimoire holds the key to ancient powers."),
]

player_inventory = {
    "Gold": 100,
    "Health Potion": 3,
    "Silver Dagger": 1,
    "Iron Shield": 1
}

enemies = [
    {"name": "Dire Bat", "health": 30, "attack": 10},
    {"name": "Blooded Vampire", "health": 25, "attack": 12},
    {"name": "Elder Vampire Lord", "health": 40, "attack": 11},
    {"name": "Vampire's Thrall", "health": 20, "attack": 9},
    {"name": "Blooded Elder Vampire Lord", "health": 50, "attack": 20, "defense": 10},
    {"name": "Gothic Succubus", "health": 15, "attack": 12, "defense": 6},
    {"name": "Dark Cultists", "health": 15, "attack": 10, "defense": 5},
    {"name": "Blood Spiders", "health": 10, "attack": 14, "defense": 3},
]

# Simulate open-world gameplay
player_race = input("Choose your race (Vampire or Human): ").capitalize()
player_name = input("Enter your name: ")

if player_race == 'Vampire':
    player = Vampire(player_name)
elif player_race == 'Human':
    player = Human(player_name)
else:
    print("Invalid race. Defaulting to Human.")
    player = Human(player_name)

def undertake_quest(player, quests):
    quest_options(quests)
    selected_quest_idx = input("Enter the quest number you want to undertake (or 'back' to choose another town): ")

    if selected_quest_idx.lower() == 'back':
        return None

    try:
        selected_quest_idx = int(selected_quest_idx) - 1
        if 0 <= selected_quest_idx < len(quests):
            return quests[selected_quest_idx]
        else:
            print("Invalid quest index.")
            return None
    except ValueError:
        print("Invalid input. Please enter a valid quest index.")
        return None

while True:
    town_options()
    selected_town = input("Enter the town you want to visit (or 'exit' to end the game): ").capitalize()

    if selected_town == 'Exit':
        print("Exiting the game. Goodbye!")
        break

    if selected_town not in towns:
        print("Invalid town. Please choose a valid town.")
        continue

    player.current_city = selected_town
    print(f"Welcome to {selected_town}, {player.name} the {player.race}!")

    quests = city_quests[selected_town]
    quest_options(quests)

    merchant = Merchant()

    while True:
        choice = input("Enter your choice: ")

        print("\nOptions:")
        print("1. Undertake a quest")
        print("2. Explore the surroundings")
        print("3. Visit the Gothic Market")
        print("4. Interact with NPCs")
        print("5. View Inventory")
        print("6. Exit town")

        if choice == '1':
            selected_quest = undertake_quest(player, quests)
            if selected_quest:
                simulate_quest(player, selected_quest)
        elif choice == '2':
            explore_command(player, merchant, None)
        elif choice == '3':
            merchant_interaction(player, merchant)
        elif choice == '4':
            interact_with_npcs(player)
        elif choice == '5':
            player.view_inventory()
            print(f"Level: {player.level}")
            print(f"Experience: {player.experience}/{player.level * 100}")
            print(f"Health: {player.health}/{player.max_health}")
            print(f"Attack: {player.attack}")
            print(f"Defense: {player.defense}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

