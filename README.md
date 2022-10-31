# ting tuan zi (聽團仔) discord bot
一個聽團仔專用的discord bot，後端API在https://github.com/asd24684782/ting-tuan-zi-api
## Discord Bot Cmd

### select festival in 7 days
```
.f
```

### select festival by id
```
.fid [id]
```

### select festival is free
```
.free
```

### select festival with band
```
.fband [band]
```


## Creat bot
source https://discordpy.readthedocs.io/en/stable/discord.html
1. go https://discord.com/developers/applications and click New application  
![My image](https://discordpy.readthedocs.io/en/stable/_images/discord_create_app_button.png)
2. Create a Bot User by navigating to the “Bot” tab and clicking “Add Bot”.  
![](https://discordpy.readthedocs.io/en/stable/_images/discord_create_bot_user.png)
3. Make sure that Public Bot is ticked if you want others to invite your bot.  
![](https://discordpy.readthedocs.io/en/stable/_images/discord_bot_user_options.png)

## Inviting bot

1. Click on your bot’s page.

2. Go to the “OAuth2” tab.

3. OAuth2 page look like.  
![](https://discordpy.readthedocs.io/en/stable/_images/discord_oauth2.png)
4. Tick the “bot” checkbox under “scopes”.  
![](https://discordpy.readthedocs.io/en/stable/_images/discord_oauth2_scope.png)
5. Tick the permissions required for your bot to function under “Bot Permissions”.  
![](https://discordpy.readthedocs.io/en/stable/_images/discord_oauth2_perms.png)
6. Now the resulting URL can be used to add your bot to a server. Copy and paste the URL into your browser, choose a server to invite the bot to, and click “Authorize”.
7. Add new file `.env` in src/setting and add this line in file
```
DISCORD_TOKEN=YOUR_TOKEN
```
