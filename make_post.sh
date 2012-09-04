read -p 'Title: ' TITLE
DATE=`date +%F`
TIME=`date +%R`
FTITLE=$(echo "$TITLE" | sed -e 's/ /_/g')
FILE=blog-src/$DATE-$FTITLE.rst

echo "$TITLE
###############################################################################

:date: $DATE $TIME
:author:
:category:
:tags:

" > $FILE

nano $FILE

