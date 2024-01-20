import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

class Player:
    def __init__(self, name, race):
        self.name = name
        self.health = 100
        self.gold = 0
        self.race = race
        self.gold = 125
        self.experience = 0
        self.level = 1
        self.attack = 10
        self.defense = 5
        self.guild = None

    def join_guild(self, guild_name):
        self.guild = guild_name

    def earn_experience(self, xp):
        self.experience += xp
        if self.experience >= 100:  # Example: Level up after reaching 100 XP
            self.level += 1
            self.experience = 0
            self.health += 20 

    def get_race(self):
        return self.race
    
    def use_health_potion(player):
        player['health'] += 30  # Increase player's health by 30 (adjust as needed)
        if player['health'] > 100:  # Cap player's health at 100
            player['health'] = 10

    def use_silver_dagger(player, enemy):
        damage = max(player['attack'] - enemy['defense'], 0)  # Calculate damage
        enemy['health'] -= damage 

    def use_iron_shield(player):
        player['defense'] += 10

    def upgrade_weapon(self):
        # Implement logic to increase attack power on weapon upgrade
        self.attack += 5

    def level_up(self):
        if self.experience >= 100:  # Example threshold for leveling up
            self.level += 1
            self.experience = 0

            # Increase stats on leveling up
            self.attack += 5
            self.defense += 2

            # Provide other benefits based on the game's design
            if self.level % 5 == 0:
                # Every 5 levels, provide a special ability or item, for example
                self.special_ability = True

            # Inform the player about the level-up
            return f"{self.name} leveled up to level {self.level}! Stats increased. You now have {self.attack} attack and {self.defense} defense."
        else:
            return "Not enough experience to level up."

# Assuming you have a player and an enemy dictionary:
player = {'health': 100, 'attack': 20, 'defense': 10}
enemy = {'health': 50, 'attack': 15, 'defense': 5}

def get_random_enemy():
    return random.choice(enemies)

def get_random_event():
    events = ["positive_event", "negative_event", "neutral_event"]
    return random.choice(events)


city_quests = {
    "Raven's Hollow": [
        {"name": "Retrieve Lost Amulet", "description": "Find the lost amulet in the haunted forest."},
        {"name": "Clear Vampire Nest", "description": "Eliminate the vampire nest in the old crypt."},
        {"name": "Rescue Kidnapped Villager", "description": "Save the kidnapped villager from the abandoned mansion."}
    ],
    "Crimsonshire": [
        {"name": "Investigate Strange Noises", "description": "Explore the eerie sounds coming from the abandoned church."},
        {"name": "Exterminate Giant Spiders", "description": "Clear the infestation of giant spiders from the underground catacombs."},
        {"name": "Retrieve Stolen Relic", "description": "Recover the stolen relic from the thieves' hideout."}
    ],
    # Add quests for other cities similarly
    # ...
}

gothic_cities = [
    "Raven's Hollow",
    "Crimsonshire",
    "Shadowmere",
    "Darkwood",
    "Bloodmoon",
    "Gloomhaven"
]

npcs = {
    "Vampire Lord": [
        "Greetings traveler. What brings you to my domain?",
        "Beware the night, for it belongs to me.",
        "You have the scent of a mortal about you."
        "Remember. This is my Domain! Do not think a mortal is welcome. Unless You are of Pure Blood?"
        "Can you be the Fabled Daywalker?"
        ""    
    ],
    "Innkeeper": [
        "Welcome to the Crimson Tavern. Can I get you a drink?",
        "Looking for a room for the night?"
    ],
    "Wandering Bard": [
        "Hark, brave adventurer! I have a tale to tell.",
        "In days of old, when knights were bold..."
    ]
}

enemies = [
    {"name": "Dire Bat", "health": 30, "attack": 10},
    {"name": "Blooded Vampire", "health": 25, "attack": 12},
    {"name": "Elder Vampire Lord", "health": 40, "attack": 11},
    {"name": "Vampire's Thrawl", "health": 20, "attack": 9},
    {"name": "Blooded Elder Vampire Lord", "health": 50, "attack": 20, "Defense": 10},
    {"name": "Gothic Succubus", "health": 15, "attack": 12, "defense":6},
]

