#!/bin/bash

STUDENTS_PATH=$HOME/students.txt
SCORE_PATH=$HOME/score.txt

# 死循环
while true
do
    echo '选择 1~4'

    read no
    case $no in
        1)
        # 清空用户名和密码, 单小于号是覆写
        echo -e "\c" > $STUDENTS_PATH
        # 开始输入
        index=1
        while (( $index<=5 ))
        do
            echo "请输入第 $index 位学生的用户名:"
            read username
            # 双小于号是续写
            echo $username >> $STUDENTS_PATH
            echo "请输入第 $index 位学生的密码:"
            read password
            echo $password >> $STUDENTS_PATH
            let "index++"
        done
        ;;
        2)
        # 判断 students.txt 文件是否存在
        if test ! -e $STUDENT_PATH
        then
            echo '没有学生用户, 退出'
            exit
        fi
        echo -e '\c' > $SCORE_PATH
        index=1
        while (( $index<=5 ))
        do
            echo "请输入第 $index 位学生的分数:"
            read score
            echo $score >> $SCORE_PATH
            let "index++"
        done
        ;;
        3)
        for score in $(cat $SCORE_PATH)
        do
            sum=`expr $sum + $score`
        done
        let "average=$sum/5"
        echo "5 个学生的平均分数: $average"
        ;;
        4)
        echo '退出程序'
        exit
        ;;
        *)
        echo '请重新输入'
        ;;
    esac
done


