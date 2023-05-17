from data import *


def get_jg_paths_in_match(match_data):
    team_1_path_positions = []
    print(match_data.data)

    for i in range(1, 10):
        pos = match_data.data["info"]["frames"][i]["participantFrames"]["2"]["position"]
        jungle_minions_killed = match_data.data["info"]["frames"][i]["participantFrames"]["2"]["jungleMinionsKilled"]
        xp = match_data.data["info"]["frames"][i]["participantFrames"]["2"]["xp"]
        timestamp = match_data.data["info"]["frames"][i]["timestamp"]
        timestamp_str = str(timestamp)
        time_stamp_cleaned = timestamp_str[-3:]
        minutes = int(timestamp_str[:-3]) / 60

        gold = match_data.data["info"]["frames"][i]["participantFrames"]["1"]["totalGold"]

        current_point = Point(int(pos['x']), int(pos['y']), jungle_minions_killed, minutes)

        print(current_point.x, current_point.y, jungle_minions_killed, gold)

        team_1_path_positions.append(current_point)

    team_2_path_positions = []
    for i in range(1, 10):
        pos = match_data.data["info"]["frames"][i]["participantFrames"]["7"]["position"]
        jungle_minions_killed = match_data.data["info"]["frames"][i]["participantFrames"]["7"]["jungleMinionsKilled"]
        xp = match_data.data["info"]["frames"][i]["participantFrames"]["7"]["xp"]
        timestamp = match_data.data["info"]["frames"][i]["timestamp"]
        timestamp_str = str(timestamp)
        time_stamp_cleaned = timestamp_str[-3:]
        minutes = int(timestamp_str[:-3]) / 60

        gold = match_data.data["info"]["frames"][i]["participantFrames"]["6"]["totalGold"]

        current_point = Point(int(pos['x']), int(pos['y']), jungle_minions_killed, minutes)

        print(current_point.x, current_point.y, jungle_minions_killed, gold)

        team_2_path_positions.append(current_point)

    return [Path(team_1_path_positions, 1), Path(team_2_path_positions, 2)]
