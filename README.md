potential-meme
==============

Play with Spark_0.9.0 on VirtualBox(CentOS_6.5)!

This is a tutorial site for Apache Spark Project (https://spark.apache.org/) , practice and learn Spark using VirtualBox (https://www.virtualbox.org/wiki/Downloads), welcome to fork and pull-request it!

![Screenshot of "RunningSparkOnVBox(CentOS)"](https://raw.githubusercontent.com/yangboz/potential-meme/master/Spark_VBox_CentOS_Running.jpg)

Tips
==============

###0.1 Scala mirror download link: http://www.lookbackon.com/resources/spark/Scala-2.9.3.tgz
###0.2 JDK rpm mirror download link: http://www.lookbackon.com/resources/spark/jdk-7u5-linux-i586.rpm
###0.3 Spark-prebuild-0.9.0 download link: http://www.lookbackon.com/resources/spark/spark-0.9.0-incubating.tgz

###1.Port forward on VirtualBox SSH connection,see: http://www.virtualbox.org/manual/ch06.html

###2.Spark WebUI port(8080,8081) ACCEPT by "iptables", please using: 

iptables -I INPUT -p tcp -m tcp --dport 8080 -j ACCEPT
