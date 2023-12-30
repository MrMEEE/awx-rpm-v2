%define  debug_package %{nil}

%define service_user receptor
%define service_group receptor

Summary: Receptor service
Name: receptor
Version: ¤VERSION¤
Release: 1%{dist}
Source0: receptor-%{version}.tar.gz
License: ASL2
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: Ansible
Prefix: %{_prefix}

BuildRequires: golang make python3 python3-wheel git

%description
%{summary}

%prep
%setup

%build
make build-all

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp ./receptor $RPM_BUILD_ROOT/usr/bin/receptor

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%clean

%files
%defattr(0644, receptor, receptor, 0755)
%attr(0755, receptor, receptor) /usr/bin/receptor

%changelog
* Mon Feb 13 2023 22:55:34 +0000 Martin Juhl <m@rtinjuhl.dk> $VERSION
- New version build: $VERSION
