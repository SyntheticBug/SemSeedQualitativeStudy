import json
import os
import shutil
from operator import itemgetter
from matplotlib import pyplot as plt

source_directory = './FSE_SemSeed/benchmarks/js_benchmark_seeded_bugs'
destination_directory = './SelectedFiles'
file_names = os.listdir(source_directory)
similarities = []

for file_name in file_names:
  if not file_name.endswith('.json'):
     continue
  file = open(f'{source_directory}/{file_name}', 'r')

  loaded_file = file.read()
  loaded_json = json.loads(loaded_file)
  similarity = loaded_json['mean_similarity']
  similarities.append((similarity, file_name))

similarities = sorted(similarities, key=itemgetter(0))

unziped_similarities = [tup[0] for tup in similarities]

total = len(similarities)
group_size = total // 4
group_size


quartiles = []

index = 0
iteration = 0

while iteration < 4:
  if index + group_size > total:
    quartiles.append(similarities[index:total])
  else:
    quartiles.append(similarities[index:index+group_size])
  index = index + group_size
  iteration = iteration + 1

difference = total % group_size
quartiles[3] += (similarities[index:index+difference])
print(quartiles[3])

import random
selected = []
for quartil in quartiles:
  selected.append(random.choice(quartil))
  

quarter = 1
for selected_tuple in selected:
    jsonfile = selected_tuple[1]
    shutil.copyfile(f'{source_directory}/{jsonfile}', f'{destination_directory}/{quarter}{jsonfile}')
    jsfile = jsonfile.replace('.json', f'.js')
    shutil.copyfile(f'{source_directory}/{jsfile}', f'{destination_directory}/{quarter}{jsfile}')
    quarter = quarter + 1