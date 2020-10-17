
# https://jaebradley.github.io/basketball_reference_web_scraper/api/
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import Outcome, OutputType, TEAM_TO_TEAM_ABBREVIATION
import pandas as pd
import datetime as dt

def get_full_season_scores(year):
	'''
	creates a dictionary mapping dates to a list of dictionaries representing box scores for games played on that date
	'''
	months = {"mar": 3, "feb":2, "jan":1, "aprl":4, "may":5, "june": 6, "sept": 9, "oct":10, "nov":11, "dec":12, "july":7, "aug":8}
	games = {}
	for date in months.keys():
		m_num = months[date]
		for i in range(1, 32):
			if m_num < 10: # season starts in October, goes to April of opposite year
				value = client.team_box_scores(day=i, month=m_num, year=year)
			else:
				value = client.team_box_scores(day=i, month=m_num, year=year-1)
			if value != []:
				name = date+str(i)
				games[name] = value
	return games


def get_season_schedule(year):
	'''
	[{'start_time': datetime.datetime(), 'home_team', 'away_team', 'home_team_score', 'away_team_score'}]
	'''
	return client.season_schedule(season_end_year=year)


def find_csv_data(schedule, boxscores):
	'''
	maps schedule and box score data into a list of lists 
	list of lists puts games and boxscore on the same line 
	to export to csv
	'''
	full_data = []
	num_to_month = {3:"mar", 2:"feb", 1:"jan", 4:"aprl", 5:"may", 6:"june", 9:"sept", 10:"oct", 11:"nov", 12:"dec", 7:"july", 8:"aug"}
	for games in schedule:
		info = []
		home_stats = []
		away_stats = []
		starttime = games['start_time']
		year = starttime.year
		month = starttime.month
		day = starttime.day
		home = games['home_team']
		away = games['away_team']
		v = num_to_month[month]+str(day)
		try:
			boxscore = boxscores[v]
		except:
			boxscore = None
		if boxscore != None:
			for b in boxscore: #dictionary
				if b['team'] == home:
					if b['outcome'] == Outcome.WIN:
						home_stats.append(1)
					else:
						home_stats.append(0)
					home_stats.append(b['made_field_goals'])
					home_stats.append(b['attempted_field_goals'])
					home_stats.append(b['made_three_point_field_goals'])
					home_stats.append(b['attempted_three_point_field_goals'])
					home_stats.append(b['made_free_throws'])
					home_stats.append(b['attempted_free_throws'])
					home_stats.append(b['offensive_rebounds'])
					home_stats.append(b['defensive_rebounds'])
					home_stats.append(b['assists'])
					home_stats.append(b['steals'])
					home_stats.append(b['blocks'])
					home_stats.append(b['turnovers'])
					home_stats.append(b['personal_fouls'])
				if b['team'] == away:
					if b['outcome'] == Outcome.WIN:
						away_stats.append(1)
					else:
						away_stats.append(0)
					away_stats.append(b['made_field_goals'])
					away_stats.append(b['attempted_field_goals'])
					away_stats.append(b['made_three_point_field_goals'])
					away_stats.append(b['attempted_three_point_field_goals'])
					away_stats.append(b['made_free_throws'])
					away_stats.append(b['attempted_free_throws'])
					away_stats.append(b['offensive_rebounds'])
					away_stats.append(b['defensive_rebounds'])
					away_stats.append(b['assists'])
					away_stats.append(b['steals'])
					away_stats.append(b['blocks'])
					away_stats.append(b['turnovers'])
					away_stats.append(b['personal_fouls'])
			if home_stats != [] and away_stats != []:
				info.append(year)
				info.append(month)
				info.append(day)
				info.append(TEAM_TO_TEAM_ABBREVIATION[home])
				info.append(TEAM_TO_TEAM_ABBREVIATION[away])
				info.append(games['home_team_score'])
				info.append(games['away_team_score'])
				info.extend(home_stats)
				info.extend(away_stats)
				full_data.append(info)
	return full_data

# get 2019-20 season schedule in a csv
schedule = get_season_schedule(2020)
season = get_full_season_scores(2020)
info = find_csv_data(schedule, season)
df = pd.DataFrame(info)
df.to_csv('2019_20_full_data.csv')


# get 2018-19 data
season19 = get_full_season_scores(2019)
schedule19 = get_season_schedule(2019)
info = find_csv_data(schedule19, season19)
df = pd.DataFrame(info)
df.to_csv('2018_19_full_data.csv')

