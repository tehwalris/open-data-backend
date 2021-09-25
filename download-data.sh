#! /usr/bin/env bash

mkdir -p data/air_quality
mkdir -p data/random_facts

for year in {1983..2021}; do
  wget "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte/download/ugz_ogd_air_h1_${year}.csv" -O "data/air_quality/${year}.csv"
done

wget "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005/download/BEV100OD1005.csv" -O "data/random_facts/data.csv"