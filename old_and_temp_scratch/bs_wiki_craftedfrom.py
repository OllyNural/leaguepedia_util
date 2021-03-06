from log_into_wiki import *
import mwparserfromhell

recipes = {
	"Tachyon Blade": "Engineered Arcane Motor, Laser Pointer",
	"Engineered Arcane Motor": "Motor, Arcane Stone",
	"Motor": "Steel, Electronic Parts",
	"Electronic Parts": "Wire, Battery",
	"Steel": "Iron Ore, Scrap Metal",
	"Arcane Stone": "Flint, Holy Blood",
	"Flint": "Stone, Gunpowder",
	"Arcane Edge": "Arcane Stone, Jamadhar",
	"Jamadhar": "Kitchen Knife, Knuckle",
	"Powder of Life": "Tree of Life, Stone",
	"Jewel Sword": "Knife, Ruby",
	"Ruby": "Gemstone, Hammer",
	"Axe of Pangu": "Battle Axe, Adamantium",
	"Battle Axe": "Spear Handle, Hatchet",
	"Adamantium": "Mithril, Iron Ore",
	"Sky Piercer": "Halberd Axe, Horse Guandao",
	"Halberd Axe": "Long Spear, Hatchet",
	"Long Spear": "Short Spear, Spear Handle",
	"Horse Guandao": "Spear Handle, Scimitar",
	"Scimitar": "Shamshir, Kitchen Knife",
	"Dáinsleif": "Holy Blood, Bastard Sword",
	"Bastard Sword": "Long Sword, Steel",
	"Dragon Guandao": "Halberd Axe, Tree of Life",
	"Beam Axe": "Battle Axe, Plasma Sword",
	"Plasma Sword": "Laser Pointer, Sabre",
	"Sabre": "Shamshir, Heated Whetstone",
	"Heated Whetstone": "Whetstone, Lighter",
	"Santa Muerte": "Reaper's Scythe, Horse Guandao",
	"Reaper's Scythe": "Sickle, Spear Handle",
	"Parallel Sword": "Bastard Sword, Rapier",
	"Rapier": "Sabre, Heated Whetstone",
	"Seven Star Sword": "Meteorite, Jewel Sword",
	"Vibroblade": "Motor, Knife",
	"Hǫfuð": "Jewel Sword, Glass Pieces",
	"Glass Pieces": "Stone, Glass Cup",
	"Harpe": "Scimitar, Jewel Sword",
	"Divine Dual Swords": "Muramasa, Masamune",
	"Monohoshizao": "Odachi, Blueprint",
	"Odachi": "Katana, Iron Sheet",
	"Iron Sheet": "Scrap Metal, Hammer",
	"Blueprint": "Fountain Pen, Thick Paper",
	"Durendal mk2": "Plasma Sword, Tree of Life",
	"Starsteel Claymore": "Starsteel, Long Sword",
	"Starsteel": "Meteorite, Iron Ore",
	"Starsteel Twin Sword": "Starsteel, Twin Sword",
	"Twin Sword": "Kitchen Knife, Sharp Kitchen Knife",
	"Sharp Kitchen Knife": "Kitchen Knife, Whetstone",
	"Excalibur": "Jewel Sword, Cross",
	"Chainsaw": "Soldering Iron, Battery",
	"Soldering Iron": "Nail, Electronic Parts",
	"Arondight": "Bastard Sword, Cross",
	"Sword of Justice": "Stallion Medal, Long Sword",
	"Army Knife": "Knife, Branch",
	"Axe Chain": "Steel Chain, Hatchet",
	"Chain Scythe": "Steel Chain, Sickle",
	"Spear of Longinus": "Long Spear, Holy Blood",
	"Lance of Poseidon": "Trident, Purified Water",
	"Trident": "Twin Sword, Long Spear",
	"Purified Water": "Boiling Water, Ice",
	"Boiling Water": "Water, Lighter",
	"Cosmic Bident": "Bident, Ion Battery",
	"Ion Battery": "Sports Drink, Battery",
	"Bident": "Rapier, Short Spear",
	"Shockblade": "Tails Screw, Sword of Assassin",
	"Tails Screw": "Awl, Electronic Parts",
	"Awl": "Nail, Scrap Metal",
	"Sword of Assassin": "Arm Wamers, Jamadhar",
	"Pile Bunker": "Remington M31RS, Harpoon",
	"Bamboo Spear": "Bamboo, Knife",
	"Monkey King Bar": "Engineered Arcane Motor, Long Rod",
	"Magic Stick": "Warhammer, Moonlight Pendant",
	"Warhammer": "Hammer, Spear Handle",
	"Moonlight Pendant": "Moon Stone, Ribbon",
	"Moon Stone": "Starsteel, Stone",
	"Statue of Soteria": "Torch, Anatomy Model",
	"Torch": "Torch Hold, Lighter",
	"Torch Hold": "Bamboo, Oilcloth",
	"Oilcloth": "Cloth, Oil",
	"Gleipnir": "Rope Cuffs, Thorn Whip",
	"Rope Cuffs": "Stallion Medal, Whip",
	"Thorn Whip": "Whip, Spiked Plank",
	"Spiked Plank": "Needle, Branch",
	"Fang Mace": "Arcane Stone, Goblin Bat",
	"Goblin Bat": "Nail, Short Rod",
	"Hammer of Thor": "Usurper Warhammer, High Voltage Line",
	"Usurper Warhammer": "Warhammer, Adamantium",
	"High Voltage Line": "Wire, Dead Battery",
	"Dead Battery": "Battery, Water",
	"Villainous Whip": "Lightning Whip, Electric Whip",
	"Lightning Whip": "Bullwhip, Dead Battery",
	"Bullwhip": "Razor, Whip",
	"Electric Whip": "Whip, High Voltage Line",
	"Banana Leaf Fan": "White Crane Fan, Powder of Life",
	"White Crane Fan": "Fan, Feather",
	"Titan Hammer": "Warhammer, Ogre Skin",
	"Red Muffler": "Scarf, Holy Blood",
	"Vajra": "Tree of Life, Spiked Bat",
	"Spiked Bat": "Bat (weapon), Nail",
	"Plasma Tonfa": "Steel Tonfa, Laser Pointer",
	"Steel Tonfa": "Tonfa, Steel",
	"Tonfa": "Short Rod, Cotton Work Glove",
	"KGB Agent Umbrella": "Umbrella, Poison",
	"Umbrella": "Oilcloth, Long Rod",
	"Poison": "Fertilizer, Lye",
	"Lye": "Water, Ash",
	"Ash": "Thick Paper, Lighter",
	"Double Nunchaku": "Nunchaku, Bullwhip",
	"Nunchaku": "Chain Rod, Short Rod",
	"Chain Rod": "Steel Chain, Short Rod",
	"Triple Nunchaku": "Nunchaku, Chain Rod",
	"Golden Whip": "Bullwhip, Gold",
	"Gold": "Pickaxe, Gemstone",
	"Flail": "Chain Rod, Iron Ball",
	"Golf Club": "Heated Steel Pipe, Hammer",
	"Heated Steel Pipe": "Steel Pipe, Lighter",
	"Iron Mace": "Stone Axe, Steel Chain",
	"Stone Axe": "Stone, Bamboo",
	"Leather Whip": "Scissors, Leather",
	"Heated Frying Pan": "Frying Pan, Lighter",
	"Morning Star": "Long Rod, Iron Ball",
	"Feather Duster": "Feather, Spear Handle",
	"Flag Pole": "Long Rod, Nail",
	"Petal Torrent": "Frost Venom Dart, Stingburst",
	"Frost Venom Dart": "Venom Dart, Glacial Ice",
	"Glacial Ice": "Powder of Life, Ice",
	"Venom Dart": "Needle, Poison",
	"Stingburst": "RDX, Spiked Plank",
	"RDX": "Scrap Metal, Dynamite",
	"Dynamite": "Gunpowder, Wire",
	"Sudarsana": "Engineered Arcane Motor, CD",
	"Headsman D's Axe": "Tomahawk, Motor",
	"Tomahawk": "Hatchet, Leather",
	"High Explosive Grenade": "Grenade, Mine",
	"Grenade": "Gunpowder, Iron Ball",
	"Mine": "RDX, Enhanced Mouse Trap",
	"Enhanced Mouse Trap": "Mouse Trap, Glue",
	"David's Sling": "Adamantium, Arcane Stone",
	"Fuhma Shuriken": "Throwing Stars, Twin Sword",
	"Throwing Stars": "Box Cutter, Razor",
	"Azure Dagger": "Onyx Dagger, Poison",
	"Onyx Dagger": "Throwing Dagger, Cross",
	"Astrape": "Pilum, Tails Screw",
	"Pilum": "Javelin, Short Spear",
	"Javelin": "Throwing Dagger, Spear Handle",
	"Bloody Chakram": "Chakram, Holy Blood",
	"Chakram": "Throwing Stars, CD",
	"Ruthenium Marble": "Spiky Bouncy Ball, Gold",
	"Spiky Bouncy Ball": "Glass Pieces, Flubber",
	"Flubber": "Rubber, Boiling Water",
	"Dharma Chakram": "Buddhist Scripture, Chakram",
	"Incendiary Bomb": "Molotov Cocktail, Gunpowder",
	"Molotov Cocktail": "Oil, Glass Bottle",
	"Enhanced Boomerang": "Boomerang, Oilcloth",
	"Boomerang": "Branch, Rubber",
	"Trick Card": "Buddhist Scripture, Playing Cards",
	"Storm Bolt": "Warhammer, Dead Battery",
	"Flour Bomb": "White Powder, Plastic Bottle",
	"White Powder": "White Chalk, Stone",
	"Vintage Card": "Playing Cards, Fountain Pen",
	"Heated Oil": "Lighter, Oil",
	"Glue Lump": "Glue, Boiling Water",
	"Paper Ball": "Thick Paper, Glue",
	"CD Player": "Electronic Parts, Glass Marble",
	"Kelte": "Engineered Arcane Motor, Colt Python",
	"Hand Cannon": "Iron Sheet, Gunpowder",
	"Blizzard Cannon": "Hand Cannon, Glacial Ice",
	"Barrett M82A1": "PSG-1, Hand Cannon",
	"PSG-1": "Steyr AUG, Sniping Scope",
	"Steyr AUG": "Ingram MAC-10, Laser Pointer",
	"Sniping Scope": "Binoculars, Laser Pointer",
	"Binoculars": "Bamboo, Glass Marble",
	"Uranium Cannon": "Hand Cannon, Arcane Stone",
	"T/C Arms Contender": "K5/DP51, FN57",
	"K5/DP51": "Walther PPK, Steel",
	"FN57": "Beretta M92F, Steel",
	"Plasma Railgun": "Railgun, Cell Phone",
	"Railgun": "Steyr AUG, Electronic Parts",
	"Cell Phone": "Blueprint, Electronic Parts",
	"Devil's Marksman": "Double Revolver SP, Hand Cannon",
	"Double Revolver SP": "Revolver Mk I, Revolver Mk II",
	"Gatling Gun": "Machine Gun, AK-47",
	"Machine Gun": "M16A1, Motor",
	"M16A1": "Walther PPK, Laser Pointer",
	"AK-47": "Long Rifle, Scrap Metal",
	"Long Rifle": "Bamboo, Gunpowder",
	"Plasma Rifle": "Electron Blaster, FR F2",
	"Electron Blaster": "CRT, Ion Battery",
	"CRT": "TV, Hammer",
	"FR F2": "Sniping Scope, AK-47",
	"Golden Rifle": "Bolt Action Rifle, Gold",
	"Bolt Action Rifle": "Long Rifle, Steel Pipe",
	"Holy Shotgun": "Bolt Action Rifle, Cross",
	"Harpoon Gun": "Long Rifle, Harpoon",
	"Colt Anaconda": "Colt Python, Holy Water",
	"Holy Water": "Water, Holy Grail",
	"MP5": "FN57, Laser Pointer",
	"Sharanga": "Engineered Arcane Motor, Short Crossbow",
	"Bow of Apollo": "Steel Bow, Arcane Stone",
	"Steel Bow": "Long Crossbow, Iron Sheet",
	"Long Crossbow": "Short Crossbow, Piano Wire",
	"Bow of Zephyrus": "Composite Bow, Powder of Life",
	"Composite Bow": "Bow, Piano Wire",
	"Failnaught": "Longbow, Holy Blood",
	"Longbow": "Yumi Bow, Rubber",
	"Elemental Bow": "Scorchbow, Mighty Bow",
	"Scorchbow": "Yumi Bow, Flint",
	"Mighty Bow": "Wooden Bow, Gunpowder",
	"Wooden Bow": "Branch, Piano Wire",
	"Ballista": "Steel Bow, Short Spear",
	"Twinbow": "Long Crossbow, Strong Bow",
	"Strong Bow": "Longbow, Oil",
	"Cupid's Bow": "Composite Bow, Crimson Bracelet",
	"Crimson Bracelet": "Ruby, Bracelet",
	"Stallion Bow": "Wooden Bow, Stallion Medal",
	"Hwacha": "Scorchbow, Power Crossbow",
	"Power Crossbow": "Crossbow, Rubber",
	"Crossbow": "Composite Bow, Bamboo",
	"Golden-Ratio Bow": "Pellet Bow, Gold",
	"Pellet Bow": "Branch, Wire",
	"Sniper Bow": "Long Crossbow, Laser Pointer",
	"Sniper Crossbow": "Laser Pointer, Heavy Crossbow",
	"Nanorized Arms": "Knuckle, Engineered Arcane Motor",
	"Gauntlet": "Cotton Work Glove, Steel",
	"Imperial Silk Glove": "Sap Glove, Mithril String",
	"Sap Glove": "Leather Glove, Iron Ore",
	"Leather Glove": "Cotton Work Glove, Leather",
	"Mithril String": "Wire, Mithril",
	"Dark Frost Arms": "Leather Glove, Glacial Ice",
	"Power Fist": "Bone Gauntlet, Ogre Skin",
	"Bone Gauntlet": "Gauntlet, Turtle Shell",
	"Wolverine's Claw": "Iron Claw, Adamantium",
	"Iron Claw": "Iron Ore, Claw",
	"Brasil Gauntlet": "Enhanced Gauntlet, Oilcloth",
	"Enhanced Gauntlet": "Sap Glove, Gauntlet",
	"RuLai's Palm": "Nirvana Gauntlet, Buddhist Scripture",
	"Nirvana Gauntlet": "Open Finger Glove, Ash",
	"Open Finger Glove": "Leather Glove, Scissors",
	"Corrupted Scissorhands": "Scissorhands, Motor",
	"Scissorhands": "Iron Claw, Scissors",
	"One-inch Punch": "Enhanced Gauntlet, Anatomy Model",
	"White Claw Punch": "NineYin Claw, White Powder",
	"NineYin Claw": "Ripped Scroll - 1, Ripped Scroll - 2",
	"Bloodwing Knuckle": "Wing Knuckle, Ruby",
	"Wing Knuckle": "Iron Knuckle, Feather",
	"Iron Knuckle": "Iron Ore, Knuckle",
	"Meteor Gauntlet": "Gauntlet, Meteorite",
	"Shatter Shell Gauntlet": "Bone Gauntlet, Gunpowder",
	"Poison Glass Knuckle": "Glass Knuckle, Poison",
	"Glass Knuckle": "Knuckle, Glass Pieces",
	"Crimson Gauntlet": "Gauntlet, Ruby",
	"Holy Gauntlet": "Sap Glove, Cross",
	"Lace Glove": "Cotton Work Glove, Dress",
	"Dress": "Doctor's Gown, Cloth",
	"Finger Punch": "Open Finger Glove, Iron Ore",
	"Rubber Glove": "Cotton Work Glove, Rubber",
	"Remote Mine": "Engineered Arcane Motor, RDX",
	"Double Guillotine": "Jungle Guillotine, Pendulum Axe",
	"Jungle Guillotine": "Booby Trap, Shamshir",
	"Booby Trap": "Snare, Glue",
	"Pendulum Axe": "Bamboo Trap, Axe Chain",
	"Bamboo Trap": "Snare, Bamboo",
	"Smart Bomb": "RDX, Smart Bomb",
	"Claymore": "Small Claymore, Iron Ball",
	"Small Claymore": "Glass Pieces, Mine",
	"Hidden Maiden": "Stingburst, Pirate Roulette",
	"Pirate Roulette": "Bamboo, Kitchen Knife",
	"C-4": "RDX, White Powder",
	"Fire Trap": "Explosive Trap, Oilcloth",
	"Explosive Trap": "Booby Trap, Gunpowder",
	"Fire Mine": "Mine, Oilcloth",
	"Electrical Shock Trap": "Dead Battery, Piano Wire",
	"Tiara of Light": "Crystal Tiara, Angel's Wing",
	"Crystal Tiara": "Tiara, Glass Pieces",
	"Tiara": "Circlet, Wire",
	"Circlet": "Hairband, Branch",
	"Angel's Wing": "Bishop's Cassock, Feather",
	"Bishop's Cassock": "Cross, Cassock",
	"Imperial Crown": "Crown, Crimson Bracelet",
	"Crown": "Gold, Ruby",
	"Tactical OPS Helmet": "Ballistic Helmet, Cell Phone",
	"Ballistic Helmet": "Bike Helmet, Bullets",
	"Imperial Burgonet": "Close Helm, Gold",
	"Close Helm": "Chain Coif, Mask",
	"Chain Coif": "Hat, Steel Chain",
	"Mask": "Glasses, Feather",
	"Helm of Banneret": "Close Helm, Iron Sheet",
	"Laurel Wreath": "Circlet, Tree of Life",
	"Prophet's Turban": "Scarf, Holy Water",
	"Safety Helmet": "Bike Helmet, Stone",
	"Beret": "Fabric Armor, Scissors",
	"Fire Helmet": "Bike Helmet, Water",
	"Queen of Hearts": "Arcane Stone, Playing Cards",
	"Guardian Suit": "Sheet Metal Armor, Engineered Arcane Motor",
	"Sheet Metal Armor": "Fabric Armor, Steel",
	"Rider Jacket": "Leather Jacket, Steel Chain",
	"Leather Jacket": "Windbreaker, Leather",
	"Mithril Armor": "Chain Armor, Mithril",
	"Chain Armor": "Leather Armor, Steel Chain",
	"Leather Armor": "Fabric Armor, Leather",
	"Commander's Armor": "Chain Armor, Gold",
	"Kabana": "Sheet Metal Armor, Adamantium",
	"Covert Agent Uniform": "Hanbok, Stallion  Medal",
	"Hanbok": "Dress, Flower",
	"Dazzling Armor": "Chain Armor, Dress",
	"Battle Suit": "Bulletproof Vest, Diving Suit",
	"Bulletproof Vest": "Military Suit, Iron Sheet",
	"Military Suit": "Windbreaker, Branch",
	"Diving Suit": "Full Body Swimsuit, Rubber",
	"Red Hood": "Patched Robe, Holy Blood",
	"Patched Robe": "Monk's Robe, Cloth",
	"Rocker's Jacket": "Rider Jacket, Iron Sheet",
	"Clergy's Cassock": "Bishop's Cassock, Gold",
	"Chang Pao": "Qipao, Dress Shirt",
	"Qipao": "Dress, Scissors",
	"Dress Shirt": "Cloth, Scissors",
	"EOD Suit": "Bulletproof Vest, Patched Robe",
	"Dragon Dobok": "Qipao, Turtle Dobok",
	"Turtle Dobok": "Monk's Robe, Turtle Shell",
	"Crusader Armor": "Sheet Metal Armor, Bishop's Cassock",
	"Amazoness Armor": "Sheet Metal Armor, Bikini",
	"Bikini": "Full Body Swimsuit, Scissors",
	"Optical Camouflage Suit": "Diving Suit, Glass Panel",
	"Glass Panel": "Glass Pieces, Glue",
	"Tuxedo Mask": "Suit, Moonlight Pendant",
	"Suit": "Dress Shirt, Cloth",
	"Butler's Suit": "Suit, Feather Duster",
	"Sunset Armor": "Leather Armor, Ruby",
	"Armed Shield DE": "Law of the Shield, Electron Blaster",
	"Law of the Shield": "Steel Shield, Squad Leader Armband",
	"Steel Shield": "Leather Shield, Steel",
	"Leather Shield": "Turtle Shell, Leather",
	"Squad Leader Armband": "Reserve Armband, Needle",
	"Radar": "Heartbeat Sensor, Blueprint",
	"Bracelet of Skadi": "Glacial Ice, Bracelet",
	"Galaxy Watch": "Cell Phone, Watch",
	"Draupnir": "Golden Bracelet, Wrist Band",
	"Golden Bracelet": "Gold, Bracelet",
	"Wrist Band": "Rubber, Bandage",
	"Captain's Shield": "Turtle Shell, Mithril",
	"Sword Stopper": "Bazuband, Iron Claw",
	"Bazuband": "Arm Warmers, Iron Sheet",
	"OPG": "Gauntlet, Ogre Skin",
	"Sword of Shah Jahan": "Golden Bracelet, Sheath",
	"Sheath": "Iron Sheet, Leather",
	"Bracer": "Arm Warmers, Relief Patch",
	"Boots of Hermes": "Feather Boots, Arcane Stone",
	"Feather Boots": "Feather, Boots",
	"EOD Boots": "Steel Knee Pads, Advanced Military Boots",
	"Steel Knee Pads": "Steel, Knee Pads",
	"Knee Pads": "Leather, Cloth",
	"Advanced Military Boots": "Boots, Cloth",
	"Mithril Boots": "Feather Boots, Mithril",
	"Killer Heels": "High Heels, Glass Pieces",
	"High Heels": "Slippers, Scrap Metal",
	"Detective's Heelys": "Heelys, Electronic Parts",
	"Heelys": "Running Shoes, Iron Ball",
	"Battle Boots": "Advanced Military Boots, Knee Pads",
	"Chain Leggings": "Tights, Steel Chain",
	"Kundala": "Moon Stone, Adamantium",
	"Veritas Lux Mea": "Saint's Relic, Buddha Sarira",
	"Saint's Relic": "Cross, Holy Grail",
	"Buddha Sarira": "Wooden Fish, Buddhist Scripture",
	"Schrodinger's Box": "Poison, Box",
	"Pirate Flag": "Flag, Twin Sword",
	"Flag": "Flag Pole, Cloth",
	"Sultan's Quiver": "Mounted Archer's Quiver, Gold",
	"Mounted Archer's Quiver": "Quiver, Belt",
	"Belt": "Leather, Scrap Metal",
	"Quiver": "Leather, Bamboo",
	"Quiver of Infinity": "Quiver, Mirror Marble",
	"Mirror Marble": "Glass Marble, Mithril",
	"Uchiwa": "Doll, Fan",
	"Doll": "Glass Marble, Cloth",
	"Dice of Destiny": "Dice, Playing Cards",
	"Magazine": "Iron Sheet, Box",
	"Petal Dew Pill": "Powder of Life, Flower",
	"Grilled Tuna": "Tuna, Heated Whetstone",
	"Braised Potato": "Potato, Soy Sauce",
	"Ten Tonics Soup": "Turtle Soup, Scrolls of DongYi",
	"Turtle Soup": "Turtle Shell, Cooking Pot",
	"Garlic Ramen": "Hot Ramen, Garlic",
	"Hot Ramen": "Ramen, Boiling Water",
	"Braised Burdock": "Burdock, Soy Sauce",
	"Baked Potato": "Potato, Heated Whetstone",
	"Glazed Sweet Potato": "Sweet Potato, Honey",
	"Grilled Saury": "Saury, Heated Whetstone",
	"Tuna Can": "Tuna, Can",
	"Baked Carp": "Carp, Heated Whetstone",
	"Mocha Bread": "Coffee Liqueur, Bread",
	"Coffee Liqueur": "Alcohol, Coffee",
	"Chocolate Chip Cookies": "Chocolate, Cookie",
	"Baked Sweet Potato": "Sweet Potato, Heated Whetstone",
	"Chocolate Pie Box": "Chocolate Pie, Box",
	"Chocolate Pie": "Chocolate, Bread",
	"Fish Stew": "Carp, Cooking Pot",
	"Healing Potion": "Herb, Glass Bottle",
	"Herb": "Oriental Grass, Flower",
	"Fried Chicken": "Bird Meat, Heated Oil",
	"Spicy Noodle": "Ramen, Soy Sauce",
	"Baked Mudfish": "Mudfish, Heated Whetstone",
	"Sashimi": "Tuna, Sharp Kitchen Knife",
	"Stir Fried Ramen": "Ramen, Frying Pan",
	"Pickled Garlic": "Garlic, Soy Sauce",
	"Liquor Bread": "Soju, Bread",
	"Soju": "Water, Alcohol",
	"Garlic Bread": "Garlic, Bread",
	"French Fries": "Potato, Heated Oil",
	"Herb Medicine": "Turtle Shell, Scrolls of DongYi",
	"Fried Egg": "Bird Egg, Heated Oil",
	"First Aid Kit": "Box, Pill",
	"Pill": "Scrolls of DongYi, Oriental Grass",
	"Acupuncture": "Needle, Scrolls of DongYi",
	"Bungeoppang": "Carp, Bread",
	"Honey Medicine": "Honey, Pill",
	"Curry": "Curry Powder, Boiling Water",
	"Oriental Concoction": "Oriental Grass, Boiling Water",
	"Scrambled Egg": "Bird Egg, Frying Pan",
	"Cocktail": "Orange, Whiskey",
	"Cigarettes": "Tobacco Leaves, Lighter",
	"Flower Liquor": "Sorghum Wine, Flower",
	"Sorghum Wine": "Alcohol, Lighter",
	"Ice Coffee": "Ice, Coffee",
	"Hot Chocolate": "Chocolate, Boiling Water",
	"Americano": "Coffee, Boiling Water",
	"Orangeade": "Orange, Carbonated Water",
	"Burdock Tea": "Burdock, Boiling Water",
	"Hot Honey Water": "Honey, Boiling Water",
	"Ionized Soju": "Soju, Sports Drink",
	"Sparkling Soju": "Soju, Carbonated Water",
	"Herbal Tea": "Herb, Boiling Water",
	"Herbal Liquor": "Sorghum Wine, Oriental Grass",
	"Oriental Raisin Water": "Branch, Boiling Water",
	"Honey Water": "Honey, Water",
	"Half-Filled Glass": "Glass Cup, Water",
	"Kaoliang Liquor": "Sorghum Wine, Lighter",
	"1.5L Water Bottle": "Water, Plastic Bottle",
	"Ice Water": "Ice, Water",
	"Silencer": "Rubber, Bamboo",
	"System Shutdown Code": "CD Player, Blueprint",
	"Wizard's Fishing Pole": "Bamboo, Piano Wire",
	"Searing Palm Scroll": "Anatomy Model, Blueprint",
	"Adrenaline Drink": "Bacchus, Coffee",
	"Clang Clatter": "Plate, Can",
	"Smoke Bomb": "Flour Bomb, Gunpowder",
	"Network PC": "Laptop, Cell Phone",
	"Laptop": "Laptop(dead battery), Ion Battery",
	"Laptop(dead battery)": "Laptop(faulty circuit), Soldering Iron",
	"Laptop(faulty circuit)": "Laptop (broken screen), LCD Panel",
	"LCD Panel": "Glass Panel, CRT"
}

site = login("me","blacksurvival")

infobox = site.pages['Template:ItemInfo']
pages = infobox.embeddedin()

limit = -1

lmt = 0
for page in pages:
	if lmt == limit:
		break
	lmt += 1
	print(page.name)
	if page.name in recipes:
		text = page.text()
		wikitext = mwparserfromhell.parse(text)
		for template in wikitext.filter_templates():
			if template.name.matches('ItemInfo'):
				template.add('recipe',recipes[page.name], preserve_spacing=True)
		
		newtext = str(wikitext)
		newtext = newtext.replace('|recipe','\n|recipe')
		newtext = newtext.replace('\n\n|recipe', '\n|recipe')
		if text != newtext:
			print('Saving page %s...' % page.name)
			page.save(newtext,summary="Auto adding recipe from module lookup")