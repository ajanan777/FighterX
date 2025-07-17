# FighterX
A 2D fighting game built with Pygame. Choose your hero type, fight against a friend or practice against a bot on a selection of three arenas. Includes directional attacks, string attacks/combos and can block attacks.


## Character Types & Attributes

The game features multiple character types, each with distinct attributes that affect gameplay:

<img width="1603" height="935" alt="image" src="https://github.com/user-attachments/assets/63107695-eaf8-4b63-80b5-547d11d6d374" />

- **Speedmaster:** Fast and agile, but deals less damage.
- **Flexstrike:** Balanced stats across speed, damage, and defense. Ideal for players who want an all-around fighter.
- **Heavy Hitter:** Slow but powerful, with high damage output and stronger attacks.

Each character has stats that influence how they perform in battle:

- **Speed:** Affects how fast the character moves across the screen.
- **Damage:** Determines how much health is reduced from an opponent when hitting.
- **Attack Cooldown:** The delay between successive attacks.
- **Dodge Cooldown:** The recovery time after dodging.
- **Attack Length:** Duration of an attack animation or active hitbox.
- **Bot Buffer:** Used to control the Bot’s timing for attacks and movement.

These attributes encourage players to pick a character type that fits their play style.




## Attacks & Dodging

Each player has a selection of attacks and a dodge move. Some moves have longer cooldowns or animations than others.

<img width="1600" height="936" alt="image" src="https://github.com/user-attachments/assets/f04aa655-3185-47e3-9841-bb9f48b83c8c" />

### Attacks
- **Punch:** A fast, short-range forward attack.
- **Kick:** A downward attack aimed at opponents who are below the player.
- **Upward Strike:** Targets enemies who are in the air or jumping.
- **String Attack:** If the player presses the attack key twice quickly, the character performs a short combo (a punch followed by a kick) that covers a greater distance.

Each attack has its own animation and a cooldown before it can be used again. The length of the attack and its range depend on the character’s stats.

### Dodging
Characters can dodge to avoid attacks. There's a short cooldown after dodging, so it can't be spammed. It's mainly used to avoid incoming hits or reposition during a fight.



## Practice against Bot mode

FighterX includes a **Practice Mode** where you can practice against a bot. This mode is great for warming up or practicing combos and dodging.
![ezgif-483ab3fb0de746](https://github.com/user-attachments/assets/f96b0f33-3a10-42f9-b03c-d1d552d29dbe)

You can choose from three difficulty levels, each adjusting the bot's behavior and reaction timing:

- **Easy:** The bot has a noticeable delay before attacking or dodging. Good for beginners.
- **Medium:** More reactive and balanced. The bot responds faster and attempts more frequent attacks and dodges.
- **Hard:** The bot reacts quickly with minimal delay. Fast attacks and hard to hit.
