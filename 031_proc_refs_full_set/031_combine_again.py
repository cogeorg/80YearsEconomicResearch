import os
import json
import pandas as pd

def open_json(filepath):
    with open(filepath) as json_data:
        d = json.load(json_data)
        json_data.close()
        return d    

temp=[]
folderpath='/folder to combine'
outfilename='outcomes_match_b_v2_full.json'
for i in os.listdir(folderpath):
    print(i)
    if (".py" in i) | ("full" in i):
        continue
    temp.append(pd.DataFrame(open_json(folderpath+'/'+i)))

outcome=pd.concat(temp, ignore_index=True).reset_index(drop=True)
print(outcome.shape)
print(outcome[['id_o','ref_ord']].drop_duplicates().shape)
with open(outfilename, 'w') as f:
    json.dump(outcome.to_dict(), f, indent=4)