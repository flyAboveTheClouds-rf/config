# install all the dots

cd && find ~/universe/config/ -type f -name '.*' -exec ln -sv {} \;

source ~/.zshrc

echo "Source ~/.zshrc: Done"

echo "--> All Your Dots are Installed"
