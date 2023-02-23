import runpy
from _rprocess_checker import is_running
from _rcleamser import cleanse
from _random_samplers import sampler_
import time
from _CONTROL_CENTER import set_date_s_size, game_criteria

start_time = time.time()
tmrw_date = set_date_s_size()[0]
sample_size = set_date_s_size()[1]

SPORTS = ['FLOORBALL.py', 'FIELD HOCKEY.py',
          'WATERPOLO.py', 'RUGBY LEAGUE.py',
          'RUGBY UNION.py', 'BASKETBALL.py',
          'HOCKEY.py', 'VOLLEYBALL.py', 'KABADDI.py']
for sport in SPORTS:
    runpy.run_path(path_name=sport)

if is_running(game_criteria()[13][0]) is False and is_running(game_criteria()[13][1]) is False:
    try:
        cleanse()
    except FileNotFoundError:
        pass
    sampler_(sample_size, tmrw_date)

end_time = time.time()
print(f"run speed: {end_time - start_time}s")
