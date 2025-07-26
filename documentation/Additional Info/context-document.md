# Dungeon Master AI World Generation & System Reference

## Introduction
This document serves as the comprehensive reference for the Dungeon Master AI project. It outlines the goals, world-building frameworks, system mechanics, templates, glossaries, and procedural generation tools required to enable an AI Dungeon Master powered by Llama 4 models. The AI will interact with Discord and Twitch, control all aspects of Dungeons & Dragons gameplay, and support extensible, cross-platform world creation.

---

## Project Goals & Overview
- Create a robust, modular framework for procedural world generation and AI-driven Dungeon Master support.
- Integrate real-world, fantasy, and sci-fi elements for flexible campaign settings.
- Provide exhaustive context for AI LLM/MCP to generate, manage, and narrate worlds, characters, and gameplay.
- Ensure all mechanics, templates, and glossaries are unified and cross-referenced for maximum utility.

---

## Table of Contents
1. Noble & Feudal Structure
2. Glossary of Terms
3. Feudal Obligations & Succession
4. Economy & Trade
5. Geography & Regions
6. Culture & Society
7. Religion & Pantheon
8. Magic System
9. NPC & Character Templates
10. Creatures & Encounters
11. Magic Items & Artifacts
12. Dungeons & Sites
13. Random Tables & Generators
14. Timeline & World History
15. DM Reference & Style Guide
16. Appendices
17. Core System Mechanics (Stats, Skills, Spells & Schools)

---

## 1. Noble & Feudal Structure
### 1.1 Hierarchy Map
- Monarch (King/Queen)
    - Princes/Princesses
        - Dukes/Duchesses
            - Marquesses/Marchionesses
                - Earls/Counts/Countesses
                    - Viscounts/Viscountesses
                        - Barons/Baronesses
                            - Lords/Ladies
                                - Knights/Dames
                                    - Esquires/Gentlefolk
- Visual Map: Use ASCII or diagram for quick reference in digital docs.

### 1.2 Rank Profiles
- Each rank includes: Title holders, role description, responsibilities, typical subordinates (with counts), economic/military capacity, architectural holdings, jurisdiction/legal authority.
- Example (Monarch):
    - Title Holders: King (male), Queen (female)
    - Role: Supreme sovereign, ultimate legislative, judicial, military authority.
    - Responsibilities: Enact laws, appoint nobles, oversee diplomacy, manage treasury, declare wars.
    - Subordinates: Prime Minister, Dukes, Chamberlain, Lord Chancellor, Archbishop, Court Mage, Royal Guard Commanders.
    - Economic/Military: Realm-wide land, income, forces.
    - Holdings: Capital palace, citadels, keeps.
    - Jurisdiction: Supreme court, foreign policy, justice.
- Repeat for all ranks (Prince, Duke, Marquess, Earl, Viscount, Baron, Lord, Knight, Esquire).

### 1.3 Cadet Branches & Royal Kin
- Senior Branch: Head of house, heir apparent, spares (younger sons/daughters).
- Cadet Branches: Founded by younger sons, hold lesser titles, serve in military/diplomatic roles.
- Daughters’ Lines: Marriage alliances, court roles, abbesses.
- Collateral Kin: Cousins, uncles, aunts, succession roles.
- Succession: Primogeniture, appanage, courtesy titles, extinction/elevation, marriage-based alliances.
- Heraldic/Naming: House name + territorial designation, marks of cadency, courtesy prefixes.
- Sample Genealogical Schema: House Ashvale (Dukedom, senior branch) → 1st Cadet (Earl) → 2nd Cadet (Viscount).

---

## 2. Glossary of Terms
### 2.1 Feudal & Administrative
- **Baron**: A noble ranking below a viscount and above a lord, governing manors and owing military service to higher peers.
- **Cadet Branch**: Secondary lineage of a noble house founded by younger sons; holds lesser titles and appanages but retains the family name and heraldry.
- **Castellan**: Governor or steward of a castle, responsible for defense and administration.
- **Chamberlain**: Officer managing private chambers, household staff, and finances of a noble or royal court.
- **Courtesy Title**: Style granted to non-inheriting children of peers (e.g., Lord, Lady) without substantive peerage rights.
- **Demesne**: Portion of a manor retained by the lord for personal use and income.
- **Fealty**: Sworn oath of loyalty and service that a vassal owes to their lord.
- **Peerage**: Body of noble ranks (duke, marquess, earl, viscount, baron) recognized by a realm’s monarchy.
- **Primogeniture**: Inheritance system in which the eldest child inherits the principal title and estates.
- **Vassal**: Person who holds land (fief) from a lord in exchange for military service, counsel, and fealty.

