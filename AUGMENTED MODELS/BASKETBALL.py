import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, ElementClickInterceptedException, UnexpectedAlertPresentException, \
    WebDriverException, NoSuchWindowException, TimeoutException, InvalidSessionIdException
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

OUTCOMES = ["HW", "AW", "ETov26.5", "ETov33.5", "ETov40.5", "ETov46.5", "ETov56.5", "ETov22.5", "ETov36.5", "ETov49.5",
            "GTov146.5", "GTov166.5", "GTov186.5", "GTov201.5", "GTov212.5", "GTov226.5", "12"]

start_time = time.time()
SPORT_ = master_sport_list()[0][5]

chrome_path = game_criteria()[11][1]
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
    window_before = driver.window_handles[0]
    window_ads0 = driver.window_handles[1]
    driver.switch_to.window(window_before)
    driver.switch_to.window(window_ads0)
    driver.close()
    driver.switch_to.window(window_before)
else:
    window_before = driver.window_handles[1]
    window_ads0 = driver.window_handles[0]
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
driver.find_element(By.CSS_SELECTOR,
                    '[class="modal__window modal__window--settings"] [class="close modal__closeButton"]').click()
sleep(1)


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


def team_data():
    country = \
        driver.find_element(By.CSS_SELECTOR, '.tournamentHeaderDescription .tournamentHeader__country').text.split(':')[
            0]
    league = \
        driver.find_element(By.CSS_SELECTOR, '.tournamentHeaderDescription .tournamentHeader__country').text.split(':')[
            1].split(' - ')[0]
    try:
        home_team = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__home  .participant__participantName a').text
    except NoSuchElementException:
        home_teamw = driver.find_elements(By.CSS_SELECTOR,
                                          '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[
            0].text
        home_teamv = driver.find_elements(By.CSS_SELECTOR,
                                          '[class="duelParticipant__home duelParticipant__doubles "] .participant__participantNameWrapper a')[
            1].text
        home_team = f"{home_teamw}/{home_teamv}"
    try:
        away_team = driver.find_element(By.CSS_SELECTOR, '.duelParticipant__away  .participant__participantName a').text
    except NoSuchElementException:
        away_teamw = driver.find_elements(By.CSS_SELECTOR,
                                          '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[
            0].text
        away_teamv = driver.find_elements(By.CSS_SELECTOR,
                                          '[class="duelParticipant__away duelParticipant__doubles "] .participant__participantNameWrapper a')[
            1].text
        away_team = f"{away_teamw}/{away_teamv}"
    leagues.append(league)
    countries.append(country)
    away_teams.append(away_team)
    home_teams.append(home_team)


def pts_pos_mp():
    try:
        first_entry = int(driver.find_elements(By.CSS_SELECTOR,
                                               '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[
                              0].text.strip())
        print(f"This is the first table entry: {first_entry}")
    except IndexError:
        try:
            driver.refresh()
            sleep(4)
            first_entry = int(driver.find_elements(By.CSS_SELECTOR,
                                                   '.ui-table__row:first-child [class=" table__cell table__cell--value   "]')[
                                  0].text.strip())
            print(f"This is the first table entry: {first_entry}")
        except IndexError:
            driver.refresh()
            sleep(2)
            first_entry = 0

    if selected_teams_names[0].text == home_teamx:
        try:
            home_t_position = \
                driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[0].text.split('.')[
                    0].strip()
            home_positions.append(int(home_t_position))
        except IndexError:
            home_positions.append(0)
        if first_entry > 10:
            try:
                home_t_mp = driver.find_elements(By.CSS_SELECTOR,
                                                 '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[
                    0].text.strip()
                home_nums_matches_played.append(int(home_t_mp))
            except IndexError:
                home_nums_matches_played.append(0)
        else:
            print("Home Team No Reach1")
        try:
            home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[
                0].text.strip()
            home_points.append(int(home_t_point))
        except IndexError:
            try:
                home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[
                    0].text.strip()
                home_points.append(float(home_t_point))
            except IndexError:
                home_points.append(0)
    else:
        try:
            away_t_position = \
                driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[0].text.split('.')[
                    0].strip()
            away_positions.append(int(away_t_position))
        except IndexError:
            away_positions.append(0)
        if first_entry > 10:
            try:
                away_t_mp = driver.find_elements(By.CSS_SELECTOR,
                                                 '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[
                    0].text.strip()
                away_nums_matches_played.append(int(away_t_mp))
            except IndexError:
                away_nums_matches_played.append(0)
        else:
            print("Away Team No Reach1")
        try:
            away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[
                0].text.strip()
            away_points.append(int(away_t_point))
        except IndexError:
            try:
                away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[
                    0].text.strip()
                away_points.append(float(away_t_point))
            except IndexError:
                away_points.append(0)
    try:
        if selected_teams_names[1].text == away_teamx:
            try:
                away_t_position = \
                    driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[1].text.split('.')[
                        0].strip()
                away_positions.append(int(away_t_position))
            except IndexError:
                away_positions.append(0)
            if first_entry > 10:
                try:
                    away_t_mp = driver.find_elements(By.CSS_SELECTOR,
                                                     '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[
                        3].text.strip()
                    away_nums_matches_played.append(int(away_t_mp))
                except IndexError:
                    away_nums_matches_played.append(0)
            else:
                print("Away Team No Reach2")
            try:
                away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[
                    1].text.strip()
                away_points.append(int(away_t_point))
            except IndexError:
                try:
                    away_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[
                        1].text.strip()
                    away_points.append(float(away_t_point))
                except IndexError:
                    away_points.append(0)
        else:
            try:
                home_t_position = \
                    driver.find_elements(By.CSS_SELECTOR, ".table__row--selected .tableCellRank")[1].text.split('.')[
                        0].strip()
                home_positions.append(int(home_t_position))
            except IndexError:
                home_positions.append(0)
            if first_entry > 10:
                try:
                    home_t_mp = driver.find_elements(By.CSS_SELECTOR,
                                                     '[class="ui-table__row table__row--selected "] [class=" table__cell table__cell--value   "]')[
                        3].text.strip()
                    home_nums_matches_played.append(int(home_t_mp))
                except IndexError:
                    home_nums_matches_played.append(0)
            else:
                print("Home Team No Reach2")
            try:
                home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--points ')[
                    1].text.strip()
                home_points.append(int(home_t_point))
            except IndexError:
                try:
                    home_t_point = driver.find_elements(By.CSS_SELECTOR, '.table__row--selected  .table__cell--pct ')[
                        1].text.strip()
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


def append_zeroes():
    away_positions.append(0)
    away_points.append(0)
    home_positions.append(0)
    home_points.append(0)
    home_z_prob.append(0.5)
    away_z_prob.append(0.5)
    diff_z_prob.append(0.01)


def h2h_aggregator(m, home_score, away_score, home_x, away_x):
    global valid_games
    global count_HW
    global count_AW
    global count_etov_26_5
    global count_etov_33_5
    global count_etov_40_5
    global count_etov_46_5
    global count_etov_56_5
    global count_etov_22_5
    global count_etov_36_5
    global count_etov_49_5
    global count_gtov_146_5
    global count_gtov_166_5
    global count_gtov_186_5
    global count_gtov_201_5
    global count_gtov_212_5
    global count_gtov_226_5
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
    if 0.5 * int(home_score[m].text) >= 27 and 0.5 * int(away_score[m].text) >= 27:
        count_etov_26_5 += 1
    if 0.5 * int(home_score[m].text) >= 34 and 0.5 * int(away_score[m].text) >= 34:
        count_etov_33_5 += 1
    if 0.5 * int(home_score[m].text) >= 41 and 0.5 * int(away_score[m].text) >= 41:
        count_etov_40_5 += 1
    if 0.5 * int(home_score[m].text) >= 47 and 0.5 * int(away_score[m].text) >= 47:
        count_etov_46_5 += 1
    if 0.5 * int(home_score[m].text) >= 57 and 0.5 * int(away_score[m].text) >= 57:
        count_etov_56_5 += 1
    if 0.5 * int(home_score[m].text) >= 23 and 0.5 * int(away_score[m].text) >= 23:
        count_etov_22_5 += 1
    if 0.5 * int(home_score[m].text) >= 37 and 0.5 * int(away_score[m].text) >= 37:
        count_etov_36_5 += 1
    if 0.5 * int(home_score[m].text) >= 50 and 0.5 * int(away_score[m].text) >= 50:
        count_etov_49_5 += 1
    if (int(home_score[m].text) + int(away_score[m].text)) >= 147:
        count_gtov_146_5 += 1
    if (int(home_score[m].text) + int(away_score[m].text)) >= 167:
        count_gtov_166_5 += 1
    if (int(home_score[m].text) + int(away_score[m].text)) >= 187:
        count_gtov_186_5 += 1
    if (int(home_score[m].text) + int(away_score[m].text)) >= 202:
        count_gtov_201_5 += 1
    if (int(home_score[m].text) + int(away_score[m].text)) >= 213:
        count_gtov_212_5 += 1
    if (int(home_score[m].text) + int(away_score[m].text)) >= 227:
        count_gtov_226_5 += 1
    if int(home_score[m].text) != int(away_score[m].text):
        count_12 += 1


def h2h_prob_calc():
    global valid_games
    global count_HW
    global count_AW
    global count_etov_26_5
    global count_etov_33_5
    global count_etov_40_5
    global count_etov_46_5
    global count_etov_56_5
    global count_etov_22_5
    global count_etov_36_5
    global count_etov_49_5
    global count_gtov_146_5
    global count_gtov_166_5
    global count_gtov_186_5
    global count_gtov_201_5
    global count_gtov_212_5
    global count_gtov_226_5
    global count_12

    prob_etov_26_5i = float(count_etov_26_5 / valid_games)
    prob_etov_33_5i = float(count_etov_33_5 / valid_games)
    prob_etov_40_5i = float(count_etov_40_5 / valid_games)
    prob_etov_46_5i = float(count_etov_46_5 / valid_games)
    prob_etov_56_5i = float(count_etov_56_5 / valid_games)
    prob_etov_22_5i = float(count_etov_22_5 / valid_games)
    prob_etov_36_5i = float(count_etov_36_5 / valid_games)
    prob_etov_49_5i = float(count_etov_49_5 / valid_games)
    prob_gtov_146_5i = float(count_gtov_146_5 / valid_games)
    prob_gtov_166_5i = float(count_gtov_166_5 / valid_games)
    prob_gtov_186_5i = float(count_gtov_186_5 / valid_games)
    prob_gtov_201_5i = float(count_gtov_201_5 / valid_games)
    prob_gtov_212_5i = float(count_gtov_212_5 / valid_games)
    prob_gtov_226_5i = float(count_gtov_226_5 / valid_games)
    prob_12i = float(count_12 / valid_games)
    prob_HW = float(count_HW / valid_games)
    prob_AW = float(count_AW / valid_games)

    if prob_HW == 1.0:
        prob_HW -= 0.01
    if prob_AW == 1.0:
        prob_AW -= 0.01
    if prob_etov_26_5i == 1.0:
        prob_etov_26_5i -= 0.01
    if prob_etov_33_5i == 1.0:
        prob_etov_33_5i -= 0.01
    if prob_etov_40_5i == 1.0:
        prob_etov_40_5i -= 0.01
    if prob_etov_46_5i == 1.0:
        prob_etov_46_5i -= 0.01
    if prob_etov_56_5i == 1.0:
        prob_etov_56_5i -= 0.01
    if prob_etov_22_5i == 1.0:
        prob_etov_22_5i -= 0.01
    if prob_etov_36_5i == 1.0:
        prob_etov_36_5i -= 0.01
    if prob_etov_49_5i == 1.0:
        prob_etov_49_5i -= 0.01
    if prob_gtov_146_5i == 1.0:
        prob_gtov_146_5i -= 0.01
    if prob_gtov_166_5i == 1.0:
        prob_gtov_166_5i -= 0.01
    if prob_gtov_186_5i == 1.0:
        prob_gtov_186_5i -= 0.01
    if prob_gtov_201_5i == 1.0:
        prob_gtov_201_5i -= 0.01
    if prob_gtov_212_5i == 1.0:
        prob_gtov_212_5i -= 0.01
    if prob_gtov_226_5i == 1.0:
        prob_gtov_226_5i -= 0.01
    if prob_12i == 1.0:
        prob_12i -= 0.01

    if prob_etov_26_5i == 0:
        prob_etov_26_5i += 0.01
    if prob_etov_33_5i == 0:
        prob_etov_33_5i += 0.01
    if prob_etov_40_5i == 0:
        prob_etov_40_5i += 0.01
    if prob_etov_46_5i == 0:
        prob_etov_46_5i += 0.01
    if prob_etov_56_5i == 0:
        prob_etov_56_5i += 0.01
    if prob_etov_22_5i == 0:
        prob_etov_22_5i += 0.01
    if prob_etov_36_5i == 0:
        prob_etov_36_5i += 0.01
    if prob_etov_49_5i == 0:
        prob_etov_49_5i += 0.01
    if prob_gtov_146_5i == 0:
        prob_gtov_146_5i += 0.01
    if prob_gtov_166_5i == 0:
        prob_gtov_166_5i += 0.01
    if prob_gtov_186_5i == 0:
        prob_gtov_186_5i += 0.01
    if prob_gtov_201_5i == 0:
        prob_gtov_201_5i += 0.01
    if prob_gtov_212_5i == 0:
        prob_gtov_212_5i += 0.01
    if prob_gtov_226_5i == 0:
        prob_gtov_226_5i += 0.01
    if prob_12i == 0:
        prob_12i += 0.01
    if prob_HW == 0:
        prob_HW += 0.01
    if prob_AW == 0:
        prob_AW += 0.01
    return [prob_HW, prob_AW, prob_etov_26_5i, prob_etov_33_5i, prob_etov_40_5i, prob_etov_46_5i, prob_etov_56_5i,
            prob_etov_22_5i, prob_etov_36_5i, prob_etov_49_5i, prob_gtov_146_5i, prob_gtov_166_5i,
            prob_gtov_186_5i, prob_gtov_201_5i, prob_gtov_212_5i, prob_gtov_226_5i, prob_12i]


def h2h_appender(prb_HW, prb_AW, prb_etov_26_5, prb_etov_33_5, prb_etov_40_5, prb_etov_46_5, prb_etov_56_5,
                 prb_etov_22_5, prb_etov_36_5, prb_etov_49_5, prb_gtov_146_5, prb_gtov_166_5,
                 prb_gtov_186_5, prb_gtov_201_5, prb_gtov_212_5, prb_gtov_226_5, prb_12):
    prob_HWs.append(prb_HW)
    prob_AWs.append(prb_AW)
    prob_etov_26_5s.append(prb_etov_26_5)
    prob_etov_33_5s.append(prb_etov_33_5)
    prob_etov_40_5s.append(prb_etov_40_5)
    prob_etov_46_5s.append(prb_etov_46_5)
    prob_etov_56_5s.append(prb_etov_56_5)
    prob_etov_22_5s.append(prb_etov_22_5)
    prob_etov_36_5s.append(prb_etov_36_5)
    prob_etov_49_5s.append(prb_etov_49_5)
    prob_gtov_146_5s.append(prb_gtov_146_5)
    prob_gtov_166_5s.append(prb_gtov_166_5)
    prob_gtov_186_5s.append(prb_gtov_186_5)
    prob_gtov_201_5s.append(prb_gtov_201_5)
    prob_gtov_212_5s.append(prb_gtov_212_5)
    prob_gtov_226_5s.append(prb_gtov_226_5)
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
    global count_etov_26_5_H_indp
    global count_etov_33_5_H_indp
    global count_etov_40_5_H_indp
    global count_etov_46_5_H_indp
    global count_etov_56_5_H_indp
    global count_etov_22_5_H_indp
    global count_etov_36_5_H_indp
    global count_etov_49_5_H_indp
    global count_gtov_146_5_H_indp
    global count_gtov_166_5_H_indp
    global count_gtov_186_5_H_indp
    global count_gtov_201_5_H_indp
    global count_gtov_212_5_H_indp
    global count_gtov_226_5_H_indp
    global count_12_H_indp

    valid_games_H_indp += 1
    if (int(home_score[k].text) > int(away_score[k].text)) and (home_x[k].text == home_teamx):
        count_HW_H_indp += 1
    if (int(away_score[k].text) > int(home_score[k].text)) and (away_x[k].text == home_teamx):
        count_HW_H_indp += 1
    if 0.5 * int(home_score[k].text) >= 27 and 0.5 * int(away_score[k].text) >= 27:
        count_etov_26_5_H_indp += 1
    if 0.5 * int(home_score[k].text) >= 34 and 0.5 * int(away_score[k].text) >= 34:
        count_etov_33_5_H_indp += 1
    if 0.5 * int(home_score[k].text) >= 41 and 0.5 * int(away_score[k].text) >= 41:
        count_etov_40_5_H_indp += 1
    if 0.5 * int(home_score[k].text) >= 47 and 0.5 * int(away_score[k].text) >= 47:
        count_etov_46_5_H_indp += 1
    if 0.5 * int(home_score[k].text) >= 57 and 0.5 * int(away_score[k].text) >= 57:
        count_etov_56_5_H_indp += 1
    if 0.5 * int(home_score[k].text) >= 23 and 0.5 * int(away_score[k].text) >= 23:
        count_etov_22_5_H_indp += 1
    if 0.5 * int(home_score[k].text) >= 37 and 0.5 * int(away_score[k].text) >= 37:
        count_etov_36_5_H_indp += 1
    if 0.5 * int(home_score[k].text) >= 50 and 0.5 * int(away_score[k].text) >= 50:
        count_etov_49_5_H_indp += 1

    if (int(home_score[k].text) + int(away_score[k].text)) >= 147 and (home_x[k].text == home_teamx) and int(home_score[k].text) >= 73:
        count_gtov_146_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 147 and (away_x[k].text == home_teamx) and int(
            away_score[k].text) >= 73:
        count_gtov_146_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 167 and (home_x[k].text == home_teamx) and int(
            home_score[k].text) >= 83:
        count_gtov_166_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 167 and (away_x[k].text == home_teamx) and int(
            away_score[k].text) >= 83:
        count_gtov_166_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 187 and (home_x[k].text == home_teamx) and int(
            home_score[k].text) >= 93:
        count_gtov_186_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 187 and (away_x[k].text == home_teamx) and int(
            away_score[k].text) >= 93:
        count_gtov_186_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 202 and (home_x[k].text == home_teamx) and int(
            home_score[k].text) >= 101:
        count_gtov_201_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 202 and (away_x[k].text == home_teamx) and int(
            away_score[k].text) >= 101:
        count_gtov_201_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 213 and (home_x[k].text == home_teamx) and int(
            home_score[k].text) >= 106:
        count_gtov_212_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 213 and (away_x[k].text == home_teamx) and int(
            away_score[k].text) >= 106:
        count_gtov_212_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 227 and (home_x[k].text == home_teamx) and int(
            home_score[k].text) >= 113:
        count_gtov_226_5_H_indp += 1
    if (int(home_score[k].text) + int(away_score[k].text)) >= 227 and (away_x[k].text == home_teamx) and int(
            away_score[k].text) >= 113:
        count_gtov_226_5_H_indp += 1
    if int(home_score[k].text) != int(away_score[k].text) and int(home_score[k].text) >= 1 and (
            home_x[k].text == home_teamx):
        count_12_H_indp += 1
    if int(away_score[k].text) != int(home_score[k].text) and int(away_score[k].text) >= 1 and (
            away_x[k].text == home_teamx):
        count_12_H_indp += 1


def ht_indp_prob_calc():
    global valid_games_H_indp
    global count_HW_H_indp
    global count_etov_26_5_H_indp
    global count_etov_33_5_H_indp
    global count_etov_40_5_H_indp
    global count_etov_46_5_H_indp
    global count_etov_56_5_H_indp
    global count_etov_22_5_H_indp
    global count_etov_36_5_H_indp
    global count_etov_49_5_H_indp
    global count_gtov_146_5_H_indp
    global count_gtov_166_5_H_indp
    global count_gtov_186_5_H_indp
    global count_gtov_201_5_H_indp
    global count_gtov_212_5_H_indp
    global count_gtov_226_5_H_indp
    global count_12_H_indp

    prob_HW_H_indp = float(count_HW_H_indp / valid_games_H_indp)
    prob_AW_H_indp = 1 - prob_HW_H_indp
    prob_etov_26_5_H_indp = float(count_etov_26_5_H_indp / valid_games_H_indp)
    prob_etov_33_5_H_indp = float(count_etov_33_5_H_indp / valid_games_H_indp)
    prob_etov_40_5_H_indp = float(count_etov_40_5_H_indp / valid_games_H_indp)
    prob_etov_46_5_H_indp = float(count_etov_46_5_H_indp / valid_games_H_indp)
    prob_etov_56_5_H_indp = float(count_etov_56_5_H_indp / valid_games_H_indp)
    prob_etov_22_5_H_indp = float(count_etov_22_5_H_indp / valid_games_H_indp)
    prob_etov_36_5_H_indp = float(count_etov_36_5_H_indp / valid_games_H_indp)
    prob_etov_49_5_H_indp = float(count_etov_49_5_H_indp / valid_games_H_indp)
    prob_gtov_146_5_H_indp = float(count_gtov_146_5_H_indp / valid_games_H_indp)
    prob_gtov_166_5_H_indp = float(count_gtov_166_5_H_indp / valid_games_H_indp)
    prob_gtov_186_5_H_indp = float(count_gtov_186_5_H_indp / valid_games_H_indp)
    prob_gtov_201_5_H_indp = float(count_gtov_201_5_H_indp / valid_games_H_indp)
    prob_gtov_212_5_H_indp = float(count_gtov_212_5_H_indp / valid_games_H_indp)
    prob_gtov_226_5_H_indp = float(count_gtov_226_5_H_indp / valid_games_H_indp)
    prob_12_H_indp = float(count_12_H_indp / valid_games_H_indp)

    if prob_HW_H_indp == 1.0:
        prob_HW_H_indp -= 0.01
    if prob_AW_H_indp == 1.0:
        prob_AW_H_indp -= 0.01
    if prob_etov_26_5_H_indp == 1.0:
        prob_etov_26_5_H_indp -= 0.01
    if prob_etov_33_5_H_indp == 1.0:
        prob_etov_33_5_H_indp -= 0.01
    if prob_etov_40_5_H_indp == 1.0:
        prob_etov_40_5_H_indp -= 0.01
    if prob_etov_46_5_H_indp == 1.0:
        prob_etov_46_5_H_indp -= 0.01
    if prob_etov_56_5_H_indp == 1.0:
        prob_etov_56_5_H_indp -= 0.01
    if prob_etov_22_5_H_indp == 1.0:
        prob_etov_22_5_H_indp -= 0.01
    if prob_etov_36_5_H_indp == 1.0:
        prob_etov_36_5_H_indp -= 0.01
    if prob_etov_49_5_H_indp == 1.0:
        prob_etov_49_5_H_indp -= 0.01
    if prob_gtov_146_5_H_indp == 1.0:
        prob_gtov_146_5_H_indp -= 0.01
    if prob_gtov_166_5_H_indp == 1.0:
        prob_gtov_166_5_H_indp -= 0.01
    if prob_gtov_186_5_H_indp == 1.0:
        prob_gtov_186_5_H_indp -= 0.01
    if prob_gtov_201_5_H_indp == 1.0:
        prob_gtov_201_5_H_indp -= 0.01
    if prob_gtov_212_5_H_indp == 1.0:
        prob_gtov_212_5_H_indp -= 0.01
    if prob_gtov_226_5_H_indp == 1.0:
        prob_gtov_226_5_H_indp -= 0.01
    if prob_12_H_indp == 1.0:
        prob_12_H_indp -= 0.01

    if prob_etov_26_5_H_indp == 0:
        prob_etov_26_5_H_indp += 0.01
    if prob_etov_33_5_H_indp == 0:
        prob_etov_33_5_H_indp += 0.01
    if prob_etov_40_5_H_indp == 0:
        prob_etov_40_5_H_indp += 0.01
    if prob_etov_46_5_H_indp == 0:
        prob_etov_46_5_H_indp += 0.01
    if prob_etov_56_5_H_indp == 0:
        prob_etov_56_5_H_indp += 0.01
    if prob_etov_22_5_H_indp == 0:
        prob_etov_22_5_H_indp += 0.01
    if prob_etov_36_5_H_indp == 0:
        prob_etov_36_5_H_indp += 0.01
    if prob_etov_49_5_H_indp == 0:
        prob_etov_49_5_H_indp += 0.01
    if prob_gtov_146_5_H_indp == 0:
        prob_gtov_146_5_H_indp += 0.01
    if prob_gtov_166_5_H_indp == 0:
        prob_gtov_166_5_H_indp += 0.01
    if prob_gtov_186_5_H_indp == 0:
        prob_gtov_186_5_H_indp += 0.01
    if prob_gtov_201_5_H_indp == 0:
        prob_gtov_201_5_H_indp += 0.01
    if prob_gtov_212_5_H_indp == 0:
        prob_gtov_212_5_H_indp += 0.01
    if prob_gtov_226_5_H_indp == 0:
        prob_gtov_226_5_H_indp += 0.01
    if prob_12_H_indp == 0:
        prob_12_H_indp += 0.01
    if prob_HW_H_indp == 0:
        prob_HW_H_indp += 0.01
    if prob_AW_H_indp == 0:
        prob_AW_H_indp += 0.01
    return [prob_HW_H_indp, prob_AW_H_indp, prob_etov_26_5_H_indp, prob_etov_33_5_H_indp, prob_etov_40_5_H_indp,
            prob_etov_46_5_H_indp, prob_etov_56_5_H_indp,
            prob_etov_22_5_H_indp, prob_etov_36_5_H_indp, prob_etov_49_5_H_indp, prob_gtov_146_5_H_indp,
            prob_gtov_166_5_H_indp,
            prob_gtov_186_5_H_indp, prob_gtov_201_5_H_indp, prob_gtov_212_5_H_indp, prob_gtov_226_5_H_indp,
            prob_12_H_indp]


