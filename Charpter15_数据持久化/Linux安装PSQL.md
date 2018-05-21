1. 安装PSQL:  
[root@Fedora ~]# dnf install postgresql*

2. 初始化数据库:  
[root@Fedora ~]# postgresql-setup initdb

3. 重启并设置为开机启动:  
[root@Fedora ~]# systemctl restart postgresql  
[root@Fedora ~]# systemctl enable postgresql

4. 关闭防火墙:  
   [root@Fedora ~]# systemctl stop firewalld.service  
   [root@Fedora ~]# systemctl disable firewalld.service
5. 登录PSQL查看状态:  
   [root@Fedora ~]# su - postgres  
   -bash-4.3$ psql  
   postgres=# \du（查看角色）  
   postgres=# \l（查看所有数据库）  
   postgres=# \q（退出） -bash-4.3$

6. 创建角色（PSQL中的用户）与数据库实例:  
   [root@Fedora pgsql]# su - postgres  
   -bash-4.3$ createuser qytangdbuser（创建用户）  
   -bash-4.3$ createdb -e -O qytangdbuser qytangdb（创建数据库）  
   CREATE DATABASE qytangdb OWNER qytangdbuser;（拥有者qytangdbuser）
   -bash-4.3$

7. 修改用户密码:  
   -bash-4.3$ psql  
   postgres=# \password qytangdbuser（修改用户密码）  
   输入新的密码：  
   再次键入：  
   postgres=#

8. 修改远程连接设置:  
   ***postgresql.conf***  
   （/var/lib/pgsql/data/postgresql.conf）  
   修改： （注意去掉#）  
   listen_addresses = '*'  
   ***pg_hba.conf***
   （/var/lib/pgsql/data/pg_hba.conf）  
   添加： host all all 202.100.1.138/32 md5

9. 重启服务:  
[root@Fedora pgsql]# systemctl restart postgresql
10. 关闭防火墙:  
[root@Fedora pgsql]# systemctl stop firewalld.service

11.在其他服务器上连接:      
[root@Fedora DataBase]# psql -U qytangdbuser -d qytangdb -h
202.100.1.139  
用户 qytangdbuser 的口令：  
psql (9.4.6, 服务器 9.4.7)  
输入 "help" 来获取帮助信息.  
qytangdb=>




