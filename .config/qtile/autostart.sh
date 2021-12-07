#!/bin/sh
feh --bg-scale '/home/netflux/.config/background.jpg' &
lxqt-policykit-agent &
xss-lock -- physlock -ms &
gnome-keyring-daemon --start
