#!/bin/bash

THIS_SCRIPT=$(/usr/bin/readlink "$0")
echo "This script: $THIS_SCRIPT"

echo 'configuring from ~/.bash_profile'

# System-wide .bashrc file for interactive bash(1) shells.
if [ -z "$PS1" ]; then
   return
fi

#PS1='\h:\W \u\$ '
# Make bash check its window size after a process completes
shopt -s checkwinsize

# ALL OF THE BELOW ADDED BY JON ON 2011-04-25quan

# custom prompt
PROMPT_HOSTNAME=$(hostname|cut -f1 -d.)
#PROMPT_HOSTNAME='MBP' 
PROMPT_COLOR='0;35m'

# If I am root, set the prompt to bright red
if [ ${UID} -eq 0 ]; then
PROMPT_COLOR='1;31m't
fi

PS1='\[\e]1;${PROMPT_HOSTNAME}\a\e]2;${PROMPT_HOSTNAME}:${PWD}\a\
\e[${PROMPT_COLOR}\]\
[\u@${PROMPT_HOSTNAME} \w]\n \#\$ \
\[\e[m\]'

#PS1="\e[0;45m\w:$ "

if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi

export PATH="/usr/local/share/python:/usr/local/bin:/usr/local/sbin:$PATH:$HOME/bin"
export PROMPT_COMMAND=''
export PIP_DOWNLOAD_CACHE=$HOME/Library/Caches/pip-downloads

# added by Jon on 2011/09/12 in order to have textmate work as default editor
export EDITOR='mate -w'

#Custon colors for use with ls command
export LSCOLORS=Gxfxcxdxbxegedabagacad

# added by Jon on 2012/09/25 in order to get the python virtualenvwrapper working correctly.
export WORKON_HOME=$HOME/dev/vpe
export PROJECT_HOME=$HOME/dev/
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
source /usr/local/share/python/virtualenvwrapper.sh

echo '--- PATH ---'
echo $PATH
echo '--- ---- ---'
