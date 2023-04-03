- Adding the repo file to /etc/yum.repos.d/
- Add the EPEL9 repo
- Add the copr pypi repo: "dnf copr enable @copr/PyPI"
- Add the codeready repo on RHEL9 (not on other EL9s) codeready-builder-for-rhel-9-x86_64-rpms
- Install software: dnf install -y awx-rpm postgresql-server nginx sccg
- Create selfsigned cert:
```
sscg -q                                                             \
     --cert-file           /etc/pki/tls/certs/localhost.crt         \
     --cert-key-file       /etc/pki/tls/private/localhost.key       \
     --ca-file             /etc/pki/tls/certs/localhost.crt         \
     --lifetime            365                                      \
     --hostname            $HOSTNAME                                    \
     --email               root@$HOSTNAME
```
- Firewalld config:
```
firewall-cmd --permanent --add-port=8013/tcp
firewall-cmd --permanent --add-port=8043/tcp
firewall-cmd --reload
```
- SELinux config
```
semanage port -a -t http_port_t -p tcp 8013
semanage port -a -t http_port_t -p tcp 8043
setsebool -P nis_enabled 1
setsebool -P httpd_can_network_connect 1
```
- Init database: /usr/bin/postgresql-setup --initdb
- Start the database: systemctl start postgresql
- Start nginx: systemctl start nginx
- Initiate database schema: 
```
su - awx
awx-manage migrate
awx-manage createsuperuser --noinput --username=admin --email=email@example.org
awx-manage update_password --username=admin --password=password
exit
```
- List services and start them: "systemctl list-unit-files |grep awx"
