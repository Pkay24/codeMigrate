import numpy as np
import pandas as pd
import json

def get_live_accounts(cibil_analysis):
    count_hl = []
    count_cc = []

    for i in range(len(cibil_analysis.accounts)):
        if pd.isna(cibil_analysis.accounts[i]) == False:
            temp_json = json.loads(cibil_analysis.accounts[i])
            for j in temp_json:
                if 'closed_date' in j.keys():
                    if pd.isna(j['closed_date']):
                        temp_json2 = temp_json
                else:
                    temp_json2 = temp_json

            if (len(temp_json2))>0:
                if ('house' in df.accounts[i].lower() or 'home' in df.accounts[i].lower()
                        or 'property' in df.accounts[i].lower()):
                    count_hl.append(i)
                else:
                    count_hl.append(0)

                if ('credit card' in df.accounts[i].lower()):
                    count_cc.append(i)
                else:
                    count_cc.append(0)

    cibil_analysis['prod_live_hl'] = '0'
    cibil_analysis['prod_live_cc'] = '0'
    for k in count_hl:
        if k != 0:
            cibil_analysis['prod_live_hl'][k] = 1

    for l in count_cc:
        if l != 0:
            cibil_analysis['prod_live_cc'][l] = 1

    return cibil_analysis 

    