### 2.2 Ecclesiastical
- **Abbess**: Woman who heads a convent of nuns, exercising spiritual authority and managing monastic lands.
- **Bishop**: Senior church official overseeing a diocese, ordaining priests, and administering ecclesiastical courts.
- **Diocese**: Geographical area under the jurisdiction of a bishop.
- **Ecclesiastical**: Pertaining to the Christian Church, its offices, courts, and properties.
- **Inquisition**: Church court investigating and prosecuting heresy.

### 2.3 Magical & Fantasy
- **Archmage**: Premier wizard or magician, often serving as a royal advisor or head of an arcane order.
- **Bone Knight**: Undead or necromantically animated warrior serving a soullord or hexkeeper.
- **Dreamspeaker**: Noble who weaves dreams and governs mystical forests, commanding spirit herds.
- **Flamewarden**: Flame-affiliated guardian serving an elemental lord of fire.
- **Magelord of the Hearth**: Baron-level mage who protects villages with hearth magic and folk spells.

### 2.4 Technological & Sci-Fi
- **Data Baron**: Holds server farms, media fiefdoms.
- **Holo-Duke**: Commands mech battalions, quantum archives.
- **Mech Rider**: Pilots assault exosuits, drone squadrons.
- **Network Squire**: Junior sysadmin, code apprentices.
- **Planetary Overlord**: Controls interstellar fleets, data nexus.

### 2.5 Additional Glossary Categories
#### Political & Diplomatic
- **Regent**: Temporary ruler in place of a monarch.
- **Envoy**: Diplomatic representative.
- **Treaty**: Formal agreement between states or powers.
#### Legal & Administrative
- **Charter**: Legal document granting rights or privileges.
- **Edict**: Official order or proclamation.
#### Military & Warfare
- **Levy**: Summoning of troops for service.
- **Garrison**: Troops stationed at a fortress or town.
#### Economic & Trade
- **Tithe**: Tax or tribute, often paid to religious institutions.
- **Guild**: Organization of craftsmen or merchants.
#### Architecture & Fortification
- **Motte-and-Bailey**: Type of fortification with a raised earthwork and enclosed courtyard.
- **Citadel**: Stronghold or fortress.
#### Geography & Ecology
- **Province**: Administrative region.
- **Frontier**: Borderlands or edge of settled territory.
#### Religion & Theology
- **Pantheon**: Group of deities worshipped collectively.
- **Theocracy**: Government ruled by religious leaders.
#### Culture & Society
- **Festival**: Public celebration or holiday.
- **Bard**: Poet and musician, often a storyteller.
#### Magic System
- **Mana**: Magical energy source.
- **Grimoire**: Book of spells.
#### Craft & Guild
- **Blacksmith**: Craftsman who works with metal.
- **Alchemist**: Practitioner of chemical and magical transformation.
#### Genealogy & Heraldry
- **Crest**: Symbol representing a family or house.
- **Lineage**: Ancestral descent.
#### Time & Measurement
- **Era**: Distinct period in history.
- **League**: Unit of distance.

---

## 3. Feudal Obligations & Succession
- **Vassalage**: Each rank swears fealty to the one above in exchange for land and protection.
- **Military Aid**: Defined number of troops or years of service owed when summoned.
- **Taxation**: Annual tribute or levies proportional to income.
- **Marriage Alliances**: Strategic unions to consolidate lands, form military pacts, or secure succession.
- **Inheritance**: Primogeniture (eldest heir inherits majority), ultimogeniture or partible inheritance in select cultures, dowries and jointures for noblewomen.
- **Extinction of Senior Line**: Cadet branch “ripples up” to become the new senior line.
- **Elevation by Decree**: Kings can elevate a cadet branch as reward for loyalty or military service.

---

