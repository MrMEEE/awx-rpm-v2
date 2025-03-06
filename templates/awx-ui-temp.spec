%global python3_pkgversion ¤PYTHON3PKGVERSION¤

%define  debug_package %{nil}
%define _prefix /opt/awx-rpm
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user awx
%define service_group awx
%define service_homedir /var/lib/tower
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

Summary: Ansible AWX-RPM Web UI
Name: awx-ui
Version: ¤VERSION¤
Release: 1%{dist}
Source0: awx-¤VERSION¤.tar.gz
Source1: settings.py-%{version}
Source2: awx-receiver.service-%{version}
Source3: awx-dispatcher.service-%{version}
Source4: awx-wsrelay.service-%{version}
Source5: awx-ws-heartbeat.service-%{version}
Source6: awx-daphne.service-%{version}
Source7: awx-web.service-%{version}
Source20: awx-receptor.service-%{version}
Source21: awx-receptor-hop.service-%{version}
Source22: awx-receptor-worker.service-%{version}
Source23: awx.target-%{version}
Source30: receptor.conf-%{version}
Source31: receptor-hop.conf-%{version}
Source32: receptor-worker.conf-%{version}
Source40: awx-rpm-logo.svg-%{version}
Source8: awx-rpm-nginx.conf-%{version}
License: GPLv3
Group: AWX
URL: https://awx.wiki
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: awx-core vim python%{python3_pkgversion}-pyparsing
BuildRequires: make python%{python3_pkgversion} python%{python3_pkgversion}-devel nodejs npm gettext git python%{python3_pkgversion}-build rsync libpq libpq-devel 
¤BUILDREQUIRES¤

Requires: python%{python3_pkgversion} python%{python3_pkgversion}-pyparsing nodejs >= 18 npm gettext git nginx redis xmlsec1-openssl xmlsec1 podman sscg awx-receptor libpq 

%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx
git checkout -f devel
git checkout -f %{version}

%build

%install
mkdir translations/
mv awx/locale/en-us/LC_MESSAGES/django.po translations/
#mv awx/ui/src/locales/en/messages.po translations/

echo 'node-options="--openssl-legacy-provider"' >> awx/ui/.npmrc
GIT_BRANCH=%{version} VERSION=%{version} python%{python3_pkgversion} -m build -s
#make ui-next/src
#cp %{_sourcedir}/awx-rpm-logo.svg-%{version} awx/ui_next/src/frontend/awx/main/awx-rpm-logo.svg
#sed -i "s/awx-logo.svg/awx-rpm-logo.svg/g" awx/ui_next/src/frontend/awx/main/AwxMasthead.tsx
make ui

mkdir -p %{buildroot}/var/log/tower

mkdir -p %{buildroot}/opt/awx-rpm

#pushd %{buildroot}/opt/awx-rpm

DJANGO_SETTINGS_MODULE=awx.settings.defaults SKIP_SECRET_KEY_CHECK=yes SKIP_PG_VERSION_CHECK=yes awx-manage collectstatic --noinput --clear

#popd

#chmod +x tools/scripts/l18n/post_translation.sh
#./tools/scripts/l18n/post_translation.sh



#mkdir -p %{buildroot}%{_prefix}
#for i in `find -type f |grep mappings.wasm`; do
#	echo "Removing $i"
#	rm -f $i
#done

#popd

#rsync -avr awx/ $RPM_BUILD_ROOT/opt/awx-rpm/awx/
cp -a /var/lib/awx/public %{buildroot}/opt/awx-rpm/
mkdir -p %{buildroot}/opt/awx-rpm/public/static/
cp -a awx/ui/public/static/media %{buildroot}/opt/awx-rpm/public/static/
cp -a awx/ui/build/awx %{buildroot}/opt/awx-rpm/public/static/

#mkdir -p $RPM_BUILD_ROOT/var/lib/awx/rsyslog
#mkdir -p $RPM_BUILD_ROOT/var/lib/awx/projects
#mkdir -p $RPM_BUILD_ROOT/var/lib/awx/job_status

# Collect django static
#mkdir -p /var/log/tower/
#mkdir -p %{buildroot}%{service_homedir}
#mkdir -p %{buildroot}%{service_logdir}
#mkdir -p %{buildroot}%{_prefix}/bin
#mkdir -p %{buildroot}%{service_configdir}
#echo %{version} > %{buildroot}%{service_homedir}/.tower_version

#cp %{_sourcedir}/settings.py-%{version} %{buildroot}%{service_configdir}/settings.py
#mkdir -p %{buildroot}%{_prefix}/public
#rsync -avr /var/lib/awx/public/ %{buildroot}%{_prefix}/public/


%clean

%files
%defattr(0644, awx, awx, 0755)
%attr(0755, awx, awx) %{_prefix}
#/var/lib/awx/public
#%{service_homedir}/.tower_version

%changelog
* ¤DATE¤ Martin Juhl <m@rtinjuhl.dk> ¤VERSION¤
- New version build: ¤VERSION¤
¤CHANGELOG¤