player_inventory = {
    "Gold": 100,
    "Health Potion": 3,
    "Silver Dagger": 1,
    "Iron Shield": 1
}

easter_eggs = {
    "Raven Statue": "You stumble upon a hidden glade and find a beautiful statue of a raven.",
    "Glowing Mushrooms": "As you explore a dark cave, you notice a cluster of mushrooms emitting a soft, eerie glow.",
    "Mysterious Symbol": "In an ancient ruin, you discover a mysterious symbol etched into the stone walls.",
    # Add more easter eggs as needed
}

# Create an instance of the player
players = {}

quest_journals = {}

@bot.command()
async def start_romance(ctx, name, race):
    if name in players:
        await ctx.send("You are already in the game.")
    else:
        if race.lower() == "vampire":
            player = Vampire(name)
        elif race.lower() == "human":
            player = Human(name)
        else:
            await ctx.send("Invalid race. Choose either 'vampire' or 'human'.")
            return
        players[name] = player
        await ctx.send(f"Welcome to the world, {name} the {race}!")

@bot.command()
async def check_stats(ctx, name):
    if name in players:
        player = players[name]
        stats_message = f"{player.name}'s Stats:\n" \
                        f"Level: {player.level}\n" \
                        f"Attack: {player.attack}\n" \
                        f"Defense: {player.defense}\n" \
                        f"Experience: {player.experience}/{(player.level * 100)}"
        await ctx.send(stats_message)
    else:
        await ctx.send("Player not found.")

# Command to explore the world
@bot.command()
async def explore(ctx, name):
    if name in players:
        player = players[name]
        # Implement your game logic here for exploring the world, encountering creatures, finding treasure, etc.
        # For now, let's just increase the player's gold.
        player.gold += 10
        await ctx.send(f"You found 10 gold while exploring!")
    
    # Check for secret easter eggs
    if random.random() < 0.1:  # 10% chance of encountering an easter egg
        easter_egg_name, easter_egg_description = random.choice(list(easter_eggs.items()))
        await ctx.send(f"You've discovered a secret easter egg: {easter_egg_name}!\nDescription: {easter_egg_description}")

        await ctx.send(f"You found 10 gold while exploring!")

    if name in players:
        player = players[name]
        enemy = get_random_enemy()

        await ctx.send(f"You encountered a {enemy['name']}!")

        while player.health > 0 and enemy['health'] > 0:
            # Player's turn to attack
            attack_damage = random.randint(5, 15)
            enemy['health'] -= attack_damage

            # Check if enemy is defeated
            if enemy['health'] <= 0:
                player.gold += random.randint(10, 20)
                await ctx.send(f"You defeated the {enemy['name']} and gained {player.gold} gold!")
                break

            # Enemy's turn to attack
            enemy_attack_damage = random.randint(8, 12)
            player.health -= enemy_attack_damage

            # Check if player is defeated
            if player.health <= 0:
                await ctx.send(f"You were defeated by the {enemy['name']}! Game over.")
                del players[name]
                break

        await ctx.send(f"Health: {player.health}\nGold: {player.gold}")

    if name in players:
        player = players[name]
        # Implement random events logic
        event = get_random_event()
        await ctx.send(f"Random Event: {event}")
        if "positive" in event:
            # Implement positive event effects
            player.gold += 20
            await ctx.send(f"{player.name} gained 20 gold from the event!")
        elif "negative" in event:
            # Implement negative event effects
            player.health -= 10
            await ctx.send(f"{player.name} lost 10 health from the event!")
        else:
            await ctx.send("Nothing significant happened.")
    else:
        await ctx.send("Player not found.")

        if name in players:
            player = players[name]
            await ctx.send(f"{name} is exploring...")

