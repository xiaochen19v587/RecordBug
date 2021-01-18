#! /bin/bash

bagpath="/home/user/Data/Test_Bag"

if [ ! -d "$bagpath" ];
then
mkdir -p $bagpath
fi

cp $1 $bagpath

gnome-terminal  --window -e 'bash -c "source '$2' '$3';exec bash"' \
--tab -e 'bash -c "sleep 5s;bash ~/Data/Test_Bag/record_bag.sh '$3' '$4';exec bash"'

