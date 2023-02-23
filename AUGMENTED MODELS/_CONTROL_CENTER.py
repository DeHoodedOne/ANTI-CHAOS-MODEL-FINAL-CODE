from itertools import combinations, permutations


def set_date_s_size():
    TOMORROWS_DATE = "22-02-2023"
    GAMES_SAMPLE_SIZE = 50
    return [TOMORROWS_DATE, GAMES_SAMPLE_SIZE]


def game_criteria():
    # CONFIDENCE_INTERVALS = [0.99, 0.98, 0.97, 0.96, 0.95, 0.93, 0.875]
    CONFIDENCE_INTERVALS = [0.99, 0.985, 0.98, 0.975, 0.97, 0.965, 0.93]
    NUMBER_OF_MATCHES_ALREADY_PLAYED = 5
    # FORM_VALUE_LIMIT = 0.6
    FORM_VALUE_LIMIT = 0.2
    FORM_SIZE_COUNT = 5
    FORM_DIFFERENCE = 0.4
    TEAM_POSITION_DIFFERENCE = 5
    # BAYESIAN_DIFFERENCE = 0.6
    BAYESIAN_DIFFERENCE = 0.01
    POSITION_MARK = 5
    YEAR_OF_MATCHES = 22
    DISCRIMINANT_FOR_HOME_N_AWAY_TEAMS_INDEPENDENTLY = 5
    DISCRIMINANT_FOR_HOME_N_AWAY_TEAMS_AGAINST_EACH_OTHER = 5
    HOME_N_AWAY_INDEPENDENT_MATCH_SAMPLE = 1
    SELENIUM_CHROMEDRIVER_PATH = ["C:\Development\chromedriver_win31\chromedriver.exe",
                                  "C:\Development\chromedriver_win32\chromedriver.exe",
                                  "C:\Development\chromedriver_win33\chromedriver.exe",
                                  "C:\Development\chromedriver_win34\chromedriver.exe"]

    PY_PROCESSES = ["ALT_FOOTBALL.py", "ALT_SPORTS1.py", "ALT_SPORTS2.py", "A_S_P_SPORTS.py"]
    PY_PROCESSES1 = ["_RUN1.py", "_RUN2.py", '_RUN3.py']
    return [CONFIDENCE_INTERVALS, NUMBER_OF_MATCHES_ALREADY_PLAYED, FORM_VALUE_LIMIT, FORM_SIZE_COUNT,
            TEAM_POSITION_DIFFERENCE, BAYESIAN_DIFFERENCE, POSITION_MARK, YEAR_OF_MATCHES,
            DISCRIMINANT_FOR_HOME_N_AWAY_TEAMS_INDEPENDENTLY, DISCRIMINANT_FOR_HOME_N_AWAY_TEAMS_AGAINST_EACH_OTHER,
            HOME_N_AWAY_INDEPENDENT_MATCH_SAMPLE, SELENIUM_CHROMEDRIVER_PATH, PY_PROCESSES, PY_PROCESSES1, FORM_DIFFERENCE]


def master_sport_list():

    MASTER_LIST = ["https://www.flashscore.com/american-football/",
                   "https://www.flashscore.com/aussie-rules/",
                   "https://www.flashscore.com/badminton/",
                   "https://www.flashscore.com/bandy/",
                   "https://www.flashscore.com/baseball/",
                   "https://www.flashscore.com/basketball/",
                   "https://www.flashscore.com/beach-soccer/",
                   "https://www.flashscore.com/beach-volleyball/",
                   "https://www.flashscore.com/boxing/",
                   "https://www.flashscore.com/cricket/",
                   "https://www.flashscore.com/darts/",
                   "https://www.flashscore.com/esports/",
                   "https://www.flashscore.com/field-hockey/",
                   "https://www.flashscore.com/floorball/",
                   "https://www.flashscore.com/football/",
                   "https://www.flashscore.com/futsal/",
                   "https://www.flashscore.com/handball/",
                   "https://www.flashscore.com/hockey/",
                   "https://www.flashscore.com/kabaddi/",
                   "https://www.flashscore.com/mma/",
                   "https://www.flashscore.com/netball/",
                   "https://www.flashscore.com/pesapallo/",
                   "https://www.flashscore.com/rugby-league/",
                   "https://www.flashscore.com/rugby-union/",
                   "https://www.flashscore.com/snooker/",
                   "https://www.flashscore.com/table-tennis/",
                   "https://www.flashscore.com/tennis/",
                   "https://www.flashscore.com/volleyball/",
                   "https://www.flashscore.com/water-polo/"]

    # ALTERNATIVE_SPORTS1 = []
    # ALTERNATIVE_SPORTS2 = []
    # SAMPLE_SIZE_ = len(MASTER_LIST) // 2
    # for j in range(2):
    #     if j == 0:
    #         ALTERNATIVE_SPORTS1 = rdm.sample(MASTER_LIST, SAMPLE_SIZE_ + 1)
    #         ALTERNATIVE_SPORTS1.sort()
    #         for SPORT in ALTERNATIVE_SPORTS1:
    #             MASTER_LIST.pop(MASTER_LIST.index(SPORT))
    #     if j == 1:
    #         ALTERNATIVE_SPORTS2 = rdm.sample(MASTER_LIST, SAMPLE_SIZE_)
    #         ALTERNATIVE_SPORTS2.sort()
    # # print(ALTERNATIVE_SPORTS1)
    # # print(ALTERNATIVE_SPORTS2)
    return [MASTER_LIST]


