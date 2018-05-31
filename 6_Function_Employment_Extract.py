import pandas as pd
import numpy as np
import json

def get_employment(cibil_analysis):
    cibil_analysis['number_of_employment'] = '0'
    for i in range(len(cibil_analysis)):
        if pd.isna(df.employment[i]) == False:
            cibil_analysis['number_of_employment'][i] = len(cibil_analysis.employment[i]) - \
                                                        len(cibil_analysis.employment[i].replace("{",""))

            if "[" in cibil_analysis.employment[i]:
                cibil_analysis.employment[i] = cibil_analysis.employment[i].replace('[', "")
                cibil_analysis.employment[i] = cibil_analysis.employment[i].replace(']', "")
            temp = json.loads(cibil_analysis.employment[i])
                for j in temp:
                    col = str(j) + "_"
                    if col in list(cibil_analysis):
                        cibil_analysis[col][i] = temp[j]
                    else:
                        cibil_analysis[col] = '-'
                        cibil_analysis[col][i] = temp[j]
    return cibil_analysis


