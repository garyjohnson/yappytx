#!/usr/bin/env python3

import csv
import argparse
import subprocess
import os


def main():
    parser = argparse.ArgumentParser(description='Generates OpenTx voice pack from csv file, formatted <path>;<filename>;<spoken_text>')
    parser.add_argument('csv_file', type=str)
    parser.add_argument('output_path', type=str)

    args = parser.parse_args()

    with open(args.csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            print(row)
            path = os.path.join(args.output_path, row[0])
            print(path)
            os.makedirs(path, exist_ok=True)
            wav_file_path = os.path.join(path, row[1])
            print(wav_file_path)
            subprocess.call("say -o {} --data-format=LEF32@32000 \"{}\"".format(wav_file_path, row[2]), shell=True)

if __name__ == '__main__':
    main()
