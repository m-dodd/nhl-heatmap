import requests
import json
import datetime


base_url = "https://statsapi.web.nhl.com/api/v1/"

#rest_call = "GET"


def get(end_point, params=None):
    url = base_url + end_point
    #print(url + str(params))
    response = requests.get(url, params=params)
    #print(response)
    #print(json.dumps(response.json(), indent=4, sort_keys=True))
    return response.json()


def get_teams():
    teams = get('teams')


def get_seasons():
    seasons = get('seasons')


def get_season_game_ids(season, game_type):
    x = [str(season) + game_type + str(n).zfill(4) for n in range(1, 1218)]
    return x


# def get_game_live(year):
#     ids = get_season_game_ids(year, '02')
#     games = [get('game/' + ids[i] + '/feed/live') for i in range(len(ids))]
#     return games
def get_game_live(game_id):
    game = get('game/' + game_id + '/feed/live')
    return game


# def get_game_boxscore(year):
#     ids = get_game_ids(year, '02')
#     games = [get('game/' + ids[i] + '/boxscore') for i in range(len(ids))]
#     return games
def get_game_boxscore(game_id):
    return get('game/' + game_id + '/boxscore')


# def get_game_linescore(year):
#     ids = get_game_ids(year, '02')
#     games = [get('game/' + ids[i] + '/linescore') for i in range(len(ids))]
#     return games

def get_game_linescore(game_id):
    return get('game/' + game_id + '/linescore')


def get_schedule(start_date, end_date):
    params = {"startDate": start_date, "endDate": end_date}
    schedule = get('schedule', params)
    return schedule


# def get_game_data(start_date, end_date):
#     schedule = get_schedule(start_date, end_date)
#     data = []
#     for d in schedule['dates']:
#         for g in d['games']:
#             if g['gameType'] == 'R':
#                 game = {
#                     'date': d['date'],
#                     'home': g['teams']['home']['team']['name'],
#                     'away': g['teams']['away']['team']['name'],
#                     'away_score': g['teams']['away']['score'],
#                     'home_score': g['teams']['home']['score'],
#                 }
#                 game['total'] = game['home_score'] + game['away_score']

#                 data.append(game)
#     return data


if __name__ == "__main__":
    # get_teams()
    # get_seasons()
    start = datetime.date(2018, 10, 3)
    # end = start + datetime.timedelta(days=1)
    end = datetime.date(2019, 4, 6)
    # s = get_schedule(start, end)

    # start = datetime.date(2019, 1, 26)
    # end = datetime.date(2019, 1, 26)
    # get_schedule(start, end)
    # print(s)
    # print(s['dates'][0]['games'][0]['teams']['away']['team']['name'])

    games = get_game_data(start, end)
    duplicate = []
    unique = set()
    for g in games:
        print(g)
    print(len(games))

    # get_game()
    #get_season_start_end(2018)
