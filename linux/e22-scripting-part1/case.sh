#!/bin/bash


read -p "enter a tool name : " toolname

case $toolname in
	"wireshark") echo "packet capture tool" ;;
	"nmap") echo "port scanner tool" ;;
	"john") echo "password cracker tool" ;;
	*) echo "no valid tools given" ll
esac
