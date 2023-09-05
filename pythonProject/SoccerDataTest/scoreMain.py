import soccerdata as sd
import json
#运行
def run():
   ws = sd.WhoScored(leagues="ENG-Premier League", seasons=2021)
   epl_schedule = ws.read_schedule()
   epl_schedule.head()
   events = ws.read_events(match_id=1485184, output_fmt="raw")
   print(json.dumps(events[1485184][0], indent=2))
   # events.head()
   # print(ws.__doc__)



if __name__ == '__main__':
    run()