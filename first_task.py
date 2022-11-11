# В примере кода ниже генерируется список фиксаций состояния счета игры в течение матча.
# Разработайте функцию get_score(game_stamps, offset), которая вернет счет на момент offset в списке game_stamps.
# Нужно суметь понять суть написанного кода, заметить нюансы,
# разработать функцию вписывающуюся стилем в существующий код, желательно адекватной алгоритмической сложности.

# PyShop sample code starts:
from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps

    # game_stamps = generate_game()
    # pprint(game_stamps)


# def get_score(game_stamps, offset):
#     '''
#         Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
#         Please pay attention to that for some offsets the game_stamps list may not contain scores.
#     '''
#     # return home, away

# PyShop sample code ends.


# decision by @Selge:
def get_score(game_stamps, offset):
    """
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    """
    none_message = "Game stamps list doesn't content such offset value!"
    offsets = []
    for game_stamp in game_stamps:
        offsets.append(game_stamp["offset"])

    if offset not in offsets:
        return none_message
    else:
        for game_stamp in game_stamps:
            stamp = list(game_stamp.values())
            for check in stamp:
                if check == offset:
                    score = stamp[1]
                    home = score.get('home') if score else 'No score'
                    away = score.get('away') if score else 'No score'
                    # return home, away
                    return {"offset": offset,
                            "score": {"home": home, "away": away}}


if __name__ == '__main__':
    game_stamps = generate_game()
    pprint(game_stamps)
    try:
        offset = int(input('Please, type in the target offset: '))
    except TypeError:
        print("Oops! Please,use digits only. Try again...")
    pprint(get_score(game_stamps, offset))
