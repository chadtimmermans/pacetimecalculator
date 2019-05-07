#!/usr/bin/env bash
# -v and -e are xserver requirements for gui
# -u log in as user
# pacetimecalculator is image name
docker run -it --rm \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -e DISPLAY=$DISPLAY \
    -u user \
    pacetimecalculator
