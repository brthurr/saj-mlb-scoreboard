import json
import requests
import teams
from PIL import Image
import cairosvg
from io import BytesIO

def get_unique_team_ids():
    # Load the schedule from the JSON file
    with open('schedule.json', 'r') as f:
        games = json.load(f)

    # Create a set to store the unique team ids
    team_ids = set()

    # Loop through each game
    for game in games:
        # Extract the team ids and add them to the set
        team_ids.add(game['home_id'])
        team_ids.add(game['away_id'])

    return team_ids

def download_team_logos(team_ids):
    for id in team_ids:
        url = f"https://www.mlbstatic.com/team-logos/{id}.svg"
        response = requests.get(url)
        if response.status_code == 200:
            out = BytesIO()
            cairosvg.svg2png(url=url, write_to=out)
            out.seek(0)
            img = Image.open(out)
            img = img.crop(img.getbbox())
            img.save(f"logo_{id}.png")
        else:
            print(f"Failed to download logo for team id: {id}")

unique_team_ids = get_unique_team_ids()
download_team_logos(unique_team_ids)
