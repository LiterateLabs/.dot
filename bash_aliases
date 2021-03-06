#!/bin/bash

alias so='cd ~/suborg; t'
alias neb='cd ~/dev/nebula1; t; deactivate; workon nebula1'

# make listing files easier with ls
alias u='underscore'
alias ls='ls -loFGh'
alias cl='clear'
alias h=history
alias py=python
alias t='tree -FC -L 1'
alias t2='tree -FC -L 2'
alias t3='tree -FC -L 3'
alias t4='tree -FC -L 4'
alias t5='tree -FC -L 5'
alias t6='tree -FC -L 6'
alias t7='tree -FC -L 7'
alias wr='cat - >'
alias wra='cat - >>' 
alias cp='cp -i'
alias mv='mv -i'
alias c='cd ..; t2'
alias pout='pandoc -V geometry:margin=0.8in -o Intermedia_Routes.pdf README.md'
alias dd='cd ~/dev/docdriven; t2; deactivate; workon docdriven'
alias int='iit; cd intermedia-branch'
alias dd_load='launchctl load /Users/Jon/Library/LaunchAgents/ddd.publisher.plist; launchctl load /Users/Jon/Library/LaunchAgents/ddd.runner.plist'
alias dd_unload='launchctl unload /Users/Jon/Library/LaunchAgents/ddd.publisher.plist; launchctl unload /Users/Jon/Library/LaunchAgents/ddd.runner.plist'
alias dd_start='launchctl start ddd.publisher; launchctl start ddd.runner'

# make a convenience alias of "cls" to clear screen before ls
alias cls='clear; ls -loFG'

# make find work like I expect it to.
#alias find='find . -name'
alias clsa='cls -a'
alias dot='cd ~/.dotfiles/; t2'
alias rebash='source ~/.bash_profile'
alias tt='deactivate; cd /usr/src/vcd/testing; source bin/activate; cd test_tools; clear; t2'
alias rmpyc='rm *.pyc'
alias s='git status'

alias make_cwautopro_soap_proxy='cd ~/dev/; deactivate; workon soap_tools; python -m soap_tools.cwautopro.generator interface2.mako > ~/dev/nebula1/cwautopro/soap_proxy.py'
alias make_cwmanager_soap_proxy='cd ~/dev/; deactivate; workon soap_tools; python -m soap_tools.cwmanager.generator interface3.mako > ~/dev/nebula1/cwmanager/soap_proxy.py'
alias vimalias='vim ~/.dotfiles/bash_aliases'
alias vimprofile='vim ~/.dotfiles/bash_profile'
alias vimvimrc='vim $DOT/vim/vimrc'

if [ -f ~/.bash_aliases_local ]; then
. ~/.bash_aliases_local
fi

alias interjson='iit; export PYTHONSTARTUP='\''./interjson.py'\''; python'
alias autoprojson='iit; export PYTHONSTARTUP='\''./autoprojson.py'\''; python'

alias sst='ssh -o ServerAliveInterval=10 5212b20d4382ecbdd100009b@tabs-literatelabs.rhcloud.com'
alias sshiit='ssh -o ServerAliveInterval=10 jon@216.224.141.220 -p 32547'
alias shmedia='ssh -o ServerAliveInterval=10 joncrowell.org@s101210.gridserver.com'
alias s='git status'
alias co='git checkout'
alias add='git add'

alias reindent='py ~/reindent.py'
alias rmpyc='rm *.pyc'
alias rvm-restart='rvm_reload_flag=1 source '\''/Users/Jon/.rvm/scripts/rvm'\'''
alias soapset='iit; cd cwautopro_soap; export PYTHONSTARTUP='\''/Users/Jon/dev/iit/cwautopro_soap/soap_setup.py'\''; python'
alias spy='iit; cd test-tools/npanel; export PYTHONSTARTUP='\''/Users/Jon/dev/iit/test-tools/npanel/s.py'\''; python'
alias sshiit='ssh -o ServerAliveInterval=10 jon@216.224.141.220 -p 32547'
alias clinp='workon clinp; cd ~/dev/clinp; clear; t'
alias pulltransfer='rsync -avzr --exclude-from "/Users/Jon/.dotfiles/rsync-exclude" --links --perms --progress --stats --delete -e "ssh -p 32547" jon@216.224.141.220:transfer/ ~/transfer/'
alias pushtransfer='rsync -avzr --exclude-from "/Users/Jon/.dotfiles/rsync-exclude" --links --perms --progress --stats --delete -e "ssh -p 32547" ~/transfer/ jon@216.224.141.220:transfer/'

alias pullnebula1='rsync -avzr --exclude-from "/Users/iit/.dotfiles/rsync-exclude" --links --perms --progress --stats --delete -e "ssh -p 32547" jon@216.224.141.220:dev/vcd/env/npanel/nebula1/ ~/dev/nebula1/'

alias pullsoaptools='rsync -avzr --exclude-from "/Users/iit/.dotfiles/rsync-exclude" --links --perms --progress --stats --delete -e "ssh -p 32547" jon@216.224.141.220:soap_tools/ ~/dev/soap_tools/'
alias pulltesttools='rsync -avzr --exclude-from "/Users/iit/.dotfiles/rsync-exclude" --links --perms --progress --stats --delete -e "ssh -p 32547" jon@216.224.141.220:test_tools/ ~/dev/test_tools/'
alias pullntest='rsync -avzr --exclude-from "/Users/iit/.dotfiles/rsync-exclude" --links --perms --progress --stats --delete -e "ssh -p 32547" jon@216.224.141.220:ntest/ ~/dev/ntest/'
