Installation:

    git clone git://github.com/jononomo/.dotfiles.git ~/.dotfiles

Create symlinks:

    ln -s ~/.dotfiles/vim/vimrc ~/.vimrc
    ln -s ~/.dotfiles/vim/gvimrc ~/.gvimrc
    ln -s ~/.dotfiles/.vim/ ~/.vim

The `vim` directory is where vim will look for configuration options.  Vim usually
looks for a `.vim` directory in the $HOME directory, so we create a symlink from
`~/.vim/` to point to the `vim` directory that is within the `~/.dotfiles/`
directory.  Similar logic applies to the `.vimrc` and `.gvimrc` files.

The structure of the `vim` directory as of Tue Oct 23, 2012, is as follows:


/bin/bash: t2: command not found



The purpose of the autoload directory is to automatically load the vim plugin
*Pathogen*, which we'll then use to load all other plugins that are located in the
bundle directory. So download pathogen and put it in your autoload folder.


You'll need to add the following to your ~/.vimrc so that pathogen will be loaded
properly. Filetype detection must be off when you run the commands so its best to
execute them first:

filetype off
call pathogen#runtime_append_all_bundles()
call pathogen#helptags()

