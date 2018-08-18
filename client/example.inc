/*
    @Author: dy1zan
    @Command: !a
    This callback is invoked whenever someone types !a in Discord.
    This will send an admin chat message in-game, of the message sent from Discord.
*/
DiscordResponse::say(data[]) {
    //Convert string into JSON object so we can extract data e.g sender, message
    new JSONNode:jsonData = json_parse_string(data);

    new sender[MAX_PLAYER_NAME+1], message[110];
    //Get the 'sender'/'message' contained within the JSON object
    json_get_string(jsonData, sender, sizeof sender, "sender");
    json_get_string(jsonData, message, sizeof message, "message");
    
    //Output the data
    new string[144];
    format(string, sizeof string, "** [Discord] %s: %s **", sender, message);
    printf(string);
    SendClientMessageToAll(0xFEB918FF, string);
    return 1;
}