def ht_indp_appender(prb_HW_H_indp, prb_AW_H_indp, prb_etov_26_5_H_indp, prb_etov_33_5_H_indp, prb_etov_40_5_H_indp,
                     prb_etov_46_5_H_indp, prb_etov_56_5_H_indp,
                     prb_etov_22_5_H_indp, prb_etov_36_5_H_indp, prb_etov_49_5_H_indp, prb_gtov_146_5_H_indp,
                     prb_gtov_166_5_H_indp,
                     prb_gtov_186_5_H_indp, prb_gtov_201_5_H_indp, prb_gtov_212_5_H_indp, prb_gtov_226_5_H_indp,
                     prb_12_H_indp):
    prob_HW_H_indps.append(prb_HW_H_indp)
    prob_AW_H_indps.append(prb_AW_H_indp)
    prob_etov_26_5_H_indps.append(prb_etov_26_5_H_indp)
    prob_etov_33_5_H_indps.append(prb_etov_33_5_H_indp)
    prob_etov_40_5_H_indps.append(prb_etov_40_5_H_indp)
    prob_etov_46_5_H_indps.append(prb_etov_46_5_H_indp)
    prob_etov_56_5_H_indps.append(prb_etov_56_5_H_indp)
    prob_etov_22_5_H_indps.append(prb_etov_22_5_H_indp)
    prob_etov_36_5_H_indps.append(prb_etov_36_5_H_indp)
    prob_etov_49_5_H_indps.append(prb_etov_49_5_H_indp)
    prob_gtov_146_5_H_indps.append(prb_gtov_146_5_H_indp)
    prob_gtov_166_5_H_indps.append(prb_gtov_166_5_H_indp)
    prob_gtov_186_5_H_indps.append(prb_gtov_186_5_H_indp)
    prob_gtov_201_5_H_indps.append(prb_gtov_201_5_H_indp)
    prob_gtov_212_5_H_indps.append(prb_gtov_212_5_H_indp)
    prob_gtov_226_5_H_indps.append(prb_gtov_226_5_H_indp)
    prob_12_H_indps.append(prb_12_H_indp)


def at_indp_aggregator(n, home_score, away_score, home_x, away_x):
    global valid_games_A_indp
    global count_AW_A_indp
    global count_etov_26_5_A_indp
    global count_etov_33_5_A_indp
    global count_etov_40_5_A_indp
    global count_etov_46_5_A_indp
    global count_etov_56_5_A_indp
    global count_etov_22_5_A_indp
    global count_etov_36_5_A_indp
    global count_etov_49_5_A_indp
    global count_gtov_146_5_A_indp
    global count_gtov_166_5_A_indp
    global count_gtov_186_5_A_indp
    global count_gtov_201_5_A_indp
    global count_gtov_212_5_A_indp
    global count_gtov_226_5_A_indp
    global count_12_A_indp

    valid_games_A_indp += 1
    if (int(home_score[n].text) > int(away_score[n].text)) and (home_x[n].text == away_teamx):
        count_AW_A_indp += 1
    if (int(away_score[n].text) > int(home_score[n].text)) and (away_x[n].text == away_teamx):
        count_AW_A_indp += 1
    if 0.5 * int(home_score[n].text) >= 27 and 0.5 * int(away_score[n].text) >= 27:
        count_etov_26_5_A_indp += 1
    if 0.5 * int(home_score[n].text) >= 34 and 0.5 * int(away_score[n].text) >= 34:
        count_etov_33_5_A_indp += 1
    if 0.5 * int(home_score[n].text) >= 41 and 0.5 * int(away_score[n].text) >= 41:
        count_etov_40_5_A_indp += 1
    if 0.5 * int(home_score[n].text) >= 47 and 0.5 * int(away_score[n].text) >= 47:
        count_etov_46_5_A_indp += 1
    if 0.5 * int(home_score[n].text) >= 57 and 0.5 * int(away_score[n].text) >= 57:
        count_etov_56_5_A_indp += 1
    if 0.5 * int(home_score[n].text) >= 23 and 0.5 * int(away_score[n].text) >= 23:
        count_etov_22_5_A_indp += 1
    if 0.5 * int(home_score[n].text) >= 37 and 0.5 * int(away_score[n].text) >= 37:
        count_etov_36_5_A_indp += 1
    if 0.5 * int(home_score[n].text) >= 50 and 0.5 * int(away_score[n].text) >= 50:
        count_etov_49_5_A_indp += 1

    if (int(home_score[n].text) + int(away_score[n].text)) >= 147 and (home_x[n].text == away_teamx) and int(
            home_score[n].text) >= 73:
        count_gtov_146_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 147 and (away_x[n].text == away_teamx) and int(
            away_score[n].text) >= 73:
        count_gtov_146_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 167 and (home_x[n].text == away_teamx) and int(
            home_score[n].text) >= 83:
        count_gtov_166_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 167 and (away_x[n].text == away_teamx) and int(
            away_score[n].text) >= 83:
        count_gtov_166_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 187 and (home_x[n].text == away_teamx) and int(
            home_score[n].text) >= 93:
        count_gtov_186_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 187 and (away_x[n].text == away_teamx) and int(
            away_score[n].text) >= 93:
        count_gtov_186_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 202 and (home_x[n].text == away_teamx) and int(
            home_score[n].text) >= 101:
        count_gtov_201_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 202 and (away_x[n].text == away_teamx) and int(
            away_score[n].text) >= 101:
        count_gtov_201_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 213 and (home_x[n].text == away_teamx) and int(
            home_score[n].text) >= 106:
        count_gtov_212_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 213 and (away_x[n].text == away_teamx) and int(
            away_score[n].text) >= 106:
        count_gtov_212_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 227 and (home_x[n].text == away_teamx) and int(
            home_score[n].text) >= 113:
        count_gtov_226_5_A_indp += 1
    if (int(home_score[n].text) + int(away_score[n].text)) >= 227 and (away_x[n].text == away_teamx) and int(
            away_score[n].text) >= 113:
        count_gtov_226_5_A_indp += 1
    if int(home_score[n].text) != int(away_score[n].text) and int(home_score[n].text) >= 1 and (
            home_x[n].text == away_teamx):
        count_12_A_indp += 1
    if int(away_score[n].text) != int(home_score[n].text) and int(away_score[n].text) >= 1 and (
            away_x[n].text == away_teamx):
        count_12_A_indp += 1


def at_indp_prob_calc():
    global valid_games_A_indp
    global count_AW_A_indp
    global count_etov_26_5_A_indp
    global count_etov_33_5_A_indp
    global count_etov_40_5_A_indp
    global count_etov_46_5_A_indp
    global count_etov_56_5_A_indp
    global count_etov_22_5_A_indp
    global count_etov_36_5_A_indp
    global count_etov_49_5_A_indp
    global count_gtov_146_5_A_indp
    global count_gtov_166_5_A_indp
    global count_gtov_186_5_A_indp
    global count_gtov_201_5_A_indp
    global count_gtov_212_5_A_indp
    global count_gtov_226_5_A_indp
    global count_12_A_indp

    prob_AW_A_indp = float(count_AW_A_indp / valid_games_A_indp)
    prob_HW_A_indp = 1 - prob_AW_A_indp
    prob_etov_26_5_A_indp = float(count_etov_26_5_A_indp / valid_games_A_indp)
    prob_etov_33_5_A_indp = float(count_etov_33_5_A_indp / valid_games_A_indp)
    prob_etov_40_5_A_indp = float(count_etov_40_5_A_indp / valid_games_A_indp)
    prob_etov_46_5_A_indp = float(count_etov_46_5_A_indp / valid_games_A_indp)
    prob_etov_56_5_A_indp = float(count_etov_56_5_A_indp / valid_games_A_indp)
    prob_etov_22_5_A_indp = float(count_etov_22_5_A_indp / valid_games_A_indp)
    prob_etov_36_5_A_indp = float(count_etov_36_5_A_indp / valid_games_A_indp)
    prob_etov_49_5_A_indp = float(count_etov_49_5_A_indp / valid_games_A_indp)
    prob_gtov_146_5_A_indp = float(count_gtov_146_5_A_indp / valid_games_A_indp)
    prob_gtov_166_5_A_indp = float(count_gtov_166_5_A_indp / valid_games_A_indp)
    prob_gtov_186_5_A_indp = float(count_gtov_186_5_A_indp / valid_games_A_indp)
    prob_gtov_201_5_A_indp = float(count_gtov_201_5_A_indp / valid_games_A_indp)
    prob_gtov_212_5_A_indp = float(count_gtov_212_5_A_indp / valid_games_A_indp)
    prob_gtov_226_5_A_indp = float(count_gtov_226_5_A_indp / valid_games_A_indp)
    prob_12_A_indp = float(count_12_A_indp / valid_games_A_indp)

    if prob_HW_A_indp == 1.0:
        prob_HW_A_indp -= 0.01
    if prob_AW_A_indp == 1.0:
        prob_AW_A_indp -= 0.01
    if prob_etov_26_5_A_indp == 1.0:
        prob_etov_26_5_A_indp -= 0.01
    if prob_etov_33_5_A_indp == 1.0:
        prob_etov_33_5_A_indp -= 0.01
    if prob_etov_40_5_A_indp == 1.0:
        prob_etov_40_5_A_indp -= 0.01
    if prob_etov_46_5_A_indp == 1.0:
        prob_etov_46_5_A_indp -= 0.01
    if prob_etov_56_5_A_indp == 1.0:
        prob_etov_56_5_A_indp -= 0.01
    if prob_etov_22_5_A_indp == 1.0:
        prob_etov_22_5_A_indp -= 0.01
    if prob_etov_36_5_A_indp == 1.0:
        prob_etov_36_5_A_indp -= 0.01
    if prob_etov_49_5_A_indp == 1.0:
        prob_etov_49_5_A_indp -= 0.01
    if prob_gtov_146_5_A_indp == 1.0:
        prob_gtov_146_5_A_indp -= 0.01
    if prob_gtov_166_5_A_indp == 1.0:
        prob_gtov_166_5_A_indp -= 0.01
    if prob_gtov_186_5_A_indp == 1.0:
        prob_gtov_186_5_A_indp -= 0.01
    if prob_gtov_201_5_A_indp == 1.0:
        prob_gtov_201_5_A_indp -= 0.01
    if prob_gtov_212_5_A_indp == 1.0:
        prob_gtov_212_5_A_indp -= 0.01
    if prob_gtov_226_5_A_indp == 1.0:
        prob_gtov_226_5_A_indp -= 0.01
    if prob_12_A_indp == 1.0:
        prob_12_A_indp -= 0.01

    if prob_etov_26_5_A_indp == 0:
        prob_etov_26_5_A_indp += 0.01
    if prob_etov_33_5_A_indp == 0:
        prob_etov_33_5_A_indp += 0.01
    if prob_etov_40_5_A_indp == 0:
        prob_etov_40_5_A_indp += 0.01
    if prob_etov_46_5_A_indp == 0:
        prob_etov_46_5_A_indp += 0.01
    if prob_etov_56_5_A_indp == 0:
        prob_etov_56_5_A_indp += 0.01
    if prob_etov_22_5_A_indp == 0:
        prob_etov_22_5_A_indp += 0.01
    if prob_etov_36_5_A_indp == 0:
        prob_etov_36_5_A_indp += 0.01
    if prob_etov_49_5_A_indp == 0:
        prob_etov_49_5_A_indp += 0.01
    if prob_gtov_146_5_A_indp == 0:
        prob_gtov_146_5_A_indp += 0.01
    if prob_gtov_166_5_A_indp == 0:
        prob_gtov_166_5_A_indp += 0.01
    if prob_gtov_186_5_A_indp == 0:
        prob_gtov_186_5_A_indp += 0.01
    if prob_gtov_201_5_A_indp == 0:
        prob_gtov_201_5_A_indp += 0.01
    if prob_gtov_212_5_A_indp == 0:
        prob_gtov_212_5_A_indp += 0.01
    if prob_gtov_226_5_A_indp == 0:
        prob_gtov_226_5_A_indp += 0.01
    if prob_12_A_indp == 0:
        prob_12_A_indp += 0.01
    if prob_HW_A_indp == 0:
        prob_HW_A_indp += 0.01
    if prob_AW_A_indp == 0:
        prob_AW_A_indp += 0.01

    return [prob_HW_A_indp, prob_AW_A_indp, prob_etov_26_5_A_indp, prob_etov_33_5_A_indp, prob_etov_40_5_A_indp,
            prob_etov_46_5_A_indp, prob_etov_56_5_A_indp,
            prob_etov_22_5_A_indp, prob_etov_36_5_A_indp, prob_etov_49_5_A_indp, prob_gtov_146_5_A_indp,
            prob_gtov_166_5_A_indp,
            prob_gtov_186_5_A_indp, prob_gtov_201_5_A_indp, prob_gtov_212_5_A_indp, prob_gtov_226_5_A_indp,
            prob_12_A_indp]


