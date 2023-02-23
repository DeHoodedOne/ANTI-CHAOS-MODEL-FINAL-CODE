import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException, ElementClickInterceptedException, UnexpectedAlertPresentException, WebDriverException, NoSuchWindowException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import math
import random as rdm
import statistics as stats
import scipy.stats
import numpy as np
import time
import traceback
from datetime import datetime
from _CONTROL_CENTER import set_date_s_size, game_criteria, master_sport_list, combinatorials


tmrw_date = set_date_s_size()[0]
sample_size = set_date_s_size()[1]

now = datetime.now()
date_time = now.strftime("%d-%m-%Y")

CONFINTVLS = game_criteria()[0]
NMP = game_criteria()[1]
FORM_VALUE = game_criteria()[2]
FORM_COUNT = game_criteria()[3]
FORM_DIFF = game_criteria()[-1]
POS_DIFF = game_criteria()[4]
BAY_DIFF = game_criteria()[5]
POS_MARK = game_criteria()[6]
YEAR = game_criteria()[7]
DSCRM_H_A = game_criteria()[8]
DSCRM_BT = game_criteria()[9]
INDP_MATCH_SAMPLE = game_criteria()[10]

PROB_METRICS = combinatorials()[0]
PROB_METRICS1 = combinatorials()[1]
COMBINERS = combinatorials()[2]
COMB_PROB_METRICS1 = combinatorials()[3]
COMB_PROB_METRICS2 = combinatorials()[4]
COMB_PROB_METRICS3 = combinatorials()[5]
COMB_PROB_METRICS4 = combinatorials()[6]

OUTCOMES = ["HW", "AW", "ov33.5", "ov43.5", "ov53.5", "sh1_4.5", "sh1_7.5", "sh2_4.5", "sh2_7.5", "12"]

start_time = time.time()
SPORT_ = master_sport_list()[0][23]

chrome_path = game_criteria()[11][3]
service = Service(chrome_path)
options = webdriver.ChromeOptions()
options.add_extension("_AdblockPlus.crx")
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(2.5)
try:
    driver.get(SPORT_)
    sleep(10)
except WebDriverException:
    try:
        driver.get(SPORT_)
        sleep(10)
    except WebDriverException:
        traceback.print_exc()

sport = SPORT_.split('/')[3]
if driver.current_url == SPORT_:
    try:
        window_before = driver.window_handles[0]
        window_ads0 = driver.window_handles[1]
        driver.switch_to.window(window_before)
        driver.switch_to.window(window_ads0)
        driver.close()
        driver.switch_to.window(window_before)
    except IndexError:
        window_before = driver.window_handles[1]
        window_ads0 = driver.window_handles[0]
        driver.switch_to.window(window_before)
        driver.switch_to.window(window_ads0)
        driver.close()
        driver.switch_to.window(window_before)
else:
    try:
        window_before = driver.window_handles[1]
        window_ads0 = driver.window_handles[0]
        driver.switch_to.window(window_before)
        driver.switch_to.window(window_ads0)
        driver.close()
        driver.switch_to.window(window_before)
    except IndexError:
        window_before = driver.window_handles[0]
        window_ads0 = driver.window_handles[1]
        driver.switch_to.window(window_before)
        driver.switch_to.window(window_ads0)
        driver.close()
        driver.switch_to.window(window_before)

if driver.current_url != SPORT_:
    try:
        driver.get(SPORT_)
        sleep(10)
    except WebDriverException:
        try:
            driver.get(SPORT_)
            sleep(10)
        except WebDriverException:
            traceback.print_exc()
try:
    accept_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_cookies.click()
    sleep(1.5)
except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
    pass

if date_time != tmrw_date:
    try:
        try:
            accept_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_cookies.click()
            sleep(1.5)
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
            pass
        driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
        sleep(1)
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
        try:
            driver.refresh()
            sleep(3)
            try:
                accept_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
                accept_cookies.click()
                sleep(1.5)
            except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                pass
            driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
            sleep(1)
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
            traceback.print_exc()
try:
    driver.find_element(By.CSS_SELECTOR, ".filters__group .filters__tab:last-child").click()
    sleep(1)
except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
    try:
        driver.refresh()
        sleep(3)
        try:
            accept_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_cookies.click()
            sleep(1.5)
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
            pass
        if date_time != tmrw_date:
            driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
            sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".filters__group .filters__tab:last-child").click()
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
        traceback.print_exc()

sleep(1)

driver.find_element(By.XPATH, '//*[@id="hamburger-menu"]/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="hamburger-menu-window"]/div/div[1]').click()
driver.find_element(By.XPATH, '//*[@id="hamburger-menu"]/div[1]/div/div[3]/div[2]/div[2]/label[2]').click()
driver.find_element(By.CSS_SELECTOR, '[class="modal__window modal__window--settings"] [class="close modal__closeButton"]').click()
sleep(1)


