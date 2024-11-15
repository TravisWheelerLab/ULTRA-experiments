import json
import os
import torch
import sys
class Repeat:
    def __init__(self, data):
        self.sequence_name = data.get("SequenceName")
        self.start = data.get("Start")
        self.length = data.get("Length")
        self.period = data.get("Period")
        self.score = data.get("Score")
        self.substitutions = data.get("Substitutions")
        self.insertions = data.get("Insertions")
        self.deletions = data.get("Deletions")
        self.consensus = data.get("Consensus")
        self.sequence = data.get("Sequence")
        self.sub_repeats = [SubRepeat(sr) for sr in data.get("SubRepeats", [])]

class SubRepeat:
    def __init__(self, data):
        self.start = data.get("Start")
        self.end = float(data.get("End"))
        self.score = data.get("Score")
        self.consensus = data.get("Consensus")


# Base directory - replace with your actual base directory path
base_dir = '.'

# Function to process each JSON file
def process_json_file(file_path):

    with open(file_path, 'r') as file:
        data = json.load(file)
        repeats = [Repeat(repeat_data) for repeat_data in data["Repeats"]]
   # print(len(repeats))
    if len(repeats) != 1:
        return 1, 0
    #print(len(repeats[0].sub_repeats))
    if len(repeats[0].sub_repeats) != 2:
        return 1, 0


    return 0, repeats[0].sub_repeats[0].end
# Mean
# Std Dev
# Number missed
periods = [[[0.0, 0.0, 0, 0] for _ in range(501)] for _ in range(11)]

for period in range(1, 11):
    period_dir = os.path.join(base_dir, f'Period_{period}')

    # Iterate through Sub directories
    for sub in range(501):
        sub_rate = "{:.3f}".format(0.001 * sub)
        sub_dir = os.path.join(period_dir, f'Sub_{sub_rate}')

        # Check if the sub directory exists
        if os.path.exists(sub_dir):
            missed = 0
            mostly_missed = 0
            splits = []

            for file in os.listdir(sub_dir):
                #print(file)
                if file.endswith('.json'):
                    file_path = os.path.join(sub_dir, file)
                    m, s = process_json_file(file_path)
                    missed += m
                    mostly_missed += m
                    if m == 0:
                        splits.append(float(s))
                        if abs(s - 500) > 10:
                            mostly_missed += 1
                    #print(m, s)
            splits = torch.tensor(splits)
            periods[period][sub][0] = float(torch.mean(splits))
            periods[period][sub][1] = float(torch.mean(torch.abs(500.0 - splits)))
            periods[period][sub][2] = missed / 5000.0
            periods[period][sub][3] = mostly_missed / 5000.0
        else:
            print(f"Sub directory does not exist: {sub_dir}")

print("1\t2\t3\t4\t5\t6\t7\t8\t9\t10")
for i in range(501):
    s = '\t'.join([str(periods[j][i][3]) for j in range(1, 11)])
    print(s)


