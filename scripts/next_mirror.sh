#!/bin/bash


DMN_IN_USE_COUNT=`ls -1 /etc/nginx/vhosts/_mirror-ordinary/3_in-use/ | wc -l`
DMN_IN_USE_OLD=`ls -1 /etc/nginx/vhosts/_mirror-ordinary/3_in-use/ | head -1`
DMN_NEW=`ls -1 /etc/nginx/vhosts/_mirror-ordinary/2_ready2prod/ | head -1`
STUB="/etc/nginx/vhosts/_mirror-ordinary/8_stub/"
IN_USE="/etc/nginx/vhosts/_mirror-ordinary/3_in-use/"
READY2PROD="/etc/nginx/vhosts/_mirror-ordinary/2_ready2prod/"
ANCHOR="/var/tmp/nginx/anchor_auto_change_mirror"

#---First_check
nginx -t

if [ $? -ne 0 ]; then
	exit 1
fi
#/


if [ ! -f "$ANCHOR" ]; then 
	#---If_didn't_have_mirror---
	if [ `ls -1 $READY2PROD | wc -l` -eq 0 ]; then
		echo "Not enough mirrors..."
		exit 1
	fi
	#/---If_didn't_have_mirror---

	#---in_use_to_stub---
	if [ -n "$DMN_IN_USE_OLD" ]; then 
		mv $IN_USE$DMN_IN_USE_OLD $STUB
		yes y | /etc/nginx/vhosts/_mirror-ordinary/update_other_stub
	fi
	#/---in_use_to_stub---

	#---new_to_in_use---
	if [ -n "$DMN_NEW" ]; then
		mv $READY2PROD$DMN_NEW $IN_USE
		yes y | /etc/nginx/vhosts/_mirror-ordinary/update_other_public
	fi
	#/---new_to_in_use---

	#---check_after_change---
	nginx -t

	if [ $? -ne 0 ]; then
		touch $ANCHOR
		exit 1
	fi
	#/---check_after_change---

	ansible-playbook /etc/ansible/playbook/rsync_fbpr01.yml

else
	ansible-playbook /etc/ansible/playbook/rsync_fbpr01.yml
	rm $ANCHOR
	echo "Anchor is remove"
fi
