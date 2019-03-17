# dotfiles

Personal dotfiles for Arch Linux.

## Included Configuration

* [bspwm](https://github.com/baskerville/bspwm)
* [sxhkd](https://github.com/baskerville/sxhkd)
* [dunst](https://github.com/dunst-project/dunst)
* [mpd](https://www.musicpd.org/)
* [Neovim](https://neovim.io/)
* [npm](https://www.npmjs.com/)
* [Polybar](https://github.com/jaagr/polybar)
* [Rofi](https://github.com/DaveDavenport/rofi)
* [Termite](https://github.com/thestinger/termite)
* [Zsh](http://www.zsh.org/)
* SSH Agent Service (systemd)
* Font Configuration
	* [Croscore Fonts](https://github.com/google/fonts)
	* [Noto Fonts](https://github.com/googlei18n/noto-fonts)
	* [Cherry Bitmap Font](https://github.com/turquoise-hexagon/cherry)
	* [Siji Bitmap Icon Font](https://github.com/stark/siji)
* GTK+ 3 Theme
	* [Arc Darker Theme](https://github.com/horst3180/arc-theme)
	* [Paper Mono Dark Icons](https://github.com/snwh/paper-icon-theme)

## Installation

All dotfiles are managed using a [Git bare repository](https://developer.atlassian.com/blog/2016/02/best-way-to-store-dotfiles-git-bare-repo/).

1. Clone the repository.
```
git clone --bare https://github.com/Netflux/dotfiles.git $HOME/.cfg
```

2. Define the `config` alias.
```
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
```

3. Checkout the repository files to `$HOME`.
```
config checkout
```

4. **(Optional)** Hide all untracked files for the repository.
```
config config --local status.showUntrackedFiles no
```

## Configuration

To auto-run applications and scripts, create `~/.autostart.sh`:
```
#! /bin/sh

feh --bg-center <PATH-TO-IMAGE>
```
