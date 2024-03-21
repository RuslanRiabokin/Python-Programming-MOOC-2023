import json

def read_json(file_name):
    with open(file_name) as f:
        data = json.load(f)
    return data

def search_player(data, name):
    for player in data:
        if player['name'] == name:
            return player
    return None

def list_team_abbreviations(data):
    teams = set(player['team'] for player in data)
    return sorted(teams)

def list_country_abbreviations(data):
    countries = set(player['nationality'] for player in data)
    return sorted(countries)

def list_players_by_points_in_team(data, team):
    team_players = [player for player in data if player['team'] == team]
    team_players.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)
    return team_players

def list_players_by_points_from_country(data, country):
    country_players = [player for player in data if player['nationality'] == country]
    country_players.sort(key=lambda x: x['goals'] + x['assists'], reverse=True)
    return country_players

def list_top_players_by_points(data, n):
    data.sort(key=lambda x: (x['goals'] + x['assists'], x['goals']), reverse=True)
    return data[:n]

def list_top_players_by_goals(data, n):
    data.sort(key=lambda x: (x['goals'], -x['games']))
    return data[:n]

def print_player_stats(player):
    name = player['name']
    team = player['team']
    goals = player['goals']
    assists = player['assists']
    points = goals + assists
    print(f"{name:<20} {team:<3} {goals:2} + {assists:2} = {points:3}")


def main():
    file_name = input("file name: ")
    data = read_json(file_name)
    print(f"read the data of {len(data)} players\n")

    while True:
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

        command = input("\ncommand: ")

        if command == '0':
            break
        elif command == '1':
            name = input("name: ")
            player = search_player(data, name)
            if player:
                print_player_stats(player)
            else:
                print("Player not found.")
        elif command == '2':
            teams = list_team_abbreviations(data)
            for team in teams:
                print(team)
        elif command == '3':
            countries = list_country_abbreviations(data)
            for country in countries:
                print(country)
        elif command == '4':
            team = input("team: ")
            team_players = list_players_by_points_in_team(data, team)
            for player in team_players:
                print_player_stats(player)
        elif command == '5':
            country = input("country: ")
            country_players = list_players_by_points_from_country(data, country)
            for player in country_players:
                print_player_stats(player)
        elif command == '6':
            n = int(input("how many: "))
            top_players = list_top_players_by_points(data, n)
            for player in top_players:
                print_player_stats(player)
        elif command == '7':
            n = int(input("how many: "))
            top_goal_scorers = list_top_players_by_goals(data, n)
            for player in top_goal_scorers:
                print_player_stats(player)
        else:
            print("Invalid command. Please try again.")


main()
