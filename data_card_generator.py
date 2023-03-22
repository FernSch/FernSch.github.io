import statbotics
from PIL import Image, ImageFont, ImageDraw
import random
from datetime import datetime


#enter team num
team_num = 2056

year = datetime.now().strftime("%Y")
white = (255,255,255)
black = (0,0,0)
img = Image.open("template.png")
title_font = ImageFont.truetype('Europa Regular.ttf', 50)
small_font = ImageFont.truetype('Europa Regular.ttf', 25)


sb = statbotics.Statbotics()
try:
  data = sb.get_team(team_num)
except: 
  print("invalid team num")

name = data['name']
image_editable = ImageDraw.Draw(img)
image_editable.text((60, 35), name, white, font=title_font)
team_data = sb.get_team_year(team_num, int(year))
current_epa = team_data['epa_mean']
country_epa_rank = team_data['country_epa_rank']
win = team_data['winrate']


th = ["4","5","6","7","8","9","0"]
st = ["1"]
nd = ["2"]
rd = ["3"]
if str(country_epa_rank)[-1] in th:
  country_epa_rank = str(country_epa_rank) + "th"
elif str(country_epa_rank)[-1] in st:
  country_epa_rank = str(country_epa_rank) + "st"
elif str(country_epa_rank)[-1] in nd:
  country_epa_rank = str(country_epa_rank) + "nd"
elif str(country_epa_rank)[-1] in rd:
  country_epa_rank = str(country_epa_rank) + "rd"
  
  

image_editable.text((50,225), str(current_epa), black, font=small_font)

image_editable.text((50,365), str(country_epa_rank), black, font=small_font)

image_editable.text((50,520), str(win * 100) + "%", black, font=small_font)


img.save(f"{team_num}_data.png")
print("done")
