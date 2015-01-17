# Mechanics

## Game structure

Game structure:
* Phase
** Tick (or turn)

Game is split into rounds. During a round a player plays cards and they
come into effect in the beginning of next turn. During a turn a wave
of attackers is spawned on each lane. Round ends when these reach goal
or are destroyed. Probably some minimum time is also needed so that
the player has time to play their cards.


The game is split into phases (EARLY, MID, LATE, END) which defines which
cards are playable. In the EARLY phase only EARLY cards are playable,
and in the END phase all are playable.


Each phase lasts 3-5 rounds? Except the END phase which lasts until the bitter end.
Phase count for each could be different:
First phase could have 5 ticks so that the players can choose the direction and to expose their responses.
Second should last less, so that the players can test each other, but should also have an opportunity to still hide
some approaches.


Late and end should be the same.
First phase is to set up the battlefield and expose the direction in which a player will steer their game.
Second to test the opponent's strategy and explore the possibilities
End should be there to exploit the weaknesses and finish the game. It should not restrict the player to do what they
would do in the first two, but doing that can change the outcome, for better or worse.

## Entities

### Towers

Towers are placed in slots that are given to each player. Each lane starts with a basic tower.

Basic attributes:

* Range (discrete, in fact a whole state machine can (and should) be compiled for each combination of tower and slot)
* Rate of fire
* Damage type (only one by default, (de)buffs can change that)
  * Physical/Kinetic
  * Fire (Also causes maybe dot?). Fire should cause dot.
  * Acid (The old ones splash)
  * Cold (Slows targets?)
  * Electric? sure: a different kind of aoe.
  * Laser (strong, slow rate of fire, armor piercing)
* Projectile type
  * Direct - pewpew!
  * Splash - shoots projectile that damages all units in an area
  * omnidirectional - Wave eminates from the tower outwards and damages all in radius

There are several possibilities for targeting.
* Nearest to the tower (this should be a slider of values - preference: closest, farthest, none)
* Nearest to the base (does this make sense? What about the towers which are too far? And most will be :))
  * No I mean that given option of targeting multiple targets, it always chooses the one closest to the end in range.
* Strongest attacker (this should be a slider of three values - preference: strongest, weakest, none)

Not sure whether two types of preferences (no matter what options the player has) would work. This could complicate
things design-wise, balancing. It sounds awesome, but it could be a problem.

Towers target the first attacker that enters its range. It keeps on
firing on it until it's out of range or is destroyed. It selects the
new target with the targeting heuristic.

Targeting heuristic could also be a attribute of the tower? This is overengineering :) But is an interesting idea though.

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
* Type (Mechanical, Organic)
* Size?
* Hit points (Scales with time)
* Shields? Maybe just for the von Neumann Probes
* Damage (which is inflicted upon the enemy when reaching base.
* Resistances to different data types
* Number of attackers per wave


### Projectiles

Do we also model these or are they just cosmetic? At simplest they should be auto hit.
Auto hit, yes. But for the sake of graphics they should be modelled and is not a concern of backend at all.
Backend just has to report who hits what and the new state of the units in a proper sequence.

## Cards

So cards are of three factions and neutral ones. Human, Probes, the old ones. See cards.md

### Towers

These cards are placed on an empty (or already occupied slots?) and they spawn a new tower. It becomes operational in
the next tick

Some tower cards should be able to spawn more than one tower. Weaker, but still. Not more than the number of lanes, though.

### Attackers

These can be used to change the attacker type for a lane. Maybe they should have a duration? (n waves).

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

Should we allow selling or replacing? Will the games be long enough for that? Players should be able to make mistakes. Have to test.

Maybe there needs to be cap how many upgrades tower can have?

Examples:

More the merrier: +1 creep to the wave

Kamikaze: +X speed -Y resistances

### Special

Routing changes in map, etc.
