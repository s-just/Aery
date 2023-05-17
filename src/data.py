from riot_api import *


class ChampData:
    def __init__(self, setup, mobility):
        self.setup = setup
        self.mobility = mobility


class TeamData:
    def __init__(self, top_champ, jng_champ, mid_champ, bot_champ, sup_champ):
        self.top_champ = top_champ
        self.jng_champ = jng_champ
        self.mid_champ = mid_champ
        self.bot_champ = bot_champ
        self.sup_champ = sup_champ


class MatchData:
    def __init__(self, match_id):
        self.match_id = match_id
        self.match_overview = get_overview(self.match_id)
        self.data = get_data(self.match_id)
        self.team_1_jg = self.get_team_1_jg()
        self.team_2_jg = self.get_team_2_jg()

    def get_team_1_jg(self):
        for participant in self.match_overview["info"]["participants"]:
            if participant["teamPosition"] == "JUNGLE" and participant["teamId"] == 100:
                return participant["championName"]
        # champ = self.match_overview["info"]["participants"][2]["championName"]
        return None

    def get_team_2_jg(self):
        for participant in self.match_overview["info"]["participants"]:
            if participant["teamPosition"] == "JUNGLE" and participant["teamId"] == 200:
                return participant["championName"]
        # champ = self.match_overview["info"]["participants"][2]["championName"]
        return None


class Point:
    def __init__(self, x, y, jungle_count, game_time):
        self.x = x
        self.y = y
        self.jungle_count = jungle_count
        self.game_time = game_time


class Path:
    def __init__(self, point_list, team):
        self.point_list = point_list
        self.team = team
