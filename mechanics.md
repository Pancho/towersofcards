# Mechanics

## Game structure

Game is split into rounds. During a round player plays cards and they
come into effect in the beginning of next turn. During the turn a wave
a attackers is spawned on each lane. Round ends when these reach goal
or are destroyed. Probably some minimum time is also needed so that
the player has time to play his cards.

The game split into phases (EARLY, MID, LATE, END) which defines which
cards are playable. In the EARLY phase only EARLY cards are playable,
and in the END phase all are playable.

Each phase lasts 3-5 rounds? Except the END phase which lasts until the bitter end.

## Entities

### Towers

Towers are placed in slots that are given to each player. Each lane starts with a basic tower.

Basic attributes:

* Range
* Rate of fire
* Damage type
  * Physical/Kinetic
  * Fire (Also causes maybe dot?)
  * Cold (Slows targets?)
  * Electric? 
* Projectile type
  * Direct - pewpew!
  * Splash - shoots projectile that damages all units in an area
  * omnidirectional - Wave eminates from the tower outwards and damages all in radius

There are several possibilities for targeting.
* Nearest to the tower
* Nearest to the base
* Strongest attacker

Towers target the first attacker that enters its range. It keeps on
firing on it until it's out of range or is destroyed. It selects the
new target with the targeting heuristic.

Targeting heuristic could also be a attribute of the tower?

Examples:

Sniper tower: Low ROF, High Damage, direct. Targets the strongest in range.

Freeze tower: Low ROF, Low damage, Omni. Targets everyone in range.

Basic tower: low Damage, direct, targets nearest to base
  
### Attackers

When a round starts a wave of attackers is spawned at at the spawning
points. From there they proceed until they reach the opposing
base. They damage it and are destroyed.

They proceed at constant speed and don't interact with opposing attackers.

As the game goes on the attackers stats scale up. This serves as a tie
breaker mechanism to ensure game ending.

Attributes:
* Speed (Scales with time)
* Hit points (Scales with time)
* Shields?
* Damage (which is inflicted upon the enemy when reaching base.
* Resistances to different data types
* Number of attackers per wave


### Projecties

Do we also model these or are they just cosmetic? At simplest they should be autohit.

## Cards

Factions?

### Towers

These cards are placed on an empty (or already occupied slots?) and they spawn a new tower.

### Attackers

These can used to change the attacker type for a lane. Maybe they should have a duration? (n waves).

Examples:

Basic attackers: 5x creeps with average stats

Juggernaut: 1x creep with high hit points and damage resistance

Lings: 10x low health fast creeps.

### (De)buffs

Buffs can be temporary (de)boosts to attackers or towers.

Examples:

Your creeps have extra X resistance to Y for a round.

Enemy towers fire at -X ROF.

Enemy tower switches sides for a round.

### Upgrade tower/attacker

Upgrades tower or attacker permanently. They are lost if the attacker/tower is changed.

This gives gameplay options, where the player can invest heavily in
early game attackers hoping to gain an early win, or save them later
on the stronger late game attackers and towers.

Maybe there needs to be cap how many upgrades tower can have?

Examples:

More the merrier: +1 creep to the wave

Kamikaze: +X speed -Y resistances

### Special

Routing changes in map, etc.
