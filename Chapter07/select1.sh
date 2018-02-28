#!/bin/bash
select ROUTER in R1 R2 R3 R4
do
     case $ROUTER in
     R1) echo "Hostname is R1, IP address is 10.1.1.1" ;;
     R2) echo "Hostname is R2, IP address is 10.2.2.2" ;;
     R3) echo "Hostname is R3, IP address is 10.3.3.3" ;;
     R4) echo "Hostname is R3, IP address is 10.4.4.4" ;;
     *)  echo "exit" && break ;;
     esac
     echo "please select "
done

