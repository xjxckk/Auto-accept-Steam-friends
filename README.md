# Automatically accept Steam friend requests and optionally send them a message.

## Installation
You will need Python & the [Steam python library](https://github.com/ValvePython/steam) installed.

## How to use
* Download the respository as a zip file and extract it to a folder.
* Open the config.txt file and replace "username" with your Steam username and "password" with your Steam password.
* Replace "shared_secret" with your shared secret and "identity_secret" with your identity secret.
* Replace "Hey, what's up" with the message you want sent or delete it or leave it blank for no message.
* Enjoy!

How to get your shared and identity secret: https://github.com/SteamTimeIdler/stidler/wiki/Getting-your-%27shared_secret%27-code-for-use-with-Auto-Restarter-on-Mobile-Authentication

## To run in the background
Create a shortcut to "Steam Bot.vbs" and add it to your startup folder.

## To improve
* Add auto responding to certain [messages](https://steam.readthedocs.io/en/latest/api/steam.client.html#steam.client.SteamClient.EVENT_CHAT_MESSAGE).
