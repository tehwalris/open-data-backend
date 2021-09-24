{ pkgs ? import <nixpkgs> {} }:
with pkgs;
let
  my-python-packages = python-packages: with python-packages; [
    numpy
    pandas
    matplotlib
    tqdm
    scikitlearn
    jupyterlab
    seaborn
  ];
in 
  mkShell {
    nativeBuildInputs = [
      nodejs
      yarn
      (python3.withPackages my-python-packages)
    ];
  }
