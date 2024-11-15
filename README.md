# ULTRA-experiments

Source code for tools used in the paper can be found in `tools/`.
Results for the score distribution can be found in `results/repeat_dist`
Results for the repeat-splitting experiment can be found in `results/repeat_split`
Results for the coverage experiment can be found in `results/coverage.xlsx`

Each tool was run on fasta files containing individual sequences from genomes listed in the paper. To estimate false coverage, each tool was run on a shuffled version of genome sequences. Shuffling was performed using: 
`esl-shuffle -w 20000 --seed 42 -o output_seq.fa input_seq.fa`

Each genome/shuffled-genome was analyzed using ULTRA/tantan/TRF as described in the paper. The AT rich tantan score matrix can be found in tools/atmask.mat. The GC rich tantan score matrix can be found in tools/gcmask.mat
