#! /bin/bash

source $1/devel/setup.bash
bagpath="/home/user/Data/Test_Bag"
cd $bagpath

if [ $2 == '127.0.0.1' ];
then
    adb pull /data/zros/res/car_instance/default.xml $bagpath
    pull_res=$?
else
    timeout 5 scp root@$2:/data/zros/res/car_instance/default.xml $bagpath
    pull_res=$?
fi

if [ ${pull_res} == 0 ]
then
    date=$(date "+%Y-%m-%d")
    echo $date

    xmlfile="/home/user/Data/Test_Bag/default.xml"
    if [ ! -f "$xmlfile" ];
    then
        echo "Please Check Communication!"
    else
        carname=$(echo $(cat $xmlfile | awk  -v FS="<car_instance>" '{print $2}' | awk -v FS="</car_instance>" '{print $1}') | awk '{gsub(/ /,"")}1')
        echo $bagpath/$date/$carname
        if [ ! -d "$bagpath/$date/$carname" ];
        then 
            mkdir -p $bagpath/$date/$carname
        fi
        cd $bagpath/$date/$carname
        rosbag record -a
    fi
fi