def team_data():
    country = driver.find_element(By.CSS_SELECTOR, '.tournamentHeaderDescription .tournamentHeader__country').text.split(':')[0]
    league = driver.find_element(By.CSS_SELECTOR, '.tournamentHeaderDescription .tournamentHeader__country').text.split(':')[1].split(' - ')[0]
    try:
        home_team = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__home  .participant__participantName a').text
    except NoSuchElementException:
        home_teamw = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[0].text
        home_teamv = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[1].text
        home_team = f"{home_teamw}/{home_teamv}"
    try:
        away_team = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__away  .participant__participantName a').text
    except NoSuchElementException:
        away_teamw = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[0].text
        away_teamv = driver.find_elements(By.CSS_SELECTOR, '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[1].text
        away_team = f"{away_teamw}/{away_teamv}"
    leagues.append(league)
    countries.append(country)
    away_teams.append(away_team)
    home_teams.append(home_team)


def pts_pos_mp():
    try:
        first_entry = int(driver.find_elements(By.CSS_SELECTOR, '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[0].text.strip())
        print(f"This is the first table entry: {first_entry}")
    except IndexError:
        try:
            driver.refresh()
            sleep(4)
            first_entry = int(driver.find_elements(By.CSS_SELECTOR, '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[0].text.strip())
            print(f"This is the first table entry: {first_entry}")
        except IndexError:
            driver.refresh()
            sleep(2)
            first_entry = 0

    if selected_teams_names[0].text == home_teamx:
        try:
            home_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[0].text.split('.')[0].strip()
            home_positions.append(int(home_t_position))
        except IndexError:
            home_positions.append(0)
        if first_entry > 10:
            try:
                home_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[0].text.strip()
                home_nums_matches_played.append(int(home_t_mp))
            except IndexError:
                home_nums_matches_played.append(0)
        else:
            print("Home Team No Reach1")
        try:
            home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[0].text.strip()
            home_points.append(int(home_t_point))
        except IndexError:
            try:
                home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[0].text.strip()
                home_points.append(float(home_t_point))
            except IndexError:
                home_points.append(0)
    else:
        try:
            away_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[0].text.split('.')[0].strip()
            away_positions.append(int(away_t_position))
        except IndexError:
            away_positions.append(0)
        if first_entry > 10:
            try:
                away_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[0].text.strip()
                away_nums_matches_played.append(int(away_t_mp))
            except IndexError:
                away_nums_matches_played.append(0)
        else:
            print("Away Team No Reach1")
        try:
            away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[0].text.strip()
            away_points.append(int(away_t_point))
        except IndexError:
            try:
                away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[0].text.strip()
                away_points.append(float(away_t_point))
            except IndexError:
                away_points.append(0)
    try:
        if selected_teams_names[1].text == away_teamx:
            try:
                away_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[1].text.split('.')[0].strip()
                away_positions.append(int(away_t_position))
            except IndexError:
                away_positions.append(0)
            if first_entry > 10:
                try:
                    away_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[4].text.strip()
                    away_nums_matches_played.append(int(away_t_mp))
                except IndexError:
                    away_nums_matches_played.append(0)
            else:
                print("Away Team No Reach2")
            try:
                away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[1].text.strip()
                away_points.append(int(away_t_point))
            except IndexError:
                try:
                    away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[1].text.strip()
                    away_points.append(float(away_t_point))
                except IndexError:
                    away_points.append(0)
        else:
            try:
                home_t_position = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[1].text.split('.')[0].strip()
                home_positions.append(int(home_t_position))
            except IndexError:
                home_positions.append(0)
            if first_entry > 10:
                try:
                    home_t_mp = driver.find_elements(By.CSS_SELECTOR, '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[4].text.strip()
                    home_nums_matches_played.append(int(home_t_mp))
                except IndexError:
                    home_nums_matches_played.append(0)
            else:
                print("Home Team No Reach2")
            try:
                home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[1].text.strip()
                home_points.append(int(home_t_point))
            except IndexError:
                try:
                    home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[1].text.strip()
                    home_points.append(float(home_t_point))
                except IndexError:
                    home_points.append(0)
    except IndexError:
        if selected_teams_names[0].text == home_teamx:
            away_positions.append(0)
            away_nums_matches_played.append(0)
            away_points.append(0)
        elif selected_teams_names[0].text == away_teamx:
            home_points.append(0)
            home_nums_matches_played.append(0)
            home_positions.append(0)


def z_scorer(htpts, atpts):
    try:
        teams_pts = driver.find_elements(By.CSS_SELECTOR, '.ui-table__row  .table__cell--points ')
        print(teams_pts[0])
    except IndexError:
        teams_pts = driver.find_elements(By.CSS_SELECTOR, '.ui-table__row  .table__cell--pct ')
    team_pts = []
    for t in range(len(teams_pts)):
        pts = float(teams_pts[t].text.strip())
        team_pts.append(pts)
    try:
        mean_ = stats.mean(team_pts)
        stdv = stats.pstdev(team_pts)
        if mean_ > 0 and stdv > 0:
            home_zsc = scipy.stats.norm.cdf(htpts, loc=mean_, scale=stdv)
            away_zsc = scipy.stats.norm.cdf(atpts, loc=mean_, scale=stdv)
            diff_zsc = abs(home_zsc - away_zsc)
            home_z_prob.append(home_zsc)
            away_z_prob.append(away_zsc)
            diff_z_prob.append(diff_zsc)
        else:
            home_z_prob.append(0.5)
            away_z_prob.append(0.5)
            diff_z_prob.append(0.01)
    except stats.StatisticsError:
        home_z_prob.append(0.5)
        away_z_prob.append(0.5)
        diff_z_prob.append(0.01)


def append_zeroes1():
    away_points.append(0)
    home_points.append(0)
    home_z_prob.append(0.5)
    away_z_prob.append(0.5)
    diff_z_prob.append(0.01)
    v_sports = ["tennis", "darts", "badminton", "snooker"]
    if sport not in v_sports:
        home_positions.append(0)
        away_positions.append(0)


def append_zeroes(home_pos, away_pos):
    away_points.append(0)
    home_points.append(0)
    v_sports = ["tennis", "darts", "badminton", "snooker"]
    if sport in v_sports:
        try:
            home_z = 1 - (int(home_pos) / (int(home_pos) + int(away_pos)))
            away_z = 1 - (int(away_pos) / (int(home_pos) + int(away_pos)))
            diff_z = abs(home_z - away_z)
            if 0 < home_z < 1 and 0 < away_z < 1:
                home_z_prob.append(home_z)
                away_z_prob.append(away_z)
                diff_z_prob.append(diff_z)
            else:
                home_z_prob.append(0.5)
                away_z_prob.append(0.5)
                diff_z_prob.append(0.01)
        except ZeroDivisionError:
            home_z_prob.append(0.5)
            away_z_prob.append(0.5)
            diff_z_prob.append(0.01)
    else:
        home_z_prob.append(0.5)
        away_z_prob.append(0.5)
        diff_z_prob.append(0.01)


def h2h_aggregator(m, home_score, away_score, home_x, away_x):
    global valid_games
    global count_HW
    global count_AW
    global count_33_5
    global count_43_5
    global count_53_5
    global count_sh1_4_5
    global count_sh1_7_5
    global count_sh2_4_5
    global count_sh2_7_5
    global count_12
    valid_games += 1
    sleep(0.5)
    if (int(home_score[m].text) > int(away_score[m].text)) and (home_x[m].text == home_teamx):
        count_HW += 1
    if (int(home_score[m].text) > int(away_score[m].text)) and (home_x[m].text == away_teamx):
        count_AW += 1
    if (int(away_score[m].text) > int(home_score[m].text)) and (away_x[m].text == away_teamx):
        count_AW += 1
    if (int(away_score[m].text) > int(home_score[m].text)) and (away_x[m].text == home_teamx):
        count_HW += 1
    if int(home_score[m].text) == int(away_score[m].text) and (int(home_score[m].text) > 0 and int(away_score[m].text) > 0):
        count_HW += 0.5
        count_AW += 0.5
    if int(home_score[m].text) == int(away_score[m].text) and (int(home_score[m].text) == 0 and int(away_score[m].text) == 0):
        count_HW += 0
        count_AW += 0
    if (int(home_score[m].text) + int(away_score[m].text)) >= 34:
        count_33_5 += 1
    if (int(home_score[m].text) + int(away_score[m].text)) >= 44:
        count_43_5 += 1
    if (int(home_score[m].text) + int(away_score[m].text)) >= 54:
        count_53_5 += 1
    if ((int(home_score[m].text) + 4.5) > int(away_score[m].text)) and (home_x[m].text == home_teamx):
        count_sh1_4_5 += 1
    if ((int(away_score[m].text) + 4.5) > int(home_score[m].text)) and (away_x[m].text == home_teamx):
        count_sh1_4_5 += 1
    if ((int(home_score[m].text) + 4.5) > int(away_score[m].text)) and (home_x[m].text == away_teamx):
        count_sh2_4_5 += 1
    if ((int(away_score[m].text) + 4.5) > int(home_score[m].text)) and (away_x[m].text == away_teamx):
        count_sh2_4_5 += 1
    if ((int(home_score[m].text) + 7.5) > int(away_score[m].text)) and (home_x[m].text == home_teamx):
        count_sh1_7_5 += 1
    if ((int(away_score[m].text) + 7.5) > int(home_score[m].text)) and (away_x[m].text == home_teamx):
        count_sh1_7_5 += 1
    if ((int(home_score[m].text) + 7.5) > int(away_score[m].text)) and (home_x[m].text == away_teamx):
        count_sh2_7_5 += 1
    if ((int(away_score[m].text) + 7.5) > int(home_score[m].text)) and (away_x[m].text == away_teamx):
        count_sh2_7_5 += 1
    if int(home_score[m].text) != int(away_score[m].text):
        count_12 += 1


def h2h_prob_calc():
    global valid_games
    global count_HW
    global count_AW
    global count_33_5
    global count_43_5
    global count_53_5
    global count_sh1_4_5
    global count_sh1_7_5
    global count_sh2_4_5
    global count_sh2_7_5
    global count_12
    prob_33_5i = float(count_33_5 / valid_games)
    prob_43_5i = float(count_43_5 / valid_games)
    prob_53_5i = float(count_53_5 / valid_games)
    prob_sh1_4_5i = float(count_sh1_4_5 / valid_games)
    prob_sh1_7_5i = float(count_sh1_7_5 / valid_games)
    prob_sh2_4_5i = float(count_sh2_4_5 / valid_games)
    prob_sh2_7_5i = float(count_sh2_7_5 / valid_games)
    prob_12i = float(count_12 / valid_games)
    prob_HW = float(count_HW / valid_games)
    prob_AW = float(count_AW / valid_games)

    if prob_HW == 1.0:
        prob_HW -= 0.01
    if prob_AW == 1.0:
        prob_AW -= 0.01
    if prob_33_5i == 1.0:
        prob_33_5i -= 0.01
    if prob_43_5i == 1.0:
        prob_43_5i -= 0.01
    if prob_53_5i == 1.0:
        prob_53_5i -= 0.01
    if prob_sh1_4_5i == 1.0:
        prob_sh1_4_5i -= 0.01
    if prob_sh2_4_5i == 1.0:
        prob_sh2_4_5i -= 0.01
    if prob_sh1_7_5i == 1.0:
        prob_sh1_7_5i -= 0.01
    if prob_sh2_7_5i == 1.0:
        prob_sh2_7_5i -= 0.01
    if prob_12i == 1.0:
        prob_12i -= 0.01

    if prob_33_5i == 0:
        prob_33_5i += 0.01
    if prob_43_5i == 0:
        prob_43_5i += 0.01
    if prob_53_5i == 0:
        prob_53_5i += 0.01
    if prob_sh1_4_5i == 0:
        prob_sh1_4_5i += 0.01
    if prob_sh2_4_5i == 0:
        prob_sh2_4_5i += 0.01
    if prob_sh1_7_5i == 0:
        prob_sh1_7_5i += 0.01
    if prob_sh2_7_5i == 0:
        prob_sh2_7_5i += 0.01
    if prob_12i == 0:
        prob_12i += 0.01
    if prob_HW == 0:
        prob_HW += 0.01
    if prob_AW == 0:
        prob_AW += 0.01
    return [prob_HW, prob_AW, prob_33_5i, prob_43_5i, prob_53_5i, prob_sh1_4_5i, prob_sh1_7_5i, prob_sh2_4_5i, prob_sh2_7_5i, prob_12i]


def h2h_appender(prb_HW, prb_AW, prb_33_5, prb_43_5, prb_53_5, prb_sh1_4_5, prb_sh1_7_5, prb_sh2_4_5, prb_sh2_7_5, prb_12):
    prob_HWs.append(prb_HW)
    prob_AWs.append(prb_AW)
    prob_33_5s.append(prb_33_5)
    prob_43_5s.append(prb_43_5)
    prob_53_5s.append(prb_53_5)
    prob_sh1_4_5s.append(prb_sh1_4_5)
    prob_sh1_7_5s.append(prb_sh1_7_5)
    prob_sh2_4_5s.append(prb_sh2_4_5)
    prob_sh2_7_5s.append(prb_sh2_7_5)
    prob_12s.append(prb_12)


def ht_g_avg_aggregator(m, home_score, away_score, home_x, away_x, home_scores):
    if home_x[m].text == home_teamx:
        home_scores.append(int(home_score[m].text))
    if away_x[m].text == home_teamx:
        home_scores.append(int(away_score[m].text))


def at_g_avg_aggregator(m, home_score, away_score, home_x, away_x, away_scores):
    if away_x[m].text == away_teamx:
        away_scores.append(int(away_score[m].text))
    if home_x[m].text == away_teamx:
        away_scores.append(int(home_score[m].text))


def bt_g_avg_aggregator(m, home_score, away_score, home_x, away_x, bt_home_scores, bt_away_scores):
    if home_x[m].text == home_teamx:
        bt_home_scores.append(int(home_score[m].text))
    if away_x[m].text == home_teamx:
        bt_home_scores.append(int(away_score[m].text))
    if away_x[m].text == away_teamx:
        bt_away_scores.append(int(away_score[m].text))
    if home_x[m].text == away_teamx:
        bt_away_scores.append(int(home_score[m].text))


def ht_indp_aggregator(k, home_score, away_score, home_x, away_x):
    global valid_games_H_indp
    global count_HW_H_indp
    global count_33_5_H_indp
    global count_43_5_H_indp
    global count_53_5_H_indp
    global count_sh1_4_5_H_indp
    global count_sh1_7_5_H_indp
    global count_12_H_indp

    valid_games_H_indp += 1
    if (int(home_score[k].text) > int(away_score[k].text)) and (home_x[k].text == home_teamx):
        count_HW_H_indp += 1
    if (int(away_score[k].text) > int(home_score[k].text)) and (away_x[k].text == home_teamx):
        count_HW_H_indp += 1
    if int(home_score[k].text) == int(away_score[k].text) and (int(home_score[k].text) > 0 and int(away_score[k].text) > 0):
        count_HW_H_indp += 0.33
    if int(home_score[k].text) == int(away_score[k].text) and (int(home_score[k].text) == 0 and int(away_score[k].text) == 0):
        count_HW_H_indp += 0
    if (int(home_score[k].text) + int(away_score[k].text)) >= 34 and (home_x[k].text == home_teamx) and int(home_score[k].text) >= 20:
        count_33_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 34 and (away_x[k].text == home_teamx) and int(away_score[k].text) >= 20:
        count_33_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 44 and (home_x[k].text == home_teamx) and int(home_score[k].text) >= 28:
        count_43_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 44 and (away_x[k].text == home_teamx) and int(away_score[k].text) >= 28:
        count_43_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 54 and (home_x[k].text == home_teamx) and int(home_score[k].text) >= 36:
        count_53_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 54 and (away_x[k].text == home_teamx) and int(away_score[k].text) >= 36:
        count_53_5_H_indp += 1
    if ((int(home_score[k].text) + 4.5) > int(away_score[k].text)) and (home_x[k].text == home_teamx):
        count_sh1_4_5_H_indp += 1
    if ((int(away_score[k].text) + 4.5) > int(home_score[k].text)) and (away_x[k].text == home_teamx):
        count_sh1_4_5_H_indp += 1
    if ((int(home_score[k].text) + 7.5) > int(away_score[k].text)) and (home_x[k].text == home_teamx):
        count_sh1_7_5_H_indp += 1
    if ((int(away_score[k].text) + 7.5) > int(home_score[k].text)) and (away_x[k].text == home_teamx):
        count_sh1_7_5_H_indp += 1
    if int(home_score[k].text) != int(away_score[k].text) and int(home_score[k].text) >= 1 and (home_x[k].text == home_teamx):
        count_12_H_indp += 1
    if int(away_score[k].text) != int(home_score[k].text) and int(away_score[k].text) >= 1 and (away_x[k].text == home_teamx):
        count_12_H_indp += 1


def ht_indp_prob_calc():
    global valid_games_H_indp
    global count_HW_H_indp
    global count_33_5_H_indp
    global count_43_5_H_indp
    global count_53_5_H_indp
    global count_sh1_4_5_H_indp
    global count_sh1_7_5_H_indp
    global count_12_H_indp

    prob_HW_H_indp = float(count_HW_H_indp / valid_games_H_indp)
    prob_AW_H_indp = 1 - prob_HW_H_indp
    prob_33_5_H_indp = float(count_33_5_H_indp / valid_games_H_indp)
    prob_43_5_H_indp = float(count_43_5_H_indp / valid_games_H_indp)
    prob_53_5_H_indp = float(count_53_5_H_indp / valid_games_H_indp)
    prob_sh1_4_5_H_indp = float(count_sh1_4_5_H_indp / valid_games_H_indp)
    prob_sh1_7_5_H_indp = float(count_sh1_7_5_H_indp / valid_games_H_indp)
    prob_sh2_4_5_H_indp = 1 - prob_sh1_4_5_H_indp
    prob_sh2_7_5_H_indp = 1 - prob_sh1_7_5_H_indp
    prob_12_H_indp = float(count_12_H_indp / valid_games_H_indp)

    if prob_HW_H_indp == 1.0:
        prob_HW_H_indp -= 0.01
    if prob_AW_H_indp == 1.0:
        prob_AW_H_indp -= 0.01
    if prob_33_5_H_indp == 1.0:
        prob_33_5_H_indp -= 0.01
    if prob_43_5_H_indp == 1.0:
        prob_43_5_H_indp -= 0.01
    if prob_53_5_H_indp == 1.0:
        prob_53_5_H_indp -= 0.01
    if prob_sh1_4_5_H_indp == 1.0:
        prob_sh1_4_5_H_indp -= 0.01
    if prob_sh2_4_5_H_indp == 1.0:
        prob_sh2_4_5_H_indp -= 0.01
    if prob_sh1_7_5_H_indp == 1.0:
        prob_sh1_7_5_H_indp -= 0.01
    if prob_sh2_7_5_H_indp == 1.0:
        prob_sh2_7_5_H_indp -= 0.01
    if prob_12_H_indp == 1.0:
        prob_12_H_indp -= 0.01

    if prob_33_5_H_indp == 0:
        prob_33_5_H_indp += 0.01
    if prob_43_5_H_indp == 0:
        prob_43_5_H_indp += 0.01
    if prob_53_5_H_indp == 0:
        prob_53_5_H_indp += 0.01
    if prob_sh1_4_5_H_indp == 0:
        prob_sh1_4_5_H_indp += 0.01
    if prob_sh2_4_5_H_indp == 0:
        prob_sh2_4_5_H_indp += 0.01
    if prob_sh1_7_5_H_indp == 0:
        prob_sh1_7_5_H_indp += 0.01
    if prob_sh2_7_5_H_indp == 0:
        prob_sh2_7_5_H_indp += 0.01
    if prob_12_H_indp == 0:
        prob_12_H_indp += 0.01
    if prob_HW_H_indp == 0:
        prob_HW_H_indp += 0.01
    if prob_AW_H_indp == 0:
        prob_AW_H_indp += 0.01
    return [prob_HW_H_indp, prob_AW_H_indp, prob_33_5_H_indp, prob_43_5_H_indp, prob_53_5_H_indp, prob_sh1_4_5_H_indp,
            prob_sh1_7_5_H_indp, prob_sh2_4_5_H_indp, prob_sh2_7_5_H_indp, prob_12_H_indp]


def ht_indp_appender(prb_HW_H_indp, prb_AW_H_indp, prb_33_5_H_indp, prb_43_5_H_indp, prb_53_5_H_indp, prb_sh1_4_5_H_indp,
                     prb_sh1_7_5_H_indp, prb_sh2_4_5_H_indp, prb_sh2_7_5_H_indp, prb_12_H_indp):
    prob_HW_H_indps.append(prb_HW_H_indp)
    prob_AW_H_indps.append(prb_AW_H_indp)
    prob_33_5_H_indps.append(prb_33_5_H_indp)
    prob_43_5_H_indps.append(prb_43_5_H_indp)
    prob_53_5_H_indps.append(prb_53_5_H_indp)
    prob_sh1_4_5_H_indps.append(prb_sh1_4_5_H_indp)
    prob_sh1_7_5_H_indps.append(prb_sh1_7_5_H_indp)
    prob_sh2_4_5_H_indps.append(prb_sh2_4_5_H_indp)
    prob_sh2_7_5_H_indps.append(prb_sh2_7_5_H_indp)
    prob_12_H_indps.append(prb_12_H_indp)


def at_indp_aggregator(n, home_score, away_score, home_x, away_x):
    global valid_games_A_indp
    global count_AW_A_indp
    global count_33_5_A_indp
    global count_43_5_A_indp
    global count_53_5_A_indp
    global count_sh2_4_5_A_indp
    global count_sh2_7_5_A_indp
    global count_12_A_indp
    global count_12_A_indp

    valid_games_A_indp += 1
    if (int(home_score[n].text) > int(away_score[n].text)) and (home_x[n].text == away_teamx):
        count_AW_A_indp += 1
    if (int(away_score[n].text) > int(home_score[n].text)) and (away_x[n].text == away_teamx):
        count_AW_A_indp += 1
    if int(home_score[n].text) == int(away_score[n].text) and (int(home_score[n].text) > 0 and int(away_score[n].text) > 0):
        count_AW_A_indp += 0.33
    if int(home_score[n].text) == int(away_score[n].text) and (int(home_score[n].text) == 0 and int(away_score[n].text) == 0):
        count_AW_A_indp += 0
    if (int(home_score[n].text) + int(away_score[n].text)) >= 34 and (home_x[n].text == away_teamx) and int(home_score[n].text) >= 20:
        count_33_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 34 and (away_x[n].text == away_teamx) and int(away_score[n].text) >= 20:
        count_33_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 44 and (home_x[n].text == away_teamx) and int(home_score[n].text) >= 28:
        count_43_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 44 and (away_x[n].text == away_teamx) and int(away_score[n].text) >= 28:
        count_43_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 54 and (home_x[n].text == away_teamx) and int(home_score[n].text) >= 36:
        count_53_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 54 and (away_x[n].text == away_teamx) and int(away_score[n].text) >= 36:
        count_53_5_A_indp += 1
    if ((int(home_score[n].text) + 4.5) > int(away_score[n].text)) and (home_x[n].text == away_teamx):
        count_sh2_4_5_A_indp += 1
    if ((int(away_score[n].text) + 4.5) > int(home_score[n].text)) and (away_x[n].text == away_teamx):
        count_sh2_4_5_A_indp += 1
    if ((int(home_score[n].text) + 7.5) > int(away_score[n].text)) and (home_x[n].text == away_teamx):
        count_sh2_7_5_A_indp += 1
    if ((int(away_score[n].text) + 7.5) > int(home_score[n].text)) and (away_x[n].text == away_teamx):
        count_sh2_7_5_A_indp += 1
    if int(home_score[n].text) != int(away_score[n].text) and int(home_score[n].text) >= 1 and (home_x[n].text == away_teamx):
        count_12_A_indp += 1
    if int(away_score[n].text) != int(home_score[n].text) and int(away_score[n].text) >= 1 and (away_x[n].text == away_teamx):
        count_12_A_indp += 1


def at_indp_prob_calc():
    global valid_games_A_indp
    global count_AW_A_indp
    global count_33_5_A_indp
    global count_43_5_A_indp
    global count_53_5_A_indp
    global count_sh2_4_5_A_indp
    global count_sh2_7_5_A_indp
    global count_12_A_indp

    prob_AW_A_indp = float(count_AW_A_indp / valid_games_A_indp)
    prob_HW_A_indp = 1 - prob_AW_A_indp
    prob_33_5_A_indp = float(count_33_5_A_indp / valid_games_A_indp)
    prob_43_5_A_indp = float(count_43_5_A_indp / valid_games_A_indp)
    prob_53_5_A_indp = float(count_53_5_A_indp / valid_games_A_indp)
    prob_sh2_4_5_A_indp = float(count_sh2_4_5_A_indp / valid_games_A_indp)
    prob_sh2_7_5_A_indp = float(count_sh2_7_5_A_indp / valid_games_A_indp)
    prob_sh1_4_5_A_indp = 1 - prob_sh2_4_5_A_indp
    prob_sh1_7_5_A_indp = 1 - prob_sh2_7_5_A_indp
    prob_12_A_indp = float(count_12_A_indp / valid_games_A_indp)

    if prob_HW_A_indp == 1.0:
        prob_HW_A_indp -= 0.01
    if prob_AW_A_indp == 1.0:
        prob_AW_A_indp -= 0.01
    if prob_33_5_A_indp == 1.0:
        prob_33_5_A_indp -= 0.01
    if prob_43_5_A_indp == 1.0:
        prob_43_5_A_indp -= 0.01
    if prob_53_5_A_indp == 1.0:
        prob_53_5_A_indp -= 0.01
    if prob_sh1_4_5_A_indp == 1.0:
        prob_sh1_4_5_A_indp -= 0.01
    if prob_sh2_4_5_A_indp == 1.0:
        prob_sh2_4_5_A_indp -= 0.01
    if prob_sh1_7_5_A_indp == 1.0:
        prob_sh1_7_5_A_indp -= 0.01
    if prob_sh2_7_5_A_indp == 1.0:
        prob_sh2_7_5_A_indp -= 0.01
    if prob_12_A_indp == 1.0:
        prob_12_A_indp -= 0.01

    if prob_33_5_A_indp == 0:
        prob_33_5_A_indp += 0.01
    if prob_43_5_A_indp == 0:
        prob_43_5_A_indp += 0.01
    if prob_53_5_A_indp == 0:
        prob_53_5_A_indp += 0.01
    if prob_sh1_4_5_A_indp == 0:
        prob_sh1_4_5_A_indp += 0.01
    if prob_sh2_4_5_A_indp == 0:
        prob_sh2_4_5_A_indp += 0.01
    if prob_sh1_7_5_A_indp == 0:
        prob_sh1_7_5_A_indp += 0.01
    if prob_sh2_7_5_A_indp == 0:
        prob_sh2_7_5_A_indp += 0.01
    if prob_12_A_indp == 0:
        prob_12_A_indp += 0.01
    if prob_HW_A_indp == 0:
        prob_HW_A_indp += 0.01
    if prob_AW_A_indp == 0:
        prob_AW_A_indp += 0.01
    return [prob_HW_A_indp, prob_AW_A_indp, prob_33_5_A_indp, prob_43_5_A_indp, prob_53_5_A_indp, prob_sh1_4_5_A_indp,
            prob_sh1_7_5_A_indp, prob_sh2_4_5_A_indp, prob_sh2_7_5_A_indp, prob_12_A_indp]


def at_indp_appender(prb_HW_A_indp, prb_AW_A_indp, prb_33_5_A_indp, prb_43_5_A_indp, prb_53_5_A_indp, prb_sh1_4_5_A_indp,
                     prb_sh1_7_5_A_indp, prb_sh2_4_5_A_indp, prb_sh2_7_5_A_indp, prb_12_A_indp):
    prob_HW_A_indps.append(prb_HW_A_indp)
    prob_AW_A_indps.append(prb_AW_A_indp)
    prob_33_5_A_indps.append(prb_33_5_A_indp)
    prob_43_5_A_indps.append(prb_43_5_A_indp)
    prob_53_5_A_indps.append(prb_53_5_A_indp)
    prob_sh1_4_5_A_indps.append(prb_sh1_4_5_A_indp)
    prob_sh1_7_5_A_indps.append(prb_sh1_7_5_A_indp)
    prob_sh2_4_5_A_indps.append(prb_sh2_4_5_A_indp)
    prob_sh2_7_5_A_indps.append(prb_sh2_7_5_A_indp)
    prob_12_A_indps.append(prb_12_A_indp)


def home_counter():
    games_count_home = 0
    try:
        suby1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        for n in range(len(suby1)):
            dattee = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
            try:
                if int(dattee[n].text.split('.')[-1].strip()) >= YEAR:
                    games_count_home += 1
            except ValueError:
                print(f"Error at Count Home: {dattee[n].text}")
                if n + 1 != len(suby1):
                    games_count_home += 1
        home_nums_matches_played.append(games_count_home)
    except ElementNotInteractableException:
        home_nums_matches_played.append(0)
    except NoSuchElementException:
        home_nums_matches_played.append(0)


def away_counter():
    games_count_away = 0
    try:
        suby2 = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row')
        for n in range(len(suby2)):
            dattte = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
            try:
                if int(dattte[n].text.split('.')[-1].strip()) >= YEAR:
                    games_count_away += 1
            except ValueError:
                print(f"Error at Count Away: {dattte[n].text}")
                if n + 1 != len(suby2):
                    games_count_away += 1
        away_nums_matches_played.append(games_count_away)
    except ElementNotInteractableException:
        away_nums_matches_played.append(0)
    except NoSuchElementException:
        away_nums_matches_played.append(0)


def show_more_matches():
    try:
        shows = driver.find_elements(By.CSS_SELECTOR, '[class="h2h__showMore showMore"]')
        if len(shows) == 3:
            shows[0].click()
            sleep(0.1)
            shows[1].click()
            sleep(0.1)
            shows[2].click()
        elif len(shows) == 2:
            shows[0].click()
            sleep(0.1)
            shows[1].click()
        else:
            show = driver.find_element(By.CSS_SELECTOR, '[class="h2h__showMore showMore"]')
            show.click()
    except ElementClickInterceptedException:
        try:
            pass
        except ElementClickInterceptedException:
            pass
    except NoSuchElementException:
        pass


def home_form_checker(home_teamk):
    count_HW_form = 0
    count_HD_form = 0
    try:
        subx1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        if len(subx1) >= FORM_COUNT:
            dssc = 0
            for k in range(FORM_COUNT):
                datte = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
                homme_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
                awway_x = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
                homme_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:first-child')
                awway_score = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:last-child')
                try:
                    if int(datte[k].text.split('.')[-1].strip()) >= YEAR:
                        if (int(homme_score[k].text) > int(awway_score[k].text)) and (str(homme_x[k].text) == str(home_teamk)):
                            count_HW_form += 1
                        if (int(awway_score[k].text) > int(homme_score[k].text)) and (str(awway_x[k].text) == str(home_teamk)):
                            count_HW_form += 1
                        if int(homme_score[k].text) == int(awway_score[k].text):
                            count_HD_form += 1
                        dssc += 1
                    else:
                        print(f"Home Form Year Unaccepted: {int(datte[k].text.split('.')[-1].strip())}")
                        dssc += 1
                except ValueError:
                    print(f"Value Error at FORM Home : {datte[k].text} | {homme_x[k].text} vs {awway_x[k].text}")
                    print(f"ScoreH - {homme_score[k].text} : {awway_score[k].text}")
                    count_HD_form += 1
                    dssc += 1
            print(f"H-DSSC: {dssc}")
            if dssc >= FORM_COUNT:
                try:
                    H_form_W = float(count_HW_form / dssc)
                    H_form_D = float(count_HD_form / dssc)
                    H_form_L = float(1 - (H_form_W + H_form_D))
                    h_form_W.append(round(H_form_W, 1))
                    h_form_D.append(round(H_form_D, 1))
                    h_form_L.append(round(H_form_L, 1))
                except ZeroDivisionError:
                    h_form_W.append(0)
                    h_form_D.append(0)
                    h_form_L.append(0)
            else:
                h_form_W.append(0)
                h_form_D.append(0)
                h_form_L.append(0)
        else:
            h_form_W.append(0)
            h_form_D.append(0)
            h_form_L.append(0)
    except ElementNotInteractableException:
        h_form_W.append(0)
        h_form_D.append(0)
        h_form_L.append(0)


def away_form_checker(away_teamk):
    count_AW_form = 0
    count_AD_form = 0
    try:
        subx2 = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row')
        if len(subx2) >= FORM_COUNT:
            dssc = 0
            for n in range(FORM_COUNT):
                datte = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
                homme_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__homeParticipant .h2h__participantInner')
                awway_x = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__awayParticipant .h2h__participantInner')
                homme_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:first-child')
                awway_score = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:last-child')

                try:
                    if int(datte[n].text.split('.')[-1].strip()) >= YEAR:
                        if (int(homme_score[n].text) > int(awway_score[n].text)) and (str(homme_x[n].text) == str(away_teamk)):
                            count_AW_form += 1
                        if (int(awway_score[n].text) > int(homme_score[n].text)) and (str(awway_x[n].text) == str(away_teamk)):
                            count_AW_form += 1
                        if int(homme_score[n].text) == int(awway_score[n].text):
                            count_AD_form += 1
                        dssc += 1
                    else:
                        print(f"Away Form Year Unaccepted: {int(datte[n].text.split('.')[-1].strip())}")
                        dssc += 1
                except ValueError:
                    print(f"Error at FORM Away: {datte[n].text} | {homme_x[n].text} vs {awway_x[n].text}")
                    print(f"ScoreA - {homme_score[n].text} : {awway_score[n].text}")
                    count_AD_form += 1
                    dssc += 1
            print(f"A-DSSC: {dssc}")
            if dssc >= FORM_COUNT:
                try:
                    A_form_W = float(count_AW_form / dssc)
                    A_form_D = float(count_AD_form / dssc)
                    A_form_L = float(1 - (A_form_W + A_form_D))
                    a_form_W.append(round(A_form_W, 1))
                    a_form_D.append(round(A_form_D, 1))
                    a_form_L.append(round(A_form_L, 1))
                except ZeroDivisionError:
                    a_form_W.append(0)
                    a_form_D.append(0)
                    a_form_L.append(0)
            else:
                a_form_W.append(0)
                a_form_D.append(0)
                a_form_L.append(0)
        else:
            a_form_W.append(0)
            a_form_D.append(0)
            a_form_L.append(0)
    except ElementNotInteractableException:
        a_form_W.append(0)
        a_form_D.append(0)
        a_form_L.append(0)


def odds_checker():
    try:
        driver.find_element(By.LINK_TEXT, "ODDS").click()
        sleep(1)
        try:
            _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
            _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[2].text.strip()
            _1HWS.append(1 / float(_1HW))
            _2AWS.append(1 / float(_2AW))
        except NoSuchElementException:
            try:
                _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                _1HWS.append(1 / float(_1HW))
                _2AWS.append(1 / float(_2AW))
            except (ElementClickInterceptedException, ElementNotInteractableException):
                try:
                    driver.refresh()
                    sleep(2)
                    _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                    _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                    _1HWS.append(1 / float(_1HW))
                    _2AWS.append(1 / float(_2AW))
                except (NoSuchElementException, IndexError):
                    _1HWS.append(0.5)
                    _2AWS.append(0.5)
            except (NoSuchElementException, IndexError):
                _1HWS.append(0.5)
                _2AWS.append(0.5)
                print("No 1X2 ODDS")
        except IndexError:
            try:
                driver.find_element(By.LINK_TEXT, "HOME/AWAY").click()
                _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                _1HWS.append(1 / float(_1HW))
                _2AWS.append(1 / float(_2AW))
            except (NoSuchElementException, IndexError, ElementNotInteractableException,
                    ElementClickInterceptedException, StaleElementReferenceException):
                _1HWS.append(0.5)
                _2AWS.append(0.5)
                print("No 1X2 ODDS")
        try:
            try:
                driver.find_element(By.LINK_TEXT, "DC").click()
            except (ElementClickInterceptedException, ElementNotInteractableException):
                pass
            _12 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
            _12S.append(1 / float(_12))
        except (NoSuchElementException, IndexError):
            try:
                _12 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                _12S.append(1 / float(_12))
            except (NoSuchElementException, IndexError):
                _12S.append(rdm.choice(CONFINTVLS))
                print("No DC")
        try:
            try:
                driver.find_element(By.LINK_TEXT, "AH").click()
            except (ElementClickInterceptedException, ElementNotInteractableException):
                pass
            ahl = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds')
            for y in range(len(ahl)):
                try:
                    id_sh_4_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_sh_4_5 == "+4.5":
                        OVER_sh1_4_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_sh1_4_5_S.append(1 / float(OVER_sh1_4_5))
                        OVER_sh2_4_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                        OVER_sh2_4_5_S.append(1 / float(OVER_sh2_4_5))
                        break
                    if y == (len(ahl) - 1):
                        OVER_sh1_4_5_S.append(0.5)
                        OVER_sh2_4_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_sh1_4_5_S.append(0.5)
                    OVER_sh2_4_5_S.append(0.5)

            for y in range(len(ahl)):
                try:
                    id_sh_7_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_sh_7_5 == "+7.5":
                        OVER_sh1_7_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_sh1_7_5_S.append(1 / float(OVER_sh1_7_5))
                        OVER_sh2_7_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                        OVER_sh2_7_5_S.append(1 / float(OVER_sh2_7_5))
                        break
                    if y == (len(ahl) - 1):
                        OVER_sh1_7_5_S.append(0.5)
                        OVER_sh2_7_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_sh1_7_5_S.append(0.5)
                    OVER_sh2_7_5_S.append(0.5)
        except (NoSuchElementException, IndexError, ElementNotInteractableException,
                ElementClickInterceptedException, StaleElementReferenceException):
            OVER_sh1_4_5_S.append(0.5)
            OVER_sh1_7_5_S.append(0.5)
            OVER_sh2_4_5_S.append(0.5)
            OVER_sh2_7_5_S.append(0.5)
            print("No AH")
        try:
            try:
                driver.find_element(By.LINK_TEXT, "O/U").click()
            except (ElementClickInterceptedException, ElementNotInteractableException):
                pass
            ahl = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds')
            for x in range(len(ahl)):
                try:
                    id_33_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_33_5 == "33.5":
                        OVER_33_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_33_5_S.append(1 / float(OVER_33_5))
                        break
                    if x == (len(ahl) - 1):
                        OVER_33_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_33_5_S.append(0.5)
            for x in range(len(ahl)):
                try:
                    id_43_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_43_5 == "43.5":
                        OVER_43_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_43_5_S.append(1 / float(OVER_43_5))
                        break
                    if x == (len(ahl) - 1):
                        OVER_43_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_43_5_S.append(0.5)
            for z in range(len(ahl)):
                try:
                    id_53_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_53_5 == "53.5":
                        OVER_53_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_53_5_S.append(1 / float(OVER_53_5))
                        break
                    if z == (len(ahl) - 1):
                        OVER_53_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_53_5_S.append(0.5)
        except (NoSuchElementException, IndexError, ElementNotInteractableException,
                ElementClickInterceptedException, StaleElementReferenceException):
            OVER_33_5_S.append(0.5)
            OVER_43_5_S.append(0.5)
            OVER_53_5_S.append(0.5)
            print("No O/U")
    except (StaleElementReferenceException, NoSuchElementException):
        driver.refresh()
        sleep(3)
        _1HWS.append(0.5)
        _2AWS.append(0.5)
        OVER_33_5_S.append(0.5)
        OVER_43_5_S.append(0.5)
        OVER_53_5_S.append(0.5)
        OVER_sh1_4_5_S.append(0.5)
        OVER_sh1_7_5_S.append(0.5)
        OVER_sh2_4_5_S.append(0.5)
        OVER_sh2_7_5_S.append(0.5)
        _12S.append(rdm.choice(CONFINTVLS))
        print("All Odds are assumed to be 0.5")


def writer(w, A, B, C, data):
    data.write(f"{countries[w]}|{leagues[w]}|{home_teams[w]}|{away_teams[w]}|{home_positions[w]}|"
               f"{away_positions[w]}|{home_nums_matches_played[w]}|{away_nums_matches_played[w]}|{home_points[w]}|"
               f"{away_points[w]}|{h_form_W[w]}|{h_form_D[w]}|{h_form_L[w]}|{a_form_W[w]}|{a_form_D[w]}|{a_form_L[w]}|"
               f"{ht_g_avgs[w]}|{at_g_avgs[w]}|{bth_g_avgs[w]}|{bta_g_avgs[w]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[w]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[w]}|"
               f"{OUTCOMES[2]}:-{bayesian_33_5_d[w]}|{OUTCOMES[3]}:-{bayesian_43_5_d[w]}|"
               f"{OUTCOMES[4]}:-{bayesian_53_5_d[w]}|{OUTCOMES[5]}:-{bayesian_sh1_4_5_d[w]}|{OUTCOMES[6]}:-{bayesian_sh1_7_5_d[w]}|"
               f"{OUTCOMES[7]}:-{bayesian_sh2_4_5_d[w]}|{OUTCOMES[8]}:-{bayesian_sh2_7_5_d[w]}|{OUTCOMES[9]}:-{bayesian_12_d[w]}|"
               f"{match_times[w]}|{sport}|{C}_{A}_{B}|{set_date_s_size()[0]}\n")


def writer1(y, F, G, H, J, data):
    data.write(f"{countries[y]}|{leagues[y]}|{home_teams[y]}|{away_teams[y]}|{home_positions[y]}|"
               f"{away_positions[y]}|{home_nums_matches_played[y]}|{away_nums_matches_played[y]}|{home_points[y]}|"
               f"{away_points[y]}|{h_form_W[y]}|{h_form_D[y]}|{h_form_L[y]}|{a_form_W[y]}|{a_form_D[y]}|{a_form_L[y]}|"
               f"{ht_g_avgs[y]}|{at_g_avgs[y]}|{bth_g_avgs[y]}|{bta_g_avgs[y]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[y]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[y]}|"
               f"{OUTCOMES[2]}:-{bayesian_33_5_d[y]}|{OUTCOMES[3]}:-{bayesian_43_5_d[y]}|"
               f"{OUTCOMES[4]}:-{bayesian_53_5_d[y]}|{OUTCOMES[5]}:-{bayesian_sh1_4_5_d[y]}|{OUTCOMES[6]}:-{bayesian_sh1_7_5_d[y]}|"
               f"{OUTCOMES[7]}:-{bayesian_sh2_4_5_d[y]}|{OUTCOMES[8]}:-{bayesian_sh2_7_5_d[y]}|{OUTCOMES[9]}:-{bayesian_12_d[y]}|"
               f"{match_times[y]}|{sport}|{J}_{F}_{G}_{H}|{set_date_s_size()[0]}\n")


def writer2(z, K, L, M, N, P, data):
    data.write(f"{countries[z]}|{leagues[z]}|{home_teams[z]}|{away_teams[z]}|{home_positions[z]}|"
               f"{away_positions[z]}|{home_nums_matches_played[z]}|{away_nums_matches_played[z]}|{home_points[z]}|"
               f"{away_points[z]}|{h_form_W[z]}|{h_form_D[z]}|{h_form_L[z]}|{a_form_W[z]}|{a_form_D[z]}|{a_form_L[z]}|"
               f"{ht_g_avgs[z]}|{at_g_avgs[z]}|{bth_g_avgs[z]}|{bta_g_avgs[z]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[z]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[z]}|"
               f"{OUTCOMES[2]}:-{bayesian_33_5_d[z]}|{OUTCOMES[3]}:-{bayesian_43_5_d[z]}|"
               f"{OUTCOMES[4]}:-{bayesian_53_5_d[z]}|{OUTCOMES[5]}:-{bayesian_sh1_4_5_d[z]}|{OUTCOMES[6]}:-{bayesian_sh1_7_5_d[z]}|"
               f"{OUTCOMES[7]}:-{bayesian_sh2_4_5_d[z]}|{OUTCOMES[8]}:-{bayesian_sh2_7_5_d[z]}|{OUTCOMES[9]}:-{bayesian_12_d[z]}|"
               f"{match_times[z]}|{sport}|{P}_{K}_{L}_{M}_{N}|{set_date_s_size()[0]}\n")


def baye_appender(baye_HW, baye_AW, baye_33_5, baye_43_5, baye_53_5, baye_sh1_4_5, baye_sh1_7_5, baye_sh2_4_5,
                  baye_sh2_7_5, baye_12):
    bayesian_home_Win_d.append(round((float(baye_HW)), 4))
    bayesian_away_Win_d.append(round((float(baye_AW)), 4))
    bayesian_33_5_d.append(round((float(baye_33_5)), 4))
    bayesian_43_5_d.append(round((float(baye_43_5)), 4))
    bayesian_53_5_d.append(round((float(baye_53_5)), 4))
    bayesian_sh1_4_5_d.append(round((float(baye_sh1_4_5)), 4))
    bayesian_sh1_7_5_d.append(round((float(baye_sh1_7_5)), 4))
    bayesian_sh2_4_5_d.append(round((float(baye_sh2_4_5)), 4))
    bayesian_sh2_7_5_d.append(round((float(baye_sh2_7_5)), 4))
    bayesian_12_d.append(round((float(baye_12)), 4))


def scheduler():
    driver.refresh()
    if date_time != tmrw_date:
        try:
            driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
            sleep(1)
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
            try:
                driver.refresh()
                sleep(5)
                driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
                sleep(1)
            except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
                traceback.print_exc()
    try:
        driver.find_element(By.CSS_SELECTOR, ".filters__group .filters__tab:last-child").click()
        sleep(1)
    except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
        try:
            driver.refresh()
            sleep(5)
            if date_time != tmrw_date:
                driver.find_element(By.CSS_SELECTOR, '[title="Next day"]').click()
                sleep(1)
            driver.find_element(By.CSS_SELECTOR, ".filters__group .filters__tab:last-child").click()
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException):
            traceback.print_exc()


def total_aggregator():
    global valid_games
    global valid_games_H_indp
    global valid_games_A_indp

    try:
        sub1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        if len(sub1) == 0:
            ht_indp_appender(prb_HW_H_indp=0.01, prb_AW_H_indp=0.01, prb_33_5_H_indp=0.01, prb_43_5_H_indp=0.01,
                             prb_53_5_H_indp=0.01, prb_sh1_4_5_H_indp=0.01, prb_sh1_7_5_H_indp=0.01,
                             prb_sh2_4_5_H_indp=0.01, prb_sh2_7_5_H_indp=0.01, prb_12_H_indp=0.01)
            ht_scores = []
            for r in range(DSCRM_H_A):
                ht_scores.append(rdm.uniform(0, 3))
            try:
                hts_mean = stats.mean(ht_scores)
                if hts_mean > 0:
                    ht_g_avgs.append(round(hts_mean, 2))
                else:
                    ht_g_avgs.append(0)
            except stats.StatisticsError:
                ht_g_avgs.append(0)
        else:
            dsc = 0
            ht_scores = []
            for a in range(DSCRM_H_A):
                date_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__date')
                home_x_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
                away_x_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
                home_score_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:first-child')
                away_score_ = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row .h2h__result span:last-child')
                try:
                    if YEAR <= int(date_[a].text.split('.')[-1].strip()) < 90:
                        ht_indp_aggregator(k=a, home_score=home_score_, away_score=away_score_, home_x=home_x_, away_x=away_x_)
                        ht_g_avg_aggregator(m=a, home_score=home_score_, away_score=away_score_, home_x=home_x_, away_x=away_x_, home_scores=ht_scores)
                        dsc += 1
                    else:
                        print(f"Date Error at Home1 : {date_[a].text}")
                        valid_games_H_indp += 1
                        dsc += 1
                except ValueError:
                    print(f"Value Error at Home1 : {date_[a].text} | {home_x_[a].text} vs {away_x_[a].text}")
                    print(f"Score1H - {home_score_[a].text} : {away_score_[a].text}")
                    valid_games_H_indp += 1
                    dsc += 1
                except IndexError:
                    valid_games_H_indp += 1
                    dsc += 1
            try:
                hts_mean = stats.mean(ht_scores)
                if hts_mean > 0:
                    ht_g_avgs.append(round(hts_mean, 2))
                else:
                    ht_g_avgs.append(0)
            except stats.StatisticsError:
                ht_g_avgs.append(0)
            if dsc >= DSCRM_H_A:
                try:
                    ht_indp_values = ht_indp_prob_calc()
                    ht_indp_appender(prb_HW_H_indp=ht_indp_values[0], prb_AW_H_indp=ht_indp_values[1],
                                     prb_33_5_H_indp=ht_indp_values[2], prb_43_5_H_indp=ht_indp_values[3],
                                     prb_53_5_H_indp=ht_indp_values[4], prb_sh1_4_5_H_indp=ht_indp_values[5],
                                     prb_sh1_7_5_H_indp=ht_indp_values[6], prb_sh2_4_5_H_indp=ht_indp_values[7],
                                     prb_sh2_7_5_H_indp=ht_indp_values[8], prb_12_H_indp=ht_indp_values[9])
                except ZeroDivisionError:
                    ht_indp_appender(prb_HW_H_indp=0.01, prb_AW_H_indp=0.01, prb_33_5_H_indp=0.01, prb_43_5_H_indp=0.01,
                                     prb_53_5_H_indp=0.01, prb_sh1_4_5_H_indp=0.01, prb_sh1_7_5_H_indp=0.01,
                                     prb_sh2_4_5_H_indp=0.01, prb_sh2_7_5_H_indp=0.01, prb_12_H_indp=0.01)
            else:
                ht_indp_appender(prb_HW_H_indp=0.01, prb_AW_H_indp=0.01, prb_33_5_H_indp=0.01, prb_43_5_H_indp=0.01,
                                 prb_53_5_H_indp=0.01, prb_sh1_4_5_H_indp=0.01, prb_sh1_7_5_H_indp=0.01,
                                 prb_sh2_4_5_H_indp=0.01, prb_sh2_7_5_H_indp=0.01, prb_12_H_indp=0.01)
    except ElementNotInteractableException:
        ht_indp_appender(prb_HW_H_indp=0.01, prb_AW_H_indp=0.01, prb_33_5_H_indp=0.01, prb_43_5_H_indp=0.01,
                         prb_53_5_H_indp=0.01, prb_sh1_4_5_H_indp=0.01, prb_sh1_7_5_H_indp=0.01,
                         prb_sh2_4_5_H_indp=0.01, prb_sh2_7_5_H_indp=0.01, prb_12_H_indp=0.01)
    sleep(0.1)
    try:
        sub2 = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row')
        if len(sub2) == 0:
            at_indp_appender(prb_HW_A_indp=0.01, prb_AW_A_indp=0.01, prb_33_5_A_indp=0.01, prb_43_5_A_indp=0.01,
                             prb_53_5_A_indp=0.01, prb_sh1_4_5_A_indp=0.01, prb_sh1_7_5_A_indp=0.01,
                             prb_sh2_4_5_A_indp=0.01, prb_sh2_7_5_A_indp=0.01, prb_12_A_indp=0.01)
            at_scores = []
            for r in range(DSCRM_H_A):
                at_scores.append(rdm.uniform(0, 3))
            try:
                ats_mean = stats.mean(at_scores)
                if ats_mean > 0:
                    at_g_avgs.append(round(ats_mean, 2))
                else:
                    at_g_avgs.append(0)
            except stats.StatisticsError:
                at_g_avgs.append(0)
        else:
            dsc = 0
            at_scores = []
            for b in range(DSCRM_H_A):
                date__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
                home_x__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__homeParticipant .h2h__participantInner')
                away_x__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__awayParticipant .h2h__participantInner')
                home_score__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:first-child')
                away_score__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__result span:last-child')
                try:
                    if YEAR <= int(date__[b].text.split('.')[-1].strip()) < 90:
                        at_indp_aggregator(n=b, home_score=home_score__, away_score=away_score__, home_x=home_x__, away_x=away_x__)
                        at_g_avg_aggregator(m=b, home_score=home_score__, away_score=away_score__, home_x=home_x__, away_x=away_x__, away_scores=at_scores)
                        dsc += 1
                    else:
                        print(f"Date Error at Away1: {date__[b].text}")
                        valid_games_A_indp += 1
                        dsc += 1
                except ValueError:
                    print(f"Error at Away1: {date__[b].text} | {home_x__[b].text} vs {away_x__[b].text}")
                    print(f"Score1A - {home_score__[b].text} : {away_score__[b].text}")
                    valid_games_A_indp += 1
                    dsc += 1
                except IndexError:
                    valid_games_A_indp += 1
                    dsc += 1
            try:
                ats_mean = stats.mean(at_scores)
                if ats_mean > 0:
                    at_g_avgs.append(round(ats_mean, 2))
                else:
                    at_g_avgs.append(0)
            except stats.StatisticsError:
                at_g_avgs.append(0)
            if dsc >= DSCRM_H_A:
                try:
                    at_indp_values = at_indp_prob_calc()
                    at_indp_appender(prb_HW_A_indp=at_indp_values[0], prb_AW_A_indp=at_indp_values[1],
                                     prb_33_5_A_indp=at_indp_values[2], prb_43_5_A_indp=at_indp_values[3],
                                     prb_53_5_A_indp=at_indp_values[4], prb_sh1_4_5_A_indp=at_indp_values[5],
                                     prb_sh1_7_5_A_indp=at_indp_values[6], prb_sh2_4_5_A_indp=at_indp_values[7],
                                     prb_sh2_7_5_A_indp=at_indp_values[8], prb_12_A_indp=at_indp_values[9])
                except ZeroDivisionError:
                    at_indp_appender(prb_HW_A_indp=0.01, prb_AW_A_indp=0.01, prb_33_5_A_indp=0.01, prb_43_5_A_indp=0.01,
                                     prb_53_5_A_indp=0.01, prb_sh1_4_5_A_indp=0.01, prb_sh1_7_5_A_indp=0.01,
                                     prb_sh2_4_5_A_indp=0.01, prb_sh2_7_5_A_indp=0.01, prb_12_A_indp=0.01)
            else:
                at_indp_appender(prb_HW_A_indp=0.01, prb_AW_A_indp=0.01, prb_33_5_A_indp=0.01, prb_43_5_A_indp=0.01,
                                 prb_53_5_A_indp=0.01, prb_sh1_4_5_A_indp=0.01, prb_sh1_7_5_A_indp=0.01,
                                 prb_sh2_4_5_A_indp=0.01, prb_sh2_7_5_A_indp=0.01, prb_12_A_indp=0.01)
    except ElementNotInteractableException:
        at_indp_appender(prb_HW_A_indp=0.01, prb_AW_A_indp=0.01, prb_33_5_A_indp=0.01, prb_43_5_A_indp=0.01,
                         prb_53_5_A_indp=0.01, prb_sh1_4_5_A_indp=0.01, prb_sh1_7_5_A_indp=0.01,
                         prb_sh2_4_5_A_indp=0.01, prb_sh2_7_5_A_indp=0.01, prb_12_A_indp=0.01)
    sleep(0.1)
    try:
        sub3 = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row')
        if len(sub3) == 0:
            h2h_appender(prb_HW=0.01, prb_AW=0.01, prb_33_5=0.01, prb_43_5=0.01, prb_53_5=0.01, prb_sh1_4_5=0.01,
                         prb_sh1_7_5=0.01, prb_sh2_4_5=0.01, prb_sh2_7_5=0.01, prb_12=0.01)
            bth_scores = []
            bta_scores = []
            for r in range(DSCRM_BT):
                bth_scores.append(rdm.uniform(0, 3))
                bta_scores.append(rdm.uniform(0, 3))
            try:
                bths_mean = stats.mean(bth_scores)
                btas_mean = stats.mean(bta_scores)
                if btas_mean > 0 and bths_mean > 0:
                    bth_g_avgs.append(round(bths_mean, 2))
                    bta_g_avgs.append(round(btas_mean, 2))
                else:
                    bth_g_avgs.append(0)
                    bta_g_avgs.append(0)
            except stats.StatisticsError:
                bth_g_avgs.append(0)
                bta_g_avgs.append(0)
        else:
            dsc = 0
            bth_scores = []
            bta_scores = []
            for c in range(DSCRM_BT):
                date___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__date')
                home_x___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
                away_x___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
                home_score___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result span:first-child')
                away_score___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__result span:last-child')
                try:
                    if YEAR <= int(date___[c].text.split('.')[-1].strip()) < 90:
                        h2h_aggregator(m=c, home_score=home_score___, away_score=away_score___, home_x=home_x___, away_x=away_x___)
                        bt_g_avg_aggregator(m=c, home_score=home_score___, away_score=away_score___, home_x=home_x___, away_x=away_x___, bt_home_scores=bth_scores, bt_away_scores=bta_scores)
                        dsc += 1
                    else:
                        print(f"Date Error at 1H2H: {date___[c].text}")
                        valid_games += 1
                        dsc += 1
                except ValueError:
                    print(f"Value Error at 1H2H: {date___[c].text} | {home_x___[c].text} vs {away_x___[c].text}")
                    print(f"Score1H2H - {home_score___[c].text} : {away_score___[c].text}")
                    valid_games += 1
                    dsc += 1
                except IndexError:
                    valid_games += 1
                    dsc += 1
            try:
                bths_mean = stats.mean(bth_scores)
                btas_mean = stats.mean(bta_scores)
                if btas_mean > 0 and bths_mean > 0:
                    bth_g_avgs.append(round(bths_mean, 2))
                    bta_g_avgs.append(round(btas_mean, 2))
                else:
                    bth_g_avgs.append(0)
                    bta_g_avgs.append(0)
            except stats.StatisticsError:
                bth_g_avgs.append(0)
                bta_g_avgs.append(0)
            if dsc >= DSCRM_BT:
                try:
                    h2h_values = h2h_prob_calc()
                    h2h_appender(prb_HW=h2h_values[0], prb_AW=h2h_values[1], prb_33_5=h2h_values[2], prb_43_5=h2h_values[3],
                                 prb_53_5=h2h_values[4], prb_sh1_4_5=h2h_values[5], prb_sh1_7_5=h2h_values[6],
                                 prb_sh2_4_5=h2h_values[7], prb_sh2_7_5=h2h_values[8], prb_12=h2h_values[9])
                except ZeroDivisionError:
                    h2h_appender(prb_HW=0.01, prb_AW=0.01, prb_33_5=0.01, prb_43_5=0.01, prb_53_5=0.01, prb_sh1_4_5=0.01,
                                 prb_sh1_7_5=0.01, prb_sh2_4_5=0.01, prb_sh2_7_5=0.01, prb_12=0.01)
            else:
                h2h_appender(prb_HW=0.01, prb_AW=0.01, prb_33_5=0.01, prb_43_5=0.01, prb_53_5=0.01, prb_sh1_4_5=0.01,
                             prb_sh1_7_5=0.01, prb_sh2_4_5=0.01, prb_sh2_7_5=0.01, prb_12=0.01)
    except ElementNotInteractableException:
        h2h_appender(prb_HW=0.01, prb_AW=0.01, prb_33_5=0.01, prb_43_5=0.01, prb_53_5=0.01, prb_sh1_4_5=0.01,
                     prb_sh1_7_5=0.01, prb_sh2_4_5=0.01, prb_sh2_7_5=0.01, prb_12=0.01)


def print_all_data():
    print(f"Countries: {countries}")
    print(f"Leagues: {leagues}")
    print(f"Home Teams: {home_teams}")
    print(f"Home Positions: {home_positions}")
    print(f"Home Points: {home_points}")
    print(f"Home No Matches Played: {home_nums_matches_played}")
    print(f"Away Teams: {away_teams}")
    print(f"Away Positions: {away_positions}")
    print(f"Away Points: {away_points}")
    print(f"Away No Matches Played: {away_nums_matches_played}")
    print(f"Match Times: {match_times}")
    print(f"Home W Form: {h_form_W}")
    print(f"Home D Form: {h_form_D}")
    print(f"Home L Form: {h_form_L}")
    print(f"Away W Form: {a_form_W}")
    print(f"Away D Form: {a_form_D}")
    print(f"Away L Form: {a_form_L}")
    print(f"Prob 33_5s: {prob_33_5s}")
    print(f"Prob 43_5s: {prob_43_5s}")
    print(f"Prob 53_5s: {prob_53_5s}")
    print(f"Prob sh1_1_43_5s: {prob_sh1_4_5s}")
    print(f"Prob sh1_2_43_5s: {prob_sh1_7_5s}")
    print(f"Prob sh2_1_43_5s: {prob_sh2_4_5s}")
    print(f"Prob sh2_2_43_5s: {prob_sh2_7_5s}")
    print(f"Prob 12s: {prob_12s}")
    print(f"Prob HWs: {prob_HWs}")
    print(f"Prob AWs: {prob_AWs}")
    print(f"Prob 33_5_H_indps: {prob_33_5_H_indps}")
    print(f"Prob 43_5_H_indps: {prob_43_5_H_indps}")
    print(f"Prob 53_5_H_indps: {prob_53_5_H_indps}")
    print(f"Prob sh1_4_5_H_indps: {prob_sh1_4_5_H_indps}")
    print(f"Prob sh1_7_5_H_indps: {prob_sh1_7_5_H_indps}")
    print(f"Prob sh2_4_5_H_indps: {prob_sh2_4_5_H_indps}")
    print(f"Prob sh2_7_5_H_indps: {prob_sh2_7_5_H_indps}")
    print(f"Prob 12_H_indps: {prob_12_H_indps}")
    print(f"Prob HW_H_indps: {prob_HW_H_indps}")
    print(f"Prob AW_H_indps: {prob_AW_H_indps}")
    print(f"Prob 33_5_A_indps: {prob_33_5_A_indps}")
    print(f"Prob 43_5_A_indps: {prob_43_5_A_indps}")
    print(f"Prob 53_5_A_indps: {prob_53_5_A_indps}")
    print(f"Prob sh1_4_5_A_indps: {prob_sh1_4_5_A_indps}")
    print(f"Prob 12_A_indps: {prob_12_A_indps}")
    print(f"Prob HW_A_indps: {prob_HW_A_indps}")
    print(f"Prob AW_A_indps: {prob_AW_A_indps}")
    print(f"Bayesian Home Win: {bayesian_home_Win_d}")
    print(f"Bayesian Away Win: {bayesian_away_Win_d}")
    print(f"Bayesian 4.5: {bayesian_33_5_d}")
    print(f"Bayesian 5.5: {bayesian_43_5_d}")
    print(f"Bayesian 6.5: {bayesian_53_5_d}")
    print(f"Bayesian sh1_4_5: {bayesian_sh1_4_5_d}")
    print(f"Bayesian 12: {bayesian_12_d}")
    print(f"Odds _1HWS: {_1HWS}")
    print(f"Odds _2AWS: {_2AWS}")
    print(f"Odds OVER_33_5_S: {OVER_33_5_S}")
    print(f"Odds OVER_43_5_S: {OVER_43_5_S}")
    print(f"Odds OVER_53_5_S: {OVER_53_5_S}")
    print(f"Odds OVER_sh1_4_5_S: {OVER_sh1_4_5_S}")
    print(f"Odds _12S: {_12S}")
    print(f"Countries: {len(countries)}, Leagues: {len(leagues)}, Home Teams: {len(home_teams)}, "
          f"Home Positions: {len(home_positions)}, Home Points: {len(home_points)}, "
          f"Home No Matches Played: {len(home_nums_matches_played)}, Away Teams: {len(away_teams)}, "
          f"Away Positions: {len(away_positions)}, Away Points: {len(away_points)}, "
          f"Away No Matches Played: {len(away_nums_matches_played)}, Match Times: {len(match_times)} "
          f"Home W Form: {len(h_form_W)}, Home D Form: {len(h_form_D)}, Home L Form: {len(h_form_L)}, "
          f"Away W Form: {len(a_form_W)}, Away D Form: {len(a_form_D)}, Away L Form: {len(a_form_L)}"
          f"Prob 33_5s: {len(prob_33_5s)}, Prob 43_5s: {len(prob_43_5s)} Prob 53_5s: {len(prob_53_5s)}, Prob 43_5s: {len(prob_sh1_4_5s)},"
          f"Prob 12s: {len(prob_12s)}, Prob HWs: {len(prob_HWs)}, Prob AWs: {len(prob_AWs)}, "
          f"Prob 33_5_H_indps: {len(prob_33_5_H_indps)}, Prob 43_5_H_indps: {len(prob_43_5_H_indps)}, Prob 53_5_H_indps: {len(prob_53_5_H_indps)}, "
          f"Prob 43_5_H_indps: {len(prob_sh1_4_5_H_indps)}, Prob 12_H_indps: {len(prob_12_H_indps)},"
          f"Prob HW_H_indps: {len(prob_HW_H_indps)}, Prob AW_H_indps: {len(prob_AW_H_indps)}, "
          f"Prob 33_5_A_indps: {len(prob_33_5_A_indps)}, Prob 43_5_A_indps: {len(prob_43_5_A_indps)}, Prob 53_5_A_indps: {len(prob_53_5_A_indps)}, "
          f"Prob sh1_4_5_A_indps: {len(prob_sh1_4_5_A_indps)}, Prob 12_A_indps: {len(prob_12_A_indps)}, "
          f"Prob HW_A_indps: {len(prob_HW_A_indps)}, Prob AW_A_indps: {len(prob_AW_A_indps)}, "
          f"Odds _1HWS: {len(_1HWS)}, Odds _2AWS: {len(_2AWS)}, Odds OVER_33_5_S: {len(OVER_43_5_S)},  Odds OVER_43_5_S: {len(OVER_43_5_S)}, "
          f"Odds OVER_53_5_S: {len(OVER_53_5_S)}, Odds OVER_sh1_4_5_S: {len(OVER_sh1_4_5_S)}, Odds _12S: {len(_12S)}"
          f"Bayesian Home Win: {len(bayesian_home_Win_d)}, Bayesian Away Win: {len(bayesian_away_Win_d)}, "
          f"Bayesian 33_5: {len(bayesian_33_5_d)}, Bayesian 5.5: {len(bayesian_43_5_d)}, Bayesian 6.5: {len(bayesian_53_5_d)}, "
          f"Bayesian sh1_4_5: {len(bayesian_sh1_4_5_d)}, Bayesian 12: {len(bayesian_12_d) }")
    print(f"HTGAVG: {ht_g_avgs}")
    print(f"ATGAVG: {at_g_avgs}")
    print(f"HTGAVG: {len(ht_g_avgs)}")
    print(f"ATGAVG: {len(at_g_avgs)}")
    print(f"BTHGAVG: {bth_g_avgs}")
    print(f"BTAGAVG: {bta_g_avgs}")
    print(f"BTHGAVG: {len(bth_g_avgs)}")
    print(f"BTAGAVG: {len(bta_g_avgs)}")


countries = []
home_teams = []
away_teams = []
leagues = []
home_positions = []
away_positions = []
home_points = []
away_points = []
match_times = []
home_nums_matches_played = []
away_nums_matches_played = []
ht_g_avgs = []
at_g_avgs = []
bth_g_avgs = []
bta_g_avgs = []
h_form_W = []
h_form_L = []
h_form_D = []
a_form_W = []
a_form_D = []
a_form_L = []
prob_33_5s = []
prob_43_5s = []
prob_53_5s = []
prob_sh1_4_5s = []
prob_sh1_7_5s = []
prob_sh2_4_5s = []
prob_sh2_7_5s = []
prob_12s = []
prob_HWs = []
prob_AWs = []
prob_33_5_H_indps = []
prob_43_5_H_indps = []
prob_53_5_H_indps = []
prob_sh1_4_5_H_indps = []
prob_sh1_7_5_H_indps = []
prob_sh2_4_5_H_indps = []
prob_sh2_7_5_H_indps = []
prob_12_H_indps = []
prob_HW_H_indps = []
prob_AW_H_indps = []
prob_33_5_A_indps = []
prob_43_5_A_indps = []
prob_53_5_A_indps = []
prob_sh1_4_5_A_indps = []
prob_sh1_7_5_A_indps = []
prob_sh2_4_5_A_indps = []
prob_sh2_7_5_A_indps = []
prob_12_A_indps = []
prob_HW_A_indps = []
prob_AW_A_indps = []
home_z_prob = []
away_z_prob = []
diff_z_prob = []
_1HWS = []
_2AWS = []
OVER_33_5_S = []
OVER_43_5_S = []
OVER_53_5_S = []
OVER_sh1_4_5_S = []
OVER_sh1_7_5_S = []
OVER_sh2_4_5_S = []
OVER_sh2_7_5_S = []
_12S = []


# if date_time != tmrw_date:
try:
    hidden_matches = driver.find_elements(By.CSS_SELECTOR, '[class="arrow event__expander event__expander--close"]')
    print(len(hidden_matches))
    for hidden_m in hidden_matches:
        try:
            hidden_m.click()
        except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
            pass
except NoSuchElementException:
    print("No Hidden Matches")


divs = driver.find_elements(By.CSS_SELECTOR, f'.{sport} .event__match--scheduled')
print(len(divs))

try:
    sub_m_t = []
    match_timez = driver.find_elements(By.CLASS_NAME, 'event__time')
    for m_t in range(len(match_timez)):
        sub_m_t.append(match_timez[m_t].text.split('\n')[0])
except StaleElementReferenceException:
    driver.refresh()
    sleep(2)
    scheduler()
    sub_m_t = []
    match_timez = driver.find_elements(By.CLASS_NAME, 'event__time')
    for m_t in range(len(match_timez)):
        sub_m_t.append(match_timez[m_t].text.split('\n')[0])
print(f"Length of Match lists: {len(sub_m_t)}")

for i in range(len(sub_m_t)):
    try:
        divs[i].click()
    except (IndexError, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
        scheduler()
        try:
            divs = driver.find_elements(By.CSS_SELECTOR, f'.{sport} .event__match--scheduled')
            divs[i].click()
        except IndexError:
            try:
                divs = driver.find_elements(By.CSS_SELECTOR, f'.{sport} .event__match--scheduled')
                divs[i].click()
            except IndexError:
                traceback.print_exc()
                break

    print(f"{sport}:- {i + 1}/{len(sub_m_t)}")
    sleep(0.1)
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    try:
        home_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__home  .participant__participantName a').text
        away_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__away  .participant__participantName a').text
    except (NoSuchElementException, IndexError, ElementNotInteractableException):
        try:
            driver.refresh()
            sleep(2)
            driver.refresh()
            sleep(1)
            home_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__home  .participant__participantName a').text
            away_teamx = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__away  .participant__participantName a').text
        except (NoSuchElementException, IndexError):
            driver.close()
            driver.switch_to.window(window_before)
            traceback.print_exc()
            break

    odds_checker()

    try:
        driver.find_element(By.LINK_TEXT, "STANDINGS").click()
        rank = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")
        if len(rank) != 2:
            raise NoSuchElementException("Length of participants exceeded")
        sleep(0.1)
        try:
            fir_ent = int(driver.find_elements(By.CSS_SELECTOR, '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[0].text.strip())
        except IndexError:
            try:
                driver.refresh()
                sleep(4)
                fir_ent = int(driver.find_elements(By.CSS_SELECTOR, '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[0].text.strip())
            except IndexError:
                driver.refresh()
                sleep(2)
                fir_ent = 0
        selected_teams_names = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected  .tableCellParticipant__name")
        try:
            pts_pos_mp()
            current_ht_pts = home_points[i]
            current_at_pts = away_points[i]
            z_scorer(htpts=current_ht_pts, atpts=current_at_pts)

        except IndexError:
            print("IYYY")
            try:
                driver.close()
                driver.switch_to.window(window_before)
                divs[i].click()
                window_after = driver.window_handles[1]
                driver.switch_to.window(window_after)
                driver.find_element(By.LINK_TEXT, "STANDINGS").click()
                sleep(0.2)
                selected_teams_names = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected  .tableCellParticipant__name")
                pts_pos_mp()
                current_ht_pts = home_points[i]
                current_at_pts = away_points[i]
                z_scorer(htpts=current_ht_pts, atpts=current_at_pts)
            except IndexError:
                print("000")
                try:
                    driver.refresh()
                    sleep(1.5)
                    pts_pos_mp()
                    current_ht_pts = home_points[i]
                    current_at_pts = away_points[i]
                    z_scorer(htpts=current_ht_pts, atpts=current_at_pts)
                except IndexError:
                    print("111")
                    driver.close()
                    driver.switch_to.window(window_before)
                    driver.get(SPORT_)
                    sleep(0.1)
                    scheduler()
                    sleep(0.1)
                    divs = driver.find_elements(By.CSS_SELECTOR, f'.{sport} .event__match--scheduled')
                    try:
                        divs[i].click()
                        window_after = driver.window_handles[1]
                        driver.switch_to.window(window_after)
                        driver.find_element(By.LINK_TEXT, "STANDINGS").click()
                        sleep(0.2)
                        selected_teams_names = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected  .tableCellParticipant__name")
                        pts_pos_mp()
                        current_ht_pts = home_points[i]
                        current_at_pts = away_points[i]
                        z_scorer(htpts=current_ht_pts, atpts=current_at_pts)
                    except IndexError:
                        driver.close()
                        driver.switch_to.window(window_before)
                        traceback.print_exc()
                        break
                    except StaleElementReferenceException:
                        print("IZZZ")
                        try:
                            driver.close()
                            driver.switch_to.window(window_before)
                            divs[i].click()
                            window_after = driver.window_handles[1]
                            driver.switch_to.window(window_after)
                            driver.find_element(By.LINK_TEXT, "STANDINGS").click()
                            sleep(0.2)
                            selected_teams_names = driver.find_elements(By.CSS_SELECTOR, ".table__row--selected  .tableCellParticipant__name")
                            pts_pos_mp()
                            current_ht_pts = home_points[i]
                            current_at_pts = away_points[i]
                            z_scorer(htpts=current_ht_pts, atpts=current_at_pts)
                        except StaleElementReferenceException:
                            print("444")
                            try:
                                driver.refresh()
                                sleep(1.5)
                                pts_pos_mp()
                                current_ht_pts = home_points[i]
                                current_at_pts = away_points[i]
                                z_scorer(htpts=current_ht_pts, atpts=current_at_pts)

                            except StaleElementReferenceException:
                                print("333")
                                driver.close()
                                driver.switch_to.window(window_before)
                                traceback.print_exc()
                                break
        sleep(0.1)
        team_data()
        driver.find_element(By.LINK_TEXT, "H2H").click()
        sleep(0.1)
        valid_games = 0
        count_33_5 = 0
        count_43_5 = 0
        count_53_5 = 0
        count_sh1_4_5 = 0
        count_sh1_7_5 = 0
        count_sh2_4_5 = 0
        count_sh2_7_5 = 0
        count_12 = 0
        count_HW = 0
        count_AW = 0
        valid_games_H_indp = 0
        count_33_5_H_indp = 0
        count_43_5_H_indp = 0
        count_53_5_H_indp = 0
        count_sh1_4_5_H_indp = 0
        count_sh1_7_5_H_indp = 0
        count_12_H_indp = 0
        count_HW_H_indp = 0
        valid_games_A_indp = 0
        count_33_5_A_indp = 0
        count_43_5_A_indp = 0
        count_53_5_A_indp = 0
        count_sh2_4_5_A_indp = 0
        count_sh2_7_5_A_indp = 0
        count_12_A_indp = 0
        count_AW_A_indp = 0
        for p in range(INDP_MATCH_SAMPLE):
            show_more_matches()
        home_form_checker(home_teamk=home_teamx)
        away_form_checker(away_teamk=away_teamx)
        if fir_ent < 10:
            home_counter()
            away_counter()
        total_aggregator()
        sleep(0.5)
        driver.close()
        driver.switch_to.window(window_before)
        try:
            match_times.append(sub_m_t[i])
        except IndexError:
            traceback.print_exc()
        except NoSuchElementException:
            traceback.print_exc()

    except NoSuchElementException:
        try:
            s_sports = ["tennis", "darts", "badminton", "snooker"]
            if sport in s_sports:
                try:
                    home_t_rank = int(driver.find_element(By.CSS_SELECTOR, '.duelParticipant .duelParticipant__home .participant__participantRank').text.split(': ')[1].split('.')[0])
                    home_positions.append(home_t_rank)
                except NoSuchElementException:
                    home_positions.append(0)
                try:
                    away_t_rank = int(driver.find_element(By.CSS_SELECTOR, '.duelParticipant .duelParticipant__away .participant__participantRank').text.split(': ')[1].split('.')[0])
                    away_positions.append(away_t_rank)
                except NoSuchElementException:
                    away_positions.append(0)
            team_data()
            driver.find_element(By.LINK_TEXT, "H2H").click()
            sleep(0.1)
            valid_games = 0
            count_33_5 = 0
            count_43_5 = 0
            count_53_5 = 0
            count_sh1_4_5 = 0
            count_sh1_7_5 = 0
            count_sh2_4_5 = 0
            count_sh2_7_5 = 0
            count_12 = 0
            count_HW = 0
            count_AW = 0
            valid_games_H_indp = 0
            count_33_5_H_indp = 0
            count_43_5_H_indp = 0
            count_53_5_H_indp = 0
            count_sh1_4_5_H_indp = 0
            count_sh1_7_5_H_indp = 0
            count_12_H_indp = 0
            count_HW_H_indp = 0
            valid_games_A_indp = 0
            count_33_5_A_indp = 0
            count_43_5_A_indp = 0
            count_53_5_A_indp = 0
            count_sh2_4_5_A_indp = 0
            count_sh2_7_5_A_indp = 0
            count_12_A_indp = 0
            count_AW_A_indp = 0
            for p in range(INDP_MATCH_SAMPLE):
                show_more_matches()
            home_form_checker(home_teamk=home_teamx)
            away_form_checker(away_teamk=away_teamx)
            home_counter()
            away_counter()
            total_aggregator()
            driver.close()
            driver.switch_to.window(window_before)
            try:
                match_times.append(sub_m_t[i])
            except IndexError:
                traceback.print_exc()
            except NoSuchElementException:
                traceback.print_exc()
            s_sports = ["tennis", "darts", "badminton", "snooker"]
            if sport in s_sports:
                current_ht_pos = home_positions[i]
                current_at_pos = away_positions[i]
                append_zeroes(home_pos=current_ht_pos, away_pos=current_at_pos)
            else:
                append_zeroes1()
            sleep(0.5)
        except (TimeoutException, IndexError, StaleElementReferenceException, UnexpectedAlertPresentException,
                NoSuchWindowException, InvalidSessionIdException, WebDriverException) as e:
            print("Error Hold 1", e)
            traceback.print_exc()
            driver.close()
            driver.switch_to.window(window_before)
            break
    except (TimeoutException, IndexError, StaleElementReferenceException, UnexpectedAlertPresentException,
            NoSuchWindowException, InvalidSessionIdException, WebDriverException) as e:
        print("Error Hold 2", e)
        traceback.print_exc()
        driver.close()
        driver.switch_to.window(window_before)
        break

for CONFINTVL in CONFINTVLS:
    for COMBINER in COMBINERS[:4]:
        Z = COMBINER
        for COMB in COMB_PROB_METRICS1:
            X, Y = COMB
            bayesian_home_Win_d = []
            bayesian_away_Win_d = []
            bayesian_33_5_d = []
            bayesian_43_5_d = []
            bayesian_53_5_d = []
            bayesian_sh1_4_5_d = []
            bayesian_sh1_7_5_d = []
            bayesian_sh2_4_5_d = []
            bayesian_sh2_7_5_d = []
            bayesian_12_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = 0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_33_5 = 0.5 * (rdm.random() + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                        bayesian_43_5 = 0.5 * (rdm.random() + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                        bayesian_53_5 = 0.5 * (rdm.random() + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                        bayesian_sh1_4_5 = 0.5 * (rdm.random() + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                        bayesian_sh1_7_5 = 0.5 * (rdm.random() + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                        bayesian_sh2_4_5 = 0.5 * (rdm.random() + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                        bayesian_sh2_7_5 = 0.5 * (rdm.random() + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                        bayesian_12 = 0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = 0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_33_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                        bayesian_43_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                        bayesian_53_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                        bayesian_sh1_4_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                        bayesian_sh1_7_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                        bayesian_sh2_4_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                        bayesian_sh2_7_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                        bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = 0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_33_5 = 0.5 * (OVER_33_5_S[q] + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                        bayesian_43_5 = 0.5 * (OVER_43_5_S[q] + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                        bayesian_53_5 = 0.5 * (OVER_53_5_S[q] + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                        bayesian_sh1_4_5 = 0.5 * (OVER_sh1_4_5_S[q] + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                        bayesian_sh1_7_5 = 0.5 * (OVER_sh1_7_5_S[q] + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                        bayesian_sh2_4_5 = 0.5 * (OVER_sh2_4_5_S[q] + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                        bayesian_sh2_7_5 = 0.5 * (OVER_sh2_7_5_S[q] + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                        bayesian_12 = 0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (home_z_prob[q] + rdm.random())
                        bayesian_away_Win = 0.5 * (away_z_prob[q] + rdm.random())
                        bayesian_33_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random())
                        bayesian_43_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random())
                        bayesian_53_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random())
                        bayesian_sh1_4_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random())
                        bayesian_sh1_7_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random())
                        bayesian_sh2_4_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random())
                        bayesian_sh2_7_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random())
                        bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random())
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (_1HWS[q] + rdm.random())
                        bayesian_away_Win = 0.5 * (_2AWS[q] + rdm.random())
                        bayesian_33_5 = 0.5 * (OVER_33_5_S[q] + rdm.random())
                        bayesian_43_5 = 0.5 * (OVER_43_5_S[q] + rdm.random())
                        bayesian_53_5 = 0.5 * (OVER_53_5_S[q] + rdm.random())
                        bayesian_sh1_4_5 = 0.5 * (OVER_sh1_4_5_S[q] + rdm.random())
                        bayesian_sh1_7_5 = 0.5 * (OVER_sh1_7_5_S[q] + rdm.random())
                        bayesian_sh2_4_5 = 0.5 * (OVER_sh2_4_5_S[q] + rdm.random())
                        bayesian_sh2_7_5 = 0.5 * (OVER_sh2_7_5_S[q] + rdm.random())
                        bayesian_12 = 0.5 * (_12S[q] + rdm.random())
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (home_z_prob[q] + _1HWS[q])
                        bayesian_away_Win = 0.5 * (away_z_prob[q] + _2AWS[q])
                        bayesian_33_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + OVER_33_5_S[q])
                        bayesian_43_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + OVER_43_5_S[q])
                        bayesian_53_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + OVER_53_5_S[q])
                        bayesian_sh1_4_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + OVER_sh1_4_5_S[q])
                        bayesian_sh1_7_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + OVER_sh1_7_5_S[q])
                        bayesian_sh2_4_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + OVER_sh2_4_5_S[q])
                        bayesian_sh2_7_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + OVER_sh2_7_5_S[q])
                        bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q])
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[1]:
                        bayesian_home_Win = rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                        bayesian_away_Win = rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                        bayesian_33_5 = rdm.random() * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))
                        bayesian_43_5 = rdm.random() * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))
                        bayesian_53_5 = rdm.random() * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))
                        bayesian_sh1_4_5 = rdm.random() * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))
                        bayesian_sh1_7_5 = rdm.random() * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))
                        bayesian_sh2_4_5 = rdm.random() * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))
                        bayesian_sh2_7_5 = rdm.random() * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))
                        bayesian_12 = rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                        bayesian_home_Win = home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                        bayesian_away_Win = away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                        bayesian_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))
                        bayesian_43_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))
                        bayesian_53_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))
                        bayesian_sh1_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))
                        bayesian_sh1_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))
                        bayesian_sh2_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))
                        bayesian_sh2_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))
                        bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                        bayesian_home_Win = _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                        bayesian_away_Win = _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                        bayesian_33_5 = OVER_33_5_S[q] * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))
                        bayesian_43_5 = OVER_43_5_S[q] * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))
                        bayesian_53_5 = OVER_53_5_S[q] * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))
                        bayesian_sh1_4_5 = OVER_sh1_4_5_S[q] * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))
                        bayesian_sh1_7_5 = OVER_sh1_7_5_S[q] * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))
                        bayesian_sh2_4_5 = OVER_sh2_4_5_S[q] * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))
                        bayesian_sh2_7_5 = OVER_sh2_7_5_S[q] * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))
                        bayesian_12 = _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                        bayesian_home_Win = home_z_prob[q] * rdm.random()
                        bayesian_away_Win = away_z_prob[q] * rdm.random()
                        bayesian_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * rdm.random()
                        bayesian_43_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * rdm.random()
                        bayesian_53_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * rdm.random()
                        bayesian_sh1_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * rdm.random()
                        bayesian_sh1_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * rdm.random()
                        bayesian_sh2_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * rdm.random()
                        bayesian_sh2_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * rdm.random()
                        bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random()
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                        bayesian_home_Win = _1HWS[q] * rdm.random()
                        bayesian_away_Win = _2AWS[q] * rdm.random()
                        bayesian_33_5 = OVER_33_5_S[q] * rdm.random()
                        bayesian_43_5 = OVER_43_5_S[q] * rdm.random()
                        bayesian_53_5 = OVER_53_5_S[q] * rdm.random()
                        bayesian_sh1_4_5 = OVER_sh1_4_5_S[q] * rdm.random()
                        bayesian_sh1_7_5 = OVER_sh1_7_5_S[q] * rdm.random()
                        bayesian_sh2_4_5 = OVER_sh2_4_5_S[q] * rdm.random()
                        bayesian_sh2_7_5 = OVER_sh2_7_5_S[q] * rdm.random()
                        bayesian_12 = _12S[q] * rdm.random()
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                        bayesian_home_Win = home_z_prob[q] * _1HWS[q]
                        bayesian_away_Win = away_z_prob[q] * _2AWS[q]
                        bayesian_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * OVER_33_5_S[q]
                        bayesian_43_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * OVER_43_5_S[q]
                        bayesian_53_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * OVER_53_5_S[q]
                        bayesian_sh1_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * OVER_sh1_4_5_S[q]
                        bayesian_sh1_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * OVER_sh1_7_5_S[q]
                        bayesian_sh2_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * OVER_sh2_4_5_S[q]
                        bayesian_sh2_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * OVER_sh2_7_5_S[q]
                        bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q]
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                        bayesian_away_Win = math.sqrt(0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                        bayesian_33_5 = math.sqrt(0.5 * (rdm.random() + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))))
                        bayesian_43_5 = math.sqrt(0.5 * (rdm.random() + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))))
                        bayesian_53_5 = math.sqrt(0.5 * (rdm.random() + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))))
                        bayesian_sh1_4_5 = math.sqrt(0.5 * (rdm.random() + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))))
                        bayesian_sh1_7_5 = math.sqrt(0.5 * (rdm.random() + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))))
                        bayesian_sh2_4_5 = math.sqrt(0.5 * (rdm.random() + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))))
                        bayesian_sh2_7_5 = math.sqrt(0.5 * (rdm.random() + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))))
                        bayesian_12 = math.sqrt(0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                        bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                        bayesian_33_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))))
                        bayesian_43_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))))
                        bayesian_53_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))))
                        bayesian_sh1_4_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))))
                        bayesian_sh1_7_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))))
                        bayesian_sh2_4_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))))
                        bayesian_sh2_7_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))))
                        bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                        bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                        bayesian_33_5 = math.sqrt(0.5 * (OVER_33_5_S[q] + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))))
                        bayesian_43_5 = math.sqrt(0.5 * (OVER_43_5_S[q] + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))))
                        bayesian_53_5 = math.sqrt(0.5 * (OVER_53_5_S[q] + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))))
                        bayesian_sh1_4_5 = math.sqrt(0.5 * (OVER_sh1_4_5_S[q] + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))))
                        bayesian_sh1_7_5 = math.sqrt(0.5 * (OVER_sh1_7_5_S[q] + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))))
                        bayesian_sh2_4_5 = math.sqrt(0.5 * (OVER_sh2_4_5_S[q] + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))))
                        bayesian_sh2_7_5 = math.sqrt(0.5 * (OVER_sh2_7_5_S[q] + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))))
                        bayesian_12 = math.sqrt(0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + rdm.random()))
                        bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + rdm.random()))
                        bayesian_33_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random()))
                        bayesian_43_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random()))
                        bayesian_53_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random()))
                        bayesian_sh1_4_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random()))
                        bayesian_sh1_7_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random()))
                        bayesian_sh2_4_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random()))
                        bayesian_sh2_7_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random()))
                        bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random()))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + rdm.random()))
                        bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + rdm.random()))
                        bayesian_33_5 = math.sqrt(0.5 * (OVER_33_5_S[q] + rdm.random()))
                        bayesian_43_5 = math.sqrt(0.5 * (OVER_43_5_S[q] + rdm.random()))
                        bayesian_53_5 = math.sqrt(0.5 * (OVER_53_5_S[q] + rdm.random()))
                        bayesian_sh1_4_5 = math.sqrt(0.5 * (OVER_sh1_4_5_S[q] + rdm.random()))
                        bayesian_sh1_7_5 = math.sqrt(0.5 * (OVER_sh1_7_5_S[q] + rdm.random()))
                        bayesian_sh2_4_5 = math.sqrt(0.5 * (OVER_sh2_4_5_S[q] + rdm.random()))
                        bayesian_sh2_7_5 = math.sqrt(0.5 * (OVER_sh2_7_5_S[q] + rdm.random()))
                        bayesian_12 = math.sqrt(0.5 * (_12S[q] + rdm.random()))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + _1HWS[q]))
                        bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + _2AWS[q]))
                        bayesian_33_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + OVER_33_5_S[q]))
                        bayesian_43_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + OVER_43_5_S[q]))
                        bayesian_53_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + OVER_53_5_S[q]))
                        bayesian_sh1_4_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + OVER_sh1_4_5_S[q]))
                        bayesian_sh1_7_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + OVER_sh1_7_5_S[q]))
                        bayesian_sh2_4_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + OVER_sh2_4_5_S[q]))
                        bayesian_sh2_7_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + OVER_sh2_7_5_S[q]))
                        bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q]))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = math.sqrt(rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_33_5 = math.sqrt(rdm.random() * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                        bayesian_43_5 = math.sqrt(rdm.random() * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                        bayesian_53_5 = math.sqrt(rdm.random() * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                        bayesian_sh1_4_5 = math.sqrt(rdm.random() * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                        bayesian_sh1_7_5 = math.sqrt(rdm.random() * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                        bayesian_sh2_4_5 = math.sqrt(rdm.random() * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                        bayesian_sh2_7_5 = math.sqrt(rdm.random() * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                        bayesian_12 = math.sqrt(rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = math.sqrt(away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_33_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                        bayesian_43_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                        bayesian_53_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                        bayesian_sh1_4_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                        bayesian_sh1_7_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                        bayesian_sh2_4_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                        bayesian_sh2_7_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                        bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(_1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = math.sqrt(_2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_33_5 = math.sqrt(OVER_33_5_S[q] * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                        bayesian_43_5 = math.sqrt(OVER_43_5_S[q] * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                        bayesian_53_5 = math.sqrt(OVER_53_5_S[q] * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                        bayesian_sh1_4_5 = math.sqrt(OVER_sh1_4_5_S[q] * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                        bayesian_sh1_7_5 = math.sqrt(OVER_sh1_7_5_S[q] * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                        bayesian_sh2_4_5 = math.sqrt(OVER_sh2_4_5_S[q] * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                        bayesian_sh2_7_5 = math.sqrt(OVER_sh2_7_5_S[q] * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                        bayesian_12 = math.sqrt(_12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(home_z_prob[q] * rdm.random())
                        bayesian_away_Win = math.sqrt(away_z_prob[q] * rdm.random())
                        bayesian_33_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * rdm.random())
                        bayesian_43_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * rdm.random())
                        bayesian_53_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * rdm.random())
                        bayesian_sh1_4_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * rdm.random())
                        bayesian_sh1_7_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * rdm.random())
                        bayesian_sh2_4_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * rdm.random())
                        bayesian_sh2_7_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * rdm.random())
                        bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random())
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(_1HWS[q] * rdm.random())
                        bayesian_away_Win = math.sqrt(_2AWS[q] * rdm.random())
                        bayesian_33_5 = math.sqrt(OVER_33_5_S[q] * rdm.random())
                        bayesian_43_5 = math.sqrt(OVER_43_5_S[q] * rdm.random())
                        bayesian_53_5 = math.sqrt(OVER_53_5_S[q] * rdm.random())
                        bayesian_sh1_4_5 = math.sqrt(OVER_sh1_4_5_S[q] * rdm.random())
                        bayesian_sh1_7_5 = math.sqrt(OVER_sh1_7_5_S[q] * rdm.random())
                        bayesian_sh2_4_5 = math.sqrt(OVER_sh2_4_5_S[q] * rdm.random())
                        bayesian_sh2_7_5 = math.sqrt(OVER_sh2_7_5_S[q] * rdm.random())
                        bayesian_12 = math.sqrt(_12S[q] * rdm.random())
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(home_z_prob[q] * _1HWS[q])
                        bayesian_away_Win = math.sqrt(away_z_prob[q] * _2AWS[q])
                        bayesian_33_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * OVER_33_5_S[q])
                        bayesian_43_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * OVER_43_5_S[q])
                        bayesian_53_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * OVER_53_5_S[q])
                        bayesian_sh1_4_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * OVER_sh1_4_5_S[q])
                        bayesian_sh1_7_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * OVER_sh1_7_5_S[q])
                        bayesian_sh2_4_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * OVER_sh2_4_5_S[q])
                        bayesian_sh2_7_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * OVER_sh2_7_5_S[q])
                        bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q])
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                       f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                       f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|BAYESIAN {OUTCOMES[9]}|"
                                       f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                try:
                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                except UnicodeError:
                    pass
                except IndexError:
                    continue
                except OSError:
                    pass
            for i in range(11):
                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                    file.write("\n\n\n\n\n")

    for PROB in PROB_METRICS:
        X = PROB
        Y = "ANALYSIS"
        Z = "STANDARD"
        bayesian_home_Win_d = []
        bayesian_away_Win_d = []
        bayesian_33_5_d = []
        bayesian_43_5_d = []
        bayesian_53_5_d = []
        bayesian_sh1_4_5_d = []
        bayesian_sh1_7_5_d = []
        bayesian_sh2_4_5_d = []
        bayesian_sh2_7_5_d = []
        bayesian_12_d = []

        for q in range(len(home_teams)):
            try:
                if X == PROB_METRICS[0]:
                    bayesian_home_Win = (prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))
                    bayesian_away_Win = (prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))
                    bayesian_33_5 = (prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))
                    bayesian_43_5 = (prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))
                    bayesian_53_5 = (prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))
                    bayesian_sh1_4_5 = (prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))
                    bayesian_sh1_7_5 = (prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))
                    bayesian_sh2_4_5 = (prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))
                    bayesian_sh2_7_5 = (prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))
                    bayesian_12 = (prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS[1]:
                    prob_matches_home_W_against_EO = rdm.random()
                    prob_matches_W_indp_home1 = rdm.random()
                    prob_matches_W_indp_away1 = rdm.random()
                    bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                    prob_matches_away_W_against_EO = rdm.random()
                    prob_matches_W_indp_home2 = rdm.random()
                    prob_matches_W_indp_away2 = rdm.random()
                    bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                    prob_33_5 = rdm.random()
                    prob_33_5_indp_home = rdm.random()
                    prob_33_5_indp_away = rdm.random()
                    bayesian_33_5 = (prob_33_5 * (prob_33_5_indp_home * prob_33_5_indp_away)) / ((prob_33_5 * (prob_33_5_indp_home * prob_33_5_indp_away)) + ((1 - (prob_33_5_indp_home * prob_33_5_indp_away)) * (1 - prob_33_5)))
                    prob_43_5 = rdm.random()
                    prob_43_5_indp_home = rdm.random()
                    prob_43_5_indp_away = rdm.random()
                    bayesian_43_5 = (prob_43_5 * (prob_43_5_indp_home * prob_43_5_indp_away)) / ((prob_43_5 * (prob_43_5_indp_home * prob_43_5_indp_away)) + ((1 - (prob_43_5_indp_home * prob_43_5_indp_away)) * (1 - prob_43_5)))
                    prob_53_5 = rdm.random()
                    prob_53_5_indp_home = rdm.random()
                    prob_53_5_indp_away = rdm.random()
                    bayesian_53_5 = (prob_53_5 * (prob_53_5_indp_home * prob_53_5_indp_away)) / ((prob_53_5 * (prob_53_5_indp_home * prob_53_5_indp_away)) + ((1 - (prob_53_5_indp_home * prob_53_5_indp_away)) * (1 - prob_53_5)))
                    prob_sh1_4_5 = rdm.random()
                    prob_sh1_4_5_indp_home = rdm.random()
                    prob_sh1_4_5_indp_away = rdm.random()
                    bayesian_sh1_4_5 = (prob_sh1_4_5 * (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) / ((prob_sh1_4_5 * (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) + ((1 - (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) * (1 - prob_sh1_4_5)))
                    prob_sh1_7_5 = rdm.random()
                    prob_sh1_7_5_indp_home = rdm.random()
                    prob_sh1_7_5_indp_away = rdm.random()
                    bayesian_sh1_7_5 = (prob_sh1_7_5 * (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) / ((prob_sh1_7_5 * (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) + ((1 - (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) * (1 - prob_sh1_7_5)))
                    prob_sh2_4_5 = rdm.random()
                    prob_sh2_4_5_indp_home = rdm.random()
                    prob_sh2_4_5_indp_away = rdm.random()
                    bayesian_sh2_4_5 = (prob_sh2_4_5 * (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) / ((prob_sh2_4_5 * (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) + ((1 - (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) * (1 - prob_sh2_4_5)))
                    prob_sh2_7_5 = rdm.random()
                    prob_sh2_7_5_indp_home = rdm.random()
                    prob_sh2_7_5_indp_away = rdm.random()
                    bayesian_sh2_7_5 = (prob_sh2_7_5 * (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) / ((prob_sh2_7_5 * (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) + ((1 - (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) * (1 - prob_sh2_7_5)))
                    prob_12 = rdm.random()
                    prob_12_indp_home = rdm.random()
                    prob_12_indp_away = rdm.random()
                    bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS[2]:
                    bayesian_home_Win = home_z_prob[q]
                    bayesian_away_Win = away_z_prob[q]
                    bayesian_33_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))
                    bayesian_43_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))
                    bayesian_53_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))
                    bayesian_sh1_4_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))
                    bayesian_sh1_7_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))
                    bayesian_sh2_4_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))
                    bayesian_sh2_7_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))
                    bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS[3]:
                    bayesian_home_Win = _1HWS[q]
                    bayesian_away_Win = _2AWS[q]
                    bayesian_33_5 = OVER_33_5_S[q]
                    bayesian_43_5 = OVER_43_5_S[q]
                    bayesian_53_5 = OVER_53_5_S[q]
                    bayesian_sh1_4_5 = OVER_sh1_4_5_S[q]
                    bayesian_sh1_7_5 = OVER_sh1_7_5_S[q]
                    bayesian_sh2_4_5 = OVER_sh2_4_5_S[q]
                    bayesian_sh2_7_5 = OVER_sh2_7_5_S[q]
                    bayesian_12 = _12S[q]
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS[4]:
                    bayesian_home_Win = home_z_prob[q] * diff_z_prob[q]
                    bayesian_away_Win = away_z_prob[q] * diff_z_prob[q]
                    bayesian_33_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q])) * diff_z_prob[q]
                    bayesian_43_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q])) * diff_z_prob[q]
                    bayesian_53_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q])) * diff_z_prob[q]
                    bayesian_sh1_4_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q])) * diff_z_prob[q]
                    bayesian_sh1_7_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q])) * diff_z_prob[q]
                    bayesian_sh2_4_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q])) * diff_z_prob[q]
                    bayesian_sh2_7_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q])) * diff_z_prob[q]
                    bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])) * diff_z_prob[q]
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

            except IndexError:
                continue

        for q in range(len(bayesian_home_Win_d)):
            if q == 0:
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                        file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                   f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                   f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                   f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|BAYESIAN {OUTCOMES[9]}|"
                                   f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
            try:
                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_D[q] == 0 and a_form_D[q] == 0:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                            if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                        if h_form_D[q] == 0 or a_form_D[q] == 0:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                            if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                            if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

            except UnicodeError:
                pass
            except IndexError:
                continue
            except OSError:
                pass
        for i in range(11):
            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                file.write("\n\n\n\n\n")

    for COMB in COMB_PROB_METRICS2:
        X, Y = COMB
        Z = "COMBINATE"
        bayesian_home_Win_d = []
        bayesian_away_Win_d = []
        bayesian_33_5_d = []
        bayesian_43_5_d = []
        bayesian_53_5_d = []
        bayesian_sh1_4_5_d = []
        bayesian_sh1_7_5_d = []
        bayesian_sh2_4_5_d = []
        bayesian_sh2_7_5_d = []
        bayesian_12_d = []

        for q in range(len(home_teams)):
            try:
                if X == PROB_METRICS1[0] and Y == PROB_METRICS1[1]:
                    prob_matches_W_indp_home1 = rdm.random()
                    prob_matches_W_indp_away1 = rdm.random()
                    bayesian_home_Win = (prob_HWs[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_HWs[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_HWs[q])))
                    prob_matches_W_indp_home2 = rdm.random()
                    prob_matches_W_indp_away2 = rdm.random()
                    bayesian_away_Win = (prob_AWs[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_AWs[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_AWs[q])))
                    prob_33_5_indp_home = rdm.random()
                    prob_33_5_indp_away = rdm.random()
                    bayesian_33_5 = (prob_33_5s[q] * (prob_33_5_indp_home * prob_33_5_indp_away)) / ((prob_33_5s[q] * (prob_33_5_indp_home * prob_33_5_indp_away)) + ((1 - (prob_33_5_indp_home * prob_33_5_indp_away)) * (1 - prob_33_5s[q])))
                    prob_43_5_indp_home = rdm.random()
                    prob_43_5_indp_away = rdm.random()
                    bayesian_43_5 = (prob_43_5s[q] * (prob_43_5_indp_home * prob_43_5_indp_away)) / ((prob_43_5s[q] * (prob_43_5_indp_home * prob_43_5_indp_away)) + ((1 - (prob_43_5_indp_home * prob_43_5_indp_away)) * (1 - prob_43_5s[q])))
                    prob_53_5_indp_home = rdm.random()
                    prob_53_5_indp_away = rdm.random()
                    bayesian_53_5 = (prob_53_5s[q] * (prob_53_5_indp_home * prob_53_5_indp_away)) / ((prob_53_5s[q] * (prob_53_5_indp_home * prob_53_5_indp_away)) + ((1 - (prob_53_5_indp_home * prob_53_5_indp_away)) * (1 - prob_53_5s[q])))
                    prob_sh1_4_5_indp_home = rdm.random()
                    prob_sh1_4_5_indp_away = rdm.random()
                    bayesian_sh1_4_5 = (prob_sh1_4_5s[q] * (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) + ((1 - (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) * (1 - prob_sh1_4_5s[q])))
                    prob_sh1_7_5_indp_home = rdm.random()
                    prob_sh1_7_5_indp_away = rdm.random()
                    bayesian_sh1_7_5 = (prob_sh1_7_5s[q] * (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) + ((1 - (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) * (1 - prob_sh1_7_5s[q])))
                    prob_sh2_4_5_indp_home = rdm.random()
                    prob_sh2_4_5_indp_away = rdm.random()
                    bayesian_sh2_4_5 = (prob_sh2_4_5s[q] * (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) + ((1 - (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) * (1 - prob_sh2_4_5s[q])))
                    prob_sh2_7_5_indp_home = rdm.random()
                    prob_sh2_7_5_indp_away = rdm.random()
                    bayesian_sh2_7_5 = (prob_sh2_7_5s[q] * (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) + ((1 - (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) * (1 - prob_sh2_7_5s[q])))
                    prob_12_indp_home = rdm.random()
                    prob_12_indp_away = rdm.random()
                    bayesian_12 = (prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12s[q])))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS1[0] and Y == PROB_METRICS1[2]:
                    prob_matches_W_indp_home1 = rdm.random()
                    prob_matches_W_indp_away1 = rdm.random()
                    bayesian_home_Win = (home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - home_z_prob[q])))
                    prob_matches_W_indp_home2 = rdm.random()
                    prob_matches_W_indp_away2 = rdm.random()
                    bayesian_away_Win = (away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - away_z_prob[q])))
                    prob_33_5_indp_home = rdm.random()
                    prob_33_5_indp_away = rdm.random()
                    bayesian_33_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * (prob_33_5_indp_home * prob_33_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * (prob_33_5_indp_home * prob_33_5_indp_away)) + ((1 - (prob_33_5_indp_home * prob_33_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q])))))))
                    prob_43_5_indp_home = rdm.random()
                    prob_43_5_indp_away = rdm.random()
                    bayesian_43_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * (prob_43_5_indp_home * prob_43_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * (prob_43_5_indp_home * prob_43_5_indp_away)) + ((1 - (prob_43_5_indp_home * prob_43_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q])))))))
                    prob_53_5_indp_home = rdm.random()
                    prob_53_5_indp_away = rdm.random()
                    bayesian_53_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * (prob_53_5_indp_home * prob_53_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * (prob_53_5_indp_home * prob_53_5_indp_away)) + ((1 - (prob_53_5_indp_home * prob_53_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q])))))))
                    prob_sh1_4_5_indp_home = rdm.random()
                    prob_sh1_4_5_indp_away = rdm.random()
                    bayesian_sh1_4_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) + ((1 - (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q])))))))
                    prob_sh1_7_5_indp_home = rdm.random()
                    prob_sh1_7_5_indp_away = rdm.random()
                    bayesian_sh1_7_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) + ((1 - (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q])))))))
                    prob_sh2_4_5_indp_home = rdm.random()
                    prob_sh2_4_5_indp_away = rdm.random()
                    bayesian_sh2_4_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) + ((1 - (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q])))))))
                    prob_sh2_7_5_indp_home = rdm.random()
                    prob_sh2_7_5_indp_away = rdm.random()
                    bayesian_sh2_7_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) + ((1 - (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q])))))))
                    prob_12_indp_home = rdm.random()
                    prob_12_indp_away = rdm.random()
                    bayesian_12 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])))))))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS1[0] and Y == PROB_METRICS1[3]:
                    prob_matches_W_indp_home1 = rdm.random()
                    prob_matches_W_indp_away1 = rdm.random()
                    bayesian_home_Win = (_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - _1HWS[q])))
                    prob_matches_W_indp_home2 = rdm.random()
                    prob_matches_W_indp_away2 = rdm.random()
                    bayesian_away_Win = (_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - _2AWS[q])))
                    prob_33_5_indp_home = rdm.random()
                    prob_33_5_indp_away = rdm.random()
                    bayesian_33_5 = (OVER_33_5_S[q] * (prob_33_5_indp_home * prob_33_5_indp_away)) / ((OVER_33_5_S[q] * (prob_33_5_indp_home * prob_33_5_indp_away)) + ((1 - (prob_33_5_indp_home * prob_33_5_indp_away)) * (1 - OVER_33_5_S[q])))
                    prob_43_5_indp_home = rdm.random()
                    prob_43_5_indp_away = rdm.random()
                    bayesian_43_5 = (OVER_43_5_S[q] * (prob_43_5_indp_home * prob_43_5_indp_away)) / ((OVER_43_5_S[q] * (prob_43_5_indp_home * prob_43_5_indp_away)) + ((1 - (prob_43_5_indp_home * prob_43_5_indp_away)) * (1 - OVER_43_5_S[q])))
                    prob_53_5_indp_home = rdm.random()
                    prob_53_5_indp_away = rdm.random()
                    bayesian_53_5 = (OVER_53_5_S[q] * (prob_53_5_indp_home * prob_53_5_indp_away)) / ((OVER_53_5_S[q] * (prob_53_5_indp_home * prob_53_5_indp_away)) + ((1 - (prob_53_5_indp_home * prob_53_5_indp_away)) * (1 - OVER_53_5_S[q])))
                    prob_sh1_4_5_indp_home = rdm.random()
                    prob_sh1_4_5_indp_away = rdm.random()
                    bayesian_sh1_4_5 = (OVER_sh1_4_5_S[q] * (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) / ((OVER_sh1_4_5_S[q] * (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) + ((1 - (prob_sh1_4_5_indp_home * prob_sh1_4_5_indp_away)) * (1 - OVER_sh1_4_5_S[q])))
                    prob_sh1_7_5_indp_home = rdm.random()
                    prob_sh1_7_5_indp_away = rdm.random()
                    bayesian_sh1_7_5 = (OVER_sh1_7_5_S[q] * (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) / ((OVER_sh1_7_5_S[q] * (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) + ((1 - (prob_sh1_7_5_indp_home * prob_sh1_7_5_indp_away)) * (1 - OVER_sh1_7_5_S[q])))
                    prob_sh2_4_5_indp_home = rdm.random()
                    prob_sh2_4_5_indp_away = rdm.random()
                    bayesian_sh2_4_5 = (OVER_sh2_4_5_S[q] * (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) / ((OVER_sh2_4_5_S[q] * (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) + ((1 - (prob_sh2_4_5_indp_home * prob_sh2_4_5_indp_away)) * (1 - OVER_sh2_4_5_S[q])))
                    prob_sh2_7_5_indp_home = rdm.random()
                    prob_sh2_7_5_indp_away = rdm.random()
                    bayesian_sh2_7_5 = (OVER_sh2_7_5_S[q] * (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) / ((OVER_sh2_7_5_S[q] * (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) + ((1 - (prob_sh2_7_5_indp_home * prob_sh2_7_5_indp_away)) * (1 - OVER_sh2_7_5_S[q])))
                    prob_12_indp_home = rdm.random()
                    prob_12_indp_away = rdm.random()
                    bayesian_12 = (_12S[q] * (prob_12_indp_home * prob_12_indp_away)) / ((_12S[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - _12S[q])))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0]:
                    prob_matches_home_W_against_EO = rdm.random()
                    bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_matches_home_W_against_EO)))
                    prob_matches_away_W_against_EO = rdm.random()
                    bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_matches_away_W_against_EO)))
                    prob_33_5 = rdm.random()
                    bayesian_33_5 = ((prob_33_5 * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5 * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5))))
                    prob_43_5 = rdm.random()
                    bayesian_43_5 = ((prob_43_5 * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5 * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5))))
                    prob_53_5 = rdm.random()
                    bayesian_53_5 = ((prob_53_5 * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5 * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5))))
                    prob_sh1_4_5 = rdm.random()
                    bayesian_sh1_4_5 = ((prob_sh1_4_5 * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5 * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5))))
                    prob_sh1_7_5 = rdm.random()
                    bayesian_sh1_7_5 = ((prob_sh1_7_5 * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5 * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5))))
                    prob_sh2_4_5 = rdm.random()
                    bayesian_sh2_4_5 = ((prob_sh2_4_5 * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5 * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5))))
                    prob_sh2_7_5 = rdm.random()
                    bayesian_sh2_7_5 = ((prob_sh2_7_5 * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5 * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5))))
                    prob_12 = rdm.random()
                    bayesian_12 = ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12))))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS1[1] and Y == PROB_METRICS1[2]:
                    bayesian_home_Win = (home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - home_z_prob[q])))
                    bayesian_away_Win = (away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - away_z_prob[q])))
                    bayesian_33_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))))))
                    bayesian_43_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))))))
                    bayesian_53_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))))))
                    bayesian_sh1_4_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))))))
                    bayesian_sh1_7_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))))))
                    bayesian_sh2_4_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))))))
                    bayesian_sh2_7_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))))))
                    bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))))))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3]:
                    bayesian_home_Win = (_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - _1HWS[q])))
                    bayesian_away_Win = (_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - _2AWS[q])))
                    bayesian_33_5 = (OVER_33_5_S[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((OVER_33_5_S[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - OVER_33_5_S[q])))
                    bayesian_43_5 = (OVER_43_5_S[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((OVER_43_5_S[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - OVER_43_5_S[q])))
                    bayesian_53_5 = (OVER_53_5_S[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((OVER_53_5_S[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - OVER_53_5_S[q])))
                    bayesian_sh1_4_5 = (OVER_sh1_4_5_S[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((OVER_sh1_4_5_S[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - OVER_sh1_4_5_S[q])))
                    bayesian_sh1_7_5 = (OVER_sh1_7_5_S[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((OVER_sh1_7_5_S[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - OVER_sh1_7_5_S[q])))
                    bayesian_sh2_4_5 = (OVER_sh2_4_5_S[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((OVER_sh2_4_5_S[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - OVER_sh2_4_5_S[q])))
                    bayesian_sh2_7_5 = (OVER_sh2_7_5_S[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((OVER_sh2_7_5_S[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - OVER_sh2_7_5_S[q])))
                    bayesian_12 = (_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - _12S[q])))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)
            except IndexError:
                continue

        for q in range(len(bayesian_home_Win_d)):
            if q == 0:
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                        file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                   f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                   f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                   f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|BAYESIAN {OUTCOMES[9]}|"
                                   f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
            try:
                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_D[q] == 0 and a_form_D[q] == 0:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                            if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                        if h_form_D[q] == 0 or a_form_D[q] == 0:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                            if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                            if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

            except UnicodeError:
                pass
            except IndexError:
                continue
            except OSError:
                pass
        for i in range(11):
            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                file.write("\n\n\n\n\n")

    for COMBINER in COMBINERS:
        Z = COMBINER
        if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[6] and Z != COMBINERS[7]:
            for COMB in COMB_PROB_METRICS3:
                W, X, Y = COMB
                bayesian_home_Win_d = []
                bayesian_away_Win_d = []
                bayesian_33_5_d = []
                bayesian_43_5_d = []
                bayesian_53_5_d = []
                bayesian_sh1_4_5_d = []
                bayesian_sh1_7_5_d = []
                bayesian_sh2_4_5_d = []
                bayesian_sh2_7_5_d = []
                bayesian_12_d = []

                for q in range(len(home_teams)):
                    try:
                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_33_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random() + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                            bayesian_43_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random() + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                            bayesian_53_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random() + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                            bayesian_sh1_4_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random() + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                            bayesian_sh1_7_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random() + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                            bayesian_sh2_4_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random() + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                            bayesian_sh2_7_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random() + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                            bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * rdm.random() * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))
                            bayesian_43_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * rdm.random() * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))
                            bayesian_53_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * rdm.random() * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))
                            bayesian_sh1_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * rdm.random() * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))
                            bayesian_sh1_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * rdm.random() * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))
                            bayesian_sh2_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * rdm.random() * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))
                            bayesian_sh2_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * rdm.random() * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[4]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_33_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random() + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))))
                            bayesian_43_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random() + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))))
                            bayesian_53_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random() + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))))
                            bayesian_sh1_4_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random() + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))))
                            bayesian_sh1_7_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random() + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))))
                            bayesian_sh2_4_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random() + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))))
                            bayesian_sh2_7_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random() + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))))
                            bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[5]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_33_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random() + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))))
                            bayesian_43_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random() + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))))
                            bayesian_53_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random() + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))))
                            bayesian_sh1_4_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random() + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))))
                            bayesian_sh1_7_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random() + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))))
                            bayesian_sh2_4_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random() + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))))
                            bayesian_sh2_7_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random() + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))))
                            bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = (1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_33_5 = (1 / 3) * (OVER_33_5_S[q] + rdm.random() + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                            bayesian_43_5 = (1 / 3) * (OVER_43_5_S[q] + rdm.random() + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                            bayesian_53_5 = (1 / 3) * (OVER_53_5_S[q] + rdm.random() + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                            bayesian_sh1_4_5 = (1 / 3) * (OVER_sh1_4_5_S[q] + rdm.random() + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                            bayesian_sh1_7_5 = (1 / 3) * (OVER_sh1_7_5_S[q] + rdm.random() + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                            bayesian_sh2_4_5 = (1 / 3) * (OVER_sh2_4_5_S[q] + rdm.random() + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                            bayesian_sh2_7_5 = (1 / 3) * (OVER_sh2_7_5_S[q] + rdm.random() + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                            bayesian_12 = (1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = _2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_33_5 = OVER_33_5_S[q] * rdm.random() * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))
                            bayesian_43_5 = OVER_43_5_S[q] * rdm.random() * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))
                            bayesian_53_5 = OVER_53_5_S[q] * rdm.random() * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))
                            bayesian_sh1_4_5 = OVER_sh1_4_5_S[q] * rdm.random() * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))
                            bayesian_sh1_7_5 = OVER_sh1_7_5_S[q] * rdm.random() * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))
                            bayesian_sh2_4_5 = OVER_sh2_4_5_S[q] * rdm.random() * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))
                            bayesian_sh2_7_5 = OVER_sh2_7_5_S[q] * rdm.random() * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))
                            bayesian_12 = _12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = np.cbrt((1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_33_5 = np.cbrt((1 / 3) * (OVER_33_5_S[q] + rdm.random() + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))))
                            bayesian_43_5 = np.cbrt((1 / 3) * (OVER_43_5_S[q] + rdm.random() + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))))
                            bayesian_53_5 = np.cbrt((1 / 3) * (OVER_53_5_S[q] + rdm.random() + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))))
                            bayesian_sh1_4_5 = np.cbrt((1 / 3) * (OVER_sh1_4_5_S[q] + rdm.random() + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))))
                            bayesian_sh1_7_5 = np.cbrt((1 / 3) * (OVER_sh1_7_5_S[q] + rdm.random() + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))))
                            bayesian_sh2_4_5 = np.cbrt((1 / 3) * (OVER_sh2_4_5_S[q] + rdm.random() + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))))
                            bayesian_sh2_7_5 = np.cbrt((1 / 3) * (OVER_sh2_7_5_S[q] + rdm.random() + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))))
                            bayesian_12 = np.cbrt((1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                            bayesian_home_Win = np.cbrt(_1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = np.cbrt(_2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_33_5 = np.cbrt(OVER_33_5_S[q] * rdm.random() * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                            bayesian_43_5 = np.cbrt(OVER_43_5_S[q] * rdm.random() * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                            bayesian_53_5 = np.cbrt(OVER_53_5_S[q] * rdm.random() * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                            bayesian_sh1_4_5 = np.cbrt(OVER_sh1_4_5_S[q] * rdm.random() * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                            bayesian_sh1_7_5 = np.cbrt(OVER_sh1_7_5_S[q] * rdm.random() * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                            bayesian_sh2_4_5 = np.cbrt(OVER_sh2_4_5_S[q] * rdm.random() * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                            bayesian_sh2_7_5 = np.cbrt(OVER_sh2_7_5_S[q] * rdm.random() * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                            bayesian_12 = np.cbrt(_12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = (1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_33_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + OVER_33_5_S[q] + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                            bayesian_43_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + OVER_43_5_S[q] + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                            bayesian_53_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + OVER_53_5_S[q] + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                            bayesian_sh1_4_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + OVER_sh1_4_5_S[q] + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                            bayesian_sh1_7_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + OVER_sh1_7_5_S[q] + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                            bayesian_sh2_4_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + OVER_sh2_4_5_S[q] + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                            bayesian_sh2_7_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + OVER_sh2_7_5_S[q] + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                            bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * OVER_33_5_S[q] * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))
                            bayesian_43_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * OVER_43_5_S[q] * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))
                            bayesian_53_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * OVER_53_5_S[q] * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))
                            bayesian_sh1_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * OVER_sh1_4_5_S[q] * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))
                            bayesian_sh1_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * OVER_sh1_7_5_S[q] * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))
                            bayesian_sh2_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * OVER_sh2_4_5_S[q] * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))
                            bayesian_sh2_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * OVER_sh2_7_5_S[q] * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_33_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + OVER_33_5_S[q] + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))))
                            bayesian_43_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + OVER_43_5_S[q] + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))))
                            bayesian_53_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + OVER_53_5_S[q] + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))))
                            bayesian_sh1_4_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + OVER_sh1_4_5_S[q] + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))))
                            bayesian_sh1_7_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + OVER_sh1_7_5_S[q] + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))))
                            bayesian_sh2_4_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + OVER_sh2_4_5_S[q] + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))))
                            bayesian_sh2_7_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + OVER_sh2_7_5_S[q] + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))))
                            bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                            bayesian_home_Win = np.cbrt(home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = np.cbrt(away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_33_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * OVER_33_5_S[q] * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                            bayesian_43_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * OVER_43_5_S[q] * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                            bayesian_53_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * OVER_53_5_S[q] * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                            bayesian_sh1_4_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * OVER_sh1_4_5_S[q] * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                            bayesian_sh1_7_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * OVER_sh1_7_5_S[q] * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                            bayesian_sh2_4_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * OVER_sh2_4_5_S[q] * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                            bayesian_sh2_7_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * OVER_sh2_7_5_S[q] * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                            bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q])
                            bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q])
                            bayesian_33_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random() + OVER_33_5_S[q])
                            bayesian_43_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random() + OVER_43_5_S[q])
                            bayesian_53_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random() + OVER_53_5_S[q])
                            bayesian_sh1_4_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random() + OVER_sh1_4_5_S[q])
                            bayesian_sh1_7_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random() + OVER_sh1_7_5_S[q])
                            bayesian_sh2_4_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random() + OVER_sh2_4_5_S[q])
                            bayesian_sh2_7_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random() + OVER_sh2_7_5_S[q])
                            bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q]
                            bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q]
                            bayesian_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * rdm.random() * OVER_33_5_S[q]
                            bayesian_43_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * rdm.random() * OVER_43_5_S[q]
                            bayesian_53_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * rdm.random() * OVER_53_5_S[q]
                            bayesian_sh1_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * rdm.random() * OVER_sh1_4_5_S[q]
                            bayesian_sh1_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * rdm.random() * OVER_sh1_7_5_S[q]
                            bayesian_sh2_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * rdm.random() * OVER_sh2_4_5_S[q]
                            bayesian_sh2_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * rdm.random() * OVER_sh2_7_5_S[q]
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q]
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q]))
                            bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q]))
                            bayesian_33_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random() + OVER_33_5_S[q]))
                            bayesian_43_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random() + OVER_43_5_S[q]))
                            bayesian_53_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random() + OVER_53_5_S[q]))
                            bayesian_sh1_4_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random() + OVER_sh1_4_5_S[q]))
                            bayesian_sh1_7_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random() + OVER_sh1_7_5_S[q]))
                            bayesian_sh2_4_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random() + OVER_sh2_4_5_S[q]))
                            bayesian_sh2_7_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random() + OVER_sh2_7_5_S[q]))
                            bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q]))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                            bayesian_home_Win = np.cbrt(home_z_prob[q] * rdm.random() * _1HWS[q])
                            bayesian_away_Win = np.cbrt(away_z_prob[q] * rdm.random() * _2AWS[q])
                            bayesian_33_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * rdm.random() * OVER_33_5_S[q])
                            bayesian_43_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * rdm.random() * OVER_43_5_S[q])
                            bayesian_53_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * rdm.random() * OVER_53_5_S[q])
                            bayesian_sh1_4_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * rdm.random() * OVER_sh1_4_5_S[q])
                            bayesian_sh1_7_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * rdm.random() * OVER_sh1_7_5_S[q])
                            bayesian_sh2_4_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * rdm.random() * OVER_sh2_4_5_S[q])
                            bayesian_sh2_7_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * rdm.random() * OVER_sh2_7_5_S[q])
                            bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    except IndexError:
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                           f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                           f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|BAYESIAN {OUTCOMES[9]}|"
                                           f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2):
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                    else:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                    except UnicodeError:
                        pass
                    except IndexError:
                        continue
                    except OSError:
                        pass
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                        file.write("\n\n\n\n\n")

    for COMBINER in COMBINERS:
        Z = COMBINER
        if Z != COMBINERS[2] and Z != COMBINERS[3] and Z != COMBINERS[4] and Z != COMBINERS[5]:
            for COMB in COMB_PROB_METRICS4:
                V, W, X, Y = COMB
                bayesian_home_Win_d = []
                bayesian_away_Win_d = []
                bayesian_33_5_d = []
                bayesian_43_5_d = []
                bayesian_53_5_d = []
                bayesian_sh1_4_5_d = []
                bayesian_sh1_7_5_d = []
                bayesian_sh2_4_5_d = []
                bayesian_sh2_7_5_d = []
                bayesian_12_d = []

                for q in range(len(home_teams)):
                    try:
                        if Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = (1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_33_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random() + OVER_33_5_S[q] + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))
                            bayesian_43_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random() + OVER_43_5_S[q] + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))
                            bayesian_53_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random() + OVER_53_5_S[q] + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))
                            bayesian_sh1_4_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random() + OVER_sh1_4_5_S[q] + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))
                            bayesian_sh1_7_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random() + OVER_sh1_7_5_S[q] + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))
                            bayesian_sh2_4_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random() + OVER_sh2_4_5_S[q] + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))
                            bayesian_sh2_7_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random() + OVER_sh2_7_5_S[q] + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))
                            bayesian_12 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * rdm.random() * OVER_33_5_S[q] * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))
                            bayesian_43_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * rdm.random() * OVER_43_5_S[q] * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))
                            bayesian_53_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * rdm.random() * OVER_53_5_S[q] * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))
                            bayesian_sh1_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * rdm.random() * OVER_sh1_4_5_S[q] * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))
                            bayesian_sh1_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * rdm.random() * OVER_sh1_7_5_S[q] * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))
                            bayesian_sh2_4_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * rdm.random() * OVER_sh2_4_5_S[q] * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))
                            bayesian_sh2_7_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * rdm.random() * OVER_sh2_7_5_S[q] * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if Z == COMBINERS[6]:
                            bayesian_home_Win = ((1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))) ** 0.25
                            bayesian_away_Win = ((1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))) ** 0.25
                            bayesian_33_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) + rdm.random() + OVER_33_5_S[q] + ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q])))))) ** 0.25
                            bayesian_43_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) + rdm.random() + OVER_43_5_S[q] + ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q])))))) ** 0.25
                            bayesian_53_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) + rdm.random() + OVER_53_5_S[q] + ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q])))))) ** 0.25
                            bayesian_sh1_4_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) + rdm.random() + OVER_sh1_4_5_S[q] + ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q])))))) ** 0.25
                            bayesian_sh1_7_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) + rdm.random() + OVER_sh1_7_5_S[q] + ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q])))))) ** 0.25
                            bayesian_sh2_4_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) + rdm.random() + OVER_sh2_4_5_S[q] + ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q])))))) ** 0.25
                            bayesian_sh2_7_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) + rdm.random() + OVER_sh2_7_5_S[q] + ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q])))))) ** 0.25
                            bayesian_12 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))) ** 0.25
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                        if Z == COMBINERS[7]:
                            bayesian_home_Win = (home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))) ** 0.25
                            bayesian_away_Win = (away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))) ** 0.25
                            bayesian_33_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_33_5s[q]))) * rdm.random() * OVER_33_5_S[q] * ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) / ((prob_33_5s[q] * (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) + ((1 - (prob_33_5_H_indps[q] * prob_33_5_A_indps[q])) * (1 - prob_33_5s[q]))))) ** 0.25
                            bayesian_43_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_43_5s[q]))) * rdm.random() * OVER_43_5_S[q] * ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) / ((prob_43_5s[q] * (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) + ((1 - (prob_43_5_H_indps[q] * prob_43_5_A_indps[q])) * (1 - prob_43_5s[q]))))) ** 0.25
                            bayesian_53_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_53_5s[q]))) * rdm.random() * OVER_53_5_S[q] * ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) / ((prob_53_5s[q] * (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) + ((1 - (prob_53_5_H_indps[q] * prob_53_5_A_indps[q])) * (1 - prob_53_5s[q]))))) ** 0.25
                            bayesian_sh1_4_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_4_5s[q]))) * rdm.random() * OVER_sh1_4_5_S[q] * ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) / ((prob_sh1_4_5s[q] * (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) + ((1 - (prob_sh1_4_5_H_indps[q] * prob_sh1_4_5_A_indps[q])) * (1 - prob_sh1_4_5s[q]))))) ** 0.25
                            bayesian_sh1_7_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh1_7_5s[q]))) * rdm.random() * OVER_sh1_7_5_S[q] * ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) / ((prob_sh1_7_5s[q] * (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) + ((1 - (prob_sh1_7_5_H_indps[q] * prob_sh1_7_5_A_indps[q])) * (1 - prob_sh1_7_5s[q]))))) ** 0.25
                            bayesian_sh2_4_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_4_5s[q]))) * rdm.random() * OVER_sh2_4_5_S[q] * ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) / ((prob_sh2_4_5s[q] * (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) + ((1 - (prob_sh2_4_5_H_indps[q] * prob_sh2_4_5_A_indps[q])) * (1 - prob_sh2_4_5s[q]))))) ** 0.25
                            bayesian_sh2_7_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_sh2_7_5s[q]))) * rdm.random() * OVER_sh2_7_5_S[q] * ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) / ((prob_sh2_7_5s[q] * (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) + ((1 - (prob_sh2_7_5_H_indps[q] * prob_sh2_7_5_A_indps[q])) * (1 - prob_sh2_7_5s[q]))))) ** 0.25
                            bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))) ** 0.25
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win, baye_33_5=bayesian_33_5, baye_43_5=bayesian_43_5, baye_53_5=bayesian_53_5, baye_sh1_4_5=bayesian_sh1_4_5, baye_sh1_7_5=bayesian_sh1_7_5, baye_sh2_4_5=bayesian_sh2_4_5, baye_sh2_7_5=bayesian_sh2_7_5, baye_12=bayesian_12)

                    except IndexError:
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                           f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                           f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|BAYESIAN {OUTCOMES[9]}|"
                                           f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                        if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]):

                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_33_5_d[q] > CONFINTVL or bayesian_43_5_d[q] > CONFINTVL or bayesian_53_5_d[q] > CONFINTVL or bayesian_sh1_4_5_d[q] > CONFINTVL or bayesian_sh2_4_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] >= FORM_VALUE and a_form_W[q] >= FORM_VALUE:
                                    if bayesian_53_5_d[q] <= bayesian_43_5_d[q] <= bayesian_33_5_d[q] and bayesian_sh1_7_5_d[q] >= bayesian_sh1_4_5_d[q] and bayesian_sh2_7_5_d[q] >= bayesian_sh2_4_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                            writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                    except UnicodeError:
                        pass
                    except IndexError:
                        continue
                    except OSError:
                        pass
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                        file.write("\n\n\n\n\n")

    if CONFINTVLS.index(CONFINTVL) == 0:
        with open(f"../LISTS - SPORTS DATA/SPORTS_DATA_LIST_{sport}.txt", mode="a") as file:
            try:
                file.write(f"countries = {countries}\nleagues = {leagues}\nhome_teams = {home_teams}\n"
                           f"home_positions = {home_positions}\nhome_points = {home_points}\n"
                           f"home_nums_matches_played = {home_nums_matches_played}\naway_teams = {away_teams}\n"
                           f"away_positions = {away_positions}\naway_points = {away_points}\n"
                           f"away_nums_matches_played = {away_nums_matches_played}\nmatch_times = {match_times}\n"
                           f"h_form_W = {h_form_W}\nh_form_D = {h_form_D}\nh_form_L = {h_form_L}\n"
                           f"a_form_W = {a_form_W}\na_form_D = {a_form_D}\na_form_L = {a_form_L}\n"
                           f"prob_33_5s = {prob_33_5s}\nprob_43_5s = {prob_43_5s}\nprob_53_5s = {prob_53_5s}\n"
                           f"prob_sh1_4_5s = {prob_sh1_4_5s}\nprob_sh1_7_5s = {prob_sh1_7_5s}\n"
                           f"prob_sh2_4_5s = {prob_sh2_4_5s}\nprob_sh2_7_5s = {prob_sh2_7_5s}\n"
                           f"prob_12s = {prob_12s}\nprob_HWs = {prob_HWs}\nprob_AWs = {prob_AWs}\n"
                           f"prob_33_5_H_indps = {prob_33_5_H_indps}\nprob_43_5_H_indps = {prob_43_5_H_indps}\nprob_53_5_H_indps = {prob_53_5_H_indps}\n"
                           f"prob_sh1_4_5_H_indps = {prob_sh1_4_5_H_indps}\nprob_sh1_7_5_H_indps = {prob_sh1_7_5_H_indps}\n"
                           f"prob_sh2_4_5_H_indps = {prob_sh2_4_5_H_indps}\nprob_sh2_7_5_H_indps = {prob_sh2_7_5_H_indps}\n"
                           f"prob_12_H_indps = {prob_12_H_indps}\n"
                           f"prob_HW_H_indps = {prob_HW_H_indps}\nprob_AW_H_indps = {prob_AW_H_indps}\n"
                           f"prob_33_5_A_indps = {prob_33_5_A_indps}\nprob_43_5_A_indps = {prob_43_5_A_indps}\nprob_53_5_A_indps = {prob_53_5_A_indps}\n"
                           f"prob_sh1_4_5_A_indps = {prob_sh1_4_5_A_indps}\nprob_sh1_7_5_A_indps = {prob_sh1_7_5_A_indps}\n"
                           f"prob_sh2_4_5_A_indps = {prob_sh2_4_5_A_indps}\nprob_sh2_7_5_A_indps = {prob_sh2_7_5_A_indps}\n"
                           f"prob_12_A_indps = {prob_12_A_indps}\n"
                           f"prob_HW_A_indps = {prob_HW_A_indps}\nprob_AW_A_indps = {prob_AW_A_indps}\n"
                           f"home_z_prob = {home_z_prob}\naway_z_prob = {away_z_prob}\ndiff_z_prob = {diff_z_prob}\n"
                           f"sport = {sport}\n_1HWS = {_1HWS}\n_2AWS = {_2AWS}\nOVER_33_5_S = {OVER_33_5_S}\n"
                           f"OVER_43_5_S = {OVER_43_5_S}\nOVER_53_5_S = {OVER_53_5_S}\n"
                           f"OVER_sh1_4_5_S = {OVER_sh1_4_5_S}\nOVER_sh1_7_5_S = {OVER_sh1_7_5_S}\n"
                           f"OVER_sh2_4_5_S = {OVER_sh2_4_5_S}\nOVER_sh2_7_5_S = {OVER_sh2_7_5_S}\n"
                           f"_12S = {_12S}\nmatch_date = {set_date_s_size()[0]}\n"
                           f"HTGAVG = {ht_g_avgs}\nATGAVG = {at_g_avgs}\nBTHGAVG = {bth_g_avgs}\nBTAGAVG = {bta_g_avgs}\n\n\n\n\n")
            except UnicodeError:
                pass
            except IndexError:
                continue

    if CONFINTVLS.index(CONFINTVL) == 0:
        print_all_data()

driver.quit()

end_time = time.time()
print(f"run speed: {end_time - start_time}s")
