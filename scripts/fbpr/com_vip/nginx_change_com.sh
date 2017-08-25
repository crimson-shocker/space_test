#!/bin/bash


DMN_IN_USE_COUNT=`ls -1 /etc/nginx/vhosts/_mirro-com/3_in-use/ | wc -l`
DMN_IN_USE_OLD=`ls -1 /etc/nginx/vhosts/_mirror-com/3_in-use/ | head -1`
DMN_NEW=`ls -1 /etc/nginx/vhosts/_mirror-com/2_ready2prod/ | head -1`
DMN_TEST=`ls -1 /etc/nginx/vhosts/_mirror-com/1_test/ | head -1`
STUB="/etc/nginx/vhosts/_mirror-ordinary/8_stub/"
IN_TEST="/etc/nginx/vhosts/_mirror-ordinary/1_test/"
IN_USE="/etc/nginx/vhosts/_mirror-ordinary/3_in-use/"
READY2PROD="/etc/nginx/vhosts/_mirror-ordinary/2_ready2prod/"
DMN_IN_TRASH="/etc/nginx/vhosts/_mirror-ordinary/9_trash/"


#---First_check
echo "Check nginx conf...."
nginx -t &> /dev/null

if [ $? -ne 0 ]; then
	exit 1
else
	echo "Check Successful!"
fi
#/


#---In_Stub_to_TRASH----
if [ `ls -1 $STUB | wc -l` -ne 0 ]
	echo "Move_all_in_STUB_to_TRASH"
	mv $STUB* $DMN_IN_TRASH
else
	continue
fi
#/

#---in_use_to_stub---
if [ -n "$DMN_IN_USE_OLD" ]; then
	echo "Move_IN_USE2STUB..."
	mv $IN_USE$DMN_IN_USE_OLD $STUB
	yes y | /etc/nginx/vhosts/_mirror-ordinary/update_other_stub &> /dev/null
fi
#/

#---new_to_in_use---
if [ -n "$DMN_TEST" ]; then
	echo "Move_IN_TEST2IN_USE..."
	mv $IN_TEST$DMN_TEST $IN_USE
	yes y | /etc/nginx/vhosts/_mirror-ordinary/update_other_public &> /dev/null
fi
#/

#---ready_to_pro2test---
if [ -n $DMN_NEW ]; then
	echo "Move_Ready_to_prod2TEST..."
	mv $READY2PROD$DMN_NEW $IN_TEST
	yes y | /etc/nginx/vhosts/_mirror-ordinary/update_other_test &> /dev/null
fi
#/---ready_to_pro2test---


#---last_check---
echo "Check nginx conf...."
nginx -t &> /dev/null

if [ $? -ne 0 ]; then
	exit 1
else
	echo "Check Successful!"
fi
#/

#---stop&start---
echo "Nginx_Stop"
nginx -s stop &> /dev/null
echo "Nginx_Start"
nginx &> /dev/null
echo "PS AUX:"
ps aux | grep nginx
#/

echo "...-Old_Mirror: "$DMN_IN_USE_OLD
echo "...-Actual_Mirror: "$DMN_TEST
echo "...-Test_Mirror: "$DMN_NEW
