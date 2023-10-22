
import pandas as pd
import json
import os

path_dir = 'data/WatClaimCheck_dataset/'
json_files = [pos_json for pos_json in os.listdir(path_dir) if pos_json.endswith('.json')]



for index, js in enumerate(json_files):
    with open(os.path.join(path_dir, js)) as json_file:
        file_name = js.split('.')[0]
        json_text = json.load(json_file)
        globals()[f'{file_name}_df'] = pd.json_normalize(json_text, meta=['label'])[['metadata.claim','metadata.id','label.rating','label.original_rating']]
        globals()[f'{file_name}_df'].rename(columns = {'metadata.claim':'claim',
                     'metadata.id':'id',
                     'label.rating':'rating',
                     'label.original_rating':'original_rating'}, inplace = True)
