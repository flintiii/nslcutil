#!/bin/bash
# nslcutil.py install support 
# 02/12/2016 09:38:04 AM flint
#
read -p "This script is not yet ready!!!..." ans
# echo "Make sure only root can run script"
if [ "$(id -u)" != "0" ]; then
   echo "This script needs to run as root and you are not root, sorry..." 1>&2
   exit 1
fi 
#
read -p "This gets odd packages..." ans
# get odd packages
apt-get update
apt-get install python-pip
sudo pip install openpyxl
sudo pip install docopt
#
read -p "This install 'sf.sh' which contains secrets..." ans
# Installs sf.sh which contains secrets...
# make repository
mkdir /root/bin
# move file to repository
scp flint@192.168.1.73:/home/flint/clients/goddard/sis/nslc/bin/sf.sh /root/bin/.
# set the permissions
# http://unix.stackexchange.com/questions/34202/can-a-script-be-executable-but-not-readable
sudo chmod 4755 /root/bin/sf.sh
#
read -p "This fixes comprogram variable in program..." ans
# fix comprogram variable in program.
sed -i 's/bin\/sf.sh/\/root\/bin\/sf.sh/1' nslcutil.py
# 
read -p "This will symlink program correctly..." ans
# symlink this to /usr/local/bin/
sudo ln -s ~flint/nslc/nslcutil/nslcutil.py /usr/local/bin/
sudo ln -s ~flint/nslc/nslcutil/nslcobjects.py   /usr/local/bin/
#
read -p "This tests program..." ans
# Test from /home/flint/nslc/nslcutil
nslcutil.py -f example.csv test.xlsx
scp test.xlsx flint@192.168.1.73:/home/flint/clients/goddard/sis/nslc/.
#
echo "All Done!!!"
