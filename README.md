# dotfiles

Personal dotfiles for Arch Linux.

## Installation

All dotfiles are managed using a [Git bare repository](https://www.atlassian.com/git/tutorials/dotfiles).

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

