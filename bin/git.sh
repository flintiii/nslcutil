#!/bin/bash
# 02/05/2016 03:21:21 PM flint
# makes commits easy
git add . && \
git add -u && \
git commit -m "$(read -p 'Commit description: ')" && \
echo "Committing to goddard Redmine:"
git push nslcutil
echo "Committing to Github:"
git push github
echo \"$1\"
exit
git push origin HEAD
git add .
git commit -m $1
git push nslcutil
git push github