def at_indp_appender(prb_HW_A_indp, prb_AW_A_indp, prb_etov_26_5_A_indp, prb_etov_33_5_A_indp, prb_etov_40_5_A_indp,
                     prb_etov_46_5_A_indp, prb_etov_56_5_A_indp,
                     prb_etov_22_5_A_indp, prb_etov_36_5_A_indp, prb_etov_49_5_A_indp, prb_gtov_146_5_A_indp,
                     prb_gtov_166_5_A_indp,
                     prb_gtov_186_5_A_indp, prb_gtov_201_5_A_indp, prb_gtov_212_5_A_indp, prb_gtov_226_5_A_indp,
                     prb_12_A_indp):
    prob_HW_A_indps.append(prb_HW_A_indp)
    prob_AW_A_indps.append(prb_AW_A_indp)
    prob_etov_26_5_A_indps.append(prb_etov_26_5_A_indp)
    prob_etov_33_5_A_indps.append(prb_etov_33_5_A_indp)
    prob_etov_40_5_A_indps.append(prb_etov_40_5_A_indp)
    prob_etov_46_5_A_indps.append(prb_etov_46_5_A_indp)
    prob_etov_56_5_A_indps.append(prb_etov_56_5_A_indp)
    prob_etov_22_5_A_indps.append(prb_etov_22_5_A_indp)
    prob_etov_36_5_A_indps.append(prb_etov_36_5_A_indp)
    prob_etov_49_5_A_indps.append(prb_etov_49_5_A_indp)
    prob_gtov_146_5_A_indps.append(prb_gtov_146_5_A_indp)
    prob_gtov_166_5_A_indps.append(prb_gtov_166_5_A_indp)
    prob_gtov_186_5_A_indps.append(prb_gtov_186_5_A_indp)
    prob_gtov_201_5_A_indps.append(prb_gtov_201_5_A_indp)
    prob_gtov_212_5_A_indps.append(prb_gtov_212_5_A_indp)
    prob_gtov_226_5_A_indps.append(prb_gtov_226_5_A_indp)
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
                homme_x = driver.find_elements(By.CSS_SELECTOR,
                                               '.section:first-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
                awway_x = driver.find_elements(By.CSS_SELECTOR,
                                               '.section:first-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
                homme_score = driver.find_elements(By.CSS_SELECTOR,
                                                   '.section:first-child .h2h__row .h2h__result span:first-child')
                awway_score = driver.find_elements(By.CSS_SELECTOR,
                                                   '.section:first-child .h2h__row .h2h__result span:last-child')
                try:
                    if int(datte[k].text.split('.')[-1].strip()) >= YEAR:
                        if (int(homme_score[k].text) > int(awway_score[k].text)) and (
                                str(homme_x[k].text) == str(home_teamk)):
                            count_HW_form += 1
                        if (int(awway_score[k].text) > int(homme_score[k].text)) and (
                                str(awway_x[k].text) == str(home_teamk)):
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
                homme_x = driver.find_elements(By.CSS_SELECTOR,
                                               '.section:nth-child(2) .h2h__row .h2h__homeParticipant .h2h__participantInner')
                awway_x = driver.find_elements(By.CSS_SELECTOR,
                                               '.section:nth-child(2) .h2h__row .h2h__awayParticipant .h2h__participantInner')
                homme_score = driver.find_elements(By.CSS_SELECTOR,
                                                   '.section:nth-child(2) .h2h__row .h2h__result span:first-child')
                awway_score = driver.find_elements(By.CSS_SELECTOR,
                                                   '.section:nth-child(2) .h2h__row .h2h__result span:last-child')

                try:
                    if int(datte[n].text.split('.')[-1].strip()) >= YEAR:
                        if (int(homme_score[n].text) > int(awway_score[n].text)) and (
                                str(homme_x[n].text) == str(away_teamk)):
                            count_AW_form += 1
                        if (int(awway_score[n].text) > int(homme_score[n].text)) and (
                                str(awway_x[n].text) == str(away_teamk)):
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
        try:
            driver.find_element(By.LINK_TEXT, "ODDS").click()
        except (ElementClickInterceptedException, ElementNotInteractableException):
            pass
        sleep(1)
        try:
            try:
                driver.find_element(By.LINK_TEXT, "1X2 ODDS").click()
            except (ElementClickInterceptedException, ElementNotInteractableException):
                pass
            _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
            _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[2].text.strip()
            _1HWS.append(1 / float(_1HW))
            _2AWS.append(1 / float(_2AW))
            _12S.append(rdm.choice(CONFINTVLS))
        except NoSuchElementException:
            try:
                _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                _1HWS.append(1 / float(_1HW))
                _2AWS.append(1 / float(_2AW))
                _12S.append(rdm.choice(CONFINTVLS))
            except (ElementClickInterceptedException, ElementNotInteractableException):
                try:
                    driver.refresh()
                    sleep(2)
                    _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                    _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                    _1HWS.append(1 / float(_1HW))
                    _2AWS.append(1 / float(_2AW))
                    _12S.append(rdm.choice(CONFINTVLS))
                except NoSuchElementException:
                    _1HWS.append(0.5)
                    _2AWS.append(0.5)
                    _12S.append(rdm.choice(CONFINTVLS))
            except (IndexError, NoSuchElementException):
                _1HWS.append(0.5)
                _2AWS.append(0.5)
                _12S.append(rdm.choice(CONFINTVLS))
                print("No 1X2 ODDS")
        except IndexError:
            try:
                _1HW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                _2AW = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .ui-table__row:nth-child(1) .oddsCell__odd')[1].text.strip()
                _1HWS.append(1 / float(_1HW))
                _2AWS.append(1 / float(_2AW))
                _12S.append(rdm.choice(CONFINTVLS))
            except IndexError:
                _1HWS.append(0.5)
                _2AWS.append(0.5)
                _12S.append(rdm.choice(CONFINTVLS))
        except (ElementClickInterceptedException, ElementNotInteractableException):
            _1HWS.append(0.5)
            _2AWS.append(0.5)
            _12S.append(rdm.choice(CONFINTVLS))
        try:
            try:
                driver.find_element(By.LINK_TEXT, "O/U").click()
            except (ElementClickInterceptedException, ElementNotInteractableException):
                pass
            ahl = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds')
            for x in range(len(ahl)):
                try:
                    id_etov_26_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_etov_26_5 == "53.5":
                        OVER_etov_26_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_etov_26_5_S.append(1 / float(OVER_etov_26_5))
                        break
                    if x == (len(ahl) - 1):
                        OVER_etov_26_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_etov_26_5_S.append(0.5)
            for z in range(len(ahl)):
                try:
                    id_etov_33_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_etov_33_5 == "67.5":
                        OVER_etov_33_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_etov_33_5_S.append(1 / float(OVER_etov_33_5))
                        break
                    if z == (len(ahl) - 1):
                        OVER_etov_33_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_etov_33_5_S.append(0.5)
            for x in range(len(ahl)):
                try:
                    id_etov_40_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_etov_40_5 == "81.5":
                        OVER_etov_40_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_etov_40_5_S.append(1 / float(OVER_etov_40_5))
                        break
                    if x == (len(ahl) - 1):
                        OVER_etov_40_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_etov_40_5_S.append(0.5)
            for z in range(len(ahl)):
                try:
                    id_etov_46_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_etov_46_5 == "93.5":
                        OVER_etov_46_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_etov_46_5_S.append(1 / float(OVER_etov_46_5))
                        break
                    if z == (len(ahl) - 1):
                        OVER_etov_46_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_etov_46_5_S.append(0.5)
            for x in range(len(ahl)):
                try:
                    id_etov_56_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_etov_56_5 == "113.5":
                        OVER_etov_56_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_etov_56_5_S.append(1 / float(OVER_etov_56_5))
                        break
                    if x == (len(ahl) - 1):
                        OVER_etov_56_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_etov_56_5_S.append(0.5)
            for z in range(len(ahl)):
                try:
                    id_etov_22_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_etov_22_5 == "45.5":
                        OVER_etov_22_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_etov_22_5_S.append(1 / float(OVER_etov_22_5))
                        break
                    if z == (len(ahl) - 1):
                        OVER_etov_22_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_etov_22_5_S.append(0.5)
            for x in range(len(ahl)):
                try:
                    id_etov_36_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_etov_36_5 == "73.5":
                        OVER_etov_36_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_etov_36_5_S.append(1 / float(OVER_etov_36_5))
                        break
                    if x == (len(ahl) - 1):
                        OVER_etov_36_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_etov_36_5_S.append(0.5)
            for z in range(len(ahl)):
                try:
                    id_etov_49_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_etov_49_5 == "101.5":
                        OVER_etov_49_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_etov_49_5_S.append(1 / float(OVER_etov_49_5))
                        break
                    if z == (len(ahl) - 1):
                        OVER_etov_49_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_etov_49_5_S.append(0.5)

            for y in range(len(ahl)):
                try:
                    id_gtov_146_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_gtov_146_5 == "146.5":
                        OVER_gtov_146_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_gtov_146_5_S.append(1 / float(OVER_gtov_146_5))
                        break
                    if y == (len(ahl) - 1):
                        OVER_gtov_146_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_gtov_146_5_S.append(0.5)
            for y in range(len(ahl)):
                try:
                    id_gtov_166_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_gtov_166_5 == "166.5":
                        OVER_gtov_166_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_gtov_166_5_S.append(1 / float(OVER_gtov_166_5))
                        break
                    if y == (len(ahl) - 1):
                        OVER_gtov_166_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_gtov_166_5_S.append(0.5)
            for z in range(len(ahl)):
                try:
                    id_gtov_186_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_gtov_186_5 == "186.5":
                        OVER_gtov_186_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_gtov_186_5_S.append(1 / float(OVER_gtov_186_5))
                        break
                    if z == (len(ahl) - 1):
                        OVER_gtov_186_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_gtov_186_5_S.append(0.5)
            for x in range(len(ahl)):
                try:
                    id_gtov_201_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_gtov_201_5 == "201.5":
                        OVER_gtov_201_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({x + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_gtov_201_5_S.append(1 / float(OVER_gtov_201_5))
                        break
                    if x == (len(ahl) - 1):
                        OVER_gtov_201_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_gtov_201_5_S.append(0.5)
            for z in range(len(ahl)):
                try:
                    id_gtov_212_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_gtov_212_5 == "212.5":
                        OVER_gtov_212_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({z + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_gtov_212_5_S.append(1 / float(OVER_gtov_212_5))
                        break
                    if z == (len(ahl) - 1):
                        OVER_gtov_212_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_gtov_212_5_S.append(0.5)
            for y in range(len(ahl)):
                try:
                    id_gtov_226_5 = driver.find_element(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__noOddsCell').text
                    if id_gtov_226_5 == "226.5":
                        OVER_gtov_226_5 = driver.find_elements(By.CSS_SELECTOR, f'.oddsTab__tableWrapper .oddsCell__odds:nth-child({y + 1}) .ui-table__row:nth-child(1) .oddsCell__odd')[0].text.strip()
                        OVER_gtov_226_5_S.append(1 / float(OVER_gtov_226_5))
                        break
                    if y == (len(ahl) - 1):
                        OVER_gtov_226_5_S.append(0.5)
                except NoSuchElementException:
                    continue
                except IndexError:
                    OVER_gtov_226_5_S.append(0.5)

        except (NoSuchElementException, IndexError):
            OVER_etov_26_5_S.append(0.5)
            OVER_etov_33_5_S.append(0.5)
            OVER_etov_40_5_S.append(0.5)
            OVER_etov_46_5_S.append(0.5)
            OVER_etov_56_5_S.append(0.5)
            OVER_etov_22_5_S.append(0.5)
            OVER_etov_36_5_S.append(0.5)
            OVER_etov_49_5_S.append(0.5)
            OVER_gtov_146_5_S.append(0.5)
            OVER_gtov_166_5_S.append(0.5)
            OVER_gtov_186_5_S.append(0.5)
            OVER_gtov_201_5_S.append(0.5)
            OVER_gtov_212_5_S.append(0.5)
            OVER_gtov_226_5_S.append(0.5)
            print("No O/U")
    except (IndexError, StaleElementReferenceException, NoSuchElementException):
        driver.refresh()
        sleep(3)
        _1HWS.append(0.5)
        _2AWS.append(0.5)
        OVER_etov_26_5_S.append(0.5)
        OVER_etov_33_5_S.append(0.5)
        OVER_etov_40_5_S.append(0.5)
        OVER_etov_46_5_S.append(0.5)
        OVER_etov_56_5_S.append(0.5)
        OVER_etov_22_5_S.append(0.5)
        OVER_etov_36_5_S.append(0.5)
        OVER_etov_49_5_S.append(0.5)
        OVER_gtov_146_5_S.append(0.5)
        OVER_gtov_166_5_S.append(0.5)
        OVER_gtov_186_5_S.append(0.5)
        OVER_gtov_201_5_S.append(0.5)
        OVER_gtov_212_5_S.append(0.5)
        OVER_gtov_226_5_S.append(0.5)
        _12S.append(rdm.choice(CONFINTVLS))
        print("All Odds are assumed to be 0.5")


def writer(w, A, B, C, data):
    data.write(f"{countries[w]}|{leagues[w]}|{home_teams[w]}|{away_teams[w]}|{home_positions[w]}|"
               f"{away_positions[w]}|{home_nums_matches_played[w]}|{away_nums_matches_played[w]}|{home_points[w]}|"
               f"{away_points[w]}|{h_form_W[w]}|{h_form_D[w]}|{h_form_L[w]}|{a_form_W[w]}|{a_form_D[w]}|{a_form_L[w]}|"
               f"{ht_g_avgs[w]}|{at_g_avgs[w]}|{bth_g_avgs[w]}|{bta_g_avgs[w]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[w]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[w]}|"
               f"{OUTCOMES[2]}:-{bayesian_etov_26_5_d[w]}|{OUTCOMES[3]}:-{bayesian_etov_33_5_d[w]}|"
               f"{OUTCOMES[4]}:-{bayesian_etov_40_5_d[w]}|{OUTCOMES[5]}:-{bayesian_etov_46_5_d[w]}|"
               f"{OUTCOMES[6]}:-{bayesian_etov_56_5_d[w]}|{OUTCOMES[7]}:-{bayesian_etov_22_5_d[w]}|"
               f"{OUTCOMES[8]}:-{bayesian_etov_36_5_d[w]}|{OUTCOMES[9]}:-{bayesian_etov_49_5_d[w]}|"
               f"{OUTCOMES[10]}:-{bayesian_gtov_146_5_d[w]}|{OUTCOMES[11]}:-{bayesian_gtov_166_5_d[w]}|"
               f"{OUTCOMES[12]}:-{bayesian_gtov_186_5_d[w]}|{OUTCOMES[13]}:-{bayesian_gtov_201_5_d[w]}|"
               f"{OUTCOMES[14]}:-{bayesian_gtov_212_5_d[w]}|{OUTCOMES[15]}:-{bayesian_gtov_226_5_d[w]}|"
               f"{OUTCOMES[16]}:-{bayesian_12_d[w]}|"
               f"{match_times[w]}|{sport}|{C}_{A}_{B}|{set_date_s_size()[0]}\n")


def writer1(y, F, G, H, J, data):
    data.write(f"{countries[y]}|{leagues[y]}|{home_teams[y]}|{away_teams[y]}|{home_positions[y]}|"
               f"{away_positions[y]}|{home_nums_matches_played[y]}|{away_nums_matches_played[y]}|{home_points[y]}|"
               f"{away_points[y]}|{h_form_W[y]}|{h_form_D[y]}|{h_form_L[y]}|{a_form_W[y]}|{a_form_D[y]}|{a_form_L[y]}|"
               f"{ht_g_avgs[y]}|{at_g_avgs[y]}|{bth_g_avgs[y]}|{bta_g_avgs[y]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[y]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[y]}|"
               f"{OUTCOMES[2]}:-{bayesian_etov_26_5_d[y]}|{OUTCOMES[3]}:-{bayesian_etov_33_5_d[y]}|"
               f"{OUTCOMES[4]}:-{bayesian_etov_40_5_d[y]}|{OUTCOMES[5]}:-{bayesian_etov_46_5_d[y]}|"
               f"{OUTCOMES[6]}:-{bayesian_etov_56_5_d[y]}|{OUTCOMES[7]}:-{bayesian_etov_22_5_d[y]}|"
               f"{OUTCOMES[8]}:-{bayesian_etov_36_5_d[y]}|{OUTCOMES[9]}:-{bayesian_etov_49_5_d[y]}|"
               f"{OUTCOMES[10]}:-{bayesian_gtov_146_5_d[y]}|{OUTCOMES[11]}:-{bayesian_gtov_166_5_d[y]}|"
               f"{OUTCOMES[12]}:-{bayesian_gtov_186_5_d[y]}|{OUTCOMES[13]}:-{bayesian_gtov_201_5_d[y]}|"
               f"{OUTCOMES[14]}:-{bayesian_gtov_212_5_d[y]}|{OUTCOMES[15]}:-{bayesian_gtov_226_5_d[y]}|"
               f"{OUTCOMES[16]}:-{bayesian_12_d[y]}|"
               f"{match_times[y]}|{sport}|{J}_{F}_{G}_{H}|{set_date_s_size()[0]}\n")


def writer2(z, K, L, M, N, P, data):
    data.write(f"{countries[z]}|{leagues[z]}|{home_teams[z]}|{away_teams[z]}|{home_positions[z]}|"
               f"{away_positions[z]}|{home_nums_matches_played[z]}|{away_nums_matches_played[z]}|{home_points[z]}|"
               f"{away_points[z]}|{h_form_W[z]}|{h_form_D[z]}|{h_form_L[z]}|{a_form_W[z]}|{a_form_D[z]}|{a_form_L[z]}|"
               f"{ht_g_avgs[z]}|{at_g_avgs[z]}|{bth_g_avgs[z]}|{bta_g_avgs[z]}|"
               f"{OUTCOMES[0]}:-{bayesian_home_Win_d[z]}|{OUTCOMES[1]}:-{bayesian_away_Win_d[z]}|"
               f"{OUTCOMES[2]}:-{bayesian_etov_26_5_d[z]}|{OUTCOMES[3]}:-{bayesian_etov_33_5_d[z]}|"
               f"{OUTCOMES[4]}:-{bayesian_etov_40_5_d[z]}|{OUTCOMES[5]}:-{bayesian_etov_46_5_d[z]}|"
               f"{OUTCOMES[6]}:-{bayesian_etov_56_5_d[z]}|{OUTCOMES[7]}:-{bayesian_etov_22_5_d[z]}|"
               f"{OUTCOMES[8]}:-{bayesian_etov_36_5_d[z]}|{OUTCOMES[9]}:-{bayesian_etov_49_5_d[z]}|"
               f"{OUTCOMES[10]}:-{bayesian_gtov_146_5_d[z]}|{OUTCOMES[11]}:-{bayesian_gtov_166_5_d[z]}|"
               f"{OUTCOMES[12]}:-{bayesian_gtov_186_5_d[z]}|{OUTCOMES[13]}:-{bayesian_gtov_201_5_d[z]}|"
               f"{OUTCOMES[14]}:-{bayesian_gtov_212_5_d[z]}|{OUTCOMES[15]}:-{bayesian_gtov_226_5_d[z]}|"
               f"{OUTCOMES[16]}:-{bayesian_12_d[z]}|"
               f"{match_times[z]}|{sport}|{P}_{K}_{L}_{M}_{N}|{set_date_s_size()[0]}\n")


def baye_appender(baye_HW, baye_AW, baye_etov_26_5, baye_etov_33_5, baye_etov_40_5, baye_etov_46_5, baye_etov_56_5,
                  baye_etov_22_5, baye_etov_36_5, baye_etov_49_5, baye_gtov_146_5, baye_gtov_166_5,
                  baye_gtov_186_5, baye_gtov_201_5, baye_gtov_212_5, baye_gtov_226_5, baye_12):
    bayesian_home_Win_d.append(round((float(baye_HW)), 4))
    bayesian_away_Win_d.append(round((float(baye_AW)), 4))
    bayesian_etov_26_5_d.append(round((float(baye_etov_26_5)), 4))
    bayesian_etov_33_5_d.append(round((float(baye_etov_33_5)), 4))
    bayesian_etov_40_5_d.append(round((float(baye_etov_40_5)), 4))
    bayesian_etov_46_5_d.append(round((float(baye_etov_46_5)), 4))
    bayesian_etov_56_5_d.append(round((float(baye_etov_56_5)), 4))
    bayesian_etov_22_5_d.append(round((float(baye_etov_22_5)), 4))
    bayesian_etov_36_5_d.append(round((float(baye_etov_36_5)), 4))
    bayesian_etov_49_5_d.append(round((float(baye_etov_49_5)), 4))

    bayesian_gtov_146_5_d.append(round((float(baye_gtov_146_5)), 4))
    bayesian_gtov_166_5_d.append(round((float(baye_gtov_166_5)), 4))
    bayesian_gtov_186_5_d.append(round((float(baye_gtov_186_5)), 4))
    bayesian_gtov_201_5_d.append(round((float(baye_gtov_201_5)), 4))
    bayesian_gtov_212_5_d.append(round((float(baye_gtov_212_5)), 4))
    bayesian_gtov_226_5_d.append(round((float(baye_gtov_226_5)), 4))
    bayesian_12_d.append(round((float(baye_12)), 4))


def total_aggregator():
    global valid_games
    global valid_games_H_indp
    global valid_games_A_indp

    try:
        sub1 = driver.find_elements(By.CSS_SELECTOR, '.section:first-child .h2h__row')
        if len(sub1) == 0:
            ht_indp_appender(prb_HW_H_indp=0.01, prb_AW_H_indp=0.01, prb_etov_26_5_H_indp=0.01,
                             prb_etov_33_5_H_indp=0.01, prb_etov_40_5_H_indp=0.01, prb_etov_46_5_H_indp=0.01,
                             prb_etov_56_5_H_indp=0.01,
                             prb_etov_22_5_H_indp=0.01, prb_etov_36_5_H_indp=0.01, prb_etov_49_5_H_indp=0.01,
                             prb_gtov_146_5_H_indp=0.01, prb_gtov_166_5_H_indp=0.01,
                             prb_gtov_186_5_H_indp=0.01, prb_gtov_201_5_H_indp=0.01, prb_gtov_212_5_H_indp=0.01,
                             prb_gtov_226_5_H_indp=0.01, prb_12_H_indp=0.01)
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
                                     prb_etov_26_5_H_indp=ht_indp_values[2], prb_etov_33_5_H_indp=ht_indp_values[3],
                                     prb_etov_40_5_H_indp=ht_indp_values[4], prb_etov_46_5_H_indp=ht_indp_values[5],
                                     prb_etov_56_5_H_indp=ht_indp_values[6],
                                     prb_etov_22_5_H_indp=ht_indp_values[7], prb_etov_36_5_H_indp=ht_indp_values[8],
                                     prb_etov_49_5_H_indp=ht_indp_values[9], prb_gtov_146_5_H_indp=ht_indp_values[10],
                                     prb_gtov_166_5_H_indp=ht_indp_values[11],
                                     prb_gtov_186_5_H_indp=ht_indp_values[12], prb_gtov_201_5_H_indp=ht_indp_values[13],
                                     prb_gtov_212_5_H_indp=ht_indp_values[15], prb_gtov_226_5_H_indp=ht_indp_values[15],
                                     prb_12_H_indp=ht_indp_values[16])
                except ZeroDivisionError:
                    ht_indp_appender(prb_HW_H_indp=0.01, prb_AW_H_indp=0.01, prb_etov_26_5_H_indp=0.01,
                                     prb_etov_33_5_H_indp=0.01, prb_etov_40_5_H_indp=0.01, prb_etov_46_5_H_indp=0.01,
                                     prb_etov_56_5_H_indp=0.01,
                                     prb_etov_22_5_H_indp=0.01, prb_etov_36_5_H_indp=0.01, prb_etov_49_5_H_indp=0.01,
                                     prb_gtov_146_5_H_indp=0.01, prb_gtov_166_5_H_indp=0.01,
                                     prb_gtov_186_5_H_indp=0.01, prb_gtov_201_5_H_indp=0.01, prb_gtov_212_5_H_indp=0.01,
                                     prb_gtov_226_5_H_indp=0.01, prb_12_H_indp=0.01)
            else:
                ht_indp_appender(prb_HW_H_indp=0.01, prb_AW_H_indp=0.01, prb_etov_26_5_H_indp=0.01,
                                 prb_etov_33_5_H_indp=0.01, prb_etov_40_5_H_indp=0.01, prb_etov_46_5_H_indp=0.01,
                                 prb_etov_56_5_H_indp=0.01,
                                 prb_etov_22_5_H_indp=0.01, prb_etov_36_5_H_indp=0.01, prb_etov_49_5_H_indp=0.01,
                                 prb_gtov_146_5_H_indp=0.01, prb_gtov_166_5_H_indp=0.01,
                                 prb_gtov_186_5_H_indp=0.01, prb_gtov_201_5_H_indp=0.01, prb_gtov_212_5_H_indp=0.01,
                                 prb_gtov_226_5_H_indp=0.01, prb_12_H_indp=0.01)
    except ElementNotInteractableException:
        ht_indp_appender(prb_HW_H_indp=0.01, prb_AW_H_indp=0.01, prb_etov_26_5_H_indp=0.01, prb_etov_33_5_H_indp=0.01,
                         prb_etov_40_5_H_indp=0.01, prb_etov_46_5_H_indp=0.01, prb_etov_56_5_H_indp=0.01,
                         prb_etov_22_5_H_indp=0.01, prb_etov_36_5_H_indp=0.01, prb_etov_49_5_H_indp=0.01,
                         prb_gtov_146_5_H_indp=0.01, prb_gtov_166_5_H_indp=0.01,
                         prb_gtov_186_5_H_indp=0.01, prb_gtov_201_5_H_indp=0.01, prb_gtov_212_5_H_indp=0.01,
                         prb_gtov_226_5_H_indp=0.01, prb_12_H_indp=0.01)
    sleep(0.1)
    try:
        sub2 = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row')
        if len(sub2) == 0:
            at_indp_appender(prb_HW_A_indp=0.01, prb_AW_A_indp=0.01, prb_etov_26_5_A_indp=0.01,
                             prb_etov_33_5_A_indp=0.01,
                             prb_etov_40_5_A_indp=0.01, prb_etov_46_5_A_indp=0.01, prb_etov_56_5_A_indp=0.01,
                             prb_etov_22_5_A_indp=0.01, prb_etov_36_5_A_indp=0.01, prb_etov_49_5_A_indp=0.01,
                             prb_gtov_146_5_A_indp=0.01, prb_gtov_166_5_A_indp=0.01,
                             prb_gtov_186_5_A_indp=0.01, prb_gtov_201_5_A_indp=0.01, prb_gtov_212_5_A_indp=0.01,
                             prb_gtov_226_5_A_indp=0.01, prb_12_A_indp=0.01)
            at_g_avgs.append(0)
        else:
            dsc = 0
            at_scores = []
            for b in range(DSCRM_H_A):
                date__ = driver.find_elements(By.CSS_SELECTOR, '.section:nth-child(2) .h2h__row .h2h__date')
                home_x__ = driver.find_elements(By.CSS_SELECTOR,
                                                '.section:nth-child(2) .h2h__row .h2h__homeParticipant .h2h__participantInner')
                away_x__ = driver.find_elements(By.CSS_SELECTOR,
                                                '.section:nth-child(2) .h2h__row .h2h__awayParticipant .h2h__participantInner')
                home_score__ = driver.find_elements(By.CSS_SELECTOR,
                                                    '.section:nth-child(2) .h2h__row .h2h__result span:first-child')
                away_score__ = driver.find_elements(By.CSS_SELECTOR,
                                                    '.section:nth-child(2) .h2h__row .h2h__result span:last-child')
                try:
                    if YEAR <= int(date__[b].text.split('.')[-1].strip()) < 90:
                        at_indp_aggregator(n=b, home_score=home_score__, away_score=away_score__, home_x=home_x__,
                                           away_x=away_x__)
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
                                     prb_etov_26_5_A_indp=at_indp_values[2], prb_etov_33_5_A_indp=at_indp_values[3],
                                     prb_etov_40_5_A_indp=at_indp_values[4], prb_etov_46_5_A_indp=at_indp_values[5],
                                     prb_etov_56_5_A_indp=at_indp_values[6],
                                     prb_etov_22_5_A_indp=at_indp_values[7], prb_etov_36_5_A_indp=at_indp_values[8],
                                     prb_etov_49_5_A_indp=at_indp_values[9], prb_gtov_146_5_A_indp=at_indp_values[10],
                                     prb_gtov_166_5_A_indp=at_indp_values[11],
                                     prb_gtov_186_5_A_indp=at_indp_values[12], prb_gtov_201_5_A_indp=at_indp_values[13],
                                     prb_gtov_212_5_A_indp=at_indp_values[15], prb_gtov_226_5_A_indp=at_indp_values[15],
                                     prb_12_A_indp=at_indp_values[16])
                except ZeroDivisionError:
                    at_indp_appender(prb_HW_A_indp=0.01, prb_AW_A_indp=0.01, prb_etov_26_5_A_indp=0.01,
                                     prb_etov_33_5_A_indp=0.01,
                                     prb_etov_40_5_A_indp=0.01, prb_etov_46_5_A_indp=0.01, prb_etov_56_5_A_indp=0.01,
                                     prb_etov_22_5_A_indp=0.01, prb_etov_36_5_A_indp=0.01, prb_etov_49_5_A_indp=0.01,
                                     prb_gtov_146_5_A_indp=0.01, prb_gtov_166_5_A_indp=0.01,
                                     prb_gtov_186_5_A_indp=0.01, prb_gtov_201_5_A_indp=0.01, prb_gtov_212_5_A_indp=0.01,
                                     prb_gtov_226_5_A_indp=0.01, prb_12_A_indp=0.01)
            else:
                at_indp_appender(prb_HW_A_indp=0.01, prb_AW_A_indp=0.01, prb_etov_26_5_A_indp=0.01,
                                 prb_etov_33_5_A_indp=0.01,
                                 prb_etov_40_5_A_indp=0.01, prb_etov_46_5_A_indp=0.01, prb_etov_56_5_A_indp=0.01,
                                 prb_etov_22_5_A_indp=0.01, prb_etov_36_5_A_indp=0.01, prb_etov_49_5_A_indp=0.01,
                                 prb_gtov_146_5_A_indp=0.01, prb_gtov_166_5_A_indp=0.01,
                                 prb_gtov_186_5_A_indp=0.01, prb_gtov_201_5_A_indp=0.01, prb_gtov_212_5_A_indp=0.01,
                                 prb_gtov_226_5_A_indp=0.01, prb_12_A_indp=0.01)
    except ElementNotInteractableException:
        pass
        at_indp_appender(prb_HW_A_indp=0.01, prb_AW_A_indp=0.01, prb_etov_26_5_A_indp=0.01, prb_etov_33_5_A_indp=0.01,
                         prb_etov_40_5_A_indp=0.01, prb_etov_46_5_A_indp=0.01, prb_etov_56_5_A_indp=0.01,
                         prb_etov_22_5_A_indp=0.01, prb_etov_36_5_A_indp=0.01, prb_etov_49_5_A_indp=0.01,
                         prb_gtov_146_5_A_indp=0.01, prb_gtov_166_5_A_indp=0.01,
                         prb_gtov_186_5_A_indp=0.01, prb_gtov_201_5_A_indp=0.01, prb_gtov_212_5_A_indp=0.01,
                         prb_gtov_226_5_A_indp=0.01, prb_12_A_indp=0.01)
    sleep(0.1)
    try:
        sub3 = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row')
        if len(sub3) == 0:
            h2h_appender(prb_HW=0.01, prb_AW=0.01, prb_etov_26_5=0.01, prb_etov_33_5=0.01,
                         prb_etov_40_5=0.01, prb_etov_46_5=0.01, prb_etov_56_5=0.01,
                         prb_etov_22_5=0.01, prb_etov_36_5=0.01, prb_etov_49_5=0.01,
                         prb_gtov_146_5=0.01, prb_gtov_166_5=0.01,
                         prb_gtov_186_5=0.01, prb_gtov_201_5=0.01, prb_gtov_212_5=0.01,
                         prb_gtov_226_5=0.01, prb_12=0.01)
            bth_g_avgs.append(0)
            bta_g_avgs.append(0)
        else:
            dsc = 0
            bth_scores = []
            bta_scores = []
            for c in range(DSCRM_BT):
                date___ = driver.find_elements(By.CSS_SELECTOR, '.section:last-child .h2h__row .h2h__date')
                home_x___ = driver.find_elements(By.CSS_SELECTOR,
                                                 '.section:last-child .h2h__row .h2h__homeParticipant .h2h__participantInner')
                away_x___ = driver.find_elements(By.CSS_SELECTOR,
                                                 '.section:last-child .h2h__row .h2h__awayParticipant .h2h__participantInner')
                home_score___ = driver.find_elements(By.CSS_SELECTOR,
                                                     '.section:last-child .h2h__row .h2h__result span:first-child')
                away_score___ = driver.find_elements(By.CSS_SELECTOR,
                                                     '.section:last-child .h2h__row .h2h__result span:last-child')
                try:
                    if YEAR <= int(date___[c].text.split('.')[-1].strip()) < 90:
                        h2h_aggregator(m=c, home_score=home_score___, away_score=away_score___, home_x=home_x___,
                                       away_x=away_x___)
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
                    h2h_appender(prb_HW=h2h_values[0], prb_AW=h2h_values[1],
                                 prb_etov_26_5=h2h_values[2], prb_etov_33_5=h2h_values[3],
                                 prb_etov_40_5=h2h_values[4], prb_etov_46_5=h2h_values[5],
                                 prb_etov_56_5=h2h_values[6],
                                 prb_etov_22_5=h2h_values[7], prb_etov_36_5=h2h_values[8],
                                 prb_etov_49_5=h2h_values[9], prb_gtov_146_5=h2h_values[10],
                                 prb_gtov_166_5=h2h_values[11],
                                 prb_gtov_186_5=h2h_values[12], prb_gtov_201_5=h2h_values[13],
                                 prb_gtov_212_5=h2h_values[15], prb_gtov_226_5=h2h_values[15],
                                 prb_12=h2h_values[16])
                except ZeroDivisionError:
                    h2h_appender(prb_HW=0.01, prb_AW=0.01, prb_etov_26_5=0.01, prb_etov_33_5=0.01,
                                 prb_etov_40_5=0.01, prb_etov_46_5=0.01, prb_etov_56_5=0.01,
                                 prb_etov_22_5=0.01, prb_etov_36_5=0.01, prb_etov_49_5=0.01,
                                 prb_gtov_146_5=0.01, prb_gtov_166_5=0.01,
                                 prb_gtov_186_5=0.01, prb_gtov_201_5=0.01, prb_gtov_212_5=0.01,
                                 prb_gtov_226_5=0.01, prb_12=0.01)
            else:
                h2h_appender(prb_HW=0.01, prb_AW=0.01, prb_etov_26_5=0.01, prb_etov_33_5=0.01,
                             prb_etov_40_5=0.01, prb_etov_46_5=0.01, prb_etov_56_5=0.01,
                             prb_etov_22_5=0.01, prb_etov_36_5=0.01, prb_etov_49_5=0.01,
                             prb_gtov_146_5=0.01, prb_gtov_166_5=0.01,
                             prb_gtov_186_5=0.01, prb_gtov_201_5=0.01, prb_gtov_212_5=0.01,
                             prb_gtov_226_5=0.01, prb_12=0.01)
    except ElementNotInteractableException:
        h2h_appender(prb_HW=0.01, prb_AW=0.01, prb_etov_26_5=0.01, prb_etov_33_5=0.01,
                     prb_etov_40_5=0.01, prb_etov_46_5=0.01, prb_etov_56_5=0.01,
                     prb_etov_22_5=0.01, prb_etov_36_5=0.01, prb_etov_49_5=0.01,
                     prb_gtov_146_5=0.01, prb_gtov_166_5=0.01,
                     prb_gtov_186_5=0.01, prb_gtov_201_5=0.01, prb_gtov_212_5=0.01,
                     prb_gtov_226_5=0.01, prb_12=0.01)


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
    print(f"Prob etov_26_5s: {prob_etov_26_5s}")
    print(f"Prob etov_33_5s: {prob_etov_33_5s}")
    print(f"Prob etov_40_5s: {prob_etov_40_5s}")
    print(f"Prob etov_46_5s: {prob_etov_46_5s}")
    print(f"Prob etov_56_5s: {prob_etov_56_5s}")
    print(f"Prob etov_22_5s: {prob_etov_22_5s}")
    print(f"Prob etov_36_5s: {prob_etov_36_5s}")
    print(f"Prob etov_49_5s: {prob_etov_49_5s}")
    print(f"Prob gtov_146_5s: {prob_gtov_146_5s}")
    print(f"Prob gtov_166_5s: {prob_gtov_166_5s}")
    print(f"Prob gtov_186_5s: {prob_gtov_186_5s}")
    print(f"Prob gtov_201_5s: {prob_gtov_201_5s}")
    print(f"Prob gtov_212_5s: {prob_gtov_212_5s}")
    print(f"Prob gtov_226_5s: {prob_gtov_226_5s}")
    print(f"Prob 12s: {prob_12s}")
    print(f"Prob HWs: {prob_HWs}")
    print(f"Prob AWs: {prob_AWs}")
    print(f"Prob etov_26_5_H_indps: {prob_etov_26_5_H_indps}")
    print(f"Prob etov_33_5_H_indps: {prob_etov_33_5_H_indps}")
    print(f"Prob etov_40_5_H_indps: {prob_etov_40_5_H_indps}")
    print(f"Prob etov_46_5_H_indps: {prob_etov_46_5_H_indps}")
    print(f"Prob etov_56_5_H_indps: {prob_etov_56_5_H_indps}")
    print(f"Prob etov_22_5_H_indps: {prob_etov_22_5_H_indps}")
    print(f"Prob etov_36_5_H_indps: {prob_etov_36_5_H_indps}")
    print(f"Prob etov_49_5_H_indps: {prob_etov_49_5_H_indps}")
    print(f"Prob gtov_146_5_H_indps: {prob_gtov_146_5_H_indps}")
    print(f"Prob gtov_166_5_H_indps: {prob_gtov_166_5_H_indps}")
    print(f"Prob gtov_186_5_H_indps: {prob_gtov_186_5_H_indps}")
    print(f"Prob gtov_201_5_H_indps: {prob_gtov_201_5_H_indps}")
    print(f"Prob gtov_212_5_H_indps: {prob_gtov_212_5_H_indps}")
    print(f"Prob gtov_226_5_H_indps: {prob_gtov_226_5_H_indps}")
    print(f"Prob 12_H_indps: {prob_12_H_indps}")
    print(f"Prob HW_H_indps: {prob_HW_H_indps}")
    print(f"Prob AW_H_indps: {prob_AW_H_indps}")
    print(f"Prob etov_26_5_A_indps: {prob_etov_26_5_A_indps}")
    print(f"Prob etov_33_5_A_indps: {prob_etov_33_5_A_indps}")
    print(f"Prob etov_40_5_A_indps: {prob_etov_40_5_A_indps}")
    print(f"Prob etov_46_5_A_indps: {prob_etov_46_5_A_indps}")
    print(f"Prob etov_56_5_A_indps: {prob_etov_56_5_A_indps}")
    print(f"Prob etov_22_5_A_indps: {prob_etov_22_5_A_indps}")
    print(f"Prob etov_36_5_A_indps: {prob_etov_36_5_A_indps}")
    print(f"Prob etov_49_5_A_indps: {prob_etov_49_5_A_indps}")
    print(f"Prob gtov_146_5_A_indps: {prob_gtov_146_5_A_indps}")
    print(f"Prob gtov_166_5_A_indps: {prob_gtov_166_5_A_indps}")
    print(f"Prob gtov_186_5_A_indps: {prob_gtov_186_5_A_indps}")
    print(f"Prob gtov_201_5_A_indps: {prob_gtov_201_5_A_indps}")
    print(f"Prob gtov_212_5_A_indps: {prob_gtov_212_5_A_indps}")
    print(f"Prob gtov_226_5_A_indps: {prob_gtov_226_5_A_indps}")
    print(f"Prob 12_A_indps: {prob_12_A_indps}")
    print(f"Prob HW_A_indps: {prob_HW_A_indps}")
    print(f"Prob AW_A_indps: {prob_AW_A_indps}")
    print(f"Bayesian Home Win: {bayesian_home_Win_d}")
    print(f"Bayesian Away Win: {bayesian_away_Win_d}")
    print(f"Bayesian etov_26_5_d: {bayesian_etov_26_5_d}")
    print(f"Bayesian etov_33_5_d: {bayesian_etov_33_5_d}")
    print(f"Bayesian etov_40_5_d: {bayesian_etov_40_5_d}")
    print(f"Bayesian etov_46_5_d: {bayesian_etov_46_5_d}")
    print(f"Bayesian etov_56_5_d: {bayesian_etov_56_5_d}")
    print(f"Bayesian etov_22_5_d: {bayesian_etov_22_5_d}")
    print(f"Bayesian etov_36_5_d: {bayesian_etov_36_5_d}")
    print(f"Bayesian etov_49_5_d: {bayesian_etov_49_5_d}")
    print(f"Bayesian gtov_146_5_d: {bayesian_gtov_146_5_d}")
    print(f"Bayesian gtov_166_5_d: {bayesian_gtov_166_5_d}")
    print(f"Bayesian gtov_186_5_d: {bayesian_gtov_186_5_d}")
    print(f"Bayesian gtov_201_5_d: {bayesian_gtov_201_5_d}")
    print(f"Bayesian gtov_212_5_d: {bayesian_gtov_212_5_d}")
    print(f"Bayesian gtov_226_5_d: {bayesian_gtov_226_5_d}")
    print(f"Bayesian 12: {bayesian_12_d}")
    print(f"Odds _1HWS: {_1HWS}")
    print(f"Odds _2AWS: {_2AWS}")
    print(f"Odds OVER_etov_26_5_S: {OVER_etov_26_5_S}")
    print(f"Odds OVER_etov_33_5_S: {OVER_etov_33_5_S}")
    print(f"Odds OVER_etov_40_5_S: {OVER_etov_40_5_S}")
    print(f"Odds OVER_etov_46_5_S: {OVER_etov_46_5_S}")
    print(f"Odds OVER_etov_56_5_S: {OVER_etov_56_5_S}")
    print(f"Odds OVER_etov_22_5_S: {OVER_etov_22_5_S}")
    print(f"Odds OVER_etov_36_5_S: {OVER_etov_36_5_S}")
    print(f"Odds OVER_gtov_146_5_S: {OVER_gtov_146_5_S}")
    print(f"Odds OVER_gtov_166_5_S: {OVER_gtov_166_5_S}")
    print(f"Odds OVER_gtov_186_5_S: {OVER_gtov_186_5_S}")
    print(f"Odds OVER_gtov_201_5_S: {OVER_gtov_201_5_S}")
    print(f"Odds OVER_gtov_212_5_S: {OVER_gtov_212_5_S}")
    print(f"Odds OVER_gtov_226_5_S: {OVER_gtov_226_5_S}")
    print(f"Odds _12S: {_12S}")
    print(f"Countries: {len(countries)}, Leagues: {len(leagues)}, Home Teams: {len(home_teams)}, "
          f"Home Positions: {len(home_positions)}, Home Points: {len(home_points)}, "
          f"Home No Matches Played: {len(home_nums_matches_played)}, Away Teams: {len(away_teams)}, "
          f"Away Positions: {len(away_positions)}, Away Points: {len(away_points)}, "
          f"Away No Matches Played: {len(away_nums_matches_played)}, Match Times: {len(match_times)} "
          f"Home W Form: {len(h_form_W)}, Home D Form: {len(h_form_D)}, Home L Form: {len(h_form_L)}, "
          f"Away W Form: {len(a_form_W)}, Away D Form: {len(a_form_D)}, Away L Form: {len(a_form_L)}, "
          f"Prob 12s: {len(prob_12s)}, Prob HWs: {len(prob_HWs)}, Prob AWs: {len(prob_AWs)}, "
          f"Prob 12_H_indps: {len(prob_12_H_indps)},"
          f"Prob HW_H_indps: {len(prob_HW_H_indps)}, Prob AW_H_indps: {len(prob_AW_H_indps)}, "
          f"Prob 12_A_indps: {len(prob_12_A_indps)}, "
          f"Prob HW_A_indps: {len(prob_HW_A_indps)}, Prob AW_A_indps: {len(prob_AW_A_indps)}, "
          f"Odds _1HWS: {len(_1HWS)}, Odds _2AWS: {len(_2AWS)}, Odds _12S: {len(_12S)}, "
          f"Bayesian Home Win: {len(bayesian_home_Win_d)}, Bayesian Away Win: {len(bayesian_away_Win_d)}, "
          f"Bayesian 12: {len(bayesian_12_d)}")
    print(f"Odds OVER_etov_26_5_S: {len(OVER_etov_26_5_S)}")
    print(f"Odds OVER_etov_33_5_S: {len(OVER_etov_33_5_S)}")
    print(f"Odds OVER_etov_40_5_S: {len(OVER_etov_40_5_S)}")
    print(f"Odds OVER_etov_46_5_S: {len(OVER_etov_46_5_S)}")
    print(f"Odds OVER_etov_56_5_S: {len(OVER_etov_56_5_S)}")
    print(f"Odds OVER_etov_22_5_S: {len(OVER_etov_22_5_S)}")
    print(f"Odds OVER_etov_36_5_S: {len(OVER_etov_36_5_S)}")
    print(f"Odds OVER_gtov_146_5_S: {len(OVER_gtov_146_5_S)}")
    print(f"Odds OVER_gtov_166_5_S: {len(OVER_gtov_166_5_S)}")
    print(f"Odds OVER_gtov_186_5_S: {len(OVER_gtov_186_5_S)}")
    print(f"Odds OVER_gtov_201_5_S: {len(OVER_gtov_201_5_S)}")
    print(f"Odds OVER_gtov_212_5_S: {len(OVER_gtov_212_5_S)}")
    print(f"Odds OVER_gtov_226_5_S: {len(OVER_gtov_226_5_S)}")
    print(f"Bayesian etov_26_5_d: {len(bayesian_etov_26_5_d)}")
    print(f"Bayesian etov_33_5_d: {len(bayesian_etov_33_5_d)}")
    print(f"Bayesian etov_40_5_d: {len(bayesian_etov_40_5_d)}")
    print(f"Bayesian etov_46_5_d: {len(bayesian_etov_46_5_d)}")
    print(f"Bayesian etov_56_5_d: {len(bayesian_etov_56_5_d)}")
    print(f"Bayesian etov_22_5_d: {len(bayesian_etov_22_5_d)}")
    print(f"Bayesian etov_36_5_d: {len(bayesian_etov_36_5_d)}")
    print(f"Bayesian etov_49_5_d: {len(bayesian_etov_49_5_d)}")
    print(f"Bayesian gtov_146_5_d: {len(bayesian_gtov_146_5_d)}")
    print(f"Bayesian gtov_166_5_d: {len(bayesian_gtov_166_5_d)}")
    print(f"Bayesian gtov_186_5_d: {len(bayesian_gtov_186_5_d)}")
    print(f"Bayesian gtov_201_5_d: {len(bayesian_gtov_201_5_d)}")
    print(f"Bayesian gtov_212_5_d: {len(bayesian_gtov_212_5_d)}")
    print(f"Bayesian gtov_226_5_d: {len(bayesian_gtov_226_5_d)}")
    print(f"Prob etov_26_5_A_indps: {len(prob_etov_26_5_A_indps)}")
    print(f"Prob etov_33_5_A_indps: {len(prob_etov_33_5_A_indps)}")
    print(f"Prob etov_40_5_A_indps: {len(prob_etov_40_5_A_indps)}")
    print(f"Prob etov_46_5_A_indps: {len(prob_etov_46_5_A_indps)}")
    print(f"Prob etov_56_5_A_indps: {len(prob_etov_56_5_A_indps)}")
    print(f"Prob etov_22_5_A_indps: {len(prob_etov_22_5_A_indps)}")
    print(f"Prob etov_36_5_A_indps: {len(prob_etov_36_5_A_indps)}")
    print(f"Prob etov_49_5_A_indps: {len(prob_etov_49_5_A_indps)}")
    print(f"Prob gtov_146_5_A_indps: {len(prob_gtov_146_5_A_indps)}")
    print(f"Prob gtov_166_5_A_indps: {len(prob_gtov_166_5_A_indps)}")
    print(f"Prob gtov_186_5_A_indps: {len(prob_gtov_186_5_A_indps)}")
    print(f"Prob gtov_201_5_A_indps: {len(prob_gtov_201_5_A_indps)}")
    print(f"Prob gtov_212_5_A_indps: {len(prob_gtov_212_5_A_indps)}")
    print(f"Prob gtov_226_5_A_indps: {len(prob_gtov_226_5_A_indps)}")
    print(f"Prob etov_26_5_H_indps: {len(prob_etov_26_5_H_indps)}")
    print(f"Prob etov_33_5_H_indps: {len(prob_etov_33_5_H_indps)}")
    print(f"Prob etov_40_5_H_indps: {len(prob_etov_40_5_H_indps)}")
    print(f"Prob etov_46_5_H_indps: {len(prob_etov_46_5_H_indps)}")
    print(f"Prob etov_56_5_H_indps: {len(prob_etov_56_5_H_indps)}")
    print(f"Prob etov_22_5_H_indps: {len(prob_etov_22_5_H_indps)}")
    print(f"Prob etov_36_5_H_indps: {len(prob_etov_36_5_H_indps)}")
    print(f"Prob etov_49_5_H_indps: {len(prob_etov_49_5_H_indps)}")
    print(f"Prob gtov_146_5_H_indps: {len(prob_gtov_146_5_H_indps)}")
    print(f"Prob gtov_166_5_H_indps: {len(prob_gtov_166_5_H_indps)}")
    print(f"Prob gtov_186_5_H_indps: {len(prob_gtov_186_5_H_indps)}")
    print(f"Prob gtov_201_5_H_indps: {len(prob_gtov_201_5_H_indps)}")
    print(f"Prob gtov_212_5_H_indps: {len(prob_gtov_212_5_H_indps)}")
    print(f"Prob gtov_226_5_H_indps: {len(prob_gtov_226_5_H_indps)}")
    print(f"Prob etov_26_5s: {len(prob_etov_26_5s)}")
    print(f"Prob etov_33_5s: {len(prob_etov_33_5s)}")
    print(f"Prob etov_40_5s: {len(prob_etov_40_5s)}")
    print(f"Prob etov_46_5s: {len(prob_etov_46_5s)}")
    print(f"Prob etov_56_5s: {len(prob_etov_56_5s)}")
    print(f"Prob etov_22_5s: {len(prob_etov_22_5s)}")
    print(f"Prob etov_36_5s: {len(prob_etov_36_5s)}")
    print(f"Prob etov_49_5s: {len(prob_etov_49_5s)}")
    print(f"Prob gtov_146_5s: {len(prob_gtov_146_5s)}")
    print(f"Prob gtov_166_5s: {len(prob_gtov_166_5s)}")
    print(f"Prob gtov_186_5s: {len(prob_gtov_186_5s)}")
    print(f"Prob gtov_201_5s: {len(prob_gtov_201_5s)}")
    print(f"Prob gtov_212_5s: {len(prob_gtov_212_5s)}")
    print(f"Prob gtov_226_5s: {len(prob_gtov_226_5s)}")
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
prob_etov_26_5s = []
prob_etov_33_5s = []
prob_etov_40_5s = []
prob_etov_46_5s = []
prob_etov_56_5s = []
prob_etov_22_5s = []
prob_etov_36_5s = []
prob_etov_49_5s = []
prob_gtov_146_5s = []
prob_gtov_166_5s = []
prob_gtov_186_5s = []
prob_gtov_201_5s = []
prob_gtov_212_5s = []
prob_gtov_226_5s = []
prob_12s = []
prob_HWs = []
prob_AWs = []
prob_etov_26_5_H_indps = []
prob_etov_33_5_H_indps = []
prob_etov_40_5_H_indps = []
prob_etov_46_5_H_indps = []
prob_etov_56_5_H_indps = []
prob_etov_22_5_H_indps = []
prob_etov_36_5_H_indps = []
prob_etov_49_5_H_indps = []
prob_gtov_146_5_H_indps = []
prob_gtov_166_5_H_indps = []
prob_gtov_186_5_H_indps = []
prob_gtov_201_5_H_indps = []
prob_gtov_212_5_H_indps = []
prob_gtov_226_5_H_indps = []
prob_12_H_indps = []
prob_HW_H_indps = []
prob_AW_H_indps = []
prob_etov_26_5_A_indps = []
prob_etov_33_5_A_indps = []
prob_etov_40_5_A_indps = []
prob_etov_46_5_A_indps = []
prob_etov_56_5_A_indps = []
prob_etov_22_5_A_indps = []
prob_etov_36_5_A_indps = []
prob_etov_49_5_A_indps = []
prob_gtov_146_5_A_indps = []
prob_gtov_166_5_A_indps = []
prob_gtov_186_5_A_indps = []
prob_gtov_201_5_A_indps = []
prob_gtov_212_5_A_indps = []
prob_gtov_226_5_A_indps = []
prob_12_A_indps = []
prob_HW_A_indps = []
prob_AW_A_indps = []
home_z_prob = []
away_z_prob = []
diff_z_prob = []
_1HWS = []
_2AWS = []
OVER_etov_26_5_S = []
OVER_etov_33_5_S = []
OVER_etov_40_5_S = []
OVER_etov_46_5_S = []
OVER_etov_56_5_S = []
OVER_etov_22_5_S = []
OVER_etov_36_5_S = []
OVER_etov_49_5_S = []
OVER_gtov_146_5_S = []
OVER_gtov_166_5_S = []
OVER_gtov_186_5_S = []
OVER_gtov_201_5_S = []
OVER_gtov_212_5_S = []
OVER_gtov_226_5_S = []
_12S = []
BAYE_etov_26_5s = []
BAYE_etov_33_5s = []
BAYE_etov_40_5s = []
BAYE_etov_46_5s = []
BAYE_etov_56_5s = []
BAYE_etov_22_5s = []
BAYE_etov_36_5s = []
BAYE_etov_49_5s = []
BAYE_gtov_146_5s = []
BAYE_gtov_166_5s = []
BAYE_gtov_186_5s = []
BAYE_gtov_201_5s = []
BAYE_gtov_212_5s = []
BAYE_gtov_226_5s = []
BAYE_12s = []
BAYE_HWs = []
BAYE_AWs = []

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
    except (NoSuchElementException, IndexError):
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
                    divs = driver.find_elements(By.CSS_SELECTOR, '.soccer .event__match--scheduled')
                    try:
                        divs[i].click()
                        window_after = driver.window_handles[1]
                        driver.switch_to.window(window_after)
                        driver.find_element(By.LINK_TEXT, "STANDINGS").click()
                        sleep(0.2)
                        selected_teams_names = driver.find_elements(By.CSS_SELECTOR,
                                                                    ".table__row--selected  .tableCellParticipant__name")
                        pts_pos_mp()
                        current_ht_pts = home_points[i]
                        current_at_pts = away_points[i]
                        z_scorer(htpts=current_ht_pts, atpts=current_at_pts)
                    except IndexError:
                        traceback.print_exc()
                        driver.close()
                        driver.switch_to.window(window_before)
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
                            selected_teams_names = driver.find_elements(By.CSS_SELECTOR,
                                                                        ".table__row--selected  .tableCellParticipant__name")
                            pts_pos_mp()
                            current_ht_pts = home_points[i]
                            current_at_pts = away_points[i]
                            z_scorer(htpts=current_ht_pts, atpts=current_at_pts)
                        except IndexError:
                            traceback.print_exc()
                            driver.close()
                            driver.switch_to.window(window_before)
                            break
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
                                traceback.print_exc()
                                driver.close()
                                driver.switch_to.window(window_before)
                                break
        sleep(0.1)
        team_data()
        driver.find_element(By.LINK_TEXT, "H2H").click()
        sleep(0.1)
        valid_games = 0
        count_etov_26_5 = 0
        count_etov_33_5 = 0
        count_etov_40_5 = 0
        count_etov_46_5 = 0
        count_etov_56_5 = 0
        count_etov_22_5 = 0
        count_etov_36_5 = 0
        count_etov_49_5 = 0
        count_gtov_146_5 = 0
        count_gtov_166_5 = 0
        count_gtov_186_5 = 0
        count_gtov_201_5 = 0
        count_gtov_212_5 = 0
        count_gtov_226_5 = 0
        count_12 = 0
        count_HW = 0
        count_AW = 0
        valid_games_H_indp = 0
        count_etov_26_5_H_indp = 0
        count_etov_33_5_H_indp = 0
        count_etov_40_5_H_indp = 0
        count_etov_46_5_H_indp = 0
        count_etov_56_5_H_indp = 0
        count_etov_22_5_H_indp = 0
        count_etov_36_5_H_indp = 0
        count_etov_49_5_H_indp = 0
        count_gtov_146_5_H_indp = 0
        count_gtov_166_5_H_indp = 0
        count_gtov_186_5_H_indp = 0
        count_gtov_201_5_H_indp = 0
        count_gtov_212_5_H_indp = 0
        count_gtov_226_5_H_indp = 0
        count_12_H_indp = 0
        count_HW_H_indp = 0
        valid_games_A_indp = 0
        count_etov_26_5_A_indp = 0
        count_etov_33_5_A_indp = 0
        count_etov_40_5_A_indp = 0
        count_etov_46_5_A_indp = 0
        count_etov_56_5_A_indp = 0
        count_etov_22_5_A_indp = 0
        count_etov_36_5_A_indp = 0
        count_etov_49_5_A_indp = 0
        count_gtov_146_5_A_indp = 0
        count_gtov_166_5_A_indp = 0
        count_gtov_186_5_A_indp = 0
        count_gtov_201_5_A_indp = 0
        count_gtov_212_5_A_indp = 0
        count_gtov_226_5_A_indp = 0
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
        sleep(0.1)
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
            sleep(1)
            print(f"No Pts Pos or Form Data for {home_teamx} vs {away_teamx}")
            team_data()
            driver.find_element(By.LINK_TEXT, "H2H").click()
            sleep(0.1)
            valid_games = 0
            count_etov_26_5 = 0
            count_etov_33_5 = 0
            count_etov_40_5 = 0
            count_etov_46_5 = 0
            count_etov_56_5 = 0
            count_etov_22_5 = 0
            count_etov_36_5 = 0
            count_etov_49_5 = 0
            count_gtov_146_5 = 0
            count_gtov_166_5 = 0
            count_gtov_186_5 = 0
            count_gtov_201_5 = 0
            count_gtov_212_5 = 0
            count_gtov_226_5 = 0
            count_12 = 0
            count_HW = 0
            count_AW = 0
            valid_games_H_indp = 0
            count_etov_26_5_H_indp = 0
            count_etov_33_5_H_indp = 0
            count_etov_40_5_H_indp = 0
            count_etov_46_5_H_indp = 0
            count_etov_56_5_H_indp = 0
            count_etov_22_5_H_indp = 0
            count_etov_36_5_H_indp = 0
            count_etov_49_5_H_indp = 0
            count_gtov_146_5_H_indp = 0
            count_gtov_166_5_H_indp = 0
            count_gtov_186_5_H_indp = 0
            count_gtov_201_5_H_indp = 0
            count_gtov_212_5_H_indp = 0
            count_gtov_226_5_H_indp = 0
            count_12_H_indp = 0
            count_HW_H_indp = 0
            valid_games_A_indp = 0
            count_etov_26_5_A_indp = 0
            count_etov_33_5_A_indp = 0
            count_etov_40_5_A_indp = 0
            count_etov_46_5_A_indp = 0
            count_etov_56_5_A_indp = 0
            count_etov_22_5_A_indp = 0
            count_etov_36_5_A_indp = 0
            count_etov_49_5_A_indp = 0
            count_gtov_146_5_A_indp = 0
            count_gtov_166_5_A_indp = 0
            count_gtov_186_5_A_indp = 0
            count_gtov_201_5_A_indp = 0
            count_gtov_212_5_A_indp = 0
            count_gtov_226_5_A_indp = 0
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
            append_zeroes()
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
            bayesian_etov_26_5_d = []
            bayesian_etov_33_5_d = []
            bayesian_etov_40_5_d = []
            bayesian_etov_46_5_d = []
            bayesian_etov_56_5_d = []
            bayesian_etov_22_5_d = []
            bayesian_etov_36_5_d = []
            bayesian_etov_49_5_d = []
            bayesian_gtov_146_5_d = []
            bayesian_gtov_166_5_d = []
            bayesian_gtov_186_5_d = []
            bayesian_gtov_201_5_d = []
            bayesian_gtov_212_5_d = []
            bayesian_gtov_226_5_d = []
            bayesian_12_d = []

            for q in range(len(home_teams)):
                try:
                    if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = 0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_etov_26_5 = 0.5 * (rdm.random() + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                        bayesian_etov_33_5 = 0.5 * (rdm.random() + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                        bayesian_etov_40_5 = 0.5 * (rdm.random() + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                        bayesian_etov_46_5 = 0.5 * (rdm.random() + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                        bayesian_etov_56_5 = 0.5 * (rdm.random() + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                        bayesian_etov_22_5 = 0.5 * (rdm.random() + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                        bayesian_etov_36_5 = 0.5 * (rdm.random() + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                        bayesian_etov_49_5 = 0.5 * (rdm.random() + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                        bayesian_gtov_146_5 = 0.5 * (rdm.random() + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                        bayesian_gtov_166_5 = 0.5 * (rdm.random() + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                        bayesian_gtov_186_5 = 0.5 * (rdm.random() + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                        bayesian_gtov_201_5 = 0.5 * (rdm.random() + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                        bayesian_gtov_212_5 = 0.5 * (rdm.random() + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                        bayesian_gtov_226_5 = 0.5 * (rdm.random() + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                        bayesian_12 = 0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = 0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_etov_26_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                        bayesian_etov_33_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                        bayesian_etov_40_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                        bayesian_etov_46_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                        bayesian_etov_56_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                        bayesian_etov_22_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                        bayesian_etov_36_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                        bayesian_etov_49_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                        bayesian_gtov_146_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                        bayesian_gtov_166_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                        bayesian_gtov_186_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                        bayesian_gtov_201_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                        bayesian_gtov_212_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                        bayesian_gtov_226_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                        bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = 0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_etov_26_5 = 0.5 * (OVER_etov_26_5_S[q] + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                        bayesian_etov_33_5 = 0.5 * (OVER_etov_33_5_S[q] + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                        bayesian_etov_40_5 = 0.5 * (OVER_etov_40_5_S[q] + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                        bayesian_etov_46_5 = 0.5 * (OVER_etov_46_5_S[q] + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                        bayesian_etov_56_5 = 0.5 * (OVER_etov_56_5_S[q] + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                        bayesian_etov_22_5 = 0.5 * (OVER_etov_22_5_S[q] + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                        bayesian_etov_36_5 = 0.5 * (OVER_etov_36_5_S[q] + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                        bayesian_etov_49_5 = 0.5 * (OVER_etov_49_5_S[q] + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                        bayesian_gtov_146_5 = 0.5 * (OVER_gtov_146_5_S[q] + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                        bayesian_gtov_166_5 = 0.5 * (OVER_gtov_166_5_S[q] + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                        bayesian_gtov_186_5 = 0.5 * (OVER_gtov_186_5_S[q] + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                        bayesian_gtov_201_5 = 0.5 * (OVER_gtov_201_5_S[q] + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                        bayesian_gtov_212_5 = 0.5 * (OVER_gtov_212_5_S[q] + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                        bayesian_gtov_226_5 = 0.5 * (OVER_gtov_226_5_S[q] + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                        bayesian_12 = 0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (home_z_prob[q] + rdm.random())
                        bayesian_away_Win = 0.5 * (away_z_prob[q] + rdm.random())
                        bayesian_etov_26_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random())
                        bayesian_etov_33_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random())
                        bayesian_etov_40_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random())
                        bayesian_etov_46_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random())
                        bayesian_etov_56_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random())
                        bayesian_etov_22_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random())
                        bayesian_etov_36_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random())
                        bayesian_etov_49_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random())
                        bayesian_gtov_146_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random())
                        bayesian_gtov_166_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random())
                        bayesian_gtov_186_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random())
                        bayesian_gtov_201_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random())
                        bayesian_gtov_212_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random())
                        bayesian_gtov_226_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random())
                        bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random())
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (_1HWS[q] + rdm.random())
                        bayesian_away_Win = 0.5 * (_2AWS[q] + rdm.random())
                        bayesian_etov_26_5 = 0.5 * (OVER_etov_26_5_S[q] + rdm.random())
                        bayesian_etov_33_5 = 0.5 * (OVER_etov_33_5_S[q] + rdm.random())
                        bayesian_etov_40_5 = 0.5 * (OVER_etov_40_5_S[q] + rdm.random())
                        bayesian_etov_46_5 = 0.5 * (OVER_etov_46_5_S[q] + rdm.random())
                        bayesian_etov_56_5 = 0.5 * (OVER_etov_56_5_S[q] + rdm.random())
                        bayesian_etov_22_5 = 0.5 * (OVER_etov_22_5_S[q] + rdm.random())
                        bayesian_etov_36_5 = 0.5 * (OVER_etov_36_5_S[q] + rdm.random())
                        bayesian_etov_49_5 = 0.5 * (OVER_etov_49_5_S[q] + rdm.random())
                        bayesian_gtov_146_5 = 0.5 * (OVER_gtov_146_5_S[q] + rdm.random())
                        bayesian_gtov_166_5 = 0.5 * (OVER_gtov_166_5_S[q] + rdm.random())
                        bayesian_gtov_186_5 = 0.5 * (OVER_gtov_186_5_S[q] + rdm.random())
                        bayesian_gtov_201_5 = 0.5 * (OVER_gtov_201_5_S[q] + rdm.random())
                        bayesian_gtov_212_5 = 0.5 * (OVER_gtov_212_5_S[q] + rdm.random())
                        bayesian_gtov_226_5 = 0.5 * (OVER_gtov_226_5_S[q] + rdm.random())
                        bayesian_12 = 0.5 * (_12S[q] + rdm.random())
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                        bayesian_home_Win = 0.5 * (home_z_prob[q] + _1HWS[q])
                        bayesian_away_Win = 0.5 * (away_z_prob[q] + _2AWS[q])
                        bayesian_etov_26_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + OVER_etov_26_5_S[q])
                        bayesian_etov_33_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + OVER_etov_33_5_S[q])
                        bayesian_etov_40_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + OVER_etov_40_5_S[q])
                        bayesian_etov_46_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + OVER_etov_46_5_S[q])
                        bayesian_etov_56_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + OVER_etov_56_5_S[q])
                        bayesian_etov_22_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + OVER_etov_22_5_S[q])
                        bayesian_etov_36_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + OVER_etov_36_5_S[q])
                        bayesian_etov_49_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + OVER_etov_49_5_S[q])
                        bayesian_gtov_146_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + OVER_gtov_146_5_S[q])
                        bayesian_gtov_166_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + OVER_gtov_166_5_S[q])
                        bayesian_gtov_186_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + OVER_gtov_186_5_S[q])
                        bayesian_gtov_201_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + OVER_gtov_201_5_S[q])
                        bayesian_gtov_212_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + OVER_gtov_212_5_S[q])
                        bayesian_gtov_226_5 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + OVER_gtov_226_5_S[q])
                        bayesian_12 = 0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q])
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[1]:
                        bayesian_home_Win = rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                        bayesian_away_Win = rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                        bayesian_etov_26_5 = rdm.random() * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))
                        bayesian_etov_33_5 = rdm.random() * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))
                        bayesian_etov_40_5 = rdm.random() * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))
                        bayesian_etov_46_5 = rdm.random() * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))
                        bayesian_etov_56_5 = rdm.random() * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))
                        bayesian_etov_22_5 = rdm.random() * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))
                        bayesian_etov_36_5 = rdm.random() * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))
                        bayesian_etov_49_5 = rdm.random() * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))
                        bayesian_gtov_146_5 = rdm.random() * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))
                        bayesian_gtov_166_5 = rdm.random() * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))
                        bayesian_gtov_186_5 = rdm.random() * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))
                        bayesian_gtov_201_5 = rdm.random() * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))
                        bayesian_gtov_212_5 = rdm.random() * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))
                        bayesian_gtov_226_5 = rdm.random() * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))
                        bayesian_12 = rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                        bayesian_home_Win = home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                        bayesian_away_Win = away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                        bayesian_etov_26_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))
                        bayesian_etov_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))
                        bayesian_etov_40_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))
                        bayesian_etov_46_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))
                        bayesian_etov_56_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))
                        bayesian_etov_22_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))
                        bayesian_etov_36_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))
                        bayesian_etov_49_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))
                        bayesian_gtov_146_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))
                        bayesian_gtov_166_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))
                        bayesian_gtov_186_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))
                        bayesian_gtov_201_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))
                        bayesian_gtov_212_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))
                        bayesian_gtov_226_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))
                        bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                        bayesian_home_Win = _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                        bayesian_away_Win = _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                        bayesian_etov_26_5 = OVER_etov_26_5_S[q] * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))
                        bayesian_etov_33_5 = OVER_etov_33_5_S[q] * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))
                        bayesian_etov_40_5 = OVER_etov_40_5_S[q] * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))
                        bayesian_etov_46_5 = OVER_etov_46_5_S[q] * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))
                        bayesian_etov_56_5 = OVER_etov_56_5_S[q] * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))
                        bayesian_etov_22_5 = OVER_etov_22_5_S[q] * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))
                        bayesian_etov_36_5 = OVER_etov_36_5_S[q] * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))
                        bayesian_etov_49_5 = OVER_etov_49_5_S[q] * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))
                        bayesian_gtov_146_5 = OVER_gtov_146_5_S[q] * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))
                        bayesian_gtov_166_5 = OVER_gtov_166_5_S[q] * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))
                        bayesian_gtov_186_5 = OVER_gtov_186_5_S[q] * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))
                        bayesian_gtov_201_5 = OVER_gtov_201_5_S[q] * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))
                        bayesian_gtov_212_5 = OVER_gtov_212_5_S[q] * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))
                        bayesian_gtov_226_5 = OVER_gtov_226_5_S[q] * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))
                        bayesian_12 = _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                        bayesian_home_Win = home_z_prob[q] * rdm.random()
                        bayesian_away_Win = away_z_prob[q] * rdm.random()
                        bayesian_etov_26_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * rdm.random()
                        bayesian_etov_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * rdm.random()
                        bayesian_etov_40_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * rdm.random()
                        bayesian_etov_46_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * rdm.random()
                        bayesian_etov_56_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * rdm.random()
                        bayesian_etov_22_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * rdm.random()
                        bayesian_etov_36_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * rdm.random()
                        bayesian_etov_49_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * rdm.random()
                        bayesian_gtov_146_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * rdm.random()
                        bayesian_gtov_166_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * rdm.random()
                        bayesian_gtov_186_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * rdm.random()
                        bayesian_gtov_201_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * rdm.random()
                        bayesian_gtov_212_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * rdm.random()
                        bayesian_gtov_226_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * rdm.random()
                        bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random()
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                        bayesian_home_Win = _1HWS[q] * rdm.random()
                        bayesian_away_Win = _2AWS[q] * rdm.random()
                        bayesian_etov_26_5 = OVER_etov_26_5_S[q] * rdm.random()
                        bayesian_etov_33_5 = OVER_etov_33_5_S[q] * rdm.random()
                        bayesian_etov_40_5 = OVER_etov_40_5_S[q] * rdm.random()
                        bayesian_etov_46_5 = OVER_etov_46_5_S[q] * rdm.random()
                        bayesian_etov_56_5 = OVER_etov_56_5_S[q] * rdm.random()
                        bayesian_etov_22_5 = OVER_etov_22_5_S[q] * rdm.random()
                        bayesian_etov_36_5 = OVER_etov_36_5_S[q] * rdm.random()
                        bayesian_etov_49_5 = OVER_etov_49_5_S[q] * rdm.random()
                        bayesian_gtov_146_5 = OVER_gtov_146_5_S[q] * rdm.random()
                        bayesian_gtov_166_5 = OVER_gtov_166_5_S[q] * rdm.random()
                        bayesian_gtov_186_5 = OVER_gtov_186_5_S[q] * rdm.random()
                        bayesian_gtov_201_5 = OVER_gtov_201_5_S[q] * rdm.random()
                        bayesian_gtov_212_5 = OVER_gtov_212_5_S[q] * rdm.random()
                        bayesian_gtov_226_5 = OVER_gtov_226_5_S[q] * rdm.random()
                        bayesian_12 = _12S[q] * rdm.random()
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                        bayesian_home_Win = home_z_prob[q] * _1HWS[q]
                        bayesian_away_Win = away_z_prob[q] * _2AWS[q]
                        bayesian_etov_26_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * OVER_etov_26_5_S[q]
                        bayesian_etov_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * OVER_etov_33_5_S[q]
                        bayesian_etov_40_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * OVER_etov_40_5_S[q]
                        bayesian_etov_46_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * OVER_etov_46_5_S[q]
                        bayesian_etov_56_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * OVER_etov_56_5_S[q]
                        bayesian_etov_22_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * OVER_etov_22_5_S[q]
                        bayesian_etov_36_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * OVER_etov_36_5_S[q]
                        bayesian_etov_49_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * OVER_etov_49_5_S[q]
                        bayesian_gtov_146_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * OVER_gtov_146_5_S[q]
                        bayesian_gtov_166_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * OVER_gtov_166_5_S[q]
                        bayesian_gtov_186_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * OVER_gtov_186_5_S[q]
                        bayesian_gtov_201_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * OVER_gtov_201_5_S[q]
                        bayesian_gtov_212_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * OVER_gtov_212_5_S[q]
                        bayesian_gtov_226_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * OVER_gtov_226_5_S[q]
                        bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q]
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                        bayesian_away_Win = math.sqrt(0.5 * (rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                        bayesian_etov_26_5 = math.sqrt(0.5 * (rdm.random() + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))))
                        bayesian_etov_33_5 = math.sqrt(0.5 * (rdm.random() + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))))
                        bayesian_etov_40_5 = math.sqrt(0.5 * (rdm.random() + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))))
                        bayesian_etov_46_5 = math.sqrt(0.5 * (rdm.random() + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))))
                        bayesian_etov_56_5 = math.sqrt(0.5 * (rdm.random() + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))))
                        bayesian_etov_22_5 = math.sqrt(0.5 * (rdm.random() + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))))
                        bayesian_etov_36_5 = math.sqrt(0.5 * (rdm.random() + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))))
                        bayesian_etov_49_5 = math.sqrt(0.5 * (rdm.random() + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))))
                        bayesian_gtov_146_5 = math.sqrt(0.5 * (rdm.random() + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))))
                        bayesian_gtov_166_5 = math.sqrt(0.5 * (rdm.random() + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))))
                        bayesian_gtov_186_5 = math.sqrt(0.5 * (rdm.random() + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))))
                        bayesian_gtov_201_5 = math.sqrt(0.5 * (rdm.random() + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))))
                        bayesian_gtov_212_5 = math.sqrt(0.5 * (rdm.random() + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))))
                        bayesian_gtov_226_5 = math.sqrt(0.5 * (rdm.random() + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))))
                        bayesian_12 = math.sqrt(0.5 * (rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                        bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                        bayesian_etov_26_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))))
                        bayesian_etov_33_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))))
                        bayesian_etov_40_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))))
                        bayesian_etov_46_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))))
                        bayesian_etov_56_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))))
                        bayesian_etov_22_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))))
                        bayesian_etov_36_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))))
                        bayesian_etov_49_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))))
                        bayesian_gtov_146_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))))
                        bayesian_gtov_166_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))))
                        bayesian_gtov_186_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))))
                        bayesian_gtov_201_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))))
                        bayesian_gtov_212_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))))
                        bayesian_gtov_226_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))))
                        bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                        bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                        bayesian_etov_26_5 = math.sqrt(0.5 * (OVER_etov_26_5_S[q] + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))))
                        bayesian_etov_33_5 = math.sqrt(0.5 * (OVER_etov_33_5_S[q] + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))))
                        bayesian_etov_40_5 = math.sqrt(0.5 * (OVER_etov_40_5_S[q] + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))))
                        bayesian_etov_46_5 = math.sqrt(0.5 * (OVER_etov_46_5_S[q] + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))))
                        bayesian_etov_56_5 = math.sqrt(0.5 * (OVER_etov_56_5_S[q] + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))))
                        bayesian_etov_22_5 = math.sqrt(0.5 * (OVER_etov_22_5_S[q] + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))))
                        bayesian_etov_36_5 = math.sqrt(0.5 * (OVER_etov_36_5_S[q] + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))))
                        bayesian_etov_49_5 = math.sqrt(0.5 * (OVER_etov_49_5_S[q] + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))))
                        bayesian_gtov_146_5 = math.sqrt(0.5 * (OVER_gtov_146_5_S[q] + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))))
                        bayesian_gtov_166_5 = math.sqrt(0.5 * (OVER_gtov_166_5_S[q] + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))))
                        bayesian_gtov_186_5 = math.sqrt(0.5 * (OVER_gtov_186_5_S[q] + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))))
                        bayesian_gtov_201_5 = math.sqrt(0.5 * (OVER_gtov_201_5_S[q] + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))))
                        bayesian_gtov_212_5 = math.sqrt(0.5 * (OVER_gtov_212_5_S[q] + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))))
                        bayesian_gtov_226_5 = math.sqrt(0.5 * (OVER_gtov_226_5_S[q] + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))))
                        bayesian_12 = math.sqrt(0.5 * (_12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + rdm.random()))
                        bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + rdm.random()))
                        bayesian_etov_26_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random()))
                        bayesian_etov_33_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random()))
                        bayesian_etov_40_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random()))
                        bayesian_etov_46_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random()))
                        bayesian_etov_56_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random()))
                        bayesian_etov_22_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random()))
                        bayesian_etov_36_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random()))
                        bayesian_etov_49_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random()))
                        bayesian_gtov_146_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random()))
                        bayesian_gtov_166_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random()))
                        bayesian_gtov_186_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random()))
                        bayesian_gtov_201_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random()))
                        bayesian_gtov_212_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random()))
                        bayesian_gtov_226_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random()))
                        bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random()))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (_1HWS[q] + rdm.random()))
                        bayesian_away_Win = math.sqrt(0.5 * (_2AWS[q] + rdm.random()))
                        bayesian_etov_26_5 = math.sqrt(0.5 * (OVER_etov_26_5_S[q] + rdm.random()))
                        bayesian_etov_33_5 = math.sqrt(0.5 * (OVER_etov_33_5_S[q] + rdm.random()))
                        bayesian_etov_40_5 = math.sqrt(0.5 * (OVER_etov_40_5_S[q] + rdm.random()))
                        bayesian_etov_46_5 = math.sqrt(0.5 * (OVER_etov_46_5_S[q] + rdm.random()))
                        bayesian_etov_56_5 = math.sqrt(0.5 * (OVER_etov_56_5_S[q] + rdm.random()))
                        bayesian_etov_22_5 = math.sqrt(0.5 * (OVER_etov_22_5_S[q] + rdm.random()))
                        bayesian_etov_36_5 = math.sqrt(0.5 * (OVER_etov_36_5_S[q] + rdm.random()))
                        bayesian_etov_49_5 = math.sqrt(0.5 * (OVER_etov_49_5_S[q] + rdm.random()))
                        bayesian_gtov_146_5 = math.sqrt(0.5 * (OVER_gtov_146_5_S[q] + rdm.random()))
                        bayesian_gtov_166_5 = math.sqrt(0.5 * (OVER_gtov_166_5_S[q] + rdm.random()))
                        bayesian_gtov_186_5 = math.sqrt(0.5 * (OVER_gtov_186_5_S[q] + rdm.random()))
                        bayesian_gtov_201_5 = math.sqrt(0.5 * (OVER_gtov_201_5_S[q] + rdm.random()))
                        bayesian_gtov_212_5 = math.sqrt(0.5 * (OVER_gtov_212_5_S[q] + rdm.random()))
                        bayesian_gtov_226_5 = math.sqrt(0.5 * (OVER_gtov_226_5_S[q] + rdm.random()))
                        bayesian_12 = math.sqrt(0.5 * (_12S[q] + rdm.random()))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[2]:
                        bayesian_home_Win = math.sqrt(0.5 * (home_z_prob[q] + _1HWS[q]))
                        bayesian_away_Win = math.sqrt(0.5 * (away_z_prob[q] + _2AWS[q]))
                        bayesian_etov_26_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + OVER_etov_26_5_S[q]))
                        bayesian_etov_33_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + OVER_etov_33_5_S[q]))
                        bayesian_etov_40_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + OVER_etov_40_5_S[q]))
                        bayesian_etov_46_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + OVER_etov_46_5_S[q]))
                        bayesian_etov_56_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + OVER_etov_56_5_S[q]))
                        bayesian_etov_22_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + OVER_etov_22_5_S[q]))
                        bayesian_etov_36_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + OVER_etov_36_5_S[q]))
                        bayesian_etov_49_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + OVER_etov_49_5_S[q]))
                        bayesian_gtov_146_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + OVER_gtov_146_5_S[q]))
                        bayesian_gtov_166_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + OVER_gtov_166_5_S[q]))
                        bayesian_gtov_186_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + OVER_gtov_186_5_S[q]))
                        bayesian_gtov_201_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + OVER_gtov_201_5_S[q]))
                        bayesian_gtov_212_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + OVER_gtov_212_5_S[q]))
                        bayesian_gtov_226_5 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + OVER_gtov_226_5_S[q]))
                        bayesian_12 = math.sqrt(0.5 * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q]))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[1] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = math.sqrt(rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_etov_26_5 = math.sqrt(rdm.random() * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                        bayesian_etov_33_5 = math.sqrt(rdm.random() * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                        bayesian_etov_40_5 = math.sqrt(rdm.random() * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                        bayesian_etov_46_5 = math.sqrt(rdm.random() * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                        bayesian_etov_56_5 = math.sqrt(rdm.random() * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                        bayesian_etov_22_5 = math.sqrt(rdm.random() * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                        bayesian_etov_36_5 = math.sqrt(rdm.random() * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                        bayesian_etov_49_5 = math.sqrt(rdm.random() * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                        bayesian_gtov_146_5 = math.sqrt(rdm.random() * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                        bayesian_gtov_166_5 = math.sqrt(rdm.random() * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                        bayesian_gtov_186_5 = math.sqrt(rdm.random() * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                        bayesian_gtov_201_5 = math.sqrt(rdm.random() * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                        bayesian_gtov_212_5 = math.sqrt(rdm.random() * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                        bayesian_gtov_226_5 = math.sqrt(rdm.random() * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                        bayesian_12 = math.sqrt(rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(home_z_prob[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = math.sqrt(away_z_prob[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_etov_26_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                        bayesian_etov_33_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                        bayesian_etov_40_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                        bayesian_etov_46_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                        bayesian_etov_56_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                        bayesian_etov_22_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                        bayesian_etov_36_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                        bayesian_etov_49_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                        bayesian_gtov_146_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                        bayesian_gtov_166_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                        bayesian_gtov_186_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                        bayesian_gtov_201_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                        bayesian_gtov_212_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                        bayesian_gtov_226_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                        bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[0] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(_1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                        bayesian_away_Win = math.sqrt(_2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                        bayesian_etov_26_5 = math.sqrt(OVER_etov_26_5_S[q] * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                        bayesian_etov_33_5 = math.sqrt(OVER_etov_33_5_S[q] * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                        bayesian_etov_40_5 = math.sqrt(OVER_etov_40_5_S[q] * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                        bayesian_etov_46_5 = math.sqrt(OVER_etov_46_5_S[q] * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                        bayesian_etov_56_5 = math.sqrt(OVER_etov_56_5_S[q] * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                        bayesian_etov_22_5 = math.sqrt(OVER_etov_22_5_S[q] * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                        bayesian_etov_36_5 = math.sqrt(OVER_etov_36_5_S[q] * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                        bayesian_etov_49_5 = math.sqrt(OVER_etov_49_5_S[q] * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                        bayesian_gtov_146_5 = math.sqrt(OVER_gtov_146_5_S[q] * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                        bayesian_gtov_166_5 = math.sqrt(OVER_gtov_166_5_S[q] * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                        bayesian_gtov_186_5 = math.sqrt(OVER_gtov_186_5_S[q] * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                        bayesian_gtov_201_5 = math.sqrt(OVER_gtov_201_5_S[q] * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                        bayesian_gtov_212_5 = math.sqrt(OVER_gtov_212_5_S[q] * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                        bayesian_gtov_226_5 = math.sqrt(OVER_gtov_226_5_S[q] * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                        bayesian_12 = math.sqrt(_12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(home_z_prob[q] * rdm.random())
                        bayesian_away_Win = math.sqrt(away_z_prob[q] * rdm.random())
                        bayesian_etov_26_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * rdm.random())
                        bayesian_etov_33_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * rdm.random())
                        bayesian_etov_40_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * rdm.random())
                        bayesian_etov_46_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * rdm.random())
                        bayesian_etov_56_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * rdm.random())
                        bayesian_etov_22_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * rdm.random())
                        bayesian_etov_36_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * rdm.random())
                        bayesian_etov_49_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * rdm.random())
                        bayesian_gtov_146_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * rdm.random())
                        bayesian_gtov_166_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * rdm.random())
                        bayesian_gtov_186_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * rdm.random())
                        bayesian_gtov_201_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * rdm.random())
                        bayesian_gtov_212_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * rdm.random())
                        bayesian_gtov_226_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * rdm.random())
                        bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random())
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(_1HWS[q] * rdm.random())
                        bayesian_away_Win = math.sqrt(_2AWS[q] * rdm.random())
                        bayesian_etov_26_5 = math.sqrt(OVER_etov_26_5_S[q] * rdm.random())
                        bayesian_etov_33_5 = math.sqrt(OVER_etov_33_5_S[q] * rdm.random())
                        bayesian_etov_40_5 = math.sqrt(OVER_etov_40_5_S[q] * rdm.random())
                        bayesian_etov_46_5 = math.sqrt(OVER_etov_46_5_S[q] * rdm.random())
                        bayesian_etov_56_5 = math.sqrt(OVER_etov_56_5_S[q] * rdm.random())
                        bayesian_etov_22_5 = math.sqrt(OVER_etov_22_5_S[q] * rdm.random())
                        bayesian_etov_36_5 = math.sqrt(OVER_etov_36_5_S[q] * rdm.random())
                        bayesian_etov_49_5 = math.sqrt(OVER_etov_49_5_S[q] * rdm.random())
                        bayesian_gtov_146_5 = math.sqrt(OVER_gtov_146_5_S[q] * rdm.random())
                        bayesian_gtov_166_5 = math.sqrt(OVER_gtov_166_5_S[q] * rdm.random())
                        bayesian_gtov_186_5 = math.sqrt(OVER_gtov_186_5_S[q] * rdm.random())
                        bayesian_gtov_201_5 = math.sqrt(OVER_gtov_201_5_S[q] * rdm.random())
                        bayesian_gtov_212_5 = math.sqrt(OVER_gtov_212_5_S[q] * rdm.random())
                        bayesian_gtov_226_5 = math.sqrt(OVER_gtov_226_5_S[q] * rdm.random())
                        bayesian_12 = math.sqrt(_12S[q] * rdm.random())
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                    if X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[3]:
                        bayesian_home_Win = math.sqrt(home_z_prob[q] * _1HWS[q])
                        bayesian_away_Win = math.sqrt(away_z_prob[q] * _2AWS[q])
                        bayesian_etov_26_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * OVER_etov_26_5_S[q])
                        bayesian_etov_33_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * OVER_etov_33_5_S[q])
                        bayesian_etov_40_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * OVER_etov_40_5_S[q])
                        bayesian_etov_46_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * OVER_etov_46_5_S[q])
                        bayesian_etov_56_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * OVER_etov_56_5_S[q])
                        bayesian_etov_22_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * OVER_etov_22_5_S[q])
                        bayesian_etov_36_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * OVER_etov_36_5_S[q])
                        bayesian_etov_49_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * OVER_etov_49_5_S[q])
                        bayesian_gtov_146_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * OVER_gtov_146_5_S[q])
                        bayesian_gtov_166_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * OVER_gtov_166_5_S[q])
                        bayesian_gtov_186_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * OVER_gtov_186_5_S[q])
                        bayesian_gtov_201_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * OVER_gtov_201_5_S[q])
                        bayesian_gtov_212_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * OVER_gtov_212_5_S[q])
                        bayesian_gtov_226_5 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * OVER_gtov_226_5_S[q])
                        bayesian_12 = math.sqrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q])
                        baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                      baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                      baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                      baye_etov_56_5=bayesian_etov_56_5,
                                      baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                      baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                      baye_gtov_166_5=bayesian_gtov_166_5,
                                      baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                      baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                      baye_12=bayesian_12)

                except IndexError:
                    continue

            for q in range(len(bayesian_home_Win_d)):
                if q == 0:
                    for i in range(11):
                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                            file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                       f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                       f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                       f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                       f"BAYESIAN {OUTCOMES[9]}|BAYESIAN {OUTCOMES[10]}|BAYESIAN {OUTCOMES[11]}|BAYESIAN {OUTCOMES[12]}|"
                                       f"BAYESIAN {OUTCOMES[13]}|BAYESIAN {OUTCOMES[14]}|BAYESIAN {OUTCOMES[15]}|BAYESIAN {OUTCOMES[16]}|"
                                       f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                            # if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or bayesian_gtov_226_5_d[q] > CONFINTVL:
                try:
                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:

                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_D[q] == 0 and a_form_D[q] == 0:
                                if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                            if h_form_D[q] == 0 or a_form_D[q] == 0:
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                    if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer(w=q, A=X, B=Y, C=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)

                    if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                            bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                            bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                            bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                            bayesian_gtov_226_5_d[q] > CONFINTVL:
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS[1] or Y == PROB_METRICS[1]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
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
        bayesian_etov_26_5_d = []
        bayesian_etov_33_5_d = []
        bayesian_etov_40_5_d = []
        bayesian_etov_46_5_d = []
        bayesian_etov_56_5_d = []
        bayesian_etov_22_5_d = []
        bayesian_etov_36_5_d = []
        bayesian_etov_49_5_d = []
        bayesian_gtov_146_5_d = []
        bayesian_gtov_166_5_d = []
        bayesian_gtov_186_5_d = []
        bayesian_gtov_201_5_d = []
        bayesian_gtov_212_5_d = []
        bayesian_gtov_226_5_d = []
        bayesian_12_d = []

        for q in range(len(home_teams)):
            try:
                if X == PROB_METRICS[0]:
                    bayesian_home_Win = (prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))
                    bayesian_away_Win = (prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))
                    bayesian_etov_26_5 = (prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))
                    bayesian_etov_33_5 = (prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))
                    bayesian_etov_40_5 = (prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))
                    bayesian_etov_46_5 = (prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))
                    bayesian_etov_56_5 = (prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))
                    bayesian_etov_22_5 = (prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))
                    bayesian_etov_36_5 = (prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))
                    bayesian_etov_49_5 = (prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))
                    bayesian_gtov_146_5 = (prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))
                    bayesian_gtov_166_5 = (prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))
                    bayesian_gtov_186_5 = (prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))
                    bayesian_gtov_201_5 = (prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))
                    bayesian_gtov_212_5 = (prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))
                    bayesian_gtov_226_5 = (prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))
                    bayesian_12 = (prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS[1]:
                    prob_matches_home_W_against_EO = rdm.random()
                    prob_matches_W_indp_home1 = rdm.random()
                    prob_matches_W_indp_away1 = rdm.random()
                    bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((prob_matches_home_W_against_EO * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - prob_matches_home_W_against_EO)))
                    prob_matches_away_W_against_EO = rdm.random()
                    prob_matches_W_indp_home2 = rdm.random()
                    prob_matches_W_indp_away2 = rdm.random()
                    bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((prob_matches_away_W_against_EO * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - prob_matches_away_W_against_EO)))
                    prob_etov_26_5 = rdm.random()
                    prob_etov_26_5_indp_home = rdm.random()
                    prob_etov_26_5_indp_away = rdm.random()
                    bayesian_etov_26_5 = (prob_etov_26_5 * (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) / ((prob_etov_26_5 * (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) + ((1 - (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) * (1 - prob_etov_26_5)))
                    prob_etov_33_5 = rdm.random()
                    prob_etov_33_5_indp_home = rdm.random()
                    prob_etov_33_5_indp_away = rdm.random()
                    bayesian_etov_33_5 = (prob_etov_33_5 * (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) / ((prob_etov_33_5 * (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) + ((1 - (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) * (1 - prob_etov_33_5)))
                    prob_etov_40_5 = rdm.random()
                    prob_etov_40_5_indp_home = rdm.random()
                    prob_etov_40_5_indp_away = rdm.random()
                    bayesian_etov_40_5 = (prob_etov_40_5 * (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) / ((prob_etov_40_5 * (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) + ((1 - (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) * (1 - prob_etov_40_5)))
                    prob_etov_46_5 = rdm.random()
                    prob_etov_46_5_indp_home = rdm.random()
                    prob_etov_46_5_indp_away = rdm.random()
                    bayesian_etov_46_5 = (prob_etov_46_5 * (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) / ((prob_etov_46_5 * (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) + ((1 - (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) * (1 - prob_etov_46_5)))
                    prob_etov_56_5 = rdm.random()
                    prob_etov_56_5_indp_home = rdm.random()
                    prob_etov_56_5_indp_away = rdm.random()
                    bayesian_etov_56_5 = (prob_etov_56_5 * (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) / ((prob_etov_56_5 * (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) + ((1 - (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) * (1 - prob_etov_56_5)))
                    prob_etov_22_5 = rdm.random()
                    prob_etov_22_5_indp_home = rdm.random()
                    prob_etov_22_5_indp_away = rdm.random()
                    bayesian_etov_22_5 = (prob_etov_22_5 * (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) / ((prob_etov_22_5 * (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) + ((1 - (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) * (1 - prob_etov_22_5)))
                    prob_etov_36_5 = rdm.random()
                    prob_etov_36_5_indp_home = rdm.random()
                    prob_etov_36_5_indp_away = rdm.random()
                    bayesian_etov_36_5 = (prob_etov_36_5 * (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) / ((prob_etov_36_5 * (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) + ((1 - (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) * (1 - prob_etov_36_5)))
                    prob_etov_49_5 = rdm.random()
                    prob_etov_49_5_indp_home = rdm.random()
                    prob_etov_49_5_indp_away = rdm.random()
                    bayesian_etov_49_5 = (prob_etov_49_5 * (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) / ((prob_etov_49_5 * (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) + ((1 - (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) * (1 - prob_etov_49_5)))
                    prob_gtov_146_5 = rdm.random()
                    prob_gtov_146_5_indp_home = rdm.random()
                    prob_gtov_146_5_indp_away = rdm.random()
                    bayesian_gtov_146_5 = (prob_gtov_146_5 * (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) / ((prob_gtov_146_5 * (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) + ((1 - (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) * (1 - prob_gtov_146_5)))
                    prob_gtov_166_5 = rdm.random()
                    prob_gtov_166_5_indp_home = rdm.random()
                    prob_gtov_166_5_indp_away = rdm.random()
                    bayesian_gtov_166_5 = (prob_gtov_166_5 * (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) / ((prob_gtov_166_5 * (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) + ((1 - (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) * (1 - prob_gtov_166_5)))
                    prob_gtov_186_5 = rdm.random()
                    prob_gtov_186_5_indp_home = rdm.random()
                    prob_gtov_186_5_indp_away = rdm.random()
                    bayesian_gtov_186_5 = (prob_gtov_186_5 * (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) / ((prob_gtov_186_5 * (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) + ((1 - (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) * (1 - prob_gtov_186_5)))
                    prob_gtov_201_5 = rdm.random()
                    prob_gtov_201_5_indp_home = rdm.random()
                    prob_gtov_201_5_indp_away = rdm.random()
                    bayesian_gtov_201_5 = (prob_gtov_201_5 * (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) / ((prob_gtov_201_5 * (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) + ((1 - (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) * (1 - prob_gtov_201_5)))
                    prob_gtov_212_5 = rdm.random()
                    prob_gtov_212_5_indp_home = rdm.random()
                    prob_gtov_212_5_indp_away = rdm.random()
                    bayesian_gtov_212_5 = (prob_gtov_212_5 * (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) / ((prob_gtov_212_5 * (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) + ((1 - (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) * (1 - prob_gtov_212_5)))
                    prob_gtov_226_5 = rdm.random()
                    prob_gtov_226_5_indp_home = rdm.random()
                    prob_gtov_226_5_indp_away = rdm.random()
                    bayesian_gtov_226_5 = (prob_gtov_226_5 * (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) / ((prob_gtov_226_5 * (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) + ((1 - (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) * (1 - prob_gtov_226_5)))
                    prob_12 = rdm.random()
                    prob_12_indp_home = rdm.random()
                    prob_12_indp_away = rdm.random()
                    bayesian_12 = (prob_12 * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12 * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12)))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS[2]:
                    bayesian_home_Win = home_z_prob[q]
                    bayesian_away_Win = away_z_prob[q]
                    bayesian_etov_26_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))
                    bayesian_etov_33_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))
                    bayesian_etov_40_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))
                    bayesian_etov_46_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))
                    bayesian_etov_56_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))
                    bayesian_etov_22_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))
                    bayesian_etov_36_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))
                    bayesian_etov_49_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))
                    bayesian_gtov_146_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))
                    bayesian_gtov_166_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))
                    bayesian_gtov_186_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))
                    bayesian_gtov_201_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))
                    bayesian_gtov_212_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))
                    bayesian_gtov_226_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))
                    bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS[3]:
                    bayesian_home_Win = _1HWS[q]
                    bayesian_away_Win = _2AWS[q]
                    bayesian_etov_26_5 = OVER_etov_26_5_S[q]
                    bayesian_etov_33_5 = OVER_etov_33_5_S[q]
                    bayesian_etov_40_5 = OVER_etov_40_5_S[q]
                    bayesian_etov_46_5 = OVER_etov_46_5_S[q]
                    bayesian_etov_56_5 = OVER_etov_56_5_S[q]
                    bayesian_etov_22_5 = OVER_etov_22_5_S[q]
                    bayesian_etov_36_5 = OVER_etov_36_5_S[q]
                    bayesian_etov_49_5 = OVER_etov_49_5_S[q]
                    bayesian_gtov_146_5 = OVER_gtov_146_5_S[q]
                    bayesian_gtov_166_5 = OVER_gtov_166_5_S[q]
                    bayesian_gtov_186_5 = OVER_gtov_186_5_S[q]
                    bayesian_gtov_201_5 = OVER_gtov_201_5_S[q]
                    bayesian_gtov_212_5 = OVER_gtov_212_5_S[q]
                    bayesian_gtov_226_5 = OVER_gtov_226_5_S[q]
                    bayesian_12 = _12S[q]
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS[4]:
                    bayesian_home_Win = home_z_prob[q] * diff_z_prob[q]
                    bayesian_away_Win = away_z_prob[q] * diff_z_prob[q]
                    bayesian_etov_26_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q])) * diff_z_prob[q]
                    bayesian_etov_33_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q])) * diff_z_prob[q]
                    bayesian_etov_40_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q])) * diff_z_prob[q]
                    bayesian_etov_46_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q])) * diff_z_prob[q]
                    bayesian_etov_56_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q])) * diff_z_prob[q]
                    bayesian_etov_22_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q])) * diff_z_prob[q]
                    bayesian_etov_36_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q])) * diff_z_prob[q]
                    bayesian_etov_49_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q])) * diff_z_prob[q]
                    bayesian_gtov_146_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q])) * diff_z_prob[q]
                    bayesian_gtov_166_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q])) * diff_z_prob[q]
                    bayesian_gtov_186_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q])) * diff_z_prob[q]
                    bayesian_gtov_201_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q])) * diff_z_prob[q]
                    bayesian_gtov_212_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q])) * diff_z_prob[q]
                    bayesian_gtov_226_5 = math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q])) * diff_z_prob[q]
                    bayesian_12 = math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])) * diff_z_prob[q]
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

            except IndexError:
                continue

        for q in range(len(bayesian_home_Win_d)):
            if q == 0:
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                        file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                   f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                   f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                   f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                   f"BAYESIAN {OUTCOMES[9]}|BAYESIAN {OUTCOMES[10]}|BAYESIAN {OUTCOMES[11]}|BAYESIAN {OUTCOMES[12]}|"
                                   f"BAYESIAN {OUTCOMES[13]}|BAYESIAN {OUTCOMES[14]}|BAYESIAN {OUTCOMES[15]}|BAYESIAN {OUTCOMES[16]}|"
                                   f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
            try:
                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_D[q] == 0 and a_form_D[q] == 0:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                            if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                        if h_form_D[q] == 0 or a_form_D[q] == 0:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                            if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                            if X != PROB_METRICS[2] and X != PROB_METRICS[4]:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
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
        bayesian_etov_26_5_d = []
        bayesian_etov_33_5_d = []
        bayesian_etov_40_5_d = []
        bayesian_etov_46_5_d = []
        bayesian_etov_56_5_d = []
        bayesian_etov_22_5_d = []
        bayesian_etov_36_5_d = []
        bayesian_etov_49_5_d = []
        bayesian_gtov_146_5_d = []
        bayesian_gtov_166_5_d = []
        bayesian_gtov_186_5_d = []
        bayesian_gtov_201_5_d = []
        bayesian_gtov_212_5_d = []
        bayesian_gtov_226_5_d = []
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
                    prob_etov_26_5_indp_home = rdm.random()
                    prob_etov_26_5_indp_away = rdm.random()
                    bayesian_etov_26_5 = (prob_etov_26_5s[q] * (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) / ((prob_etov_26_5s[q] * (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) + ((1 - (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) * (1 - prob_etov_26_5s[q])))
                    prob_etov_33_5_indp_home = rdm.random()
                    prob_etov_33_5_indp_away = rdm.random()
                    bayesian_etov_33_5 = (prob_etov_33_5s[q] * (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) / ((prob_etov_33_5s[q] * (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) + ((1 - (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) * (1 - prob_etov_33_5s[q])))
                    prob_etov_40_5_indp_home = rdm.random()
                    prob_etov_40_5_indp_away = rdm.random()
                    bayesian_etov_40_5 = (prob_etov_40_5s[q] * (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) / ((prob_etov_40_5s[q] * (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) + ((1 - (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) * (1 - prob_etov_40_5s[q])))
                    prob_etov_46_5_indp_home = rdm.random()
                    prob_etov_46_5_indp_away = rdm.random()
                    bayesian_etov_46_5 = (prob_etov_46_5s[q] * (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) / ((prob_etov_46_5s[q] * (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) + ((1 - (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) * (1 - prob_etov_46_5s[q])))
                    prob_etov_56_5_indp_home = rdm.random()
                    prob_etov_56_5_indp_away = rdm.random()
                    bayesian_etov_56_5 = (prob_etov_56_5s[q] * (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) / ((prob_etov_56_5s[q] * (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) + ((1 - (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) * (1 - prob_etov_56_5s[q])))
                    prob_etov_22_5_indp_home = rdm.random()
                    prob_etov_22_5_indp_away = rdm.random()
                    bayesian_etov_22_5 = (prob_etov_22_5s[q] * (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) / ((prob_etov_22_5s[q] * (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) + ((1 - (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) * (1 - prob_etov_22_5s[q])))
                    prob_etov_36_5_indp_home = rdm.random()
                    prob_etov_36_5_indp_away = rdm.random()
                    bayesian_etov_36_5 = (prob_etov_36_5s[q] * (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) / ((prob_etov_36_5s[q] * (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) + ((1 - (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) * (1 - prob_etov_36_5s[q])))
                    prob_etov_49_5_indp_home = rdm.random()
                    prob_etov_49_5_indp_away = rdm.random()
                    bayesian_etov_49_5 = (prob_etov_49_5s[q] * (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) / ((prob_etov_49_5s[q] * (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) + ((1 - (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) * (1 - prob_etov_49_5s[q])))
                    prob_gtov_146_5_indp_home = rdm.random()
                    prob_gtov_146_5_indp_away = rdm.random()
                    bayesian_gtov_146_5 = (prob_gtov_146_5s[q] * (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) + ((1 - (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) * (1 - prob_gtov_146_5s[q])))
                    prob_gtov_166_5_indp_home = rdm.random()
                    prob_gtov_166_5_indp_away = rdm.random()
                    bayesian_gtov_166_5 = (prob_gtov_166_5s[q] * (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) + ((1 - (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) * (1 - prob_gtov_166_5s[q])))
                    prob_gtov_186_5_indp_home = rdm.random()
                    prob_gtov_186_5_indp_away = rdm.random()
                    bayesian_gtov_186_5 = (prob_gtov_186_5s[q] * (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) + ((1 - (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) * (1 - prob_gtov_186_5s[q])))
                    prob_gtov_201_5_indp_home = rdm.random()
                    prob_gtov_201_5_indp_away = rdm.random()
                    bayesian_gtov_201_5 = (prob_gtov_201_5s[q] * (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) + ((1 - (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) * (1 - prob_gtov_201_5s[q])))
                    prob_gtov_212_5_indp_home = rdm.random()
                    prob_gtov_212_5_indp_away = rdm.random()
                    bayesian_gtov_212_5 = (prob_gtov_212_5s[q] * (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) + ((1 - (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) * (1 - prob_gtov_212_5s[q])))
                    prob_gtov_226_5_indp_home = rdm.random()
                    prob_gtov_226_5_indp_away = rdm.random()
                    bayesian_gtov_226_5 = (prob_gtov_226_5s[q] * (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) + ((1 - (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) * (1 - prob_gtov_226_5s[q])))
                    prob_12_indp_home = rdm.random()
                    prob_12_indp_away = rdm.random()
                    bayesian_12 = (prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) / ((prob_12s[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - prob_12s[q])))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS1[0] and Y == PROB_METRICS1[2]:
                    prob_matches_W_indp_home1 = rdm.random()
                    prob_matches_W_indp_away1 = rdm.random()
                    bayesian_home_Win = (home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((home_z_prob[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - home_z_prob[q])))
                    prob_matches_W_indp_home2 = rdm.random()
                    prob_matches_W_indp_away2 = rdm.random()
                    bayesian_away_Win = (away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((away_z_prob[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - away_z_prob[q])))
                    prob_etov_26_5_indp_home = rdm.random()
                    prob_etov_26_5_indp_away = rdm.random()
                    bayesian_etov_26_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) + ((1 - (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q])))))))
                    prob_etov_33_5_indp_home = rdm.random()
                    prob_etov_33_5_indp_away = rdm.random()
                    bayesian_etov_33_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) + ((1 - (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q])))))))
                    prob_etov_40_5_indp_home = rdm.random()
                    prob_etov_40_5_indp_away = rdm.random()
                    bayesian_etov_40_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) + ((1 - (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q])))))))
                    prob_etov_46_5_indp_home = rdm.random()
                    prob_etov_46_5_indp_away = rdm.random()
                    bayesian_etov_46_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) + ((1 - (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q])))))))
                    prob_etov_56_5_indp_home = rdm.random()
                    prob_etov_56_5_indp_away = rdm.random()
                    bayesian_etov_56_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) + ((1 - (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q])))))))
                    prob_etov_22_5_indp_home = rdm.random()
                    prob_etov_22_5_indp_away = rdm.random()
                    bayesian_etov_22_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) + ((1 - (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q])))))))
                    prob_etov_36_5_indp_home = rdm.random()
                    prob_etov_36_5_indp_away = rdm.random()
                    bayesian_etov_36_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) + ((1 - (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q])))))))
                    prob_etov_49_5_indp_home = rdm.random()
                    prob_etov_49_5_indp_away = rdm.random()
                    bayesian_etov_49_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) + ((1 - (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q])))))))
                    prob_gtov_146_5_indp_home = rdm.random()
                    prob_gtov_146_5_indp_away = rdm.random()
                    bayesian_gtov_146_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) + ((1 - (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q])))))))
                    prob_gtov_166_5_indp_home = rdm.random()
                    prob_gtov_166_5_indp_away = rdm.random()
                    bayesian_gtov_166_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) + ((1 - (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q])))))))
                    prob_gtov_186_5_indp_home = rdm.random()
                    prob_gtov_186_5_indp_away = rdm.random()
                    bayesian_gtov_186_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) + ((1 - (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q])))))))
                    prob_gtov_201_5_indp_home = rdm.random()
                    prob_gtov_201_5_indp_away = rdm.random()
                    bayesian_gtov_201_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) + ((1 - (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q])))))))
                    prob_gtov_212_5_indp_home = rdm.random()
                    prob_gtov_212_5_indp_away = rdm.random()
                    bayesian_gtov_212_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) + ((1 - (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q])))))))
                    prob_gtov_226_5_indp_home = rdm.random()
                    prob_gtov_226_5_indp_away = rdm.random()
                    bayesian_gtov_226_5 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) + ((1 - (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q])))))))
                    prob_12_indp_home = rdm.random()
                    prob_12_indp_away = rdm.random()
                    bayesian_12 = (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q])))))))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS1[0] and Y == PROB_METRICS1[3]:
                    prob_matches_W_indp_home1 = rdm.random()
                    prob_matches_W_indp_away1 = rdm.random()
                    bayesian_home_Win = (_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) / ((_1HWS[q] * (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) + ((1 - (prob_matches_W_indp_home1 * prob_matches_W_indp_away1)) * (1 - _1HWS[q])))
                    prob_matches_W_indp_home2 = rdm.random()
                    prob_matches_W_indp_away2 = rdm.random()
                    bayesian_away_Win = (_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) / ((_2AWS[q] * (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) + ((1 - (prob_matches_W_indp_home2 * prob_matches_W_indp_away2)) * (1 - _2AWS[q])))
                    prob_etov_26_5_indp_home = rdm.random()
                    prob_etov_26_5_indp_away = rdm.random()
                    bayesian_etov_26_5 = (OVER_etov_26_5_S[q] * (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) / ((OVER_etov_26_5_S[q] * (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) + ((1 - (prob_etov_26_5_indp_home * prob_etov_26_5_indp_away)) * (1 - OVER_etov_26_5_S[q])))
                    prob_etov_33_5_indp_home = rdm.random()
                    prob_etov_33_5_indp_away = rdm.random()
                    bayesian_etov_33_5 = (OVER_etov_33_5_S[q] * (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) / ((OVER_etov_33_5_S[q] * (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) + ((1 - (prob_etov_33_5_indp_home * prob_etov_33_5_indp_away)) * (1 - OVER_etov_33_5_S[q])))
                    prob_etov_40_5_indp_home = rdm.random()
                    prob_etov_40_5_indp_away = rdm.random()
                    bayesian_etov_40_5 = (OVER_etov_40_5_S[q] * (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) / ((OVER_etov_40_5_S[q] * (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) + ((1 - (prob_etov_40_5_indp_home * prob_etov_40_5_indp_away)) * (1 - OVER_etov_40_5_S[q])))
                    prob_etov_46_5_indp_home = rdm.random()
                    prob_etov_46_5_indp_away = rdm.random()
                    bayesian_etov_46_5 = (OVER_etov_46_5_S[q] * (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) / ((OVER_etov_46_5_S[q] * (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) + ((1 - (prob_etov_46_5_indp_home * prob_etov_46_5_indp_away)) * (1 - OVER_etov_46_5_S[q])))
                    prob_etov_56_5_indp_home = rdm.random()
                    prob_etov_56_5_indp_away = rdm.random()
                    bayesian_etov_56_5 = (OVER_etov_56_5_S[q] * (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) / ((OVER_etov_56_5_S[q] * (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) + ((1 - (prob_etov_56_5_indp_home * prob_etov_56_5_indp_away)) * (1 - OVER_etov_56_5_S[q])))
                    prob_etov_22_5_indp_home = rdm.random()
                    prob_etov_22_5_indp_away = rdm.random()
                    bayesian_etov_22_5 = (OVER_etov_22_5_S[q] * (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) / ((OVER_etov_22_5_S[q] * (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) + ((1 - (prob_etov_22_5_indp_home * prob_etov_22_5_indp_away)) * (1 - OVER_etov_22_5_S[q])))
                    prob_etov_36_5_indp_home = rdm.random()
                    prob_etov_36_5_indp_away = rdm.random()
                    bayesian_etov_36_5 = (OVER_etov_36_5_S[q] * (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) / ((OVER_etov_36_5_S[q] * (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) + ((1 - (prob_etov_36_5_indp_home * prob_etov_36_5_indp_away)) * (1 - OVER_etov_36_5_S[q])))
                    prob_etov_49_5_indp_home = rdm.random()
                    prob_etov_49_5_indp_away = rdm.random()
                    bayesian_etov_49_5 = (OVER_etov_49_5_S[q] * (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) / ((OVER_etov_49_5_S[q] * (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) + ((1 - (prob_etov_49_5_indp_home * prob_etov_49_5_indp_away)) * (1 - OVER_etov_49_5_S[q])))
                    prob_gtov_146_5_indp_home = rdm.random()
                    prob_gtov_146_5_indp_away = rdm.random()
                    bayesian_gtov_146_5 = (OVER_gtov_146_5_S[q] * (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) / ((OVER_gtov_146_5_S[q] * (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) + ((1 - (prob_gtov_146_5_indp_home * prob_gtov_146_5_indp_away)) * (1 - OVER_gtov_146_5_S[q])))
                    prob_gtov_166_5_indp_home = rdm.random()
                    prob_gtov_166_5_indp_away = rdm.random()
                    bayesian_gtov_166_5 = (OVER_gtov_166_5_S[q] * (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) / ((OVER_gtov_166_5_S[q] * (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) + ((1 - (prob_gtov_166_5_indp_home * prob_gtov_166_5_indp_away)) * (1 - OVER_gtov_166_5_S[q])))
                    prob_gtov_186_5_indp_home = rdm.random()
                    prob_gtov_186_5_indp_away = rdm.random()
                    bayesian_gtov_186_5 = (OVER_gtov_186_5_S[q] * (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) / ((OVER_gtov_186_5_S[q] * (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) + ((1 - (prob_gtov_186_5_indp_home * prob_gtov_186_5_indp_away)) * (1 - OVER_gtov_186_5_S[q])))
                    prob_gtov_201_5_indp_home = rdm.random()
                    prob_gtov_201_5_indp_away = rdm.random()
                    bayesian_gtov_201_5 = (OVER_gtov_201_5_S[q] * (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) / ((OVER_gtov_201_5_S[q] * (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) + ((1 - (prob_gtov_201_5_indp_home * prob_gtov_201_5_indp_away)) * (1 - OVER_gtov_201_5_S[q])))
                    prob_gtov_212_5_indp_home = rdm.random()
                    prob_gtov_212_5_indp_away = rdm.random()
                    bayesian_gtov_212_5 = (OVER_gtov_212_5_S[q] * (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) / ((OVER_gtov_212_5_S[q] * (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) + ((1 - (prob_gtov_212_5_indp_home * prob_gtov_212_5_indp_away)) * (1 - OVER_gtov_212_5_S[q])))
                    prob_gtov_226_5_indp_home = rdm.random()
                    prob_gtov_226_5_indp_away = rdm.random()
                    bayesian_gtov_226_5 = (OVER_gtov_226_5_S[q] * (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) / ((OVER_gtov_226_5_S[q] * (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) + ((1 - (prob_gtov_226_5_indp_home * prob_gtov_226_5_indp_away)) * (1 - OVER_gtov_226_5_S[q])))
                    prob_12_indp_home = rdm.random()
                    prob_12_indp_away = rdm.random()
                    bayesian_12 = (_12S[q] * (prob_12_indp_home * prob_12_indp_away)) / ((_12S[q] * (prob_12_indp_home * prob_12_indp_away)) + ((1 - (prob_12_indp_home * prob_12_indp_away)) * (1 - _12S[q])))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS1[1] and Y == PROB_METRICS1[0]:
                    prob_matches_home_W_against_EO = rdm.random()
                    bayesian_home_Win = (prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_matches_home_W_against_EO * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_matches_home_W_against_EO)))
                    prob_matches_away_W_against_EO = rdm.random()
                    bayesian_away_Win = (prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_matches_away_W_against_EO * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_matches_away_W_against_EO)))
                    prob_etov_26_5 = rdm.random()
                    bayesian_etov_26_5 = ((prob_etov_26_5 * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5 * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5))))
                    prob_etov_33_5 = rdm.random()
                    bayesian_etov_33_5 = ((prob_etov_33_5 * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5 * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5))))
                    prob_etov_40_5 = rdm.random()
                    bayesian_etov_40_5 = ((prob_etov_40_5 * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5 * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5))))
                    prob_etov_46_5 = rdm.random()
                    bayesian_etov_46_5 = ((prob_etov_46_5 * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5 * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5))))
                    prob_etov_56_5 = rdm.random()
                    bayesian_etov_56_5 = ((prob_etov_56_5 * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5 * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5))))
                    prob_etov_22_5 = rdm.random()
                    bayesian_etov_22_5 = ((prob_etov_22_5 * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5 * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5))))
                    prob_etov_36_5 = rdm.random()
                    bayesian_etov_36_5 = ((prob_etov_36_5 * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5 * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5))))
                    prob_etov_49_5 = rdm.random()
                    bayesian_etov_49_5 = ((prob_etov_49_5 * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5 * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5))))
                    prob_gtov_146_5 = rdm.random()
                    bayesian_gtov_146_5 = ((prob_gtov_146_5 * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5 * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5))))
                    prob_gtov_166_5 = rdm.random()
                    bayesian_gtov_166_5 = ((prob_gtov_166_5 * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5 * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5))))
                    prob_gtov_186_5 = rdm.random()
                    bayesian_gtov_186_5 = ((prob_gtov_186_5 * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5 * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5))))
                    prob_gtov_201_5 = rdm.random()
                    bayesian_gtov_201_5 = ((prob_gtov_201_5 * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5 * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5))))
                    prob_gtov_212_5 = rdm.random()
                    bayesian_gtov_212_5 = ((prob_gtov_212_5 * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5 * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5))))
                    prob_gtov_226_5 = rdm.random()
                    bayesian_gtov_226_5 = ((prob_gtov_226_5 * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5 * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5))))
                    prob_12 = rdm.random()
                    bayesian_12 = ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12 * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12))))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS1[1] and Y == PROB_METRICS1[2]:
                    bayesian_home_Win = (home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((home_z_prob[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - home_z_prob[q])))
                    bayesian_away_Win = (away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((away_z_prob[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - away_z_prob[q])))
                    bayesian_etov_26_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))))))
                    bayesian_etov_33_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))))))
                    bayesian_etov_40_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))))))
                    bayesian_etov_46_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))))))
                    bayesian_etov_56_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))))))
                    bayesian_etov_22_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))))))
                    bayesian_etov_36_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))))))
                    bayesian_etov_49_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))))))
                    bayesian_gtov_146_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))))))
                    bayesian_gtov_166_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))))))
                    bayesian_gtov_186_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))))))
                    bayesian_gtov_201_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))))))
                    bayesian_gtov_212_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))))))
                    bayesian_gtov_226_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))))))
                    bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) / (((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))))))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)

                if X == PROB_METRICS1[1] and Y == PROB_METRICS1[3]:
                    bayesian_home_Win = (_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((_1HWS[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - _1HWS[q])))
                    bayesian_away_Win = (_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((_2AWS[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - _2AWS[q])))
                    bayesian_etov_26_5 = (OVER_etov_26_5_S[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((OVER_etov_26_5_S[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - OVER_etov_26_5_S[q])))
                    bayesian_etov_33_5 = (OVER_etov_33_5_S[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((OVER_etov_33_5_S[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - OVER_etov_33_5_S[q])))
                    bayesian_etov_40_5 = (OVER_etov_40_5_S[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((OVER_etov_40_5_S[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - OVER_etov_40_5_S[q])))
                    bayesian_etov_46_5 = (OVER_etov_46_5_S[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((OVER_etov_46_5_S[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - OVER_etov_46_5_S[q])))
                    bayesian_etov_56_5 = (OVER_etov_56_5_S[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((OVER_etov_56_5_S[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - OVER_etov_56_5_S[q])))
                    bayesian_etov_22_5 = (OVER_etov_22_5_S[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((OVER_etov_22_5_S[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - OVER_etov_22_5_S[q])))
                    bayesian_etov_36_5 = (OVER_etov_36_5_S[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((OVER_etov_36_5_S[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - OVER_etov_36_5_S[q])))
                    bayesian_etov_49_5 = (OVER_etov_49_5_S[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((OVER_etov_49_5_S[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - OVER_etov_49_5_S[q])))
                    bayesian_gtov_146_5 = (OVER_gtov_146_5_S[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((OVER_gtov_146_5_S[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - OVER_gtov_146_5_S[q])))
                    bayesian_gtov_166_5 = (OVER_gtov_166_5_S[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((OVER_gtov_166_5_S[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - OVER_gtov_166_5_S[q])))
                    bayesian_gtov_186_5 = (OVER_gtov_186_5_S[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((OVER_gtov_186_5_S[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - OVER_gtov_186_5_S[q])))
                    bayesian_gtov_201_5 = (OVER_gtov_201_5_S[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((OVER_gtov_201_5_S[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - OVER_gtov_201_5_S[q])))
                    bayesian_gtov_212_5 = (OVER_gtov_212_5_S[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((OVER_gtov_212_5_S[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - OVER_gtov_212_5_S[q])))
                    bayesian_gtov_226_5 = (OVER_gtov_226_5_S[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((OVER_gtov_226_5_S[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - OVER_gtov_226_5_S[q])))
                    bayesian_12 = (_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((_12S[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - _12S[q])))
                    baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                  baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                  baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                  baye_etov_56_5=bayesian_etov_56_5,
                                  baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                  baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                  baye_gtov_166_5=bayesian_gtov_166_5,
                                  baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                  baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                  baye_12=bayesian_12)
            except IndexError:
                continue

        for q in range(len(bayesian_home_Win_d)):
            if q == 0:
                for i in range(11):
                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                        file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                   f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                   f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                   f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                   f"BAYESIAN {OUTCOMES[9]}|BAYESIAN {OUTCOMES[10]}|BAYESIAN {OUTCOMES[11]}|BAYESIAN {OUTCOMES[12]}|"
                                   f"BAYESIAN {OUTCOMES[13]}|BAYESIAN {OUTCOMES[14]}|BAYESIAN {OUTCOMES[15]}|BAYESIAN {OUTCOMES[16]}|"
                                   f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
            try:
                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_D[q] == 0 and a_form_D[q] == 0:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                            if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                        if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                            if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                        if h_form_D[q] == 0 or a_form_D[q] == 0:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                            if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                    if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                        if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer(w=q, A=X, B=Y, C=Z, data=file)
                                else:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                            writer(w=q, A=X, B=Y, C=Z, data=file)

                if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                        bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                        bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                        bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                        bayesian_gtov_226_5_d[q] > CONFINTVL:
                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                        if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                            if X == PROB_METRICS1[0] or Y == PROB_METRICS1[0]:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                    with open(f"../RESULTS - {Z}_{X}_{Y}/{Z}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                        writer(w=q, A=X, B=Y, C=Z, data=file)
                            else:
                                if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= BAY_DIFF and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
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
                bayesian_etov_26_5_d = []
                bayesian_etov_33_5_d = []
                bayesian_etov_40_5_d = []
                bayesian_etov_46_5_d = []
                bayesian_etov_56_5_d = []
                bayesian_etov_22_5_d = []
                bayesian_etov_36_5_d = []
                bayesian_etov_49_5_d = []
                bayesian_gtov_146_5_d = []
                bayesian_gtov_166_5_d = []
                bayesian_gtov_186_5_d = []
                bayesian_gtov_201_5_d = []
                bayesian_gtov_212_5_d = []
                bayesian_gtov_226_5_d = []
                bayesian_12_d = []

                for q in range(len(home_teams)):
                    try:
                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_etov_26_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random() + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                            bayesian_etov_33_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random() + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                            bayesian_etov_40_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random() + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                            bayesian_etov_46_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random() + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                            bayesian_etov_56_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random() + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                            bayesian_etov_22_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random() + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                            bayesian_etov_36_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random() + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                            bayesian_etov_49_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random() + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                            bayesian_gtov_146_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random() + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                            bayesian_gtov_166_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random() + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                            bayesian_gtov_186_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random() + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                            bayesian_gtov_201_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random() + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                            bayesian_gtov_212_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random() + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                            bayesian_gtov_226_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random() + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                            bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_etov_26_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random() + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                            bayesian_etov_33_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random() + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                            bayesian_etov_40_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random() + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                            bayesian_etov_46_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random() + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                            bayesian_etov_56_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random() + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                            bayesian_etov_22_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random() + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                            bayesian_etov_36_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random() + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                            bayesian_etov_49_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random() + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                            bayesian_gtov_146_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random() + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                            bayesian_gtov_166_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random() + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                            bayesian_gtov_186_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * rdm.random() * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))
                            bayesian_gtov_201_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * rdm.random() * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))
                            bayesian_gtov_212_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * rdm.random() * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))
                            bayesian_gtov_226_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * rdm.random() * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[4]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_etov_26_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random() + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))))
                            bayesian_etov_33_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random() + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))))
                            bayesian_etov_40_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random() + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))))
                            bayesian_etov_46_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random() + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))))
                            bayesian_etov_56_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random() + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))))
                            bayesian_etov_22_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random() + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))))
                            bayesian_etov_36_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random() + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))))
                            bayesian_etov_49_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random() + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))))
                            bayesian_gtov_146_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random() + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))))
                            bayesian_gtov_166_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random() + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))))
                            bayesian_gtov_186_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random() + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))))
                            bayesian_gtov_201_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random() + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))))
                            bayesian_gtov_212_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random() + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))))
                            bayesian_gtov_226_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random() + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))))
                            bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[2] and Z == COMBINERS[5]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_etov_26_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random() + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))))
                            bayesian_etov_33_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random() + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))))
                            bayesian_etov_40_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random() + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))))
                            bayesian_etov_46_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random() + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))))
                            bayesian_etov_56_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random() + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))))
                            bayesian_etov_22_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random() + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))))
                            bayesian_etov_36_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random() + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))))
                            bayesian_etov_49_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random() + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))))
                            bayesian_gtov_146_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random() + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))))
                            bayesian_gtov_166_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random() + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))))
                            bayesian_gtov_186_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random() + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))))
                            bayesian_gtov_201_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random() + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))))
                            bayesian_gtov_212_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random() + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))))
                            bayesian_gtov_226_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random() + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))))
                            bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = (1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_etov_26_5 = (1 / 3) * (OVER_etov_26_5_S[q] + rdm.random() + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                            bayesian_etov_33_5 = (1 / 3) * (OVER_etov_33_5_S[q] + rdm.random() + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                            bayesian_etov_40_5 = (1 / 3) * (OVER_etov_40_5_S[q] + rdm.random() + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                            bayesian_etov_46_5 = (1 / 3) * (OVER_etov_46_5_S[q] + rdm.random() + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                            bayesian_etov_56_5 = (1 / 3) * (OVER_etov_56_5_S[q] + rdm.random() + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                            bayesian_etov_22_5 = (1 / 3) * (OVER_etov_22_5_S[q] + rdm.random() + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                            bayesian_etov_36_5 = (1 / 3) * (OVER_etov_36_5_S[q] + rdm.random() + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                            bayesian_etov_49_5 = (1 / 3) * (OVER_etov_49_5_S[q] + rdm.random() + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                            bayesian_gtov_146_5 = (1 / 3) * (OVER_gtov_146_5_S[q] + rdm.random() + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                            bayesian_gtov_166_5 = (1 / 3) * (OVER_gtov_166_5_S[q] + rdm.random() + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                            bayesian_gtov_186_5 = (1 / 3) * (OVER_gtov_186_5_S[q] + rdm.random() + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                            bayesian_gtov_201_5 = (1 / 3) * (OVER_gtov_201_5_S[q] + rdm.random() + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                            bayesian_gtov_212_5 = (1 / 3) * (OVER_gtov_212_5_S[q] + rdm.random() + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                            bayesian_gtov_226_5 = (1 / 3) * (OVER_gtov_226_5_S[q] + rdm.random() + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                            bayesian_12 = (1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = _1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = _2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_etov_26_5 = OVER_etov_26_5_S[q] * rdm.random() * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))
                            bayesian_etov_33_5 = OVER_etov_33_5_S[q] * rdm.random() * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))
                            bayesian_etov_40_5 = OVER_etov_40_5_S[q] * rdm.random() * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))
                            bayesian_etov_46_5 = OVER_etov_46_5_S[q] * rdm.random() * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))
                            bayesian_etov_56_5 = OVER_etov_56_5_S[q] * rdm.random() * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))
                            bayesian_etov_22_5 = OVER_etov_22_5_S[q] * rdm.random() * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))
                            bayesian_etov_36_5 = OVER_etov_36_5_S[q] * rdm.random() * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))
                            bayesian_etov_49_5 = OVER_etov_49_5_S[q] * rdm.random() * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))
                            bayesian_gtov_146_5 = OVER_gtov_146_5_S[q] * rdm.random() * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))
                            bayesian_gtov_166_5 = OVER_gtov_166_5_S[q] * rdm.random() * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))
                            bayesian_gtov_186_5 = OVER_gtov_186_5_S[q] * rdm.random() * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))
                            bayesian_gtov_201_5 = OVER_gtov_201_5_S[q] * rdm.random() * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))
                            bayesian_gtov_212_5 = OVER_gtov_212_5_S[q] * rdm.random() * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))
                            bayesian_gtov_226_5 = OVER_gtov_226_5_S[q] * rdm.random() * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))
                            bayesian_12 = _12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (_1HWS[q] + rdm.random() + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = np.cbrt((1 / 3) * (_2AWS[q] + rdm.random() + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_etov_26_5 = np.cbrt((1 / 3) * (OVER_etov_26_5_S[q] + rdm.random() + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))))
                            bayesian_etov_33_5 = np.cbrt((1 / 3) * (OVER_etov_33_5_S[q] + rdm.random() + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))))
                            bayesian_etov_40_5 = np.cbrt((1 / 3) * (OVER_etov_40_5_S[q] + rdm.random() + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))))
                            bayesian_etov_46_5 = np.cbrt((1 / 3) * (OVER_etov_46_5_S[q] + rdm.random() + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))))
                            bayesian_etov_56_5 = np.cbrt((1 / 3) * (OVER_etov_56_5_S[q] + rdm.random() + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))))
                            bayesian_etov_22_5 = np.cbrt((1 / 3) * (OVER_etov_22_5_S[q] + rdm.random() + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))))
                            bayesian_etov_36_5 = np.cbrt((1 / 3) * (OVER_etov_36_5_S[q] + rdm.random() + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))))
                            bayesian_etov_49_5 = np.cbrt((1 / 3) * (OVER_etov_49_5_S[q] + rdm.random() + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))))
                            bayesian_gtov_146_5 = np.cbrt((1 / 3) * (OVER_gtov_146_5_S[q] + rdm.random() + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))))
                            bayesian_gtov_166_5 = np.cbrt((1 / 3) * (OVER_gtov_166_5_S[q] + rdm.random() + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))))
                            bayesian_gtov_186_5 = np.cbrt((1 / 3) * (OVER_gtov_186_5_S[q] + rdm.random() + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))))
                            bayesian_gtov_201_5 = np.cbrt((1 / 3) * (OVER_gtov_201_5_S[q] + rdm.random() + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))))
                            bayesian_gtov_212_5 = np.cbrt((1 / 3) * (OVER_gtov_212_5_S[q] + rdm.random() + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))))
                            bayesian_gtov_226_5 = np.cbrt((1 / 3) * (OVER_gtov_226_5_S[q] + rdm.random() + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))))
                            bayesian_12 = np.cbrt((1 / 3) * (_12S[q] + rdm.random() + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[1] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                            bayesian_home_Win = np.cbrt(_1HWS[q] * rdm.random() * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = np.cbrt(_2AWS[q] * rdm.random() * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_etov_26_5 = np.cbrt(OVER_etov_26_5_S[q] * rdm.random() * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                            bayesian_etov_33_5 = np.cbrt(OVER_etov_33_5_S[q] * rdm.random() * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                            bayesian_etov_40_5 = np.cbrt(OVER_etov_40_5_S[q] * rdm.random() * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                            bayesian_etov_46_5 = np.cbrt(OVER_etov_46_5_S[q] * rdm.random() * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                            bayesian_etov_56_5 = np.cbrt(OVER_etov_56_5_S[q] * rdm.random() * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                            bayesian_etov_22_5 = np.cbrt(OVER_etov_22_5_S[q] * rdm.random() * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                            bayesian_etov_36_5 = np.cbrt(OVER_etov_36_5_S[q] * rdm.random() * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                            bayesian_etov_49_5 = np.cbrt(OVER_etov_49_5_S[q] * rdm.random() * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                            bayesian_gtov_146_5 = np.cbrt(OVER_gtov_146_5_S[q] * rdm.random() * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                            bayesian_gtov_166_5 = np.cbrt(OVER_gtov_166_5_S[q] * rdm.random() * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                            bayesian_gtov_186_5 = np.cbrt(OVER_gtov_186_5_S[q] * rdm.random() * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                            bayesian_gtov_201_5 = np.cbrt(OVER_gtov_201_5_S[q] * rdm.random() * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                            bayesian_gtov_212_5 = np.cbrt(OVER_gtov_212_5_S[q] * rdm.random() * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                            bayesian_gtov_226_5 = np.cbrt(OVER_gtov_226_5_S[q] * rdm.random() * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                            bayesian_12 = np.cbrt(_12S[q] * rdm.random() * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = (1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_etov_26_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + OVER_etov_26_5_S[q] + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                            bayesian_etov_33_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + OVER_etov_33_5_S[q] + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                            bayesian_etov_40_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + OVER_etov_40_5_S[q] + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                            bayesian_etov_46_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + OVER_etov_46_5_S[q] + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                            bayesian_etov_56_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + OVER_etov_56_5_S[q] + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                            bayesian_etov_22_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + OVER_etov_22_5_S[q] + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                            bayesian_etov_36_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + OVER_etov_36_5_S[q] + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                            bayesian_etov_49_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + OVER_etov_49_5_S[q] + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                            bayesian_gtov_146_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + OVER_gtov_146_5_S[q] + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                            bayesian_gtov_166_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + OVER_gtov_166_5_S[q] + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                            bayesian_gtov_186_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + OVER_gtov_186_5_S[q] + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                            bayesian_gtov_201_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + OVER_gtov_201_5_S[q] + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                            bayesian_gtov_212_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + OVER_gtov_212_5_S[q] + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                            bayesian_gtov_226_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + OVER_gtov_226_5_S[q] + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                            bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_etov_26_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * OVER_etov_26_5_S[q] * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))
                            bayesian_etov_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * OVER_etov_33_5_S[q] * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))
                            bayesian_etov_40_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * OVER_etov_40_5_S[q] * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))
                            bayesian_etov_46_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * OVER_etov_46_5_S[q] * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))
                            bayesian_etov_56_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * OVER_etov_56_5_S[q] * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))
                            bayesian_etov_22_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * OVER_etov_22_5_S[q] * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))
                            bayesian_etov_36_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * OVER_etov_36_5_S[q] * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))
                            bayesian_etov_49_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * OVER_etov_49_5_S[q] * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))
                            bayesian_gtov_146_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * OVER_gtov_146_5_S[q] * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))
                            bayesian_gtov_166_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * OVER_gtov_166_5_S[q] * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))
                            bayesian_gtov_186_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * OVER_gtov_186_5_S[q] * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))
                            bayesian_gtov_201_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * OVER_gtov_201_5_S[q] * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))
                            bayesian_gtov_212_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * OVER_gtov_212_5_S[q] * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))
                            bayesian_gtov_226_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * OVER_gtov_226_5_S[q] * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))))
                            bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))))
                            bayesian_etov_26_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + OVER_etov_26_5_S[q] + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))))
                            bayesian_etov_33_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + OVER_etov_33_5_S[q] + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))))
                            bayesian_etov_40_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + OVER_etov_40_5_S[q] + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))))
                            bayesian_etov_46_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + OVER_etov_46_5_S[q] + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))))
                            bayesian_etov_56_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + OVER_etov_56_5_S[q] + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))))
                            bayesian_etov_22_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + OVER_etov_22_5_S[q] + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))))
                            bayesian_etov_36_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + OVER_etov_36_5_S[q] + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))))
                            bayesian_etov_49_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + OVER_etov_49_5_S[q] + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))))
                            bayesian_gtov_146_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + OVER_gtov_146_5_S[q] + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))))
                            bayesian_gtov_166_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + OVER_gtov_166_5_S[q] + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))))
                            bayesian_gtov_186_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + OVER_gtov_186_5_S[q] + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))))
                            bayesian_gtov_201_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + OVER_gtov_201_5_S[q] + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))))
                            bayesian_gtov_212_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + OVER_gtov_212_5_S[q] + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))))
                            bayesian_gtov_226_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + OVER_gtov_226_5_S[q] + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))))
                            bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[0] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                            bayesian_home_Win = np.cbrt(home_z_prob[q] * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = np.cbrt(away_z_prob[q] * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_etov_26_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * OVER_etov_26_5_S[q] * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                            bayesian_etov_33_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * OVER_etov_33_5_S[q] * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                            bayesian_etov_40_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * OVER_etov_40_5_S[q] * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                            bayesian_etov_46_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * OVER_etov_46_5_S[q] * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                            bayesian_etov_56_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * OVER_etov_56_5_S[q] * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                            bayesian_etov_22_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * OVER_etov_22_5_S[q] * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                            bayesian_etov_36_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * OVER_etov_36_5_S[q] * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                            bayesian_etov_49_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * OVER_etov_49_5_S[q] * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                            bayesian_gtov_146_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * OVER_gtov_146_5_S[q] * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                            bayesian_gtov_166_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * OVER_gtov_166_5_S[q] * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                            bayesian_gtov_186_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * OVER_gtov_186_5_S[q] * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                            bayesian_gtov_201_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * OVER_gtov_201_5_S[q] * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                            bayesian_gtov_212_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * OVER_gtov_212_5_S[q] * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                            bayesian_gtov_226_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * OVER_gtov_226_5_S[q] * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                            bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q])
                            bayesian_away_Win = (1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q])
                            bayesian_etov_26_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random() + OVER_etov_26_5_S[q])
                            bayesian_etov_33_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random() + OVER_etov_33_5_S[q])
                            bayesian_etov_40_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random() + OVER_etov_40_5_S[q])
                            bayesian_etov_46_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random() + OVER_etov_46_5_S[q])
                            bayesian_etov_56_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random() + OVER_etov_56_5_S[q])
                            bayesian_etov_22_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random() + OVER_etov_22_5_S[q])
                            bayesian_etov_36_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random() + OVER_etov_36_5_S[q])
                            bayesian_etov_49_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random() + OVER_etov_49_5_S[q])
                            bayesian_gtov_146_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random() + OVER_gtov_146_5_S[q])
                            bayesian_gtov_166_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random() + OVER_gtov_166_5_S[q])
                            bayesian_gtov_186_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random() + OVER_gtov_186_5_S[q])
                            bayesian_gtov_201_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random() + OVER_gtov_201_5_S[q])
                            bayesian_gtov_212_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random() + OVER_gtov_212_5_S[q])
                            bayesian_gtov_226_5 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random() + OVER_gtov_226_5_S[q])
                            bayesian_12 = (1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q]
                            bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q]
                            bayesian_etov_26_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * rdm.random() * OVER_etov_26_5_S[q]
                            bayesian_etov_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * rdm.random() * OVER_etov_33_5_S[q]
                            bayesian_etov_40_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * rdm.random() * OVER_etov_40_5_S[q]
                            bayesian_etov_46_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * rdm.random() * OVER_etov_46_5_S[q]
                            bayesian_etov_56_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * rdm.random() * OVER_etov_56_5_S[q]
                            bayesian_etov_22_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * rdm.random() * OVER_etov_22_5_S[q]
                            bayesian_etov_36_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * rdm.random() * OVER_etov_36_5_S[q]
                            bayesian_etov_49_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * rdm.random() * OVER_etov_49_5_S[q]
                            bayesian_gtov_146_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * rdm.random() * OVER_gtov_146_5_S[q]
                            bayesian_gtov_166_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * rdm.random() * OVER_gtov_166_5_S[q]
                            bayesian_gtov_186_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * rdm.random() * OVER_gtov_186_5_S[q]
                            bayesian_gtov_201_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * rdm.random() * OVER_gtov_201_5_S[q]
                            bayesian_gtov_212_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * rdm.random() * OVER_gtov_212_5_S[q]
                            bayesian_gtov_226_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * rdm.random() * OVER_gtov_226_5_S[q]
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q]
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[4]:
                            bayesian_home_Win = np.cbrt((1 / 3) * (home_z_prob[q] + rdm.random() + _1HWS[q]))
                            bayesian_away_Win = np.cbrt((1 / 3) * (away_z_prob[q] + rdm.random() + _2AWS[q]))
                            bayesian_etov_26_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random() + OVER_etov_26_5_S[q]))
                            bayesian_etov_33_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random() + OVER_etov_33_5_S[q]))
                            bayesian_etov_40_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random() + OVER_etov_40_5_S[q]))
                            bayesian_etov_46_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random() + OVER_etov_46_5_S[q]))
                            bayesian_etov_56_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random() + OVER_etov_56_5_S[q]))
                            bayesian_etov_22_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random() + OVER_etov_22_5_S[q]))
                            bayesian_etov_36_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random() + OVER_etov_36_5_S[q]))
                            bayesian_etov_49_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random() + OVER_etov_49_5_S[q]))
                            bayesian_gtov_146_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random() + OVER_gtov_146_5_S[q]))
                            bayesian_gtov_166_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random() + OVER_gtov_166_5_S[q]))
                            bayesian_gtov_186_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random() + OVER_gtov_186_5_S[q]))
                            bayesian_gtov_201_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random() + OVER_gtov_201_5_S[q]))
                            bayesian_gtov_212_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random() + OVER_gtov_212_5_S[q]))
                            bayesian_gtov_226_5 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random() + OVER_gtov_226_5_S[q]))
                            bayesian_12 = np.cbrt((1 / 3) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q]))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if W == PROB_METRICS[1] and X == PROB_METRICS[2] and Y == PROB_METRICS[3] and Z == COMBINERS[5]:
                            bayesian_home_Win = np.cbrt(home_z_prob[q] * rdm.random() * _1HWS[q])
                            bayesian_away_Win = np.cbrt(away_z_prob[q] * rdm.random() * _2AWS[q])
                            bayesian_etov_26_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * rdm.random() * OVER_etov_26_5_S[q])
                            bayesian_etov_33_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * rdm.random() * OVER_etov_33_5_S[q])
                            bayesian_etov_40_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * rdm.random() * OVER_etov_40_5_S[q])
                            bayesian_etov_46_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * rdm.random() * OVER_etov_46_5_S[q])
                            bayesian_etov_56_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * rdm.random() * OVER_etov_56_5_S[q])
                            bayesian_etov_22_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * rdm.random() * OVER_etov_22_5_S[q])
                            bayesian_etov_36_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * rdm.random() * OVER_etov_36_5_S[q])
                            bayesian_etov_49_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * rdm.random() * OVER_etov_49_5_S[q])
                            bayesian_gtov_146_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * rdm.random() * OVER_gtov_146_5_S[q])
                            bayesian_gtov_166_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * rdm.random() * OVER_gtov_166_5_S[q])
                            bayesian_gtov_186_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * rdm.random() * OVER_gtov_186_5_S[q])
                            bayesian_gtov_201_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * rdm.random() * OVER_gtov_201_5_S[q])
                            bayesian_gtov_212_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * rdm.random() * OVER_gtov_212_5_S[q])
                            bayesian_gtov_226_5 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * rdm.random() * OVER_gtov_226_5_S[q])
                            bayesian_12 = np.cbrt((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q])
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                    except IndexError:
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                           f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                           f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                           f"BAYESIAN {OUTCOMES[9]}|BAYESIAN {OUTCOMES[10]}|BAYESIAN {OUTCOMES[11]}|BAYESIAN {OUTCOMES[12]}|"
                                           f"BAYESIAN {OUTCOMES[13]}|BAYESIAN {OUTCOMES[14]}|BAYESIAN {OUTCOMES[15]}|BAYESIAN {OUTCOMES[16]}|"
                                           f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                            if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
                                                if bayesian_12_d[q] >= (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                    with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                        writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                        else:
                                            if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                                with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                    writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                    if W != PROB_METRICS[2] and X != PROB_METRICS[2] and Y != PROB_METRICS[2]:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{W}_{X}_{Y}/{Z}_{W}_{X}_{Y}_{sport}_10.txt", mode="a") as file:
                                                writer1(y=q, F=W, G=X, H=Y, J=Z, data=file)
                                    else:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (bayesian_home_Win_d[q] + bayesian_away_Win_d[q]) <= 1 and abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) >= (BAY_DIFF / 2) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q]:
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
                bayesian_etov_26_5_d = []
                bayesian_etov_33_5_d = []
                bayesian_etov_40_5_d = []
                bayesian_etov_46_5_d = []
                bayesian_etov_56_5_d = []
                bayesian_etov_22_5_d = []
                bayesian_etov_36_5_d = []
                bayesian_etov_49_5_d = []
                bayesian_gtov_146_5_d = []
                bayesian_gtov_166_5_d = []
                bayesian_gtov_186_5_d = []
                bayesian_gtov_201_5_d = []
                bayesian_gtov_212_5_d = []
                bayesian_gtov_226_5_d = []
                bayesian_12_d = []

                for q in range(len(home_teams)):
                    try:
                        if Z == COMBINERS[0]:
                            bayesian_home_Win = (1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))
                            bayesian_away_Win = (1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))
                            bayesian_etov_26_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random() + OVER_etov_26_5_S[q] + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))
                            bayesian_etov_33_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random() + OVER_etov_33_5_S[q] + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))
                            bayesian_etov_40_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random() + OVER_etov_40_5_S[q] + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))
                            bayesian_etov_46_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random() + OVER_etov_46_5_S[q] + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))
                            bayesian_etov_56_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random() + OVER_etov_56_5_S[q] + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))
                            bayesian_etov_22_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random() + OVER_etov_22_5_S[q] + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))
                            bayesian_etov_36_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random() + OVER_etov_36_5_S[q] + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))
                            bayesian_etov_49_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random() + OVER_etov_49_5_S[q] + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))
                            bayesian_gtov_146_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random() + OVER_gtov_146_5_S[q] + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))
                            bayesian_gtov_166_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random() + OVER_gtov_166_5_S[q] + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))
                            bayesian_gtov_186_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random() + OVER_gtov_186_5_S[q] + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))
                            bayesian_gtov_201_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random() + OVER_gtov_201_5_S[q] + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))
                            bayesian_gtov_212_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random() + OVER_gtov_212_5_S[q] + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))
                            bayesian_gtov_226_5 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random() + OVER_gtov_226_5_S[q] + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))
                            bayesian_12 = (1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if Z == COMBINERS[1]:
                            bayesian_home_Win = home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))
                            bayesian_away_Win = away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))
                            bayesian_etov_26_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * rdm.random() * OVER_etov_26_5_S[q] * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))
                            bayesian_etov_33_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * rdm.random() * OVER_etov_33_5_S[q] * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))
                            bayesian_etov_40_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * rdm.random() * OVER_etov_40_5_S[q] * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))
                            bayesian_etov_46_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * rdm.random() * OVER_etov_46_5_S[q] * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))
                            bayesian_etov_56_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * rdm.random() * OVER_etov_56_5_S[q] * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))
                            bayesian_etov_22_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * rdm.random() * OVER_etov_22_5_S[q] * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))
                            bayesian_etov_36_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * rdm.random() * OVER_etov_36_5_S[q] * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))
                            bayesian_etov_49_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * rdm.random() * OVER_etov_49_5_S[q] * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))
                            bayesian_gtov_146_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * rdm.random() * OVER_gtov_146_5_S[q] * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))
                            bayesian_gtov_166_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * rdm.random() * OVER_gtov_166_5_S[q] * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))
                            bayesian_gtov_186_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * rdm.random() * OVER_gtov_186_5_S[q] * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))
                            bayesian_gtov_201_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * rdm.random() * OVER_gtov_201_5_S[q] * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))
                            bayesian_gtov_212_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * rdm.random() * OVER_gtov_212_5_S[q] * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))
                            bayesian_gtov_226_5 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * rdm.random() * OVER_gtov_226_5_S[q] * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))
                            bayesian_12 = (math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if Z == COMBINERS[6]:
                            bayesian_home_Win = ((1 / 4) * (home_z_prob[q] + rdm.random() + _1HWS[q] + ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q])))))) ** 0.25
                            bayesian_away_Win = ((1 / 4) * (away_z_prob[q] + rdm.random() + _2AWS[q] + ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q])))))) ** 0.25
                            bayesian_etov_26_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) + rdm.random() + OVER_etov_26_5_S[q] + ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q])))))) ** 0.25
                            bayesian_etov_33_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) + rdm.random() + OVER_etov_33_5_S[q] + ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q])))))) ** 0.25
                            bayesian_etov_40_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) + rdm.random() + OVER_etov_40_5_S[q] + ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q])))))) ** 0.25
                            bayesian_etov_46_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) + rdm.random() + OVER_etov_46_5_S[q] + ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q])))))) ** 0.25
                            bayesian_etov_56_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) + rdm.random() + OVER_etov_56_5_S[q] + ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q])))))) ** 0.25
                            bayesian_etov_22_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) + rdm.random() + OVER_etov_22_5_S[q] + ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q])))))) ** 0.25
                            bayesian_etov_36_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) + rdm.random() + OVER_etov_36_5_S[q] + ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q])))))) ** 0.25
                            bayesian_etov_49_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) + rdm.random() + OVER_etov_49_5_S[q] + ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q])))))) ** 0.25
                            bayesian_gtov_146_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) + rdm.random() + OVER_gtov_146_5_S[q] + ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q])))))) ** 0.25
                            bayesian_gtov_166_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) + rdm.random() + OVER_gtov_166_5_S[q] + ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q])))))) ** 0.25
                            bayesian_gtov_186_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) + rdm.random() + OVER_gtov_186_5_S[q] + ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q])))))) ** 0.25
                            bayesian_gtov_201_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) + rdm.random() + OVER_gtov_201_5_S[q] + ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q])))))) ** 0.25
                            bayesian_gtov_212_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) + rdm.random() + OVER_gtov_212_5_S[q] + ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q])))))) ** 0.25
                            bayesian_gtov_226_5 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) + rdm.random() + OVER_gtov_226_5_S[q] + ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q])))))) ** 0.25
                            bayesian_12 = ((1 / 4) * ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) + rdm.random() + _12S[q] + ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q])))))) ** 0.25
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                        if Z == COMBINERS[7]:
                            bayesian_home_Win = (home_z_prob[q] * rdm.random() * _1HWS[q] * ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) / ((prob_HWs[q] * (prob_HW_H_indps[q] * prob_AW_H_indps[q])) + ((1 - (prob_HW_H_indps[q] * prob_AW_H_indps[q])) * (1 - prob_HWs[q]))))) ** 0.25
                            bayesian_away_Win = (away_z_prob[q] * rdm.random() * _2AWS[q] * ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) / ((prob_AWs[q] * (prob_HW_A_indps[q] * prob_AW_A_indps[q])) + ((1 - (prob_HW_A_indps[q] * prob_AW_A_indps[q])) * (1 - prob_AWs[q]))))) ** 0.25
                            bayesian_etov_26_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_26_5s[q]))) * rdm.random() * OVER_etov_26_5_S[q] * ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) / ((prob_etov_26_5s[q] * (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) + ((1 - (prob_etov_26_5_H_indps[q] * prob_etov_26_5_A_indps[q])) * (1 - prob_etov_26_5s[q]))))) ** 0.25
                            bayesian_etov_33_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_33_5s[q]))) * rdm.random() * OVER_etov_33_5_S[q] * ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) / ((prob_etov_33_5s[q] * (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) + ((1 - (prob_etov_33_5_H_indps[q] * prob_etov_33_5_A_indps[q])) * (1 - prob_etov_33_5s[q]))))) ** 0.25
                            bayesian_etov_40_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_40_5s[q]))) * rdm.random() * OVER_etov_40_5_S[q] * ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) / ((prob_etov_40_5s[q] * (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) + ((1 - (prob_etov_40_5_H_indps[q] * prob_etov_40_5_A_indps[q])) * (1 - prob_etov_40_5s[q]))))) ** 0.25
                            bayesian_etov_46_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_46_5s[q]))) * rdm.random() * OVER_etov_46_5_S[q] * ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) / ((prob_etov_46_5s[q] * (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) + ((1 - (prob_etov_46_5_H_indps[q] * prob_etov_46_5_A_indps[q])) * (1 - prob_etov_46_5s[q]))))) ** 0.25
                            bayesian_etov_56_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_56_5s[q]))) * rdm.random() * OVER_etov_56_5_S[q] * ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) / ((prob_etov_56_5s[q] * (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) + ((1 - (prob_etov_56_5_H_indps[q] * prob_etov_56_5_A_indps[q])) * (1 - prob_etov_56_5s[q]))))) ** 0.25
                            bayesian_etov_22_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_22_5s[q]))) * rdm.random() * OVER_etov_22_5_S[q] * ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) / ((prob_etov_22_5s[q] * (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) + ((1 - (prob_etov_22_5_H_indps[q] * prob_etov_22_5_A_indps[q])) * (1 - prob_etov_22_5s[q]))))) ** 0.25
                            bayesian_etov_36_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_36_5s[q]))) * rdm.random() * OVER_etov_36_5_S[q] * ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) / ((prob_etov_36_5s[q] * (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) + ((1 - (prob_etov_36_5_H_indps[q] * prob_etov_36_5_A_indps[q])) * (1 - prob_etov_36_5s[q]))))) ** 0.25
                            bayesian_etov_49_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_etov_49_5s[q]))) * rdm.random() * OVER_etov_49_5_S[q] * ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) / ((prob_etov_49_5s[q] * (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) + ((1 - (prob_etov_49_5_H_indps[q] * prob_etov_49_5_A_indps[q])) * (1 - prob_etov_49_5s[q]))))) ** 0.25
                            bayesian_gtov_146_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_146_5s[q]))) * rdm.random() * OVER_gtov_146_5_S[q] * ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) / ((prob_gtov_146_5s[q] * (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) + ((1 - (prob_gtov_146_5_H_indps[q] * prob_gtov_146_5_A_indps[q])) * (1 - prob_gtov_146_5s[q]))))) ** 0.25
                            bayesian_gtov_166_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_166_5s[q]))) * rdm.random() * OVER_gtov_166_5_S[q] * ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) / ((prob_gtov_166_5s[q] * (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) + ((1 - (prob_gtov_166_5_H_indps[q] * prob_gtov_166_5_A_indps[q])) * (1 - prob_gtov_166_5s[q]))))) ** 0.25
                            bayesian_gtov_186_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_186_5s[q]))) * rdm.random() * OVER_gtov_186_5_S[q] * ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) / ((prob_gtov_186_5s[q] * (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) + ((1 - (prob_gtov_186_5_H_indps[q] * prob_gtov_186_5_A_indps[q])) * (1 - prob_gtov_186_5s[q]))))) ** 0.25
                            bayesian_gtov_201_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_201_5s[q]))) * rdm.random() * OVER_gtov_201_5_S[q] * ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) / ((prob_gtov_201_5s[q] * (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) + ((1 - (prob_gtov_201_5_H_indps[q] * prob_gtov_201_5_A_indps[q])) * (1 - prob_gtov_201_5s[q]))))) ** 0.25
                            bayesian_gtov_212_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_212_5s[q]))) * rdm.random() * OVER_gtov_212_5_S[q] * ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) / ((prob_gtov_212_5s[q] * (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) + ((1 - (prob_gtov_212_5_H_indps[q] * prob_gtov_212_5_A_indps[q])) * (1 - prob_gtov_212_5s[q]))))) ** 0.25
                            bayesian_gtov_226_5 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_gtov_226_5s[q]))) * rdm.random() * OVER_gtov_226_5_S[q] * ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) / ((prob_gtov_226_5s[q] * (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) + ((1 - (prob_gtov_226_5_H_indps[q] * prob_gtov_226_5_A_indps[q])) * (1 - prob_gtov_226_5s[q]))))) ** 0.25
                            bayesian_12 = ((math.sqrt(0.5 * (diff_z_prob[q] + prob_12s[q]))) * rdm.random() * _12S[q] * ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) / ((prob_12s[q] * (prob_12_H_indps[q] * prob_12_A_indps[q])) + ((1 - (prob_12_H_indps[q] * prob_12_A_indps[q])) * (1 - prob_12s[q]))))) ** 0.25
                            baye_appender(baye_HW=bayesian_home_Win, baye_AW=bayesian_away_Win,
                                          baye_etov_26_5=bayesian_etov_26_5, baye_etov_33_5=bayesian_etov_33_5,
                                          baye_etov_40_5=bayesian_etov_40_5, baye_etov_46_5=bayesian_etov_46_5,
                                          baye_etov_56_5=bayesian_etov_56_5,
                                          baye_etov_22_5=bayesian_etov_22_5, baye_etov_36_5=bayesian_etov_36_5,
                                          baye_etov_49_5=bayesian_etov_49_5, baye_gtov_146_5=bayesian_gtov_146_5,
                                          baye_gtov_166_5=bayesian_gtov_166_5,
                                          baye_gtov_186_5=bayesian_gtov_186_5, baye_gtov_201_5=bayesian_gtov_201_5,
                                          baye_gtov_212_5=bayesian_gtov_212_5, baye_gtov_226_5=bayesian_gtov_226_5,
                                          baye_12=bayesian_12)

                    except IndexError:
                        continue

                for q in range(len(bayesian_home_Win_d)):
                    if q == 0:
                        for i in range(11):
                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_{i}.txt", mode="a") as file:
                                file.write(f"CONFIDENCE INTERVAL - {CONFINTVL}~COUNTRIES|LEAGUES|HOME TEAMS|AWAY TEAMS|HOME POSITIONS|AWAY POSITIONS|HOME NMP|AWAY NMP|"
                                           f"HOME PTS|AWAY PTS|HW FORM|HD FORM|HL FORM|AW FORM|AD FORM|AL FORM|HT_GAVG|AT_GAVG|BTH_GAVG|BTA_GAVG|BAYESIAN {OUTCOMES[0]}|"
                                           f"BAYESIAN {OUTCOMES[1]}|BAYESIAN {OUTCOMES[2]}|BAYESIAN {OUTCOMES[3]}|BAYESIAN {OUTCOMES[4]}|"
                                           f"BAYESIAN {OUTCOMES[5]}|BAYESIAN {OUTCOMES[6]}|BAYESIAN {OUTCOMES[7]}|BAYESIAN {OUTCOMES[8]}|"
                                           f"BAYESIAN {OUTCOMES[9]}|BAYESIAN {OUTCOMES[10]}|BAYESIAN {OUTCOMES[11]}|BAYESIAN {OUTCOMES[12]}|"
                                           f"BAYESIAN {OUTCOMES[13]}|BAYESIAN {OUTCOMES[14]}|BAYESIAN {OUTCOMES[15]}|BAYESIAN {OUTCOMES[16]}|"
                                           f"MATCH TIME|SPORT|DIRECTORY|MATCH DATE\n")
                    try:
                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_D[q] == 0 and a_form_D[q] == 0:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_0.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if ((home_positions[q] <= POS_MARK < away_positions[q]) or (away_positions[q] <= POS_MARK < home_positions[q])) and (home_positions[q] > 0 and away_positions[q] > 0):
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_1.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] < a_form_W[q] and h_form_L[q] > a_form_L[q] and h_form_D[q] > a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_2.txt", mode="a") as file:
                                            writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if ((h_form_L[q] + h_form_D[q] >= FORM_VALUE and h_form_L[q] > h_form_D[q]) and (a_form_W[q] + a_form_D[q] >= FORM_VALUE and a_form_W[q] > a_form_D[q])) or ((a_form_L[q] + a_form_D[q] >= FORM_VALUE and a_form_L[q] > a_form_D[q]) and (h_form_W[q] + h_form_D[q] >= FORM_VALUE and h_form_W[q] > h_form_D[q])):
                                if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_3.txt", mode="a") as file:
                                            writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                if h_form_D[q] == 0 or a_form_D[q] == 0:
                                    if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_4.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] > a_form_W[q] and h_form_L[q] < a_form_L[q] and h_form_D[q] < a_form_D[q] and abs(h_form_W[q] - a_form_W[q]) > FORM_DIFF:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                        with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_5.txt", mode="a") as file:
                                            writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if bayesian_home_Win_d[q] > bayesian_away_Win_d[q] and ht_g_avgs[q] > at_g_avgs[q] and bth_g_avgs[q] > bta_g_avgs[q] and home_positions[q] < away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_6.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_7.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] == 1.0 or a_form_W[q] == 1.0:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_8.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if bayesian_home_Win_d[q] < bayesian_away_Win_d[q] and ht_g_avgs[q] < at_g_avgs[q] and bth_g_avgs[q] < bta_g_avgs[q] and home_positions[q] > away_positions[q] and abs(home_positions[q] - away_positions[q]) >= POS_DIFF:
                                    if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                        if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and (BAY_DIFF / 2) <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= (0.5 * bayesian_12_d[q]) and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
                                            with open(f"../RESULTS - {Z}_{V}_{W}_{X}_{Y}/{Z}_{V}_{W}_{X}_{Y}_{sport}_9.txt", mode="a") as file:
                                                writer2(z=q, K=V, L=W, M=X, N=Y, P=Z, data=file)

                        if bayesian_etov_33_5_d[q] > CONFINTVL or bayesian_etov_40_5_d[q] > CONFINTVL or bayesian_etov_46_5_d[q] > CONFINTVL or \
                                bayesian_etov_56_5_d[q] > CONFINTVL or bayesian_etov_36_5_d[q] > CONFINTVL or \
                                bayesian_etov_49_5_d[q] > CONFINTVL or bayesian_gtov_146_5_d[q] > CONFINTVL or bayesian_gtov_166_5_d[q] > CONFINTVL or \
                                bayesian_gtov_186_5_d[q] > CONFINTVL or bayesian_gtov_201_5_d[q] > CONFINTVL or bayesian_gtov_212_5_d[q] > CONFINTVL or \
                                bayesian_gtov_226_5_d[q] > CONFINTVL:
                            if home_nums_matches_played[q] >= NMP and away_nums_matches_played[q] >= NMP:
                                if h_form_W[q] >= FORM_VALUE or a_form_W[q] >= FORM_VALUE:
                                    if bayesian_gtov_226_5_d[q] <= bayesian_gtov_212_5_d[q] <= bayesian_gtov_201_5_d[q] <= bayesian_gtov_186_5_d[q] <= bayesian_gtov_166_5_d[q] <= bayesian_gtov_146_5_d[q] and BAY_DIFF <= abs(bayesian_home_Win_d[q] - bayesian_away_Win_d[q]) <= bayesian_12_d[q] and bayesian_etov_22_5_d[q] >= bayesian_etov_26_5_d[q] >= bayesian_etov_33_5_d[q] >= bayesian_etov_36_5_d[q] >= bayesian_etov_40_5_d[q] >= bayesian_etov_46_5_d[q] >= bayesian_etov_49_5_d[q] >= bayesian_etov_56_5_d[q] and bayesian_12_d[q] >= CONFINTVLS[-1]:
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
                           f"prob_HWs = {prob_HWs}\nprob_AWs = {prob_AWs}\n"
                           f"prob_etov_26_5s = {prob_etov_26_5s}\nprob_etov_33_5s = {prob_etov_33_5s}\n"
                           f"prob_etov_40_5s = {prob_etov_40_5s}\nprob_etov_46_5s = {prob_etov_46_5s}\n"
                           f"prob_etov_56_5s = {prob_etov_56_5s}\nprob_etov_22_5s = {prob_etov_22_5s}\n"
                           f"prob_etov_36_5s = {prob_etov_36_5s}\nprob_etov_49_5s = {prob_etov_49_5s}\n"
                           f"prob_gtov_146_5s = {prob_gtov_146_5s}\nprob_gtov_166_5s = {prob_gtov_166_5s}\n"
                           f"prob_gtov_186_5s = {prob_gtov_186_5s}\nprob_gtov_201_5s = {prob_gtov_201_5s}\n"
                           f"prob_gtov_212_5s = {prob_gtov_212_5s}\nprob_gtov_226_5s = {prob_gtov_226_5s}\n"
                           f"prob_12s = {prob_12s}\n"
                           f"prob_HW_H_indps = {prob_HW_H_indps}\nprob_AW_H_indps = {prob_AW_H_indps}\n"
                           f"prob_etov_26_5_H_indps = {prob_etov_26_5_H_indps}\nprob_etov_33_5_H_indps = {prob_etov_33_5_H_indps}\n"
                           f"prob_etov_40_5_H_indps = {prob_etov_40_5_H_indps}\nprob_etov_46_5_H_indps = {prob_etov_46_5_H_indps}\n"
                           f"prob_etov_56_5_H_indps = {prob_etov_56_5_H_indps}\nprob_etov_22_5_H_indps = {prob_etov_22_5_H_indps}\n"
                           f"prob_etov_36_5_H_indps = {prob_etov_36_5_H_indps}\nprob_etov_49_5_H_indps = {prob_etov_49_5_H_indps}\n"
                           f"prob_gtov_146_5_H_indps = {prob_gtov_146_5_H_indps}\nprob_gtov_166_5_H_indps = {prob_gtov_166_5_H_indps}\n"
                           f"prob_gtov_186_5_H_indps = {prob_gtov_186_5_H_indps}\nprob_gtov_201_5_H_indps = {prob_gtov_201_5_H_indps}\n"
                           f"prob_gtov_212_5_H_indps = {prob_gtov_212_5_H_indps}\nprob_gtov_226_5_H_indps = {prob_gtov_226_5_H_indps}\n"
                           f"prob_12_H_indps = {prob_12_H_indps}\n"
                           f"prob_HW_A_indps = {prob_HW_A_indps}\nprob_AW_A_indps = {prob_AW_A_indps}\n"
                           f"prob_etov_26_5_A_indps = {prob_etov_26_5_A_indps}\nprob_etov_33_5_A_indps = {prob_etov_33_5_A_indps}\n"
                           f"prob_etov_40_5_A_indps = {prob_etov_40_5_A_indps}\nprob_etov_46_5_A_indps = {prob_etov_46_5_A_indps}\n"
                           f"prob_etov_56_5_A_indps = {prob_etov_56_5_A_indps}\nprob_etov_22_5_A_indps = {prob_etov_22_5_A_indps}\n"
                           f"prob_etov_36_5_A_indps = {prob_etov_36_5_A_indps}\nprob_etov_49_5_A_indps = {prob_etov_49_5_A_indps}\n"
                           f"prob_gtov_146_5_A_indps = {prob_gtov_146_5_A_indps}\nprob_gtov_166_5_A_indps = {prob_gtov_166_5_A_indps}\n"
                           f"prob_gtov_186_5_A_indps = {prob_gtov_186_5_A_indps}\nprob_gtov_201_5_A_indps = {prob_gtov_201_5_A_indps}\n"
                           f"prob_gtov_212_5_A_indps = {prob_gtov_212_5_A_indps}\nprob_gtov_226_5_A_indps = {prob_gtov_226_5_A_indps}\n"
                           f"prob_12_A_indps = {prob_12_A_indps}\n"
                           f"home_z_prob = {home_z_prob}\naway_z_prob = {away_z_prob}\ndiff_z_prob = {diff_z_prob}\n"
                           f"sport = {sport}\n_1HWS = {_1HWS}\n_2AWS = {_2AWS}\n"
                           f"OVER_etov_26_5_S = {OVER_etov_26_5_S}\nOVER_etov_33_5_S = {OVER_etov_33_5_S}\nOVER_etov_40_5_S = {OVER_etov_40_5_S}\nOVER_etov_46_5_S = {OVER_etov_46_5_S}\n"
                           f"OVER_etov_56_5_S = {OVER_etov_56_5_S}\nOVER_etov_22_5_S = {OVER_etov_22_5_S}\nOVER_etov_36_5_S = {OVER_etov_36_5_S}\nOVER_etov_49_5_S = {OVER_etov_49_5_S}\n"
                           f"OVER_gtov_146_5_S = {OVER_gtov_146_5_S}\nOVER_gtov_166_5_S = {OVER_gtov_166_5_S}\n"
                           f"OVER_gtov_186_5_S = {OVER_gtov_186_5_S}\nOVER_gtov_201_5_S = {OVER_gtov_201_5_S}\nOVER_gtov_212_5_S = {OVER_gtov_212_5_S}\nOVER_gtov_226_5_S = {OVER_gtov_226_5_S}\n"
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
