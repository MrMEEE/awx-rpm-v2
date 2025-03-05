%global python3_pkgversion ¤PYTHON3PKGVERSION¤
%define  debug_package %{nil}

%define service_user awx-rpm-hub
%define service_group awx-rpm-hub

Summary: AWX-RPM hub service
Name: awx-rpm-hub
Version: ¤VERSION¤
Release: 1%{dist}
Source0: galaxy-hub-%{version}.tar.gz
License: ASL2
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: Ansible
Prefix: %{_prefix}

%description
%{summary}

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp ./receptor $RPM_BUILD_ROOT/usr/bin/receptor%{python3_pkgversion}

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%clean

%files
%defattr(0644, receptor, receptor, 0755)
%attr(0755, receptor, receptor) /usr/bin/receptor%{python3_pkgversion}

%changelog
* ¤DATE¤ Martin Juhl <m@rtinjuhl.dk> $VERSION
- New version build: $VERSION
