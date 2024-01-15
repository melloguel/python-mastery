{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-22.11") {} }:
  let python-packages = ps: with ps; [
    black
    mypy
  ];
  in
  pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
    	(python3.withPackages python-packages)
    ];
  }

