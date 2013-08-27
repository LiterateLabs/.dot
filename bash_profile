#!/bin/bash

# THIS_SCRIPT=$(/usr/bin/readlink "$0") 
# echo "This script: $THIS_SCRIPT" 

# echo 'configuring from ~/.bash_profile'

set -o vi

# System-wide .bashrc file for interactive bash(1) shells.
if [ -z "$PS1" ]; then
   return
fi

#HISTCONTROL=ignoreboth
export HISTCONTROL=erasedups
export HISTSIZE=1000

#PS1='\h:\W \u\$ '
# Make bash check its window size after a process completes
shopt -s checkwinsize

# custom prompt
PROMPT_HOSTNAME=$(hostname|cut -f1 -d.)
#PROMPT_HOSTNAME='MBP' 
PROMPT_COLOR='0;36m'

# If I am root, set the prompt to bright red
if [ ${UID} -eq 0 ]; then
PROMPT_COLOR='1;31m't
fi

PS1='\[\e]1;${PROMPT_HOSTNAME}\a\e]2;${PROMPT_HOSTNAME}:${PWD}\a\
\e[${PROMPT_COLOR}\]\
[\u@${PROMPT_HOSTNAME} \w]\n \#\$ \
\[\e[m\]'

#PS1="\e[0;45m\w:$ "

# The line below should be changed to change the PATH only if it is not already
# correct.
export PATH="/usr/local/share/npm/bin:/usr/local/bin:/usr/local/sbin:$PATH:$HOME/suborg/bin:$HOME/bin"

export PROMPT_COMMAND=''
export PIP_DOWNLOAD_CACHE=$HOME/Library/Caches/pip-downloads

# added by Jon on 2011/09/12 in order to have vim work as default editor
export EDITOR='vim'

export DOC_DRIVEN_HOME="$HOME/suborg"
export JAVA_HOME=`/usr/libexec/java_home -v 1.7`

#Custon colors for use with ls command
export LSCOLORS=Gxfxcxdxbxegedabagacad

# added by Jon on 2012/09/25 in order to get the python virtualenvwrapper working correctly.
export WORKON_HOME=$HOME/dev/vpe
export PROJECT_HOME=$HOME/dev/
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
source /usr/local/share/python/virtualenvwrapper.sh

[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*
[[ -s /Users/Jon/.nvm/nvm.sh ]] && . /Users/Jon/.nvm/nvm.sh # This loads NVM

if [ -f ~/.bash_profile_local ]; then
. ~/.bash_profile_local
fi

if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi

echo '--- PATH ---'
echo $PATH
echo '--- ---- ---'