## 4. Economy & Trade
- **Currency types**: Gold, silver, copper coins; magical crystals; barter systems.
- **Denominations**: Mark, talent, denarius, etc.
- **Tax structures**: Tithes, tariffs, tolls, tribute.
- **Guilds**: Blacksmiths, merchants, alchemists, shipwrights.
- **Merchant companies**: Trade routes, caravans, market fairs.
- **Market mechanics**: Price variance tables, supply/demand, resource distribution.
- **Resource distribution**: Farms, mines, magical crystals, trade goods.

---

## 5. Geography & Regions
- **Biome definitions**: Forest, swamp, mountain, desert, archipelago, highlands, lowlands, vale, marsh, steppe.
- **Province/March boundaries**: Administrative regions, climate zones.
- **Landmark templates**: Ruins, portals, dragon lairs, citadels, abbeys.
- **Seasonal effects**: Weather, natural hazards, climate cycles.
- **Random region generation tables**: Templates for procedural world-building.

---

## 6. Culture & Society
### 6.1 Social Classes & Hierarchies
- Nobility: Monarchs, princes, dukes, marquesses, earls, viscounts, barons, lords, knights, esquires.
- Gentry: Landowners below peerage, including esquires and gentlefolk.
- Merchants: Guildmasters, traders, caravan leaders.
- Peasants: Farmers, laborers, serfs.
- Clergy: Priests, monks, nuns, abbots, bishops.
- Artisans: Blacksmiths, masons, tailors, alchemists, brewers, shipwrights.

### 6.2 Titles Beyond Nobility
- Guildmaster: Leader of a craft or merchant guild.
- Bishop/Abbot: Senior religious officials.
- Knight: Armigerous warrior, often landless.
- Bard: Entertainer, chronicler, and diplomat.

### 6.3 Festivals & Rituals
- Feast Days: Celebrations tied to religious or historical events.
- Tournaments: Martial competitions, jousts, archery contests.
- Coming-of-Age: Ceremonies marking adulthood.
- Coronations: Rituals for crowning monarchs or nobles.
- Religious Ceremonies: Seasonal rites, sacrifices, processions.

### 6.4 Sumptuary Laws & Dress Codes
- Regulations on clothing, jewelry, and luxury items by class.
- Examples: Only nobles may wear purple; knights may bear arms; merchants restricted in gold adornment.

### 6.5 Faction Archetypes
- Knightly Orders: Chivalric brotherhoods, defenders of realms.
- Thieves’ Guilds: Organized criminal networks, spies, fences.
- Merchant Companies: Trade consortiums, banking houses.
- Magical Societies: Arcane colleges, secret cabals, druidic circles.

### 6.6 Court Etiquette & Honor Codes
- Livery: Colors and symbols denoting allegiance.
- Coat of Arms: Heraldic devices for families and factions.
- Honor Codes: Rules of conduct, dueling, hospitality.
- Etiquette: Bowing, addressing ranks, gift-giving, audience protocols.

### 6.7 Intrigue Hooks & Diplomacy Mechanics
- Relationship Webs: Alliances, rivalries, family ties.
- Plot Twists: Betrayals, secret heirs, forbidden romances.
- Diplomacy: Negotiation, treaties, marriage alliances, espionage.

---

## 7. Religion & Pantheon
### 7.1 Deity Archetypes & Portfolios
- Creator: God of beginnings, life, and creation.
- Destroyer: God of endings, death, and chaos.
- Trickster: God of mischief, change, and luck.
- Healer: God of restoration, mercy, and health.
- War God: God of battle, valor, and conquest.
- Nature Spirit: God of forests, animals, and seasons.
- Custom Deities: Unique gods for factions, cultures, or regions.

### 7.2 Domains of Influence
- War, Healing, Magic, Nature, Knowledge, Trickery, Sun, Moon, Sea, Death, Life, Fate, Luck, etc.

### 7.3 Church Hierarchy & Organization
- Pope: Supreme religious leader.
- Archbishop: Oversees multiple dioceses.
- Bishop: Governs a diocese.
- Inquisitor: Investigates heresy and corruption.
- Priest: Leads local congregations.
- Monk/Nun: Lives in monastic communities.
- Abbess/Abbot: Heads a convent or monastery.

