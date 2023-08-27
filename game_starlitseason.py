from ..basic_game import BasicGame


class StarlitSeasonGame(BasicGame):

    Name = "Starlit Season Support Plugin"
    Author = "IchinoseP"
    Version = "1.0.0"

    GameName = "THE IDOLM@STER STARLIT SEASON"
    GameShortName = "StarlitSeason"
    GameBinary = "StarlitSeason\Binaries\Win64\StarlitSeason-Win64-Shipping.exe"
    GameLauncher = "StarlitSeason.exe"
    GameDataPath = "%GAME_PATH%\StarlitSeason\Content\Paks\~mods"
    GameDocumentsDirectory = "%LocalAppData%\StarlitSeason\Saved\SaveGames\76561198296772315"
    GameSaveExtension = "sav"
    GameSteamId = 1046480