from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://UP:UP@cluster0.5mfpimz.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "6f3a051b5da7f5b499cde019d273fca1"]
        API_ID = [int, 5503927]
        BOT_TOKEN = [str, "5169251234:AAGc9n1hL1c99jfm7h9YsajHz-onsKdlSO4"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, True]
        AUTH_USERS = [list,[773325066 326350464]]
        OWNER_ID = [int, 773325066]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int,-1001557727149]

        TRACE_CHANNEL = [int, -1001639591381]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
