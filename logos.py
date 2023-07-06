import requests
import teams

def download_team_logos(team_ids):
    for id in team_ids:
        url = f"https://www.mlbstatic.com/team-logos/{id}.svg"
        response = requests.get(url)

        if response.status_code == 200:
            with open(f"logo_{id}.svg", 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download logo for team id: {id}")