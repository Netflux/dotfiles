setterm --blank 10 --powerdown 15

if [[ $XDG_VTNR -eq 1 ]]; then
	setterm --blank 1 --powerdown 2
	startx
fi
