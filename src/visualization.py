import matplotlib.pyplot as plt
from config import BLUE, RED


def draw_jg_maps(map_count, team_1_paths, team_2_paths, game_datas=None):
    map_y = 15000
    map_x = 15000
    img = plt.imread('images/map.png')

    print('Map Count:', map_count)
    if (len(team_1_paths) > map_count) or (len(team_2_paths) > map_count):
        print('Error: number of pathes given does not match the number of maps to draw.')
        return False
    if (map_count != 1) and (map_count != 4) and (map_count != 9):
        print('Error: map count must be 1, 4 or 9.')
        return False

    if map_count == 1:
        for point in team_1_paths[0].point_list:
            plt.scatter(point.x, point.y, c=BLUE)
            plt.text(point.x, point.y, point.jungle_count, color='#FFFFFF')
        for point in team_2_paths[0].point_list:
            plt.scatter(point.x, point.y, c=RED)
            plt.text(point.x, point.y, point.jungle_count, color='#FFFFFF')

        points_to_connect_x = []
        points_to_connect_y = []

        for point__ in team_1_paths[0].point_list:
            points_to_connect_x.append(point__.x)
            points_to_connect_y.append(point__.y)

        plt.plot(points_to_connect_x, points_to_connect_y, color=BLUE)

        points_to_connect_x_2 = []
        points_to_connect_y_2 = []

        for point_ in team_2_paths[0].point_list:
            points_to_connect_x_2.append(point_.x)
            points_to_connect_y_2.append(point_.y)

        plt.plot(points_to_connect_x_2, points_to_connect_y_2, color=RED)

        plt.xlim(0, map_x)
        plt.ylim(0, map_y)
        plt.imshow(img, extent=[0, map_x, 0, map_y])
        print('Game 1 - ' + game_datas[0].team_1_jg + ' vs ' + game_datas[0].team_2_jg)
        plt.show()

        return True

    if map_count == 4:
        plot1 = plt.subplot2grid((2, 2), (0, 0))
        plot2 = plt.subplot2grid((2, 2), (0, 1))
        plot3 = plt.subplot2grid((2, 2), (1, 0))
        plot4 = plt.subplot2grid((2, 2), (1, 1))

        for point in team_1_paths[0].point_list:
            plot1.scatter(point.x, point.y, c=BLUE)
            plot1.text(point.x, point.y, str(point.jungle_count) + '-' + str(int(point.game_time)), color='#FFFFFF',
                       fontsize='large')
            # test out time text
            # plot1.text(0, 0, point.game_time, color = '#FFFFFF')
            print("drawing point with time", point.game_time)
        for point in team_2_paths[0].point_list:
            plot1.scatter(point.x, point.y, c=RED)
            plot1.text(point.x, point.y, point.jungle_count, color='#FFFFFF', fontsize='large')

        points_to_connect_x = []
        points_to_connect_y = []

        for p in team_1_paths[0].point_list:
            points_to_connect_x.append(p.x)
            points_to_connect_y.append(p.y)

        plot1.plot(points_to_connect_x, points_to_connect_y, c=BLUE)

        points_to_connect_x_2 = []
        points_to_connect_y_2 = []

        for p in team_2_paths[0].point_list:
            points_to_connect_x_2.append(p.x)
            points_to_connect_y_2.append(p.y)

        plot1.plot(points_to_connect_x_2, points_to_connect_y_2, c=RED)

        if game_datas is not None:
            plot1.set_title('Game 1 - ' + game_datas[0].team_1_jg + ' vs ' + game_datas[0].team_2_jg)
        else:
            plot1.set_title('Game 1')

        plot1.axis(xmin=0, xmax=map_x, ymin=0, ymax=map_y)
        plot1.imshow(img, extent=[0, map_x, 0, map_y])

        for point in team_1_paths[1].point_list:
            plot2.scatter(point.x, point.y, c=BLUE)
            plot2.text(point.x, point.y, point.jungle_count, color='#FFFFFF', fontsize='large')
        for point in team_2_paths[1].point_list:
            plot2.scatter(point.x, point.y, c=RED)
            plot2.text(point.x, point.y, point.jungle_count, color='#FFFFFF', fontsize='large')

        points_to_connect_x = []
        points_to_connect_y = []

        for p in team_1_paths[1].point_list:
            points_to_connect_x.append(p.x)
            points_to_connect_y.append(p.y)

        plot2.plot(points_to_connect_x, points_to_connect_y, c=BLUE)

        points_to_connect_x_2 = []
        points_to_connect_y_2 = []

        for p in team_2_paths[1].point_list:
            points_to_connect_x_2.append(p.x)
            points_to_connect_y_2.append(p.y)

        plot2.plot(points_to_connect_x_2, points_to_connect_y_2, c=RED)

        if game_datas is not None:
            plot2.set_title('Game 2 - ' + game_datas[1].team_1_jg + ' vs ' + game_datas[1].team_2_jg)
        else:
            plot2.set_title('Game 2')

        plot2.axis(xmin=0, xmax=map_x, ymin=0, ymax=map_y)
        plot2.imshow(img, extent=[0, map_x, 0, map_y])

        for point in team_1_paths[2].point_list:
            plot3.scatter(point.x, point.y, c=BLUE)
            plot3.text(point.x, point.y, point.jungle_count, color='#FFFFFF', fontsize='large')
        for point in team_2_paths[2].point_list:
            plot3.scatter(point.x, point.y, c=RED)
            plot3.text(point.x, point.y, point.jungle_count, color='#FFFFFF', fontsize='large')

        points_to_connect_x = []
        points_to_connect_y = []

        for p in team_1_paths[2].point_list:
            points_to_connect_x.append(p.x)
            points_to_connect_y.append(p.y)

        plot3.plot(points_to_connect_x, points_to_connect_y, c=BLUE)

        points_to_connect_x_2 = []
        points_to_connect_y_2 = []

        for p in team_2_paths[2].point_list:
            points_to_connect_x_2.append(p.x)
            points_to_connect_y_2.append(p.y)

        plot3.plot(points_to_connect_x_2, points_to_connect_y_2, c=RED)

        if game_datas is not None:
            plot3.set_title('Game 3 - ' + game_datas[2].team_1_jg + ' vs ' + game_datas[2].team_2_jg)
        else:
            plot3.set_title('Game 3')

        plot3.axis(xmin=0, xmax=map_x, ymin=0, ymax=map_y)
        plot3.imshow(img, extent=[0, map_x, 0, map_y])

        for point in team_1_paths[3].point_list:
            plot4.scatter(point.x, point.y, c=BLUE)
            plot4.text(point.x, point.y, point.jungle_count, color='#FFFFFF', fontsize='large')
        for point in team_2_paths[3].point_list:
            plot4.scatter(point.x, point.y, c=RED)
            plot4.text(point.x, point.y, point.jungle_count, color='#FFFFFF', fontsize='large')

        points_to_connect_x = []
        points_to_connect_y = []

        for p in team_1_paths[3].point_list:
            points_to_connect_x.append(p.x)
            points_to_connect_y.append(p.y)

        plot4.plot(points_to_connect_x, points_to_connect_y, c=BLUE)

        points_to_connect_x_2 = []
        points_to_connect_y_2 = []

        for p in team_2_paths[3].point_list:
            points_to_connect_x_2.append(p.x)
            points_to_connect_y_2.append(p.y)

        plot4.plot(points_to_connect_x_2, points_to_connect_y_2, c=RED)

        if game_datas is not None:
            plot4.set_title('Game 4 - ' + game_datas[3].team_1_jg + ' vs ' + game_datas[3].team_2_jg)
        else:
            plot4.set_title('Game 4')
        # plot4.xlim(0, map_x)
        # plot4.ylim(0, map_y)
        plot4.axis(xmin=0, xmax=map_x, ymin=0, ymax=map_y)
        plot4.imshow(img, extent=[0, map_x, 0, map_y])

        plt.tight_layout(pad=0.2, w_pad=0.2, h_pad=0.2)
        plt.show()

        return True
    if map_count == 9:
        print('Error: not currently accepting map counts of size 9.')
        return False

    return False
