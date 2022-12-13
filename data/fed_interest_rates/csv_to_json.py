import csv
import json
import os
import pathlib

def main():
  dir = pathlib.Path(__file__).parent.resolve()

  csv_file_path = os.path.join(dir, 'fed_interest_rates.csv')
  rates = []
  with open(csv_file_path, 'r') as csv_fd:
    reader = csv.reader(csv_fd)
    for idx, row in enumerate(reader):
      # Skip header
      if idx == 0:
        continue

      [date, rate] = row
      rates.append({
        "date": date,
        "interest_rate": rate,
      })

  json_file_path = os.path.join(dir, 'fed_interest_rates.json')
  with open(json_file_path, 'w') as json_fd:
    json_fd.write(json.dumps(rates, indent=2))

if __name__ == '__main__':
  main()