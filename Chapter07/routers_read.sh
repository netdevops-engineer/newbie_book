#!/bin/bash

cat routers_infos.txt | while read LINE
do
   line=( $LINE )
   echo "hostname is ${line[0]}, IP address is ${line[1]}"
   echo "username is ${line[3]}, password is ${line[4]}"
done