def master_sport_list1():
    FOOTBALL = "https://www.flashscore.com/football/"

    # ALTERNATIVE_SPORTS1 = master_sport_list()[0]

    # ALTERNATIVE_SPORTS2 = master_sport_list()[1]

    ALTERNATIVE_SPORTS1 = ["https://www.flashscore.com/american-football/",
                           "https://www.flashscore.com/aussie-rules/",
                           "https://www.flashscore.com/beach-soccer/",
                           "https://www.flashscore.com/field-hockey/",
                           "https://www.flashscore.com/rugby-league/",
                           "https://www.flashscore.com/rugby-union/",
                           "https://www.flashscore.com/floorball/",
                           "https://www.flashscore.com/pesapallo/",
                           "https://www.flashscore.com/basketball/",
                           "https://www.flashscore.com/volleyball/"]

    ALTERNATIVE_SPORTS2 = ["https://www.flashscore.com/water-polo/",
                           "https://www.flashscore.com/baseball/",
                           "https://www.flashscore.com/kabaddi/",
                           "https://www.flashscore.com/netball/",
                           "https://www.flashscore.com/futsal/",
                           "https://www.flashscore.com/bandy/",
                           "https://www.flashscore.com/hockey/",
                           "https://www.flashscore.com/handball/"]

    SINGLE_PLAYER_SPORTS = ["https://www.flashscore.com/darts/",
                            "https://www.flashscore.com/badminton/",
                            "https://www.flashscore.com/beach-volleyball/",
                            "https://www.flashscore.com/esports/",
                            "https://www.flashscore.com/tennis/",
                            "https://www.flashscore.com/snooker/",
                            "https://www.flashscore.com/table-tennis/"]

    return [FOOTBALL, ALTERNATIVE_SPORTS1, ALTERNATIVE_SPORTS2, SINGLE_PLAYER_SPORTS]


def directories():
    PROB_METRICS = ["BAYE", "RAND", "ZSCE", "ODDS", "DZSCE"]
    PROB_METRICS1 = ["CHAOTIC", "BAYESIAN", "ZSCORED", "ODDS"]
    COMBINERS = ["AVERAGE", "PRODUCT", "SQRT_AVERAGE", "SQRT_PRODUCT",
                 "CBRT_AVERAGE", "CBRT_PRODUCT", "FRT_AVERAGE", "FRT_PRODUCT"]
    COMB_PROB_METRICS1 = list(combinations(PROB_METRICS[:4], 2))
    COMB_PROB_METRICS2 = list(permutations(PROB_METRICS1, 2))[:6]
    COMB_PROB_METRICS3 = list(combinations(PROB_METRICS[:4], 3))
    COMB_PROB_METRICS4 = list(combinations(PROB_METRICS[:4], 4))

    dir_list = []

    for COMBINER in COMBINERS[:4]:
        Z = COMBINER
        for COMB in COMB_PROB_METRICS1:
            X, Y = COMB
            dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for PROB in PROB_METRICS:
        X = PROB
        Y = "ANALYSIS"
        Z = "STANDARD"
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for COMB in COMB_PROB_METRICS2:
        X, Y = COMB
        Z = "COMBINATE"
        dir_list.append(f"RESULTS - {Z}_{X}_{Y}")

    for COMBINER in COMBINERS:
        Z = COMBINER
        if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[6] and Z != COMBINERS[7]:
            for COMB in COMB_PROB_METRICS3:
                W, X, Y = COMB
                dir_list.append(f"RESULTS - {Z}_{W}_{X}_{Y}")

    for COMBINER in COMBINERS:
        Z = COMBINER
        if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[4] and Z != COMBINERS[5]:
            for COMB in COMB_PROB_METRICS4:
                V, W, X, Y = COMB
                dir_list.append(f"RESULTS - {Z}_{V}_{W}_{X}_{Y}")

    return dir_list


def combinatorials():
    PROB_METRICS = ["BAYE", "RAND", "ZSCE", "ODDS", "DZSCE"]
    PROB_METRICS1 = ["CHAOTIC", "BAYESIAN", "ZSCORED", "ODDS"]
    COMBINERS = ["AVERAGE", "PRODUCT", "SQRT_AVERAGE", "SQRT_PRODUCT",
                 "CBRT_AVERAGE", "CBRT_PRODUCT", "FRT_AVERAGE", "FRT_PRODUCT"]
    COMB_PROB_METRICS1 = list(combinations(PROB_METRICS[:4], 2))
    COMB_PROB_METRICS2 = list(permutations(PROB_METRICS1, 2))[:6]
    COMB_PROB_METRICS3 = list(combinations(PROB_METRICS[:4], 3))
    COMB_PROB_METRICS4 = list(combinations(PROB_METRICS[:4], 4))
    return [PROB_METRICS, PROB_METRICS1, COMBINERS, COMB_PROB_METRICS1,
            COMB_PROB_METRICS2, COMB_PROB_METRICS3, COMB_PROB_METRICS4]
