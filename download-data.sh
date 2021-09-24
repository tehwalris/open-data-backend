#! /usr/bin/env bash

mkdir -p data/air_quality

for year in {1983..2021}; do
  wget "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte/download/ugz_ogd_air_h1_${year}.csv" -O "data/air_quality/${year}.csv"
done