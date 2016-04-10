#!/bin/bash

if [ "$#" -lt 1 ]
then
	echo "Usage: `basename $0` <container-name>" >&2
	exit 1
fi
echo -e "\033[01;31mPlease note: Container will be removed once shell is terminated. /root folder is shared.\033[00m"
CMD='docker run -it --name="'$1'" -v /root:/root ipport'
echo $CMD
$CMD
echo -n "Removing docker container:"
docker rm "$1"
