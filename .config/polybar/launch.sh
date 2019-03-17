#!/bin/bash

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar
WIRED_NETWORK_INTERFACE=$(ls /sys/class/net | grep "^en.*$") \
WIRELESS_NETWORK_INTERFACE=$(ls /sys/class/net | grep "^wl.*$") \
polybar topbar -r &

echo "Polybar launched..."
