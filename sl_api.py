"""This script will requests for the subway services information on Stockholm Commuter Traffic
Another script will control some LED strips that light up for every train present at a station traveling in a certain direction.

There are two different ways of collecting this information:
1. Scraping the website 'https://api.sl.se/fordonspositioner#{tunnelbanelinje}' and only selecting the stations where there are subways present
  - The stations have to be mapped to an LED and lit up individually
  - This approach is perhaps slightly slower and less stable
  - It is unknown whether it is allowed to access this site very frequently

2.
  - Get an API-key for the site 'trafiklab' and use their API to access the real-time information on all 100+ stations
  - This method requires an API access at every station approx every minute. This increases traffic significantly and the number of API accesses might be limited. 
"""

import json
import requests
from datetime import datetime

api_key = '' # Use for accessing the SL_API


def get_api_json_siteid():
    """Makes a request to the SL api with a key and collects information about every trains location."""
    req = requests.get(f'{api_url}+{api_key}+{timewindow}+')
    ans = req.text
    json_info = ans
    return json_info
# 

#

#

#

#

#

# Return the api in JSON format


# Other script:
# if __name__ == '__main__':
#    
# while True:
#     get_api_json()
