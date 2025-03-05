%global python3_pkgversion ¤PYTHON3PKGVERSION¤

%define  debug_package %{nil}
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user awx
%define service_group awx
%define service_homedir /var/lib/tower
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

Summary: Ansible AWX core libraries
Name: awx-core
Version: ¤VERSION¤
Release: 1%{dist}
Source0: awx-¤VERSION¤.tar.gz
#Patch0: awx-patch.patch-%{version}
#Patch1: awx-rpm-extract-strings.patch-%{version}
#Patch2: awx-rpm-branding.patch-%{version}
License: GPLv3
Group: AWX
URL: https://awx.wiki
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: make python%{python3_pkgversion} python%{python3_pkgversion}-devel git python%{python3_pkgversion}-build libpq libpq-devel
¤BUILDREQUIRES¤

Requires: python%{python3_pkgversion} gettext xmlsec1-openssl xmlsec1 libpq
¤REQUIRES¤

%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx
git checkout -f devel
git checkout -f %{version}
#%patch0 -p0
#%patch1 -p0
#%patch2 -p0

%build

%install
mkdir -p %{buildroot}/var/log/tower
make sdist && pip%{python3_pkgversion} install --root=%{buildroot}/ dist/awx.tar.gz

sed -i "s|/builddir.*.x86_64||g" $RPM_BUILD_ROOT/usr/bin/awx-manage
pushd %{buildroot}/usr/lib/python%{python3_pkgversion}/site-packages/
for i in `find -type f`; do
       sed -i "s|/builddir.*.x86_64||g" $i
done

find . -name "*.pyc" -exec rm -f {} \;

popd

mkdir -p $RPM_BUILD_ROOT/var/lib/awx/rsyslog
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/projects
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/job_status

mkdir -p /var/log/tower/

mkdir -p %{buildroot}/usr/lib/systemd/system

sed -i "s/supervisor_service_command(command='restart', service='awx-rsyslogd')//g" $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/awx/main/utils/external_logging.py

rm -rf $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/awx/ui/public
ln -s /opt/awx-rpm/awx-ui/awx/ $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/awx/ui/public
cd $RPM_BUILD_ROOT/usr/lib/python%{python3_pkgversion}/site-packages/awx/ui/
ln -s public build

%clean

%files
%defattr(0644, awx, awx, 0755)
%attr(0755, root, root) /usr/bin/awx-manage
%attr(0755, root, root) /usr/lib/python%{python3_pkgversion}/site-packages/awx*
%attr(0755, awx, awx) /var/log/tower
#%attr(0755, awx, awx) %{_prefix}
#%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
#%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
#%{service_homedir}/.tower_version
#%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
#%config(noreplace) %{service_configdir}/settings.py
#%config /etc/nginx/conf.d/awx-rpm.conf
#/usr/lib/systemd/system/awx.target
#/etc/receptor
#/usr/bin/ansible-tower-service
#/usr/bin/ansible-tower-setup
#/usr/bin/awx-python
#/usr/bin/failure-event-handler
#/usr/share/awx
#/usr/share/sosreport/sos/plugins/tower.py
#/var/lib/awx/favicon.ico
#/var/lib/awx/wsgi.py
#/var/lib/awx/rsyslog
#/var/lib/awx/projects
#/var/lib/awx/job_status

%changelog
* ¤DATE¤ Martin Juhl <m@rtinjuhl.dk> ¤VERSION¤
- New version build: ¤VERSION¤
¤CHANGELOG¤