### 7.4 Ecclesiastical Courts & Heresy Trials
- Canon Law: Religious legal system.
- Sanctuary: Sacred protection from secular law.
- Heresy Trials: Procedures for investigating and punishing heresy.

### 7.5 Religious Orders & Monastic Houses
- Holy Knights: Paladins, templars, crusaders.
- Monastic Orders: Benedictine, Templar, Druidic, etc.
- Abbesses/Abbots: Spiritual and administrative leaders.

### 7.6 Divine Miracles & Sacred Sites
- Holy Relics: Artifacts imbued with divine power.
- Divine Intervention: Miraculous events, prophecies, visions.
- Sacred Sites: Temples, shrines, pilgrimage destinations.

---

## 8. Magic System
### 8.1 Schools & Traditions
- Arcane: Wizards, sorcerers, magelords, archmages.
- Divine: Clerics, paladins, druids, shamans.
- Primal: Nature magic, elementalists, spirit callers.
- Custom Traditions: Blood magic, rune magic, psionics, technomancy.

### 8.2 Mana/Energy Sources & Conduits
- Ley Lines: Magical currents running through the world.
- Aether: Universal magical energy.
- Sacred Sites: Places of power, nexuses, foci.
- Artifacts: Items that store or channel magical energy.

### 8.3 Spell Lists & Ritual Frameworks
- Spell Levels: Cantrips (0), 1st–9th level spells.
- Rituals: Extended casting, group participation, rare components.
- Sample Spells: Fireball, Healing Word, Scrying, Polymorph, Animate Dead.

### 8.4 Magical Hazards & Wild-Magic Tables
- Wild Magic Surges: Unpredictable magical effects.
- Magical Hazards: Cursed items, unstable portals, arcane storms.
- Corruption: Side effects of forbidden or powerful magic.

### 8.5 Artifact Creation & Sentient Items
- Crafting Rituals: Steps, materials, and costs for creating magic items.
- Sentient Items: Weapons, armor, or objects with personalities, goals, and powers.
- Attunement: Rules for bonding with powerful artifacts.

---

## 9. NPC & Character Templates
### 9.1 Stat-Block Archetypes
- Commoner: Basic stats, minimal skills.
- Guard: Trained in combat, loyal to employer.
- Merchant: Skilled in trade, negotiation, and appraisal.
- Noble: High social skills, leadership, resources.
- Knight: Martial prowess, code of honor.
- Mage: Spellcasting, arcane knowledge.
- Priest: Divine magic, healing, religious authority.
- Thief: Stealth, sleight of hand, deception.
- Archmage: Master of magic, rare and powerful.

### 9.2 Personality Tags & Motivations
- Tags: Brave, cowardly, greedy, loyal, vengeful, curious, wise, foolish, ambitious, merciful, ruthless.
- Motivations: Power, revenge, love, duty, faith, wealth, knowledge, survival, redemption.

### 9.3 Relationship Webs & Faction Ties
- Family: Blood relations, heirs, rivals.
- Factions: Guilds, orders, cults, political groups.
- Allies & Enemies: Friends, rivals, nemeses, patrons.

### 9.4 Signature Gear, Quirks, Voice Cues
- Gear: Unique weapons, armor, magical items, heirlooms.
- Quirks: Habits, speech patterns, superstitions, physical traits.
- Voice Cues: Sample dialogue, catchphrases, accents.

---

## 10. Creatures & Encounters
### 10.1 Monster Roles & Encounter Balance
- Roles: Brute (high damage, low defense), Controller (area effects, status), Skirmisher (mobility, hit-and-run), Lurker (stealth, ambush), Artillery (ranged damage), Leader (buffs allies).
- Encounter Balance: Use CR (Challenge Rating) or custom difficulty tiers. Mix roles for dynamic encounters. Include environmental hazards and objectives.

### 10.2 Unique Creature Templates
- Fey: Trickster spirits, nature guardians, illusionists.
- Aberrations: Eldritch horrors, mind-benders, reality warpers.
- Constructs: Golems, animated objects, clockwork beasts.
- Undead: Zombies, skeletons, wraiths, bone knights.
- Elementals: Fire, water, earth, air, stormcallers.
- Dragons: Chromatic, metallic, primal, ancient.
- Custom: Hybrid monsters, magical beasts, sci-fi variants.

