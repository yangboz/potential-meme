potential-meme
==============

Play with Spark_0.9.0 on VirtualBox(CentOS_6.5)!

This is a tutorial site for Apache Spark Project (https://spark.apache.org/) , practice and learn Spark using VirtualBox (https://www.virtualbox.org/wiki/Downloads), welcome to fork and pull-request it!

Tips
==============

###1.Port forward on VirtualBox SSH connection,see: http://www.virtualbox.org/manual/ch06.html

###2.Spark WebUI port(8080) ACCEPT by "iptables", please using: 

iptables -I INPUT -p tcp -m tcp --dport 80 -j ACCEPT
