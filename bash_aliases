#!/bin/bash

# make listing files easier with ls
alias ls='ls -loFG'
alias cl='clear'
alias h=history
alias py=python
alias t='tree -FC -L 2'
alias t2='tree -FC -L 2'
alias t3='tree -FC -L 3'
alias t4='tree -FC -L 4'
alias t5='tree -FC -L 5'
alias t6='tree -FC -L 6'
alias t7='tree -FC -L 7'
alias t8='tree -FC -L 8'
alias wr='cat - >'
alias wra='cat - >>' 
alias cp='cp -i'
alias mv='mv -i'
alias c='cd ..'

# make a convenience alias of "cls" to clear screen before ls
alias cls='clear; ls -loFG'

# make find work like I expect it to.
#alias find='find . -name'
alias bloss='workon blossom; cd ~/dev/blossom/'
alias clsa='cls -a'
alias dot='cd ~/.dotfiles/; t2'
alias dev='cd ~/dev/; t2'