@bot.command()
async def quit_game(ctx, name):
    if name in players:
        del players[name]
        await ctx.send(f"{name}, your adventure has come to an end.")
    else:
        await ctx.send("Player not found.")

class Vampire(Player):
    def __init__(self, name):
        super().__init__(name, "Vampire")
        self.blood_points = 100

    def bite(self, target):
        if self.blood_points >= 10:
            self.blood_points -= 10
            target.health -= 20
            return f"{self.name} bites {target.name} and drains their blood!"
        else:
            return "Not enough blood points to bite."

class Human(Player):
    def __init__(self, name):
        super().__init__(name, "Human")
        self.arrows = 5

    def shoot_arrow(self, target):
        if self.arrows > 0:
            self.arrows -= 1
            target.health -= 15
            return f"{self.name} shoots an arrow at {target.name}!"
        else:
            return "Out of arrows."

@bot.command()
async def talk(ctx, npc_name):
    if npc_name in npcs:
        npc = npcs[npc_name]
        random_dialogue = random.choice(npc)
        await ctx.send(f"{npc_name}: {random_dialogue}")
    else:
        await ctx.send("NPC not found. Please try again.")

@bot.command()
async def inventory(ctx):
    inventory_list = "\n".join([f"{item}: {quantity}" for item, quantity in player_inventory.items()])
    await ctx.send(f"Player's Inventory:\n{inventory_list}")

# Define items for sale in each town
town_items = {
    "RavensHollow": [
        {"name": "Healing Potion", "price": 20},
        {"name": "Silver Crossbow", "price": 50},
        # Add more items for sale
    ],
    "Crimsonshire": [
        {"name": "Health Elixir", "price": 25},
        {"name": "Enchanted Dagger", "price": 60},
        # Add more items for sale
    ],
    # Add items for other towns similarly
    # ...
}

# Create an inventory for each town's merchant
town_inventories = {
    "Raven's Hollow": [
        {"name": "Healing Potion", "quantity": 10},
        {"name": "Silver Crossbow", "quantity": 5},
        # Add more items for sale
    ],
    "Crimsonshire": [
        {"name": "Health Elixir", "quantity": 8},
        {"name": "Enchanted Dagger", "quantity": 3},
        # Add more items for sale
    ],
    # Add items for other towns similarly
    # ...
}

@bot.command()
async def visit_merchant(ctx, name, town):
    if name in players and town in gothic_cities:
        player = players[name]
        await ctx.send(f"Welcome to the {town} Merchant, {name}!")

        # Show available items for sale
        items = town_items[town]
        for idx, item in enumerate(items, start=1):
            await ctx.send(f"{idx}. {item['name']} - {item['price']} gold")

        # Allow player to buy items
        await ctx.send("Type !buy [item_index] [quantity] to make a purchase.")

    else:
        await ctx.send("Invalid player or town name.")

@bot.command()
async def buy(ctx, name, item_idx, quantity=1):
    if name in players and name in quest_journals:
        player = players[name]
        if item_idx.isdigit():
            item_idx = int(item_idx) - 1
            town = player.current_city
            items = town_items[town]
            inventories = town_inventories[town]
            if 0 <= item_idx < len(items):
                item = items[item_idx]
                inventory = inventories[item_idx]
                if inventory['quantity'] >= quantity and player.gold >= item['price'] * quantity:
                    player.gold -= item['price'] * quantity
                    # Add the item to the player's inventory (implement player_inventory dictionary)
                    if item['name'] in player_inventory:
                        player_inventory[item['name']] += quantity
                    else:
                        player_inventory[item['name']] = quantity
                    inventory['quantity'] -= quantity
                    await ctx.send(f"You bought {quantity} {item['name']} for {item['price'] * quantity} gold.")
                elif player.gold < item['price'] * quantity:
                    await ctx.send("You don't have enough gold to make that purchase.")
                else:
                    await ctx.send("That item is out of stock.")
            else:
                await ctx.send("Invalid item index.")
        else:
            await ctx.send("Invalid item index.")
    else:
        await ctx.send("Invalid player or quest journal not found.")

