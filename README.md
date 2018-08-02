# Weapon Comparator

This is a tool for Warhammer 40K Kill Teams.

It is designed to answer questions like:

"If my Tau Pathfinder Gunner is shooting at a Tyranid Warrior, should I take a Rail Rifle or an Ion Rifle?"

or 

"What is the optimal weapon for my Necron Immortals when attacking Primaris Marines?"

or 

"What is the expected number of unsaved wounds for a Nemesis Falchion across all 
 Toughness/Armor pairs?"

We plan on incorporating conditions like:

* The range (if shooting)
* Any penalties, for example from flesh wounds
* Any tactics being used
* Special properties of weapons 

# Installing

Clone the directory to your local workspace, change dirs to `~/weapon_comparator/` and install with: 

```
$    pip install .
```

# Testing

To run unit tests change dirs to `~/weapon_comparator/weapon_comparator/` and run:

```
$    python -m unittest discover -vvv
```

or if you have the `pytest` package:

```
$    python -m pytest
```

# Usage 

To see some example useage look in: `weapon_comparator/bin/workbook.py`

# To do:

* Build a weapon comparison tool 
    * for the given weapons compute the array for expected unsaved wounds and expected damage
    * give the best weapon for each S/T and some summaries
    * give the rankings for each S/T

* Add all weapon profiles

* Define some units
    * Can be used to generate a weighted average
        * or to select the best weapon versus this foe

* compute probability of knocking out

* Evaluate weapon:
    * Input: weapon, wielder, target, conditions/modifiers
    * Output: expected damage, probability unsaved wound, expected number of unsaved wounds 

* Compare weapons:
    * Input: weapon(s), wielder(s), target, conditions/modifiers (for each wielder?)
    * Output: evaluate weapon for each, rank the weapons according to output

* Get optimal weapon for target
    * Input: wielder, target, [weapons to choose from], conditions/modifiers
    * Return the weapon with the highest expected damage against the target. 
      If no weapons input then do all valid weapons for wielder split by ranged/melee/overall 

* Create an tutorial either raw script or ipython notebook or both. 