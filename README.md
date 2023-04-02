# Text-based game - The spy who forgot his mission

A text-based game done in Python using OOP

26 rooms total with rigid map, except for the first joint from the room to the hostel front, which is a random generation. Some rooms have a lot of puzzles, while others are distractors.

Player attributes: Player has money, killing power, carried weight, and internal clock

Monsters: A monster that can destroy a number of random items on the player before dying, another monster that has multiple lives, and another is fixed instead of moving randomly.

Event:	After a certain amount of time has elapsed, which happens only by moving between rooms, or by waiting command, an event will happen, as in the description of an event will be printed, and the event will be removed after having been shown to the player. Done in main.

Character	A character that may or may not have a restriction on (only when a player has a certain object for example). The player can use command ask, and interact with character by choosing one of the given conversation lines. New file.

Main maneuvers in game:
1	Drop	Dropping an item to the room the player is in (removing from player and adding to room). Done as new player function.
2	Status	Listing out all player attributes that are important for decision making. Done by new function in player.
3	Inspect	Look at the description as well as important attributes of each item. Capable of inspecting within locked chests, and inspecting items contained in other items. Done by new function and player and controlled in main.
4 Climb	Moving function that only works with the right tools and rooms.
5	Limit	Putting a limit on how much the player can pick up (40), which also applies to when the player is buying. Done by new function in player, and updating pickup.
6	Wait turns	Wait a number of turns, which updates the location of some monsters, and updates player’s health, as well as player’s clock, which will control when an event will happen, and when the player can access a certain room. Done in main.
7	Heal	Adding to player’s health when using the item with a health benefit, and disappearing after usage. Done by new attribute for item.
8 Loot	After defeat, monsters with items on them will add a random one to the room, which the player can then pick up. Done in main and attack monster.
9 Hint	A hint option available in some rooms. The player can see the hints if they need.

Main objects:
1	Weapon	Many weapons with varying kill power, and many have to be paid for. Multiple of them can be equipped at the same attack round, and their strength added together to attack monsters. Done by new attribute for item.
2	Container	Items that hold other items, which reveals hidden items in a room when you inspect them. Picking up a container does not automatically pick up the insides of it. Player can pick up these hidden items separately. Done by new attribute for item.
3	Locked chest	A container with a key. Player needs to use the open command, and have the right key on them, and type in the right key name, in order to open and reveal the items within. Then they can either pick up, or inspect inside the container. They can do so outside as well. Inherit from item.
4	Locked room	Room that is locked, open only with a code or with the right tool on the player. Inherit from room.
5	Products	Items that cost and can be picked up by buying function with the player’s money. Done by adding attributes to items.