### 10.3 Terrain-Based Random Encounter Tables
- Forest: Wolves, bandits, dryads, giant spiders.
- Swamp: Will-o-wisps, crocodiles, shambling mounds.
- Mountain: Griffons, stone giants, wyverns.
- Urban: Thieves, guards, cultists, constructs.
- Dungeon: Traps, oozes, undead, aberrations.

### 10.4 Boss/Solo Encounter Frameworks
- Boss Traits: Legendary actions, lair actions, resistances, minions.
- Encounter Phases: Change tactics, environment, or abilities as boss HP drops.
- Example: Dragon with lair traps, minions, breath weapon, phase change at 50% HP.

---

## 11. Magic Items & Artifacts
### 11.1 Rarity Tiers & Attunement Rules
- Common: Minor magical effects, easily found.
- Uncommon: Useful bonuses, limited availability.
- Rare: Powerful effects, require attunement.
- Very Rare: Unique abilities, story significance.
- Legendary: World-altering, sentient, quest items.
- Artifact: Unique, campaign-defining, often sentient.
- Attunement: Limit number of attuned items per character, require rituals or conditions.

### 11.2 Property Tables (Bonuses, Curses, Sentience)
- Bonuses: +1 to +3 to stats, resistances, skill boosts.
- Curses: Drawbacks, compulsions, hidden effects.
- Sentience: Personality, goals, communication, alignment.

### 11.3 Origin & Lore Hooks
- Creation: Forged by gods, ancient wizards, lost civilizations.
- History: Past owners, famous deeds, legends.
- Lore Hooks: Quests to find, restore, or destroy items.

### 11.4 Crafting Recipes & Enchantment Rituals
- Materials: Rare metals, monster parts, magical reagents.
- Rituals: Multi-step processes, group participation, skill checks.
- Example: Sword of Flames (requires fire elemental heart, dwarven forge, three nights of ritual).

---

## 12. Dungeons & Sites
### 12.1 Blueprint Templates
- Room Types: Entry hall, guard post, treasure vault, prison, library, laboratory, shrine, boss chamber.
- Traps: Pitfalls, poison darts, magical glyphs, collapsing ceilings, alarm spells.
- Treasure: Gold, gems, magic items, lore documents, keys.

### 12.2 Dungeon Generation Tables
- Layout: Linear, branching, maze, hub-and-spoke.
- Themes: Undead crypt, arcane tower, natural cave, lost temple, sci-fi facility.
- Encounter Density: Sparse, moderate, packed.

### 12.3 Environmental Storytelling Elements
- Clues: Bloodstains, broken weapons, murals, journals, magical echoes.
- Hazards: Flooded chambers, unstable floors, magical storms, darkness.
- NPCs: Prisoners, ghosts, rival adventurers, shopkeepers.

### 12.4 Pacing & Milestone XP Models
- Pacing: Mix combat, puzzles, exploration, roleplay.
- Milestone XP: Level up at key story points, boss defeats, major discoveries.

---

## 13. Random Tables & Generators
### 13.1 Name Generators
- People: Syllable tables, cultural lists, noble/fantasy/sci-fi variants.
- Places: Prefix/suffix tables, terrain-based names, historical/fantasy/sci-fi.
- Items: Weapon types, magical properties, artifact names.

### 13.2 Quest Hooks & Plot Twist Tables
- Hooks: Rescue, theft, betrayal, prophecy, lost artifact, forbidden love, monster hunt.
- Twists: Secret villain, double agent, cursed reward, time travel, mistaken identity.

### 13.3 Weather, Event, and Rumor Tables
- Weather: Clear, rain, storm, fog, magical phenomena.
- Events: Festivals, disasters, invasions, omens, royal decrees.
- Rumors: Hidden treasure, monster sightings, political intrigue, prophecy.

### 13.4 Treasure & Loot Distribution Matrices
- Common: Coins, mundane gear, minor potions.
- Uncommon: Magic scrolls, enchanted weapons, rare gems.
- Rare: Unique items, sentient artifacts, legendary gear.
- Distribution: By encounter difficulty, location, story relevance.

---

