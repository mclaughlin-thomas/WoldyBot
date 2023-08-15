import discord
import os
import csv
import random

phrases = []
with open("quotes.csv") as csv_file:
  csv_reader = csv.reader(csv_file)
  for row in csv_reader:
    phrases.append(row[1])
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f"{client.user} is logged in!")


@client.event
async def on_message(message):
  if message.content.startswith("*hi"):
    await message.channel.send("Hello! I am Woldy bot!")

  elif "*inspire" in message.content:
    command_args = message.content[len("*inspire"):].strip()

    if not command_args:
      response = phrases[random.randint(0, len(phrases) - 1)]

      await message.channel.send(response)
    else:
      response = phrases[random.randint(0, len(phrases) - 1)]
      mentioned_user = message.author

      await message.channel.send(
        f"Hey there {command_args}, heres a quote from your pal {mentioned_user.mention} to give you some motivation: \n "
      )
      await message.channel.send(response)

  elif "*squad" in message.content:
    command_args = message.content[len("*squad"):].strip()

    if not command_args:
      await message.channel.send("Lets squad up baby!")
    else:
      await message.channel.send(
        f"{command_args}! Lets squad up baby! Get in the game {command_args}!"
      )
  elif message.content.startswith('*kick'):
    command_args = message.content[len('*kick'):].strip()
    mentioned_members = message.mentions

    if len(mentioned_members) == 0:
      await message.channel.send("No members mentioned to kick.")
    else:
      for member in mentioned_members:
        if message.author.guild_permissions.kick_members:
          if member.guild_permissions.administrator:
            await message.channel.send("You can't kick an administrator.")
          else:
            await member.kick()
            await message.channel.send(f"{member.mention} has been kicked.")
        else:
          await message.channel.send(
            "You don't have the required permissions to use this command.")


my_secret = os.environ['TOKEN']
client.run(my_secret)
