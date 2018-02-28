#!/bin/bash
function checkIP() {
      declare -a ips
      for ((i=1; i<256; i++))
      do
          ips[$i]="10.1.1.$i"
      done
      for ip in ${ips[@]}
      do
          if [ "$1" = "$ip" ]; then
              return 0
          fi
      done
      return 1

}

checkIP $1

if [  $? -eq 0 ]; then
    echo "$1 is found"
else
    echo "$1 can't find"
fi

