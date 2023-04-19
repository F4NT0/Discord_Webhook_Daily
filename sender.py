from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import json
import sys
import datetime

##########
# MESSAGE
##########

# Set the webhook URL and message content
#webhook_url = input("Enter the webhook code: ")
webhook_url = sys.argv[1]
message = "@everyone NÃO ESQUEÇAM DA DAILY DE SEXTA"

# Create a webhook object
webhook = DiscordWebhook(url=webhook_url)

# Create an embed object and add it to the webhook
embed = DiscordEmbed(title="DAILY DE SEXTA", description=message)
webhook.add_embed(embed)

# Send the message to Discord using the webhook
response = webhook.execute()

# Print the response from Discord
print(response)

#########
# THREAD
#########

# get the ID from the last message on channel
channel_id = "1083766453028786317"
api_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
bot_code = sys.argv[2]

headers = {
    "Authorization": f"Bot {bot_code}"
}

params = {
    "limit": 1
}

response = requests.get(api_url, headers=headers, params=params)
message_id = response.json()[len(response.json())-1]["id"]

# get current date
current_date = datetime.datetime.today()
brazilian_date = current_date.strftime("%d/%m/%Y")

# create a thread
thread_data = {
    "name": f"DAILY DE SEXTA - {brazilian_date}",
    "type": 11,
    "auto_archive_duration": 1440
}
json_data = json.dumps(thread_data)
api_thread = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/threads"
header_thread = {
    "content-type": "application/json",
    "Authorization": f"Bot {bot_code}"
}
data = json_data
respose_thread = requests.post(api_thread, headers=header_thread, data=data)