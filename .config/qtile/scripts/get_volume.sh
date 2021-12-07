#!/bin/sh

muted=$(pamixer --get-mute)

if [ $muted == true ]
then
	echo "[off]"
else
	volume=$(pamixer --get-volume-human)

	echo "[$volume]"
fi
