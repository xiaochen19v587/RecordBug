#! /bin/bash

bagpath="/home/user/Data/Test_Bag"

if [ ! -d "$bagpath" ];
then
mkdir -p $bagpath
fi

cp $1 $bagpath
gnome-terminal --tab -e 'bash -c "bash ~/Data/Test_Bag/record_bag.sh '$2' '$3';exec bash"'