#!/bin/bash

# Base directory
base_dir="."

# Create Period directories with underscores instead of spaces
for period in {1,2,3,4,5,6,7,8,9,10}; do
    echo "Creating period $period"
    period_dir="$base_dir/Period_$period"
    mkdir -p "$period_dir"

    # Create Sub directories within each Period directory with uniformly distributed rates
    for sub in {0..500}; do
        sub_rate=$(printf "%.3f" $(echo "$sub * 0.001" | bc))
        echo "     Creating subrate $sub_rate"
        sub_dir="$period_dir/Sub_$sub_rate"
        mkdir -p "$sub_dir"

        python3 make_split.py "$period" "$sub_rate" "$sub_dir/" 5000
    done
done

# Analyze Period directories
for period in {1,2,3,4,5,6,7,8,9,10}; do
    period_dir="$base_dir/Period_$period"
    echo "Analyzing $period"

    for sub in {0..500}; do
        sub_rate=$(printf "%.3f" $(echo "$sub * 0.001" | bc))
        sub_dir="$period_dir/Sub_$sub_rate"
        #mkdir -p "$sub_dir"
        echo "     Analyzing subrate $sub_rate"

        for iteration in {0..4999}; do
            ultra --min_split_window 15 --decay 1.0 -p $period --nr 0.9 --rn 0.00000001 --maxsplit 11 -i 0 -d 0 --json --hs -o "$sub_dir/$iteration.json" "$sub_dir/$iteration.fa"
        done
    done
done