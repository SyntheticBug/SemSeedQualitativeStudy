import json
import os

from operator import itemgetter
directory = 'js_benchmark_seeded_bugs'
file_names = os.listdir(directory)

similarities = []

for file_name in file_names:
  if not file_name.endswith('.json'):
     continue
  file = open(f'{directory}/{file_name}', 'r')

  loaded_file = file.read()
  loaded_json = json.loads(loaded_file)
  similarity = loaded_json['mean_similarity']
  similarities.append((similarity, file_name))

similarities = sorted(similarities, key=itemgetter(0))

from matplotlib import pyplot as plt

unziped_similarities = [tup[0] for tup in similarities]

plt.xlabel("Output files")
plt.ylabel("Similarity")
plt.title("Semseed's output files' Similarity")
plt.plot(unziped_similarities)

plt.show()

interval = 0.1

groupdisc = []
intervals = []
groups = []
i = 0
while i + interval <= 1.0:
  group = [cell for cell in similarities if (cell[0] >=i and cell[0] < i+interval)]
  groupdisc.append(group)
  intervals.append(f'[{round(i,1)}-{round(i+interval, 1)}]')
  groups.append(len(group))
  i = i + interval


lastgroup = [cell for cell in unziped_similarities if cell == 1]
intervals.append('[1]')
groups.append(len(lastgroup))
del groups[0:2]
del intervals[0:2]
groups

groupdisc[5]

figure, axes = plt.subplots(1,1, figsize=(10,6))
axes.bar(intervals, groups, width = 0.8)
axes.set_title("File output quantity by similarity range")
axes.set_ylabel("Quantity")
axes.set_xlabel("Similarity Ranges")

plt.show()