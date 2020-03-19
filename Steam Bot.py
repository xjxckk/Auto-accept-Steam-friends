import gevent.monkey
gevent.monkey.patch_socket()
gevent.monkey.patch_ssl()
from steam import guard
from steam.client import SteamClient
from steam.enums import EResult

print("\nSteam Bot")
print("-"*20)

config = open("config.txt", "r+").read().splitlines()

secrets = {'shared_secret': config[5], 'identity_secret': config[7]}

SA = guard.SteamAuthenticator(secrets)

client = SteamClient()

@client.on("error")
def handle_error(result):
    print("\nError", result)

@client.on("connected")
def handle_connected():
    print("Logged on as", user)
    print("Auto accept friend requests is enabled.")
    print("Auto message is enabled.")
    print("-"*20)
    print("Press Ctrl + C to exit")

@client.on("reconnect")
def handle_reconnect(delay):
    print("\nReconnect in", delay, "seconds...\n")

@client.on("disconnected")
def handle_disconnect():
    print("\nDisconnected.")
    if client.relogin_available:
        print("\nReconnecting...")
        client.reconnect(maxdelay=30)

@client.friends.on("friend_invite")
def accept_invite(user):
    client.friends.add(user)
    if user.name == None:
        print("\nAdded:", user.steam_id)
    else:
        print("\nAdded:", user.name)
    gevent.sleep(2)
    user.send_message(config[9])

try:
    result = client.login(username=config[1], password=config[3], two_factor_code=SA.get_code())

    if result != EResult.OK:
        print("Failed to login:", repr(result))
        raise SystemExit
    
    client.run_forever()

except KeyboardInterrupt:
    if client.connected:
        print("Logout")
        client.logout()
    raise SystemExit