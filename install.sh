# install all the dots

cd && find ~/universe/config/ -type f -name '.*' -exec ln -sv {} \;

echo "--> All Your Dots are Installed"
