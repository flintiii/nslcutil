#!/bin/bash
# 02/05/2016 03:21:21 PM flint
# makes commits easy
# 02/10/2016 08:52:59 AM added changes suggested in:
# SOURCE:http://stackoverflow.com/questions/8482843/git-commit-bash-script answer 5
git add . && \
git add -u && \
git commit --all && \
git commit -m "$(read -p 'Commit description: ')" && \
echo "Committing to goddard Redmine:"; git push nslcutil
echo "Committing to Github:";git push gitssl
echo \"$1\"
exit
