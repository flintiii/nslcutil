!#/bin/bash
pwd
read -p "you better be in the right directory...2git" ans
#
rm -rf example.tab
rm -rf nslcobjects.py
rm -rf example.xlsx
rm -rf example.csv
rm -rf nslcutil.py
#
echo "relinking..."
#
ln ../bin/nslcobjects.py
ln ../bin/nslcutil.py
ln ../example.tab
ln ../example.xlsx
ln ../example.csv

