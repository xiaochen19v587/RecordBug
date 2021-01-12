#!/bin/bash

# 拉取文件
copy_file(){
  file_path="$1/"
  file_name=$2
  com_file_path=$3
  count=0
  file_arr=()
  for file in `ls ${file_path}`
  do
    file_arr[${count}]=${file}
    count=`expr ${count} + 1`
  done
  # 创建文件夹
  eval "mkdir ${com_file_path}${file_name}"
  # 拉取.tat.gz文件
  eval "scp -r ${file_path}${file_arr[1]} ${com_file_path}${file_name}"
  # 拉取sha256校验文件
  eval "scp -r ${file_path}${file_arr[2]} ${com_file_path}${file_name}"
  # 校验文件
  check_file  ${file_arr[1]} ${file_arr[2]} ${com_file_path}${file_name}
}


# 校验文件完整性
check_file(){
  tar_file=$1
  sha_file=$2
  file_path="$3/"
  # 进入本地文件路径
  eval "cd ${file_path}"
  # 开始校验
  eval "sha256sum -c <(grep ${tar_file} ${sha_file})"
  # 判断校验结果
  if [ "$?" == "0" ]    
  then
    echo "校验完成，文件完整."
    # 删除本地校验文件
    eval "rm ${file_path}${sha_file}"
  else
    echo "校验失败,请重新拉取."
  fi
}

# 获取ftp路径第二层文件信息
get_file_info(){
  # ftp文件目录
  ftp_file_path=$1
  com_file_path=$2
  ftp_file_arr=()
  count=0
  # 记录文件信息
  for file in `ls ${ftp_file_path}`
  do
    ftp_file_arr[${count}]=${file}
    count=`expr ${count} + 1`
  done
  # 找到最新的文件
  count=`expr ${count} - 1 `
  ftp_file_name=${ftp_file_arr[${count}]}
  ftp_file=${ftp_file_path}${ftp_file_name}
  # 拉取文件
  copy_file ${ftp_file} ${ftp_file_name} ${com_file_path}
}


# 获取ftp文件路径最新文件名
get_ftp_file_name(){
  ftp_file_path=$1
  ftp_file_arr=()
  count=0
  # 将文件名加入数组
  # 记录文件数量
  for file in `ls ${ftp_file_path}`
  do
    ftp_file_arr[${count}]=${file}
    count=`expr ${count} + 1`
  done
  # ftp最新文件索引
  file_index=`expr ${count} - 1`
  file=${ftp_file_arr[${file_index}]}
  echo ${file}
}


# 判断本地文件是否为最新
judge_file(){
  # 切片获取文件名中的日期
  ftp_file_name=$1
  com_file_path=$2
  count=0
  for file in `ls ${com_file_path}`
  do
      if [ ${file} == ${ftp_file_name} ]; then
          count=`expr ${count} + 1`
      else
          count=${count}
      fi
  done
  if [ ${count} -gt 0 ]; then
      echo "已经有最新的DailyBuild..."
  else
      get_file_info ${ftp_file_path} ${com_file_path}
  fi
}


main(){
  # 定义本地文件路径和ftp文件路径
  com_file_path=$1
  ftp_file_path="/run/user/1000/gvfs/smb-share:server=shfp07,share=smartecu/DailyBuild/B_DropnGo/zros_B_DropnGo_feature_mvp_dev/"
  # 判断ftp文件夹是否正确
  if `cd ${ftp_file_path}`
  then
    # 查看本地文件夹是否存在
    if `cd ${com_file_path}`
    then
      count=0
      for file in `ls ${com_file_path}`
      do
        count=`expr ${count} + 1`
      done
      # 判断本地文件夹中是否有原始文件
      if [ ${count} -gt 0 ]
      then
        # 如果有原始文件,将两个文件进行比较
        # 将两个函数返回的文件名传入judge_file函数进行比较
        judge_file `get_ftp_file_name ${ftp_file_path}` ${com_file_path}
      else 
        # 如果没有原始文件,直接拉取最新文件
        get_file_info ${ftp_file_path} ${com_file_path}
      fi
    else
      # 文件夹不存在，创建文件夹，直接拉取最新文件
      eval "mkdir ${com_file_path}"
      get_file_info ${ftp_file_path} ${com_file_path}
    fi
  else
    echo "连接服务器失败..."
  fi
}


main $1