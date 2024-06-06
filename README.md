# TS4 The Paralysed Android Doll
This is a tiny and incomplete alpha mod release without any pie menu interactions.

It has two cheat commands:
* `o19.android.add` adds some buffs and traits to the active sims to avoid most interactions. Use the 'Control Menu' cheat to control any NPC.
Other sims can still use autonomy to interact with this sim.
The sim can no longer get pregnant or impregnate other sims. The pie menu to execute actions still works for the sim while active.
* `o19.android.control` tries to remove a few buffs and traits to allow to interact with the sim.

There is no `undo` command so one needs to remove buffs and traits manually to 'restore' the sim as a normal sim.

Only tested with adult human sims while it should also work for younger and/or animal sims.

### Known Issues
* Some interactions never complete.
* Some buffs / traits are not properly saved / loaded.

### Missing (not yet planned) features:
* Disable all pie menu interactions for the sim.
* Block all autonomy actions of other sims towards this sim.
* Add 'Hide in closet' interaction to get rid of the sim temporarily.
* Copy a few 'Au Pair' mod features:
  * Menu to request that the sim performs an interaction.
  * Menu to schedule that the sim performs an interaction at the specified time.
  * Set spawn location for the sim.

##### Added Buffs and Traits
* trait_GenderOptions_Pregnancy_CanNotImpregnate
* trait_GenderOptions_Pregnancy_CanNot_BeImpregnated
* trait_Cauldron_Potion_Immortality
* trait_Hidden_ChildCannotAgeUp_DoesNotPersist
* buff_NoGreetings
* buff_NPC_Suppress_All_Motive_Decay
* buff_Suntan_LockDecay
* buff_Trait_SpeedCleaner
* buff_Trait_SpeedReader
* buff_Suppress_*


# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.107.112, S4CL 3.4, TS4Lib 0.3.20 (2024-05).
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2024 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
