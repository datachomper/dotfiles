Installation
-----------

	git clone git://github.com/datachomper/dotfiles.git

Vim plugins are installed as git submodules and need to be initialized. See :
http://vimcasts.org/episodes/synchronizing-plugins-with-git-submodules-and-pathogen/

	git submodule init
	git submodule update	

Passwords
--------
	.muttrc: Modify imap_pass


Vim Specific
------------
Plugins that are published on github can be installed as submodules. To install one:
	git submodule add https://github.com/tpope/vim-fugitive.git .vim/bundle/fugitive

This will update the .gitmodules file and checkout the git repo into the .vim/bundle/fugitive directory. Don't forget to commit the changes.
