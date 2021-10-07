{ pkgs ? import <nixpkgs> {} }:
with pkgs;
let
  my-python-packages = python-packages: with python-packages; [
    numpy
    pandas
    matplotlib
    tqdm
    scipy
    scikitlearn
    jupyterlab
    seaborn
    fastapi
    uvicorn
    black
  ];
in 
  mkShell {
    nativeBuildInputs = [
      nodejs
      yarn
      (python3.withPackages my-python-packages)
    ];
  }
