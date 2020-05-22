#!/usr/bin/env sh

set -uex

rm -rvf ./*.zip
zip -r ./script.program.skype-launcher.zip ./script.program.skype-launcher 
zip -r ./script.program.zoom-launcher.zip ./script.program.zoom-launcher 

