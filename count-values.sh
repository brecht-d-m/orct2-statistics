#! /bin/bash

output_file="orct2_statistics.csv"
current_dir=$(pwd)
cd $1

sep=","

header="commit"$sep"timestamp"$sep"count_global"$sep"count_address"$sep"count_call"
echo $header > $current_dir"/"$output_file

total=$(git rev-list --count develop)
count=1

for commit in $(git rev-list develop)
do
    echo -ne $count"/"$total"\r"
    count=$(echo $count+1 | bc)

    commit_timestamp=$(git show -s --format=%ci $commit)
    header=$commit$sep$commit_timestamp
    counts=$(git grep -h -c RCT2_GLOBAL $commit | numsum)$sep$(git grep -h -c RCT2_ADDRESS $commit | numsum)$sep$(git grep -h -c RCT2_CALL $commit | numsum)
    echo $header$sep$counts >> $current_dir"/"$output_file
done

cd $current_dir

python3 plot_statistics_orct2.py

sed -i "$ d" $output_file