@bot.command()
async def sell(ctx, name, item_name, quantity=1):
    if name in players and name in quest_journals:
        player = players[name]
        if item_name in player_inventory and player_inventory[item_name] >= quantity:
            town = player.current_city
            items = town_items[town]
            inventories = town_inventories[town]
            item_index = next((i for i, item in enumerate(items) if item['name'] == item_name), None)
            if item_index is not None:
                item = items[item_index]
                inventory = inventories[item_index]
                player.gold += item['price'] * quantity
                player_inventory[item_name] -= quantity
                inventory['quantity'] += quantity
                await ctx.send(f"You sold {quantity} {item_name} for {item['price'] * quantity} gold.")
            else:
                await ctx.send("Item not found in the town's inventory.")
        else:
            await ctx.send("You don't have enough of that item to sell.")
    else:
        await ctx.send("Invalid player or quest journal not found.")

easter_egg_bosses = {
    "Ancient Guardian": {"health": 100, "attack": 15, "defense": 10},
    "Enchanted Spirit": {"health": 80, "attack": 20, "defense": 5},
    "Cursed Knight": {"health": 120, "attack": 18, "defense": 15},
    # Add more easter egg bosses as needed
}

@bot.command()
async def level(ctx, name):
    if name in players:
        player = players[name]
        await ctx.send(f"{player.name} - Level {player.level} - XP: {player.experience}/100")
    else:
        await ctx.send("Player not found.")

@bot.command()
async def upgrade_weapon(ctx, name):
    if name in players and "Silver Dagger" in player_inventory and player_inventory["Silver Dagger"] > 0:
        player = players[name]
        # Implement logic for upgrading the weapon
        player.upgrade_weapon()
        player_inventory["Silver Dagger"] -= 1
        await ctx.send(f"{player.name} upgraded their weapon! New attack power: {player.attack}")
    else:
        await ctx.send("Unable to upgrade weapon. Make sure you have a Silver Dagger in your inventory.")


@bot.command()
async def complete_quest(ctx, name, quest_idx):
    if name in players and name in quest_journals:
        player = players[name]
        if quest_idx.isdigit():
            quest_idx = int(quest_idx) - 1
            quests = city_quests[player.current_city]
            if 0 <= quest_idx < len(quests):
                quest = quests[quest_idx]
                quest_journals[name].remove(quest)  # Remove completed quest from the journal
                # Implement quest completion rewards
                player.experience += 50
                player.gold += 30
                await ctx.send(f"{player.name} completed the quest '{quest['name']}' and gained 50 experience and 30 gold!")
            else:
                await ctx.send("Invalid quest index.")
        else:
            await ctx.send("Invalid quest index.")
    else:
        await ctx.send("Invalid player or quest journal not found.")

async def check_guild(ctx, name):
    if name in players:
        player = players[name]
        if player.guild:
            await ctx.send(f"{player.name} is a member of the {player.guild} guild.")
        else:
            await ctx.send(f"{player.name} is not part of any guild.")
    else:
        await ctx.send("Player not found.")

# Command to join a guild
@bot.command()
async def join_guild(ctx, name, guild_name):
    if name in players:
        player = players[name]
        if not player.guild:
            player.guild = guild_name
            await ctx.send(f"{player.name} has joined the {player.guild} guild!")
        else:
            await ctx.send(f"{player.name} is already a member of the {player.guild} guild.")
    else:
        await ctx.send("Player not found.")

# Command to leave the current guild
@bot.command()
async def leave_guild(ctx, name):
    if name in players:
        player = players[name]
        if player.guild:
            await ctx.send(f"{player.name} has left the {player.guild} guild.")
            player.guild = None
        else:
            await ctx.send(f"{player.name} is not part of any guild.")
    else:
        await ctx.send("Player not found.")

bot.run('MTE2OTc1MDE4MjgwNDU5ODgyNA.GCzoPf.0jH4Ed7JtEbgqweJ-UhngaA_ELIO2Tk3Zt-qYo')
