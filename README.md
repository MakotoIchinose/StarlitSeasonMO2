# StarlitSeasonMO2
This is a Mod Organizer 2 plugin that adds support for THE IDOLM@STER STARLIT SEASON.

As I also play a lot of Bethesda games and use Mod Organizer 2, I have the idea to make my own mod organizer for Starlit Season.
However, I'm struggling to get I/O and virtual folder system in place, so instead I make plugin for MO2 to save my sanity.

## Installation
Simply download the Python file, and put it inside the Mod Organizer's plugin directory:
`<path to MO2>\plugins\basic_games\games`

[Also available on GameBanana.](https://gamebanana.com/mods/465148)

## Mod Installation

As this plugin simply adds support for Starlit Season in MO2, the same steps
[outlined in this guide](https://stepmodifications.org/wiki/Guide:Mod_Organizer#First-Launch_Setup) applies here.

However, most Starlit Season mods originated from GameBanana, thus missing direct Nexus Mods download feature and ability to check for updates,
but you're still able to drag and drop the archive into MO2 and proceed as necessary. Mods made before this plugin's publishing may also not
taking advantage of MO2's metadata features, listing version and category.

## Workings
This plugin uses MO2 to create virtual directory for `~mods`, which is expected

## Caveats
- Saves tab does not do anything, as the game stores save slots into a single .sav file, making it pointless even if it actually reads sav files.
- Conflict checking is not supported as most of the mods are packaged inside .pak/.sig files and not as loose .uasset/.uexp files. Always test the mods once you install them.

## License

BSD 3-Clause License
