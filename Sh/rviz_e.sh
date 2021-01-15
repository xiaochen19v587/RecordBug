#!/bin/bash
#######################################################################
# File Name: mini_loc.sh
# Author: ma6174
# mail: ma6174@163.com
# Created Time: 2019年04月05日 星期五 11时30分24秒
#########################################################################


# source /home/adama/catkin_ws/devel/setup.bash
source $1/devel/setup.bash

echo 'source OK'

adb forward tcp:8888 tcp:8888
adb forward tcp:8889 tcp:8889
adb forward tcp:8890 tcp:8890
adb forward tcp:8891 tcp:8891
adb forward tcp:8892 tcp:8892
adb forward tcp:8893 tcp:8893
adb forward tcp:8894 tcp:8894
adb forward tcp:8895 tcp:8895
adb forward tcp:8896 tcp:8896
adb forward tcp:8897 tcp:8897
adb forward tcp:8898 tcp:8898
adb forward tcp:8899 tcp:8899
adb forward tcp:8900 tcp:8900
adb forward tcp:8901 tcp:8901
adb forward tcp:8902 tcp:8902
adb forward tcp:8903 tcp:8903
adb forward tcp:8904 tcp:8904
adb forward tcp:8905 tcp:8905
adb forward tcp:8906 tcp:8906
adb forward tcp:8907 tcp:8907
adb forward tcp:8908 tcp:8908
adb forward tcp:8909 tcp:8909
adb forward tcp:8910 tcp:8910
adb forward tcp:8911 tcp:8911
adb forward tcp:8912 tcp:8912
adb forward tcp:8913 tcp:8913
adb forward tcp:8914 tcp:8914
adb forward tcp:8915 tcp:8915
adb forward tcp:8916 tcp:8916
adb forward tcp:8917 tcp:8917
adb forward tcp:8918 tcp:8918
adb forward tcp:8919 tcp:8919
adb forward tcp:8920 tcp:8920
adb forward tcp:8921 tcp:8921
adb forward tcp:8922 tcp:8922
adb forward tcp:8923 tcp:8923
adb forward tcp:8924 tcp:8924
 
 
echo '11111111111111111111111111111111111111111111111'
roslaunch zros_dbg localization.launch 
echo '22222222222222222222222222222222222222222222222'