## 14. Timeline & World History
### 14.1 Epochs & Eras
- Ancient Age: Creation myths, primordial gods, first civilizations.
- Classical Age: Rise of empires, magic discovery, legendary heroes.
- Dark Age: Collapse, wars, plagues, forbidden magic.
- Renaissance: Rebirth, innovation, rediscovery of lost lore.
- Modern/Future Age: Technological/magical fusion, interplanetary travel, AI governance.

### 14.2 Key Historical Events & Turning Points
- Founding of kingdoms, dynasties, and cities.
- Cataclysms: Meteor strikes, magical disasters, divine intervention.
- Wars: Succession crises, invasions, revolutions.
- Discoveries: New continents, magical schools, artifacts.

### 14.3 Royal Dynasties & Succession Crises
- Family trees, notable rulers, famous heirs.
- Extinction events, civil wars, branch elevation.

### 14.4 Cultural Renaissances & Dark Ages
- Golden ages of art, science, magic.
- Periods of decline, oppression, lost knowledge.

---

## 15. DM Reference & Style Guide
### 15.1 Narration Tone & Pacing Tips
- Tone: Match setting (epic, grimdark, whimsical, mysterious).
- Pacing: Alternate action, exploration, roleplay, downtime.
- Read-aloud text: Prepare evocative scene descriptions, NPC dialogue, sensory details.

### 15.2 Handling Improv & Player Agency
- Improv: Use random tables, NPC quirks, plot twists for spontaneity.
- Player Agency: Let choices shape story, world, and outcomes.
- Memory: Track NPC knowledge, world state, consequences.

### 15.3 Managing NPC Memory & World State
- NPC Memory: Record relationships, secrets, past actions.
- World State: Track political changes, wars, magical events, economy.
- Session Logs: Summarize events, decisions, unresolved hooks.

### 15.4 Session Flow Templates & Read-Aloud Text
- Session Template: Opening recap, scene setup, encounter, downtime, closing summary.
- Read-Aloud: Sample intros, room descriptions, NPC greetings, quest hooks.

---

## 16. Appendices
### 16.1 Abbreviations & Symbols
- STR: Strength
- DEX: Dexterity
- CON: Constitution
- INT: Intelligence
- WIS: Wisdom
- CHA: Charisma
- CR: Challenge Rating
- XP: Experience Points
- NPC: Non-Player Character
- PC: Player Character
- DM: Dungeon Master

### 16.2 Conversion Charts
- Distance: 1 mile = 1.6 km, 1 league = ~3 miles
- Weight: 1 pound = 0.45 kg, 1 stone = 14 pounds
- Currency: 1 gold = 10 silver = 100 copper

### 16.3 Sample Genealogies, Maps, and Diagrams
- Genealogy: Example family tree for House Ashvale
- Map: Sample kingdom map with regions, cities, landmarks
- Diagram: Noble hierarchy, magical ley lines, dungeon layouts

### 16.4 Cross-Reference Index
- Link terms, rules, and templates to relevant sections for quick lookup
- Example: "See also: Primogeniture (Section 1.3), Succession Crises (Section 14.3), Attunement (Section 11.1)"

---

## 17. Core System Mechanics (Stats, Skills, Spells & Schools)
### 17.1 Ability Scores
- Strength (STR): Physical power, carrying capacity, melee damage
- Dexterity (DEX): Agility, reflexes, ranged attacks, stealth
- Constitution (CON): Health, stamina, resilience, hit-points
- Intelligence (INT): Reasoning, memory, arcane knowledge, investigation
- Wisdom (WIS): Perception, insight, willpower, survival
- Charisma (CHA): Force of personality, social interaction, leadership
- Mechanics: Scores range 1–20 for PCs (modifiers –5 to +5). Checks, saves, and skills use these modifiers.

