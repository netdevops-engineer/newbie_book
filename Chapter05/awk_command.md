# 5.3.5 awk command example

```
$ awk -v ip_counter=0 \
      -v noip_counter=0 \
 '{if ($2 ~/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/) \
	{ip_counter++; print NR, $1, $2} \
	else if($2 ~/unassigned/) \
	{noip_counter++}}\
	END{print "ip inf counter: ",ip_counter; \
	print "no ip inf counter:", noip_counter  }' \
	if_info_ios.txt
```

output:

```
4 GigabitEthernet0/2 192.168.190.235
6 GigabitEthernet0/4 192.168.191.2
ip inf counter:  2
no ip inf counter: 10
```