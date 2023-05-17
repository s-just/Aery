from data import MatchData
from data_processing import get_jg_paths_in_match
from visualization import draw_jg_maps
import time

match_1 = MatchData('OC1_560768758')
match_1_paths = get_jg_paths_in_match(match_1)
print(match_1_paths[0].point_list, match_1_paths[1].point_list)

time.sleep(10)

match_2 = MatchData('OC1_560768758')
match_2_paths = get_jg_paths_in_match(match_2)

time.sleep(10)

match_3 = MatchData('OC1_560768758')
match_3_paths = get_jg_paths_in_match(match_3)

time.sleep(10)

match_4 = MatchData('OC1_560768758')
match_4_paths = get_jg_paths_in_match(match_4)

draw_jg_maps(1, [match_1_paths[0]], [match_1_paths[1]], [match_1])
# DrawJungleMaps(4,[match_1_paths[0],match_2_paths[0],match_3_paths[0],match_4_paths[0]],[match_1_paths[1],match_2_paths[1],match_3_paths[1],match_4_paths[1]],[match_1,match_2,match_3,match_4])
