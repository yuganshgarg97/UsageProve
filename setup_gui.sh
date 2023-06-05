sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-tk

# Install Python modules
pip3 install csv
pip3 install matplotlib
pip3 install numpy

# Install Matplotlib backend for non-GUI environments
sudo apt-get install -y xvfb
pip3 install pyvirtualdisplay
pip3 install EasyProcess
pip3 install xpyvirtualdisplay

