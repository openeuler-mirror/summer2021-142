Graphene-1.2-rc1

介绍
编写了spec文件，用于将Graphene源码打包为rpm包。
rpm包中包括编译好的源码，可以直接安装使用。

安装教程
将源码包放置在rpmbuild/SOURCES，SPEC文件放置在rpmbuild/SPEC。
构建rpm包：
rpmbuild -ba graphene.spec
安装：
rpm -ivh (--nodevs)  graphene-1.2_rc1-1.x86_64.rpm

官方文档
https://graphene.readthedocs.io
