import pandas as pd
import numpy as np
import json
import re


def email_domain(cibil_analysis):
    length = len(cibil_analysis)

    for i in length:
        if pd.isna(cibil_analysis.email[i]) == False:
            t = json.loads(cibil_analysis.email[i])
            t['domain'] = "gmail"
            for j in range(len(t)):
                temp = t[j].split("@")
                t['domain'][j] = temp[1]

    return cibil_analysis

#have to check if the emails are in JSON format or string in the source file