#include <discord>

/*
    Setup:
        * include this file into some gamemode,
        * adjust the channel IDs to some channel you have access to.
*/
/* ====================================================================
    Discord colour definitions here only please
=======================================================================*/
#define DISCORD_COLOR_INFO 0x58aecb

/* ====================================================================
    Channel definitions here only please
=======================================================================*/
#define DISCORD_ADMINCHAT_CHANNEL   "46447385567455485"


//=====================================================================

Hook:Discord_OnGameModeInit() {
    discord_connect("127.0.0.1", 7778);
    return 1;
}

Hook:Discord_OnGameModeExit() {
    discord_disconnect();
    return 1;
}


/* ====================================================================
    Include any files containing message types e.g what should the
    server do when !admins is sent on Discord?
=======================================================================*/
#include "inc/discord/example.inc"

//=====================================================================
