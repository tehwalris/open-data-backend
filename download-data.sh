#! /usr/bin/env bash

mkdir -p data/air_quality
for year in {1983..2021}; do
  wget "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte/download/ugz_ogd_air_h1_${year}.csv" -O "data/air_quality/${year}.csv"
done

mkdir -p data/random_facts
wget "https://data.stadt-zuerich.ch/dataset/prd_ssz_gang-dur-zueri_od1005/download/BEV100OD1005.csv" -O "data/random_facts/data.csv"

mkdir -p data/energy
wget "https://data.stadt-zuerich.ch/dataset/ewz_bruttolastgang_stadt_zuerich/download/2020_ewz_bruttolastgang.csv" -O "data/energy/data.csv"

mkdir -p data/dogs
wget "https://data.stadt-zuerich.ch/dataset/sid_stapo_hundebestand/download/20210301_hundehalter.csv" -O "data/dogs/data.csv"

mkdir -p data/search
wget "http://nlp.stanford.edu/data/glove.6B.zip" -O "data/search/glove.6B.csv"