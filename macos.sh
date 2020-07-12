# install OhMyZsh!
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# install HomeBrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# install tldr
brew install tldr

# install wget on mac
brew install wget

# install powerlevel10k theme
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/themes/powerlevel10k

echo "--> Remember to set your ZSH_THEME=\"powerlevel10k/powerlevel10k\" in ~/.zshrc"

# install anybar
brew cask install anybar

# install mactex ( for emacs org-mode pdf-exporting )
brew cask install mactex
# don't install basictex
