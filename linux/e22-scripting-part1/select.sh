#!/bin/bash


PS3="Choose a toolname:"

select toolname in wireshark nmap tshark gobuster hashcat:
do
	echo "you have seleceted $toolname"
	if [ $toolname = "nmap" ]
	then
		echo "runnning nmap scan"
		nmap -F 12.3.12.3
	if
		:wq
done
