zmodload zsh/zprof

# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install

# The following lines were added by compinstall
zstyle :compinstall filename '/home/netflux/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Alias for dotfiles repository management
alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
