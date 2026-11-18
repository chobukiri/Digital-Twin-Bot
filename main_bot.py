# main_bot.py
import discord
import requests

from config import DISCORD_BOT_TOKEN
from config import GITHUB_TOKEN
from config import GITHUB_USERNAME
from database import supabase  # <-- NEW: Imports your cloud database connection

# 1. Enable Privileged Intents
intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True

# 2. Initialize the client
client = discord.Client(intents=intents)

# 3. Connection confirmation
@client.event
async def on_ready():
    print(f"✅ Digital Twin Bridge is ONLINE!")
    print(f"Logged in successfully as {client.user}")

# 4. Message handling
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 1. Status Command
    if message.content.startswith('!status'):
        await message.channel.send("🟢 System Online. Supabase Connected.")

    # 2. Log Command
    if message.content.startswith('!log '):
        log_text = message.content[5:] 
        try:
            supabase.table("analytics_log").insert({"event_type": "Discord Command", "topic_tag": log_text}).execute()
            await message.channel.send(f"💾 Logged to Analytics: `{log_text}`")
        except Exception as e:
            await message.channel.send(f"❌ Database error: {e}")

    # 3. Journal Command
    if message.content.startswith('!journal '):
        raw_content = message.content[9:] 
        parts = [piece.strip() for piece in raw_content.split('|')]
        if len(parts) != 3:
            await message.channel.send("⚠️ **Format Error.** Use: `!journal Phase | Concept | Learnings`")
            return
        try:
            supabase.table("engineering_journal").insert({
                "development_phase": parts[0],
                "core_concept": parts[1],
                "key_learnings": parts[2]
            }).execute()
            await message.channel.send(f"📓 **Journal Entry Secured!**\n**Phase:** {parts[0]}")
        except Exception as e:
            await message.channel.send(f"❌ Database error: {e}")

    # 4. Vault Command
    if message.content.startswith('!vault '):
        raw_content = message.content[7:] 
        parts = [piece.strip() for piece in raw_content.split('|')]
        if len(parts) != 3:
            await message.channel.send("⚠️ **Format Error.** Use: `!vault Language | Code | Summary`")
            return
        try:
            supabase.table("code_vault").insert({
                "language": parts[0],
                "code_snippet": parts[1],
                "ai_summary": parts[2]
            }).execute()
            await message.channel.send(f"🔐 **Code secured in the Vault!**\n**Language:** {parts[0]}")
        except Exception as e:
            await message.channel.send(f"❌ Database error: {e}")

    # 5. GitHub Command
    if message.content.startswith('!github '):
        repo_name = message.content[8:].strip() 
        
        # Authenticate with GitHub
        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/commits'
        
        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                commits = response.json()
                latest_commit = commits[0]['commit']['message']
                commit_url = commits[0]['html_url']
                
                # Push the GitHub data directly into your Supabase Vault
                supabase.table("code_vault").insert({
                    "language": "GitHub Update",
                    "code_snippet": commit_url,
                    "ai_summary": f"Latest commit in {repo_name}:\n{latest_commit}"
                }).execute()
                
                await message.channel.send(f"🐙 **GitHub Synced!** Logged latest commit for `{repo_name}` to the Vault.")
            else:
                await message.channel.send(f"⚠️ **GitHub Error {response.status_code}:** Could not find a repository named `{repo_name}`.")
                
        except Exception as e:
            await message.channel.send(f"❌ Connection error: {e}")

client.run(DISCORD_BOT_TOKEN)