### 17.2 Skills & Proficiencies
- Acrobatics (DEX): Tumbling, balance
- Animal Handling (WIS): Calming beasts, riding
- Arcana (INT): Magical lore, spell identification
- Athletics (STR): Climbing, jumping, swimming
- Deception (CHA): Lying, disguise
- History (INT): Lore, events
- Insight (WIS): Motives, lies
- Intimidation (CHA): Threats, coercion
- Investigation (INT): Clues, hidden doors
- Medicine (WIS): Healing, diagnosis
- Nature (INT): Plants, animals, weather
- Perception (WIS): Traps, sounds, hidden foes
- Performance (CHA): Entertainment, rituals
- Persuasion (CHA): Negotiation, leadership
- Religion (INT): Theology, rituals
- Sleight of Hand (DEX): Pickpocketing, tricks
- Stealth (DEX): Hiding, sneaking
- Survival (WIS): Tracking, foraging
- Proficiencies: Skills, tools, weapons, armor. Proficient characters add proficiency bonus.

### 17.3 Spells & Schools of Magic
- Schools: Abjuration (protection), Conjuration (summoning), Divination (prophecy), Enchantment (charm), Evocation (damage), Illusion (deception), Necromancy (life/death), Transmutation (alteration)
- Spell Structure: Name, level, school, casting time, range, components, duration, effect
- Example: Fireball (Evocation, 3rd level, 1 action, 150 ft, VSM, instant, 8d6 fire damage)

### 17.4 Classes & Archetypes
- Barbarian: STR, CON; tank, rage
- Bard: CHA, INT; support, skills
- Cleric: WIS, CHA; healer, divine
- Druid: WIS, CON; nature, shapeshifting
- Fighter: STR/DEX, CON; martial
- Monk: DEX, WIS; unarmed, ki
- Paladin: STR, CHA; tank/healer
- Ranger: DEX, WIS; hunter, ranged
- Rogue: DEX, INT/CHA; stealth, damage
- Sorcerer: CHA; arcane power
- Warlock: CHA; pact magic
- Wizard: INT; spell variety
- Archetypes: Subclasses grant unique features at key levels

### 17.5 Feats & Traits
- Feats: Optional abilities (Sharpshooter, War Caster)
- Racial Traits: Unique abilities by race (darkvision, innate spells)
- Background Features: Roleplaying bonuses (tool proficiency, contacts)

### 17.6 Conditions & Status Effects
- Blinded, Charmed, Deafened, Frightened, Grappled, Incapacitated, Paralyzed, Poisoned, Prone, Restrained, Stunned, Unconscious
- Effects: Advantage/disadvantage, movement, actions, saves

### 17.7 Saving Throws
- STR: Restraints, pushes
- DEX: Area effects, traps
- CON: Poisons, exhaustion
- INT: Illusions, domination
- WIS: Fear, deception
- CHA: Banishment, charm
- Mechanics: 1d20 + modifier + proficiency (if proficient)

### 17.8 Proficiency Bonus & Level Progression
- Bonus: +2 (1–4), +3 (5–8), +4 (9–12), +5 (13–16), +6 (17–20)
- Milestones: Ability score increases, class upgrades

### 17.9 Tool Proficiencies & Languages
- Tools: Artisan’s, gaming sets, musical instruments, thieves’, herbalism, alchemist’s, navigator’s, disguise
- Languages: Common, Dwarvish, Elvish, Draconic, Giant, Halfling, Orc, Abyssal, Celestial, Infernal, custom

### 17.10 Backgrounds & Background Features
- Backgrounds: Acolyte, Criminal, Folk Hero, Noble, Sage, Soldier, Entertainer, Guild Artisan, Hermit, Outlander
- Features: Shelter of the Faithful, Criminal Contact, Rustic Hospitality, Position of Privilege, Researcher, Military Rank, By Popular Demand, Guild Membership, Discovery, Wanderer
- Custom: Faction, religion, culture backgrounds

### 17.11 Inspiration, Luck & Variant Ability Systems
- Inspiration: Hero point for roleplay, spend for advantage
- Luck Points: Pool for rerolls (optional)
- Ability Variants: Point buy, standard array, rolling, homebrew attributes, skill specialization

### 17.12 Advancement Milestones & XP Models
- XP Model: Level thresholds (1: 0, 2: 300, 3: 900, ... 20: 355,000)
- Milestone: Level up at story/session milestones
- Variants: Milestone only, tiered XP, downtime XP

---

## Summary & Next Steps
This document now provides a unified, exhaustive reference for procedural world generation and AI-driven DM support. Continue to fill in missing content, cross-link related sections, and update as the project evolves. Refer to copilot-instructions.md for coding and implementation guidelines.

# End of Document

