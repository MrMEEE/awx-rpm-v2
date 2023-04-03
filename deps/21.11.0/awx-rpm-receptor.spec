%define  debug_package %{nil}

%define service_user receptor
%define service_group receptor

Summary: Receptor service
Name: receptor
Version: 1.3.0
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
* Mon Aug 26 2019 19:27:25 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.315
- New Git version build: 6.1.0.315
* Mon Aug 26 2019 15:56:45 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.311
- New Git version build: 6.1.0.311
* Mon Aug 26 2019 13:57:07 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.308
- New Git version build: 6.1.0.308
* Fri Aug 23 2019 21:27:07 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.306
- New Git version build: 6.1.0.306
* Fri Aug 23 2019 20:27:20 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.300
- New Git version build: 6.1.0.300
* Fri Aug 23 2019 17:26:34 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.298
- New Git version build: 6.1.0.298
* Fri Aug 23 2019 16:56:39 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.296
- New Git version build: 6.1.0.296
* Fri Aug 23 2019 15:56:50 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.294
- New Git version build: 6.1.0.294
* Thu Aug 22 2019 22:27:12 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.292
- New Git version build: 6.1.0.292
* Thu Aug 22 2019 15:27:05 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.288
- New Git version build: 6.1.0.288
* Thu Aug 22 2019 14:26:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.284
- New Git version build: 6.1.0.284
* Wed Aug 21 2019 22:27:04 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.280
- New Git version build: 6.1.0.280
* Wed Aug 21 2019 16:57:08 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.277
- New Git version build: 6.1.0.277
* Tue Aug 20 2019 21:56:46 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.275
- New Git version build: 6.1.0.275
* Tue Aug 20 2019 19:27:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.273
- New Git version build: 6.1.0.273
* Tue Aug 20 2019 18:57:06 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.271
- New Git version build: 6.1.0.271
* Tue Aug 20 2019 16:56:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.265
- New Git version build: 6.1.0.265
* Mon Aug 19 2019 23:56:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.258
- New Git version build: 6.1.0.258
* Mon Aug 19 2019 21:27:47 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.256
- New Git version build: 6.1.0.256
* Mon Aug 19 2019 16:56:42 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.254
- New Git version build: 6.1.0.254
* Mon Aug 19 2019 14:57:17 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.252
- New Git version build: 6.1.0.252
* Mon Aug 19 2019 14:27:11 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.250
- New Git version build: 6.1.0.250
* Mon Aug 19 2019 13:27:26 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.248
- New Git version build: 6.1.0.248
* Fri Aug 16 2019 23:57:04 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.246
- New Git version build: 6.1.0.246
* Fri Aug 16 2019 22:27:04 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.244
- New Git version build: 6.1.0.244
* Fri Aug 16 2019 18:56:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.242
- New Git version build: 6.1.0.242
* Fri Aug 16 2019 17:56:41 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.240
- New Git version build: 6.1.0.240
* Fri Aug 16 2019 17:26:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.238
- New Git version build: 6.1.0.238
* Fri Aug 16 2019 16:57:14 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.236
- New Git version build: 6.1.0.236
* Thu Aug 15 2019 18:27:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.229
- New Git version build: 6.1.0.229
* Thu Aug 15 2019 16:26:37 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.225
- New Git version build: 6.1.0.225
* Thu Aug 15 2019 15:26:45 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.223
- New Git version build: 6.1.0.223
* Thu Aug 15 2019 14:57:00 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.221
- New Git version build: 6.1.0.221
* Thu Aug 15 2019 08:22:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 07:44:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 06:22:59 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 05:52:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 05:22:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 04:52:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 04:22:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 03:52:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 03:22:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 02:52:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 02:22:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 01:52:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 01:22:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 00:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 00:48:18 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Wed Aug 14 2019 23:52:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Wed Aug 14 2019 23:26:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
- New Git version build: 6.1.0.219
* Wed Aug 14 2019 22:52:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.215
* Wed Aug 14 2019 22:22:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.215
* Wed Aug 14 2019 22:13:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.215
* Wed Aug 14 2019 20:56:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.215
- New Git version build: 6.1.0.215
* Wed Aug 14 2019 20:27:00 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.213
- New Git version build: 6.1.0.213
* Wed Aug 14 2019 19:57:12 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.211
- New Git version build: 6.1.0.211
* Wed Aug 14 2019 19:22:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.205
* Wed Aug 14 2019 18:57:20 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.205
- New Git version build: 6.1.0.205
* Wed Aug 14 2019 18:23:23 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.203
* Wed Aug 14 2019 17:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.203
* Wed Aug 14 2019 17:27:06 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.203
- New Git version build: 6.1.0.203
* Wed Aug 14 2019 16:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.201
* Wed Aug 14 2019 16:22:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.201
* Wed Aug 14 2019 15:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.201
* Wed Aug 14 2019 15:27:45 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.201
- New Git version build: 6.1.0.201
* Tue Aug 13 2019 21:57:21 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.183
- New Git version build: 6.1.0.183
* Tue Aug 13 2019 19:27:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.168
- New Git version build: 6.1.0.168
* Tue Aug 13 2019 18:27:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.166
- New Git version build: 6.1.0.166
* Tue Aug 13 2019 17:57:15 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.159
- New Git version build: 6.1.0.159
* Tue Aug 13 2019 13:28:09 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.157
- New Git version build: 6.1.0.157
* Mon Aug 12 2019 23:57:19 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.155
- New Git version build: 6.1.0.155
* Mon Aug 12 2019 20:57:42 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.150
- New Git version build: 6.1.0.150
* Mon Aug 12 2019 19:27:37 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.148
- New Git version build: 6.1.0.148
* Mon Aug 12 2019 15:27:30 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.146
- New Git version build: 6.1.0.146
* Fri Aug 09 2019 20:57:09 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.144
- New Git version build: 6.1.0.144
* Fri Aug 09 2019 16:27:35 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.142
- New Git version build: 6.1.0.142
* Thu Aug 08 2019 18:57:18 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.139
- New Git version build: 6.1.0.139
* Thu Aug 08 2019 18:28:40 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.137
- New Git version build: 6.1.0.137
* Thu Aug 08 2019 15:27:47 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.134
- New Git version build: 6.1.0.134
* Wed Aug 07 2019 20:27:29 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.132
- New Git version build: 6.1.0.132
* Tue Aug 06 2019 19:58:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.128
- New Git version build: 6.1.0.128
* Tue Aug 06 2019 14:57:27 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.126
- New Git version build: 6.1.0.126
* Mon Aug 05 2019 17:57:39 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.124
- New Git version build: 6.1.0.124
* Mon Aug 05 2019 13:27:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.121
- New Git version build: 6.1.0.121
* Sat Aug 03 2019 16:27:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.119
- New Git version build: 6.1.0.119
* Sat Aug 03 2019 13:57:36 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.116
- New Git version build: 6.1.0.116
* Fri Aug 02 2019 22:56:59 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.114
- New Git version build: 6.1.0.114
* Fri Aug 02 2019 15:27:19 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.110
- New Git version build: 6.1.0.110
* Fri Aug 02 2019 00:54:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Fri Aug 02 2019 00:51:41 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 23:52:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 23:22:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 22:52:52 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 22:22:50 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 21:52:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 21:27:09 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
- New Git version build: 6.1.0.108
* Thu Aug 01 2019 20:52:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.99
* Thu Aug 01 2019 20:22:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.99
* Thu Aug 01 2019 19:52:50 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.99
* Thu Aug 01 2019 19:26:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.99
- New Git version build: 6.1.0.99
* Thu Aug 01 2019 18:52:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.97
* Thu Aug 01 2019 18:26:38 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.97
- New Git version build: 6.1.0.97
* Thu Aug 01 2019 16:27:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.94
- New Git version build: 6.1.0.94
* Thu Aug 01 2019 12:27:15 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.92
- New Git version build: 6.1.0.92
* Thu Aug 01 2019 00:52:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.88
- New Git version build: 6.1.0.88
* Wed Jul 31 2019 21:57:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.86
- New Git version build: 6.1.0.86
* Wed Jul 31 2019 20:57:34 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.84
- New Git version build: 6.1.0.84
* Tue Jul 30 2019 22:57:12 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.82
- New Git version build: 6.1.0.82
* Tue Jul 30 2019 22:27:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.79
- New Git version build: 6.1.0.79
* Tue Jul 30 2019 21:27:07 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.75
- New Git version build: 6.1.0.75
* Tue Jul 30 2019 19:57:36 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.73
- New Git version build: 6.1.0.73
* Tue Jul 30 2019 15:57:13 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.70
- New Git version build: 6.1.0.70
* Tue Jul 30 2019 13:57:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.66
- New Git version build: 6.1.0.66
* Mon Jul 29 2019 17:57:04 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.64
- New Git version build: 6.1.0.64
* Mon Jul 29 2019 16:57:14 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.53
- New Git version build: 6.1.0.53
* Mon Jul 29 2019 12:57:30 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.50
- New Git version build: 6.1.0.50
* Fri Jul 26 2019 16:57:25 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.48
- New Git version build: 6.1.0.48
* Thu Jul 25 2019 21:56:53 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.46
- New Git version build: 6.1.0.46
* Thu Jul 25 2019 20:57:17 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.44
- New Git version build: 6.1.0.44
* Thu Jul 25 2019 19:57:34 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.42
- New Git version build: 6.1.0.42
* Thu Jul 25 2019 19:27:35 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.40
- New Git version build: 6.1.0.40
* Wed Jul 24 2019 21:27:32 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.38
- New Git version build: 6.1.0.38
* Wed Jul 24 2019 18:27:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.20
- New Git version build: 6.1.0.20
* Wed Jul 24 2019 00:02:16 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.18
- New Git version build: 6.1.0.18
* Thu Jul 18 2019 19:00:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.14
- New Git version build: 6.1.0.14
* Thu Jul 18 2019 17:27:10 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.747
- New Git version build: 6.0.0.747
* Thu Jul 18 2019 16:27:56 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.732
- New Git version build: 6.0.0.732
* Thu Jul 18 2019 15:58:45 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.728
- New Git version build: 6.0.0.728
* Wed Jul 17 2019 20:53:24 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.726
- New Git version build: 6.0.0.726
* Wed Jul 17 2019 16:53:30 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.721
* Wed Jul 17 2019 16:27:25 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.721
- New Git version build: 6.0.0.721
* Tue Jul 16 2019 22:18:46 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
* Tue Jul 16 2019 22:02:45 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
- New version build: 05a1137
* Tue Jul 16 2019 20:53:15 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.719
* Tue Jul 16 2019 18:57:21 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.719
- New Git version build: 6.0.0.719
* Tue Jul 16 2019 18:32:47 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.717
- New Git version build: 6.0.0.717
* Tue Jul 16 2019 18:21:09 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.715
- New Git version build: 6.0.0.715
* Tue Jul 16 2019 17:23:24 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
* Tue Jul 16 2019 17:19:25 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
* Tue Jul 16 2019 16:23:18 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
* Tue Jul 16 2019 15:53:17 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
* Tue Jul 16 2019 15:27:13 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
- New Git version build: 6.0.0.713
* Tue Jul 16 2019 14:58:02 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.710
- New Git version build: 6.0.0.710
* Mon Jul 15 2019 23:27:40 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.703
- New Git version build: 6.0.0.703
* Mon Jul 15 2019 13:28:25 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.675
- New Git version build: 6.0.0.675
* Fri Jul 12 2019 19:27:15 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.673
- New Git version build: 6.0.0.673
* Fri Jul 12 2019 18:57:04 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.671
- New Git version build: 6.0.0.671
* Fri Jul 12 2019 02:26:42 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.669
- New Git version build: 6.0.0.669
* Thu Jul 11 2019 18:56:53 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.667
- New Git version build: 6.0.0.667
* Thu Jul 11 2019 17:27:05 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.665
- New Git version build: 6.0.0.665
* Thu Jul 11 2019 16:57:31 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.663
- New Git version build: 6.0.0.663
* Wed Jul 10 2019 14:57:31 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.656
- New Git version build: 6.0.0.656
* Tue Jul 09 2019 21:27:04 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.652
- New Git version build: 6.0.0.652
* Tue Jul 09 2019 18:57:03 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.650
- New Git version build: 6.0.0.650
* Tue Jul 09 2019 17:27:07 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.644
- New Git version build: 6.0.0.644
* Tue Jul 09 2019 13:57:30 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.638
- New Git version build: 6.0.0.638
* Tue Jul 09 2019 13:27:24 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.636
- New Git version build: 6.0.0.636
* Tue Jul 09 2019 05:57:02 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.630
- New Git version build: 6.0.0.630
* Mon Jul 08 2019 21:27:16 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.628
- New Git version build: 6.0.0.628
* Fri Jul 05 2019 16:27:54 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.618
- New Git version build: 6.0.0.618
* Wed Jul 03 2019 12:57:13 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.616
- New Git version build: 6.0.0.616
* Wed Jul 03 2019 12:27:21 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.614
- New Git version build: 6.0.0.614
* Tue Jul 02 2019 19:26:32 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 19:22:56 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 18:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 18:22:59 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 17:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 17:26:51 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
- New Git version build: 6.0.0.610
* Tue Jul 02 2019 16:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.608
* Tue Jul 02 2019 16:26:55 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.608
- New Git version build: 6.0.0.608
* Tue Jul 02 2019 12:57:36 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.603
- New Git version build: 6.0.0.603
* Mon Jul 01 2019 23:26:57 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.600
- New Git version build: 6.0.0.600
* Mon Jul 01 2019 21:56:51 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.597
- New Git version build: 6.0.0.597
* Mon Jul 01 2019 16:27:13 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.69
- New Git version build: 5.0.0.69
* Mon Jul 01 2019 15:57:33 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.67
- New Git version build: 5.0.0.67
* Fri Jun 28 2019 16:57:42 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.65
- New Git version build: 5.0.0.65
* Thu Jun 27 2019 20:27:03 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.63
- New Git version build: 5.0.0.63
* Thu Jun 27 2019 18:57:09 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.61
- New Git version build: 5.0.0.61
* Wed Jun 26 2019 20:26:52 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.59
- New Git version build: 5.0.0.59
* Wed Jun 26 2019 12:57:07 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.57
- New Git version build: 5.0.0.57
* Wed Jun 26 2019 01:26:53 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.55
- New Git version build: 5.0.0.55
* Tue Jun 25 2019 21:57:28 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.53
- New Git version build: 5.0.0.53
* Mon Jun 24 2019 21:28:41 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.51
- New Git version build: 5.0.0.51
* Sat Jun 22 2019 22:51:49 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.49
* Sat Jun 22 2019 22:46:12 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.49
* Sat Jun 22 2019 21:37:08 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.49
- New Git version build: 5.0.0.49
* Thu Jun 20 2019 23:49:15 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.0
* Thu Jun 20 2019 23:31:16 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.0
* Tue Jun 18 2019 21:00:21 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.0
* Tue Jun 18 2019 20:47:31 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.0
- New Git version build: 5.0.0.0
* Mon Jun 17 2019 21:12:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.746
- New Git version build: 4.0.0.746
* Sat Jun 15 2019 01:27:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.742
- New Git version build: 4.0.0.742
* Fri Jun 14 2019 14:57:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.740
- New Git version build: 4.0.0.740
* Fri Jun 14 2019 14:27:16 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.738
- New Git version build: 4.0.0.738
* Fri Jun 14 2019 13:57:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.734
- New Git version build: 4.0.0.734
* Thu Jun 13 2019 22:26:32 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.731
- New Git version build: 4.0.0.731
* Thu Jun 13 2019 21:57:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.729
- New Git version build: 4.0.0.729
* Thu Jun 13 2019 20:26:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.725
- New Git version build: 4.0.0.725
* Thu Jun 13 2019 14:27:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.723
- New Git version build: 4.0.0.723
* Thu Jun 13 2019 12:31:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.721
* Wed Jun 12 2019 21:26:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.721
- New Git version build: 4.0.0.721
* Wed Jun 12 2019 18:56:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.719
- New Git version build: 4.0.0.719
* Wed Jun 12 2019 17:56:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.707
- New Git version build: 4.0.0.707
* Wed Jun 12 2019 16:26:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.705
- New Git version build: 4.0.0.705
* Wed Jun 12 2019 15:26:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.703
- New Git version build: 4.0.0.703
* Wed Jun 12 2019 13:56:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.701
- New Git version build: 4.0.0.701
* Wed Jun 12 2019 12:27:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.699
- New Git version build: 4.0.0.699
* Tue Jun 11 2019 18:56:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.697
- New Git version build: 4.0.0.697
* Tue Jun 11 2019 16:26:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.695
- New Git version build: 4.0.0.695
* Tue Jun 11 2019 15:56:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.693
- New Git version build: 4.0.0.693
* Tue Jun 11 2019 14:57:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.691
- New Git version build: 4.0.0.691
* Mon Jun 10 2019 17:58:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.689
- New Git version build: 4.0.0.689
* Thu Jun 06 2019 18:56:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.682
- New Git version build: 4.0.0.682
* Thu Jun 06 2019 16:26:42 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.678
- New Git version build: 4.0.0.678
* Thu Jun 06 2019 15:26:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.676
- New Git version build: 4.0.0.676
* Thu Jun 06 2019 14:56:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.674
- New Git version build: 4.0.0.674
* Wed Jun 05 2019 20:26:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.672
- New Git version build: 4.0.0.672
* Wed Jun 05 2019 17:26:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.670
- New Git version build: 4.0.0.670
* Wed Jun 05 2019 11:56:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.668
- New Git version build: 4.0.0.668
* Tue Jun 04 2019 20:27:01 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.663
- New Git version build: 4.0.0.663
* Mon Jun 03 2019 21:56:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.661
- New Git version build: 4.0.0.661
* Mon Jun 03 2019 18:26:45 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.658
- New Git version build: 4.0.0.658
* Mon Jun 03 2019 17:56:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.656
- New Git version build: 4.0.0.656
* Mon Jun 03 2019 14:57:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.652
- New Git version build: 4.0.0.652
* Fri May 31 2019 16:27:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.650
- New Git version build: 4.0.0.650
* Fri May 31 2019 15:28:01 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.648
- New Git version build: 4.0.0.648
* Fri May 31 2019 12:27:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.646
- New Git version build: 4.0.0.646
* Fri May 31 2019 01:57:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.644
- New Git version build: 4.0.0.644
* Thu May 30 2019 19:27:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.642
- New Git version build: 4.0.0.642
* Thu May 30 2019 17:27:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.640
- New Git version build: 4.0.0.640
* Thu May 30 2019 14:58:14 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.638
- New Git version build: 4.0.0.638
* Wed May 29 2019 20:58:15 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.631
- New Git version build: 4.0.0.631
* Tue May 28 2019 20:28:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.629
- New Git version build: 4.0.0.629
* Tue May 28 2019 19:57:52 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.627
- New Git version build: 4.0.0.627
* Tue May 28 2019 17:27:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.625
- New Git version build: 4.0.0.625
* Tue May 28 2019 16:58:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.623
- New Git version build: 4.0.0.623
* Tue May 28 2019 13:58:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.619
- New Git version build: 4.0.0.619
* Fri May 24 2019 20:57:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.616
- New Git version build: 4.0.0.616
* Fri May 24 2019 19:58:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.614
- New Git version build: 4.0.0.614
* Thu May 23 2019 19:27:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.612
- New Git version build: 4.0.0.612
* Thu May 23 2019 17:27:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.610
- New Git version build: 4.0.0.610
* Thu May 23 2019 15:27:37 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.608
- New Git version build: 4.0.0.608
* Thu May 23 2019 12:58:13 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.605
- New Git version build: 4.0.0.605
* Wed May 22 2019 23:59:15 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.601
- New Git version build: 4.0.0.601
* Wed May 22 2019 20:57:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.599
- New Git version build: 4.0.0.599
* Wed May 22 2019 19:27:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.597
- New Git version build: 4.0.0.597
* Wed May 22 2019 14:28:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.595
- New Git version build: 4.0.0.595
* Tue May 21 2019 14:58:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.593
- New Git version build: 4.0.0.593
* Mon May 20 2019 17:27:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.590
- New Git version build: 4.0.0.590
* Mon May 20 2019 16:57:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.588
- New Git version build: 4.0.0.588
* Mon May 20 2019 15:58:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.586
- New Git version build: 4.0.0.586
* Fri May 17 2019 18:53:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.582
* Fri May 17 2019 18:27:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.582
- New Git version build: 4.0.0.582
* Fri May 17 2019 15:58:00 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.577
- New Git version build: 4.0.0.577
* Thu May 16 2019 20:27:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.573
- New Git version build: 4.0.0.573
* Thu May 16 2019 18:57:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.569
- New Git version build: 4.0.0.569
* Thu May 16 2019 18:27:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.567
- New Git version build: 4.0.0.567
* Thu May 16 2019 17:27:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.565
- New Git version build: 4.0.0.565
* Thu May 16 2019 15:27:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.563
- New Git version build: 4.0.0.563
* Thu May 16 2019 03:58:13 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.561
- New Git version build: 4.0.0.561
* Wed May 15 2019 18:58:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.558
- New Git version build: 4.0.0.558
* Mon May 13 2019 22:23:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.547
* Mon May 13 2019 21:50:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.547
* Mon May 13 2019 21:23:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.547
* Mon May 13 2019 20:58:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.547
- New Git version build: 4.0.0.547
* Fri May 10 2019 19:23:06 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.541
- New Git version build: 4.0.0.541
* Thu May 09 2019 21:27:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.521
- New Git version build: 4.0.0.521
* Thu May 09 2019 19:57:29 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.516
- New Git version build: 4.0.0.516
* Thu May 09 2019 18:27:37 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.514
- New Git version build: 4.0.0.514
* Thu May 09 2019 16:57:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.512
- New Git version build: 4.0.0.512
* Thu May 09 2019 14:27:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.510
- New Git version build: 4.0.0.510
* Thu May 09 2019 13:57:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.508
- New Git version build: 4.0.0.508
* Thu May 09 2019 13:28:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.505
- New Git version build: 4.0.0.505
* Thu May 09 2019 01:28:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.503
- New Git version build: 4.0.0.503
* Wed May 08 2019 19:57:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.501
- New Git version build: 4.0.0.501
* Wed May 08 2019 16:27:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.494
- New Git version build: 4.0.0.494
* Wed May 08 2019 13:59:13 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.492
- New Git version build: 4.0.0.492
* Tue May 07 2019 14:28:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.490
- New Git version build: 4.0.0.490
* Mon May 06 2019 16:29:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.488
- New Git version build: 4.0.0.488
* Fri May 03 2019 21:29:12 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.483
- New Git version build: 4.0.0.483
* Fri May 03 2019 13:03:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.456
- New Git version build: 4.0.0.456
* Thu May 02 2019 17:27:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.444
- New Git version build: 4.0.0.444
* Thu May 02 2019 13:58:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.442
- New Git version build: 4.0.0.442
* Thu May 02 2019 00:50:55 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.440
- New Git version build: 4.0.0.440
* Wed May 01 2019 20:27:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.438
- New Git version build: 4.0.0.438
* Wed May 01 2019 17:28:29 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.430
- New Git version build: 4.0.0.430
* Sat Apr 27 2019 06:30:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 05:53:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 05:23:00 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 04:53:00 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 04:23:19 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 03:53:07 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 03:23:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 02:53:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 02:23:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 01:52:55 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 01:23:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 00:53:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 00:41:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 23:52:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 23:23:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 22:52:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 22:23:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 21:53:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 21:23:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 20:53:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 20:23:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 19:53:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 19:28:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
- New Git version build: 4.0.0.428
* Fri Apr 26 2019 18:53:32 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.426
* Fri Apr 26 2019 18:28:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.426
- New Git version build: 4.0.0.426
* Fri Apr 26 2019 17:53:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.424
* Fri Apr 26 2019 17:28:20 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.424
- New Git version build: 4.0.0.424
* Fri Apr 26 2019 16:53:37 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.378
* Fri Apr 26 2019 16:23:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.378
* Fri Apr 26 2019 15:59:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.378
- New Git version build: 4.0.0.378
* Wed Apr 24 2019 16:57:29 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.376
- New Git version build: 4.0.0.376
* Wed Apr 24 2019 15:27:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.374
- New Git version build: 4.0.0.374
* Wed Apr 24 2019 13:27:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.372
- New Git version build: 4.0.0.372
* Tue Apr 23 2019 20:57:38 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.370
- New Git version build: 4.0.0.370
* Tue Apr 23 2019 18:27:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.367
- New Git version build: 4.0.0.367
* Tue Apr 23 2019 17:58:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.365
- New Git version build: 4.0.0.365
* Mon Apr 22 2019 17:57:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.363
- New Git version build: 4.0.0.363
* Mon Apr 22 2019 16:57:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.361
- New Git version build: 4.0.0.361
* Mon Apr 22 2019 15:58:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.356
- New Git version build: 4.0.0.356
* Mon Apr 22 2019 01:40:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Mon Apr 22 2019 01:30:15 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 02:27:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 02:12:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 02:04:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 01:57:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 01:51:02 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:19:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:18:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:14:41 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:13:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:07:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:03:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:01:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Fri Apr 19 2019 23:58:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Fri Apr 19 2019 23:55:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
- New Git version build: 4.0.0.354
* Thu Apr 18 2019 17:27:38 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.347
- New Git version build: 4.0.0.347
* Thu Apr 18 2019 16:57:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.345
- New Git version build: 4.0.0.345
* Thu Apr 18 2019 16:27:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.343
- New Git version build: 4.0.0.343
* Thu Apr 18 2019 12:57:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.341
- New Git version build: 4.0.0.341
* Thu Apr 18 2019 11:27:48 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.339
- New Git version build: 4.0.0.339
* Wed Apr 17 2019 23:28:51 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.337
- New Git version build: 4.0.0.337
* Wed Apr 17 2019 22:03:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 21:52:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 21:41:31 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 21:22:49 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 20:52:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 20:22:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 19:52:32 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 19:22:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 18:52:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 18:22:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 17:52:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 17:22:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 16:52:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 16:22:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 15:52:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 15:22:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 14:52:45 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 14:22:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 13:52:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 13:27:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
- New Git version build: 4.0.0.335
* Wed Apr 17 2019 12:57:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.333
- New Git version build: 4.0.0.333
* Wed Apr 17 2019 10:57:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.329
- New Git version build: 4.0.0.329
* Tue Apr 16 2019 20:57:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.327
- New Git version build: 4.0.0.327
* Tue Apr 16 2019 20:27:13 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.325
- New Git version build: 4.0.0.325
* Tue Apr 16 2019 17:57:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.323
- New Git version build: 4.0.0.323
* Mon Apr 15 2019 21:27:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.321
- New Git version build: 4.0.0.321
* Mon Apr 15 2019 20:57:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.319
- New Git version build: 4.0.0.319
* Mon Apr 15 2019 18:57:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.315
- New Git version build: 4.0.0.315
* Mon Apr 15 2019 18:33:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.313
- New Git version build: 4.0.0.313
* Mon Apr 15 2019 17:27:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.311
- New Git version build: 4.0.0.311
* Mon Apr 15 2019 16:52:49 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.309
* Mon Apr 15 2019 16:23:07 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.309
* Mon Apr 15 2019 15:52:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.309
* Mon Apr 15 2019 15:27:38 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.309
- New Git version build: 4.0.0.309
* Mon Apr 15 2019 14:52:56 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.307
* Mon Apr 15 2019 14:27:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.307
- New Git version build: 4.0.0.307
* Mon Apr 15 2019 13:58:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.305
- New Git version build: 4.0.0.305
* Sat Apr 13 2019 11:57:41 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.301
- New Git version build: 4.0.0.301
* Fri Apr 12 2019 21:57:31 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.299
- New Git version build: 4.0.0.299
* Fri Apr 12 2019 20:57:58 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.297
- New Git version build: 4.0.0.297
* Fri Apr 12 2019 20:27:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.295
- New Git version build: 4.0.0.295
* Fri Apr 12 2019 17:27:19 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.291
- New Git version build: 4.0.0.291
* Fri Apr 12 2019 16:27:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.289
- New Git version build: 4.0.0.289
* Fri Apr 12 2019 15:57:51 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.284
- New Git version build: 4.0.0.284
* Thu Apr 11 2019 22:02:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.282
- New Git version build: 4.0.0.282
* Thu Apr 11 2019 18:27:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.280
- New Git version build: 4.0.0.280
* Thu Apr 11 2019 18:03:02 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.278
- New Git version build: 4.0.0.278
* Thu Apr 11 2019 16:28:19 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.276
- New Git version build: 4.0.0.276
* Wed Apr 10 2019 20:57:06 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.274
- New Git version build: 4.0.0.274
* Wed Apr 10 2019 20:27:06 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.272
- New Git version build: 4.0.0.272
* Wed Apr 10 2019 19:57:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.270
- New Git version build: 4.0.0.270
* Wed Apr 10 2019 19:28:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.266
- New Git version build: 4.0.0.266
* Wed Apr 10 2019 15:27:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.264
- New Git version build: 4.0.0.264
* Wed Apr 10 2019 14:57:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.259
- New Git version build: 4.0.0.259
* Wed Apr 10 2019 14:28:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.257
- New Git version build: 4.0.0.257
* Tue Apr 09 2019 21:27:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.255
- New Git version build: 4.0.0.255
* Tue Apr 09 2019 21:01:56 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.252
- New Git version build: 4.0.0.252
* Tue Apr 09 2019 19:57:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.248
- New Git version build: 4.0.0.248
* Tue Apr 09 2019 17:57:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.246
- New Git version build: 4.0.0.246
* Tue Apr 09 2019 15:57:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.244
- New Git version build: 4.0.0.244
* Tue Apr 09 2019 14:27:32 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.233
- New Git version build: 4.0.0.233
* Tue Apr 09 2019 11:57:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.229
- New Git version build: 4.0.0.229
* Mon Apr 08 2019 22:44:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.227
* Mon Apr 08 2019 21:22:48 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.227
* Mon Apr 08 2019 20:52:56 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.227
* Mon Apr 08 2019 20:27:31 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.227
- New Git version build: 4.0.0.227
* Mon Apr 08 2019 19:52:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.225
* Mon Apr 08 2019 19:22:48 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.225
* Mon Apr 08 2019 18:52:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.225
* Mon Apr 08 2019 18:27:41 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.225
- New Git version build: 4.0.0.225
* Mon Apr 08 2019 17:52:55 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.223
* Mon Apr 08 2019 17:27:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.223
- New Git version build: 4.0.0.223
* Mon Apr 08 2019 16:52:45 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
* Mon Apr 08 2019 16:22:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
* Mon Apr 08 2019 16:16:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
* Mon Apr 08 2019 15:22:52 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
* Mon Apr 08 2019 14:57:52 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
- New Git version build: 4.0.0.220
* Mon Apr 08 2019 01:25:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.216
* Mon Apr 08 2019 00:20:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.216
* Fri Apr 05 2019 19:27:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.216
- New Git version build: 4.0.0.216
* Fri Apr 05 2019 18:56:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.214
- New Git version build: 4.0.0.214
* Fri Apr 05 2019 17:26:42 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.212
- New Git version build: 4.0.0.212
* Fri Apr 05 2019 16:27:20 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.203
- New Git version build: 4.0.0.203
* Fri Apr 05 2019 15:57:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.201
- New Git version build: 4.0.0.201
* Fri Apr 05 2019 15:27:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.194
- New Git version build: 4.0.0.194
* Fri Apr 05 2019 14:57:20 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.186
- New Git version build: 4.0.0.186
* Fri Apr 05 2019 01:28:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.182
- New Git version build: 4.0.0.182
* Thu Apr 04 2019 23:28:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.180
- New Git version build: 4.0.0.180
* Thu Apr 04 2019 18:57:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.177
- New Git version build: 4.0.0.177
* Thu Apr 04 2019 15:56:55 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.175
- New Git version build: 4.0.0.175
* Thu Apr 04 2019 13:56:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.171
- New Git version build: 4.0.0.171
* Thu Apr 04 2019 13:28:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.169
- New Git version build: 4.0.0.169
* Wed Apr 03 2019 21:29:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.164
- New Git version build: 4.0.0.164
* Wed Apr 03 2019 19:57:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.162
- New Git version build: 4.0.0.162
* Wed Apr 03 2019 19:27:48 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.160
- New Git version build: 4.0.0.160
* Wed Apr 03 2019 18:57:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.158
- New Git version build: 4.0.0.158
* Wed Apr 03 2019 17:57:00 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.150
- New Git version build: 4.0.0.150
* Wed Apr 03 2019 16:27:31 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.148
- New Git version build: 4.0.0.148
* Wed Apr 03 2019 15:57:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.146
- New Git version build: 4.0.0.146
* Wed Apr 03 2019 14:57:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.144
- New Git version build: 4.0.0.144
* Wed Apr 03 2019 09:25:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 08:22:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 07:52:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 07:22:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 06:52:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 06:22:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 06:09:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 05:22:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 04:52:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 04:22:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 03:52:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 03:22:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 02:52:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 02:22:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 01:52:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 01:22:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 01:20:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 01:15:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
- New Git version build: 4.0.0.142
* Tue Apr 02 2019 23:52:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 23:22:51 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 22:52:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 22:22:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 21:52:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 21:22:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 20:52:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 20:43:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 20:23:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 20:22:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 19:52:29 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 19:22:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 18:52:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 18:27:15 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
- New Git version build: 4.0.0.140
* Tue Apr 02 2019 17:52:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.138
* Tue Apr 02 2019 17:22:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.138
* Tue Apr 02 2019 16:52:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.138
* Tue Apr 02 2019 16:27:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.138
- New Git version build: 4.0.0.138
* Tue Apr 02 2019 13:26:45 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.63
- New Git version build: 4.0.0.63
* Tue Apr 02 2019 12:27:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.61
- New Git version build: 4.0.0.61
* Mon Apr 01 2019 21:56:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.58
- New Git version build: 4.0.0.58
* Mon Apr 01 2019 20:56:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.56
- New Git version build: 4.0.0.56
* Mon Apr 01 2019 19:56:38 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.54
- New Git version build: 4.0.0.54
* Mon Apr 01 2019 18:32:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.52
- New Git version build: 4.0.0.52
* Mon Apr 01 2019 15:57:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.50
- New Git version build: 4.0.0.50
* Sun Mar 31 2019 02:57:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.48
- New Git version build: 4.0.0.48
* Fri Mar 29 2019 20:56:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.43
- New Git version build: 4.0.0.43
* Fri Mar 29 2019 19:56:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.41
- New Git version build: 4.0.0.41
* Fri Mar 29 2019 18:26:49 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.39
- New Git version build: 4.0.0.39
* Fri Mar 29 2019 17:26:58 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.37
- New Git version build: 4.0.0.37
* Fri Mar 29 2019 16:56:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.35
- New Git version build: 4.0.0.35
* Fri Mar 29 2019 15:27:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.33
- New Git version build: 4.0.0.33
* Fri Mar 29 2019 14:26:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.25
- New Git version build: 4.0.0.25
* Fri Mar 29 2019 13:27:16 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.23
- New Git version build: 4.0.0.23
* Fri Mar 29 2019 00:29:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.17
- New Git version build: 4.0.0.17
* Thu Mar 28 2019 23:48:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.15
* Thu Mar 28 2019 22:57:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.15
- New Git version build: 4.0.0.15
* Thu Mar 28 2019 18:27:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.2
- New Git version build: 4.0.0.2
* Thu Mar 28 2019 12:41:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.6
* Thu Mar 28 2019 12:00:16 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.6
* Thu Mar 28 2019 01:26:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.0
- New Git version build: 4.0.0.0
* Thu Mar 28 2019 00:57:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.6
- New Git version build: 4.0.0.6
* Wed Mar 27 2019 22:57:42 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.4
- New Git version build: 4.0.0.4
* Wed Mar 27 2019 17:56:43 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.398
- New Git version build: 3.0.1.398
* Wed Mar 27 2019 16:57:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.396
- New Git version build: 3.0.1.396
* Wed Mar 27 2019 16:27:11 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.394
- New Git version build: 3.0.1.394
* Wed Mar 27 2019 15:56:53 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.392
- New Git version build: 3.0.1.392
* Wed Mar 27 2019 14:27:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.390
- New Git version build: 3.0.1.390
* Tue Mar 26 2019 19:57:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.387
- New Git version build: 3.0.1.387
* Tue Mar 26 2019 19:27:51 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.384
- New Git version build: 3.0.1.384
* Tue Mar 26 2019 16:57:00 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.377
- New Git version build: 3.0.1.377
* Tue Mar 26 2019 15:29:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.375
- New Git version build: 3.0.1.375
* Tue Mar 26 2019 12:57:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.361
- New Git version build: 3.0.1.361
* Tue Mar 26 2019 12:29:27 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.358
- New Git version build: 3.0.1.358
* Mon Mar 25 2019 23:26:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.356
- New Git version build: 3.0.1.356
* Mon Mar 25 2019 22:56:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.353
- New Git version build: 3.0.1.353
* Mon Mar 25 2019 20:27:14 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.351
- New Git version build: 3.0.1.351
* Mon Mar 25 2019 19:57:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.349
- New Git version build: 3.0.1.349
* Mon Mar 25 2019 17:29:20 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.344
- New Git version build: 3.0.1.344
* Mon Mar 25 2019 16:07:53 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.340
- New Git version build: 3.0.1.340
* Mon Mar 25 2019 15:27:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.340
- New Git version build: 3.0.1.340
* Fri Mar 22 2019 20:57:05 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.338
- New Git version build: 3.0.1.338
* Fri Mar 22 2019 18:56:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.335
- New Git version build: 3.0.1.335
* Fri Mar 22 2019 16:57:07 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.333
- New Git version build: 3.0.1.333
* Fri Mar 22 2019 15:57:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.331
- New Git version build: 3.0.1.331
* Fri Mar 22 2019 01:23:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Fri Mar 22 2019 00:22:50 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Thu Mar 21 2019 23:52:53 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Thu Mar 21 2019 23:22:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Thu Mar 21 2019 23:01:33 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Thu Mar 21 2019 20:57:02 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.311
- New Git version build: 3.0.1.311
* Thu Mar 21 2019 19:27:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.309
- New Git version build: 3.0.1.309
* Thu Mar 21 2019 16:57:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.307
- New Git version build: 3.0.1.307
* Thu Mar 21 2019 16:26:27 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.305
- New Git version build: 3.0.1.305
* Thu Mar 21 2019 15:26:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.303
- New Git version build: 3.0.1.303
* Thu Mar 21 2019 14:56:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.281
- New Git version build: 3.0.1.281
* Thu Mar 21 2019 12:57:52 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.275
- New Git version build: 3.0.1.275
* Wed Mar 20 2019 20:26:45 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.273
- New Git version build: 3.0.1.273
* Wed Mar 20 2019 16:26:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.271
- New Git version build: 3.0.1.271
* Wed Mar 20 2019 15:57:09 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.269
- New Git version build: 3.0.1.269
* Tue Mar 19 2019 19:56:59 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.267
- New Git version build: 3.0.1.267
* Tue Mar 19 2019 12:27:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.265
- New Git version build: 3.0.1.265
* Mon Mar 18 2019 16:52:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.263
- New Git version build: 3.0.1.263
* Mon Mar 18 2019 14:56:30 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.261
- New Git version build: 3.0.1.261
* Mon Mar 18 2019 13:58:38 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.259
- New Git version build: 3.0.1.259
* Mon Mar 18 2019 13:27:29 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.257
- New Git version build: 3.0.1.257
* Sat Mar 16 2019 12:57:06 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.255
- New Git version build: 3.0.1.255
* Fri Mar 15 2019 15:26:32 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.253
- New Git version build: 3.0.1.253
* Fri Mar 15 2019 13:57:40 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.251
- New Git version build: 3.0.1.251
* Fri Mar 15 2019 13:27:19 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.246
- New Git version build: 3.0.1.246
* Fri Mar 15 2019 12:27:20 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.244
- New Git version build: 3.0.1.244
* Thu Mar 14 2019 20:28:02 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.242
- New Git version build: 3.0.1.242
* Thu Mar 14 2019 00:27:26 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.238
- New Git version build: 3.0.1.238
* Wed Mar 13 2019 18:57:18 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.236
- New Git version build: 3.0.1.236
* Wed Mar 13 2019 14:57:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.234
- New Git version build: 3.0.1.234
* Tue Mar 12 2019 19:58:48 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.232
- New Git version build: 3.0.1.232
* Tue Mar 12 2019 16:26:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.230
- New Git version build: 3.0.1.230
* Tue Mar 12 2019 15:26:57 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.228
- New Git version build: 3.0.1.228
* Tue Mar 12 2019 15:02:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.226
- New Git version build: 3.0.1.226
* Tue Mar 12 2019 14:27:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.226
- New Git version build: 3.0.1.226
* Mon Mar 11 2019 20:56:50 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.223
- New Git version build: 3.0.1.223
* Mon Mar 11 2019 15:57:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.221
- New Git version build: 3.0.1.221
* Fri Mar 08 2019 17:56:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.219
- New Git version build: 3.0.1.219
* Fri Mar 08 2019 16:27:12 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.217
- New Git version build: 3.0.1.217
* Fri Mar 08 2019 15:26:57 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.214
- New Git version build: 3.0.1.214
* Fri Mar 08 2019 14:26:46 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.212
- New Git version build: 3.0.1.212
* Thu Mar 07 2019 18:56:48 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.205
- New Git version build: 3.0.1.205
* Thu Mar 07 2019 17:26:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.201
- New Git version build: 3.0.1.201
* Thu Mar 07 2019 16:26:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.199
- New Git version build: 3.0.1.199
* Thu Mar 07 2019 15:56:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.194
- New Git version build: 3.0.1.194
* Thu Mar 07 2019 15:27:01 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.189
- New Git version build: 3.0.1.189
* Thu Mar 07 2019 14:57:09 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.186
- New Git version build: 3.0.1.186
* Wed Mar 06 2019 23:57:33 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.184
- New Git version build: 3.0.1.184
* Tue Mar 05 2019 17:26:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.182
- New Git version build: 3.0.1.182
* Mon Mar 04 2019 21:57:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.177
- New Git version build: 3.0.1.177
* Mon Mar 04 2019 21:27:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.173
- New Git version build: 3.0.1.173
* Fri Mar 01 2019 20:32:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.170
- New Git version build: 3.0.1.170
* Fri Mar 01 2019 16:27:20 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.167
- New Git version build: 3.0.1.167
* Thu Feb 28 2019 21:57:07 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.165
- New Git version build: 3.0.1.165
* Thu Feb 28 2019 21:27:37 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.137
- New Git version build: 3.0.1.137
* Thu Feb 28 2019 18:57:16 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.135
- New Git version build: 3.0.1.135
* Thu Feb 28 2019 14:56:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.130
- New Git version build: 3.0.1.130
* Thu Feb 28 2019 13:57:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.128
- New Git version build: 3.0.1.128
* Wed Feb 27 2019 17:27:04 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.126
- New Git version build: 3.0.1.126
* Wed Feb 27 2019 16:27:22 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.124
- New Git version build: 3.0.1.124
* Mon Feb 25 2019 18:27:14 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.120
- New Git version build: 3.0.1.120
* Fri Feb 22 2019 18:56:39 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.114
- New Git version build: 3.0.1.114
* Fri Feb 22 2019 18:26:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.109
- New Git version build: 3.0.1.109
* Thu Feb 21 2019 21:26:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.107
- New Git version build: 3.0.1.107
* Thu Feb 21 2019 18:57:13 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.105
- New Git version build: 3.0.1.105
* Thu Feb 21 2019 18:26:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.102
- New Git version build: 3.0.1.102
* Thu Feb 21 2019 16:27:00 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.99
- New Git version build: 3.0.1.99
* Wed Feb 20 2019 20:26:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.97
- New Git version build: 3.0.1.97
* Wed Feb 20 2019 19:56:30 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.94
- New Git version build: 3.0.1.94
* Wed Feb 20 2019 17:26:40 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.92
- New Git version build: 3.0.1.92
* Wed Feb 20 2019 16:26:22 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.89
- New Git version build: 3.0.1.89
* Wed Feb 20 2019 15:56:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.87
- New Git version build: 3.0.1.87
* Tue Feb 19 2019 17:56:34 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.84
- New Git version build: 3.0.1.84
* Tue Feb 19 2019 17:27:12 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.82
- New Git version build: 3.0.1.82
* Mon Feb 18 2019 21:27:11 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.80
- New Git version build: 3.0.1.80
* Fri Feb 15 2019 22:26:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.78
- New Git version build: 3.0.1.78
* Fri Feb 15 2019 16:56:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.72
- New Git version build: 3.0.1.72
* Fri Feb 15 2019 15:57:11 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.70
- New Git version build: 3.0.1.70
* Thu Feb 14 2019 22:56:32 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.68
- New Git version build: 3.0.1.68
* Thu Feb 14 2019 21:56:29 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.65
- New Git version build: 3.0.1.65
* Thu Feb 14 2019 21:26:45 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.63
- New Git version build: 3.0.1.63
* Thu Feb 14 2019 16:56:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.59
- New Git version build: 3.0.1.59
* Thu Feb 14 2019 16:26:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.55
- New Git version build: 3.0.1.55
* Thu Feb 14 2019 15:56:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.53
- New Git version build: 3.0.1.53
* Thu Feb 14 2019 15:26:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.42
- New Git version build: 3.0.1.42
* Thu Feb 14 2019 14:26:39 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.39
- New Git version build: 3.0.1.39
* Thu Feb 14 2019 13:57:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.37
- New Git version build: 3.0.1.37
* Wed Feb 13 2019 23:26:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.35
- New Git version build: 3.0.1.35
* Wed Feb 13 2019 22:27:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.33
- New Git version build: 3.0.1.33
* Wed Feb 13 2019 20:26:48 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.31
- New Git version build: 3.0.1.31
* Wed Feb 13 2019 18:29:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.29
- New Git version build: 3.0.1.29
* Wed Feb 13 2019 15:26:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.27
- New Git version build: 3.0.1.27
* Wed Feb 13 2019 14:56:48 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.25
- New Git version build: 3.0.1.25
* Tue Feb 12 2019 22:56:45 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.17
- New Git version build: 3.0.1.17
* Tue Feb 12 2019 18:56:43 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.14
- New Git version build: 3.0.1.14
* Mon Feb 11 2019 19:00:13 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.12
- New Git version build: 3.0.1.12
* Mon Feb 11 2019 17:32:16 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.10
- New Git version build: 3.0.1.10
* Mon Feb 11 2019 16:57:26 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.7
- New Git version build: 3.0.1.7
* Mon Feb 11 2019 15:28:24 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.5
- New Git version build: 3.0.1.5
* Mon Feb 11 2019 14:57:09 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.2
- New Git version build: 3.0.1.2
* Fri Feb 08 2019 19:57:06 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.128
- New Git version build: 3.0.0.128
* Fri Feb 08 2019 14:57:13 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.126
- New Git version build: 3.0.0.126
* Thu Feb 07 2019 21:56:14 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.124
- New Git version build: 3.0.0.124
* Thu Feb 07 2019 21:26:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.122
- New Git version build: 3.0.0.122
* Thu Feb 07 2019 19:56:46 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.120
- New Git version build: 3.0.0.120
* Thu Feb 07 2019 16:57:22 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.118
- New Git version build: 3.0.0.118
* Thu Feb 07 2019 15:27:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.113
- New Git version build: 3.0.0.113
* Wed Feb 06 2019 17:26:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.111
- New Git version build: 3.0.0.111
* Wed Feb 06 2019 16:57:07 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.109
- New Git version build: 3.0.0.109
* Wed Feb 06 2019 01:58:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.107
- New Git version build: 3.0.0.107
* Wed Feb 06 2019 01:28:52 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.105
- New Git version build: 3.0.0.105
* Tue Feb 05 2019 22:58:19 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.102
- New Git version build: 3.0.0.102
* Tue Feb 05 2019 19:27:06 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.100
- New Git version build: 3.0.0.100
* Tue Feb 05 2019 17:57:18 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.98
- New Git version build: 3.0.0.98
* Tue Feb 05 2019 13:57:42 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.96
- New Git version build: 3.0.0.96
* Mon Feb 04 2019 17:27:34 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.94
- New Git version build: 3.0.0.94
* Sat Feb 02 2019 12:27:23 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.92
- New Git version build: 3.0.0.92
* Fri Feb 01 2019 21:57:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.90
- New Git version build: 3.0.0.90
* Fri Feb 01 2019 17:57:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.88
- New Git version build: 3.0.0.88
* Fri Feb 01 2019 14:27:12 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.84
- New Git version build: 3.0.0.84
* Thu Jan 31 2019 16:59:19 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.82
- New Git version build: 3.0.0.82
* Thu Jan 31 2019 14:57:28 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.80
- New Git version build: 3.0.0.80
* Wed Jan 30 2019 18:57:09 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.78
- New Git version build: 3.0.0.78
* Wed Jan 30 2019 18:26:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.74
- New Git version build: 3.0.0.74
* Wed Jan 30 2019 17:57:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.72
- New Git version build: 3.0.0.72
* Tue Jan 29 2019 21:57:00 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.68
- New Git version build: 3.0.0.68
* Tue Jan 29 2019 21:27:01 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.66
- New Git version build: 3.0.0.66
* Tue Jan 29 2019 20:27:41 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.63
- New Git version build: 3.0.0.63
* Tue Jan 29 2019 12:34:40 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.59
- New Git version build: 3.0.0.59
* Tue Jan 29 2019 12:21:57 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.59
- New Git version build: 3.0.0.59
* Tue Jan 29 2019 11:38:33 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 11:28:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 11:21:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 11:15:39 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 11:00:51 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:43:34 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:40:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:38:02 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:36:15 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:34:50 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:19:27 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:06:59 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:41:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:30:13 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:26:27 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:23:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:15:00 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Thu Jan 17 2019 14:50:45 +0000 Martin Juhl <m@rtinjuhl.dk> 3.0.0.0
- New Version v.3.0.0
* Thu Jan 17 2019 14:50:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 14:42:30 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 14:14:13 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 14:12:06 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 13:34:11 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 13:15:48 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 12:51:30 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 06:45:28 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 06:43:54 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 01:34:56 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 00:52:54 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:52:46 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:46:16 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:27:19 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:14:55 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:11:23 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:08:25 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:05:55 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 22:59:19 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 22:23:41 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Tue Jan 15 2019 18:28:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.59
- New Git version build: 2.1.2.59
* Tue Jan 15 2019 14:29:14 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.57
- New Git version build: 2.1.2.57
* Mon Jan 14 2019 17:59:01 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.48
- New Git version build: 2.1.2.48
* Fri Jan 11 2019 20:28:52 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.46
- New Git version build: 2.1.2.46
* Fri Jan 11 2019 15:27:53 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.44
- New Git version build: 2.1.2.44
* Fri Jan 11 2019 13:57:54 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.42
- New Git version build: 2.1.2.42
* Fri Jan 11 2019 13:28:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.40
- New Git version build: 2.1.2.40
* Mon Jan 07 2019 19:58:42 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.38
- New Git version build: 2.1.2.38
* Sat Jan 05 2019 01:21:20 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.36
- New Git version build: 2.1.2.36
* Sat Jan 05 2019 00:56:33 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.36
- New Git version build: 2.1.2.36
* Sat Jan 05 2019 00:35:25 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.36
- New Git version build: 2.1.2.36
* Fri Jan 04 2019 23:25:59 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.36
- New Git version build: 2.1.2.36
* Wed Jan 02 2019 19:32:59 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.34
- New Git version build: 2.1.2.34
* Thu Dec 20 2018 22:45:08 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.32
- New Git version build: 2.1.2.32
* Wed Dec 19 2018 14:28:21 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.29
- New Git version build: 2.1.2.29
* Tue Dec 18 2018 12:29:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.26
- New Git version build: 2.1.2.26
* Mon Dec 17 2018 15:28:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.15
- New Git version build: 2.1.2.15
* Fri Dec 14 2018 20:00:49 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.13
- New Git version build: 2.1.2.13
* Thu Dec 13 2018 18:29:17 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.9
- New Git version build: 2.1.2.9
* Thu Dec 13 2018 13:28:34 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.7
- New Git version build: 2.1.2.7
* Thu Dec 13 2018 01:32:09 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.5
- New Git version build: 2.1.2.5
* Wed Dec 12 2018 15:58:24 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.3
- New Git version build: 2.1.2.3
* Tue Dec 11 2018 18:31:09 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.1
- New Git version build: 2.1.2.1
* Tue Dec 11 2018 17:58:57 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.42
- New Git version build: 2.1.1.42
* Mon Dec 10 2018 16:58:41 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.40
- New Git version build: 2.1.1.40
* Mon Dec 10 2018 01:13:38 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.0
- New Git version build: 2.1.1.0
* Fri Dec 07 2018 21:57:57 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.36
- New Git version build: 2.1.1.36
* Fri Dec 07 2018 20:58:13 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.34
- New Git version build: 2.1.1.34
* Fri Dec 07 2018 20:28:23 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.32
- New Git version build: 2.1.1.32
* Fri Dec 07 2018 15:04:01 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.30
- New Git version build: 2.1.1.30
* Fri Dec 07 2018 09:55:25 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.27
- New Git version build: 2.1.1.27
* Thu Dec 06 2018 14:47:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.23
- New Git version build: 2.1.1.23
* Tue Dec 04 2018 23:22:48 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.21
- New Git version build: 2.1.1.21
* Wed Nov 28 2018 04:38:17 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.384
- New Git version build: 2.1.0.384
* Wed Nov 28 2018 04:07:46 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.382
- New Git version build: 2.1.0.382
* Tue Nov 27 2018 22:38:39 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.380
- New Git version build: 2.1.0.380
* Tue Nov 27 2018 18:08:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.280
- New Git version build: 2.1.0.280
* Tue Nov 27 2018 16:08:46 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.276
- New Git version build: 2.1.0.276
* Tue Nov 27 2018 15:38:12 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.274
- New Git version build: 2.1.0.274
* Mon Nov 26 2018 19:08:27 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.272
- New Git version build: 2.1.0.272
* Mon Nov 26 2018 17:08:02 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.270
- New Git version build: 2.1.0.270
* Mon Nov 26 2018 16:09:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.267
- New Git version build: 2.1.0.267
* Wed Nov 21 2018 20:38:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.265
- New Git version build: 2.1.0.265
* Wed Nov 21 2018 19:38:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.263
- New Git version build: 2.1.0.263
* Wed Nov 21 2018 15:37:46 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.261
- New Git version build: 2.1.0.261
* Wed Nov 21 2018 03:37:59 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.258
- New Git version build: 2.1.0.258
* Tue Nov 20 2018 21:38:35 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.256
- New Git version build: 2.1.0.256
* Tue Nov 20 2018 20:39:48 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.254
- New Git version build: 2.1.0.254
* Tue Nov 20 2018 18:38:57 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.251
- New Git version build: 2.1.0.251
* Tue Nov 20 2018 17:08:09 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.249
- New Git version build: 2.1.0.249
* Tue Nov 20 2018 16:08:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.247
- New Git version build: 2.1.0.247
* Tue Nov 20 2018 15:37:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.245
- New Git version build: 2.1.0.245
* Tue Nov 20 2018 14:38:05 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.243
- New Git version build: 2.1.0.243
* Tue Nov 20 2018 09:07:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.241
- New Git version build: 2.1.0.241
* Tue Nov 20 2018 03:38:05 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.239
- New Git version build: 2.1.0.239
* Mon Nov 19 2018 19:39:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.196
- New Git version build: 2.1.0.196
* Mon Nov 19 2018 19:09:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.194
- New Git version build: 2.1.0.194
* Mon Nov 19 2018 18:09:32 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.192
- New Git version build: 2.1.0.192
* Mon Nov 19 2018 17:38:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.190
- New Git version build: 2.1.0.190
* Mon Nov 19 2018 17:07:52 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.186
- New Git version build: 2.1.0.186
* Mon Nov 19 2018 16:09:21 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.181
- New Git version build: 2.1.0.181
* Mon Nov 19 2018 15:38:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.179
- New Git version build: 2.1.0.179
* Mon Nov 19 2018 14:38:21 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.177
- New Git version build: 2.1.0.177
* Mon Nov 19 2018 14:08:32 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.169
- New Git version build: 2.1.0.169
* Fri Nov 16 2018 22:38:23 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.167
- New Git version build: 2.1.0.167
* Fri Nov 16 2018 22:10:24 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.164
- New Git version build: 2.1.0.164
* Fri Nov 16 2018 20:07:58 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.162
- New Git version build: 2.1.0.162
* Fri Nov 16 2018 16:08:06 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.160
- New Git version build: 2.1.0.160
* Fri Nov 16 2018 15:38:20 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.158
- New Git version build: 2.1.0.158
* Thu Nov 15 2018 20:41:16 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.155
- New Git version build: 2.1.0.155
* Thu Nov 15 2018 20:09:49 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.153
- New Git version build: 2.1.0.153
* Thu Nov 15 2018 15:38:13 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.151
- New Git version build: 2.1.0.151
* Thu Nov 15 2018 14:38:26 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.147
- New Git version build: 2.1.0.147
* Wed Nov 14 2018 22:37:50 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.143
- New Git version build: 2.1.0.143
* Wed Nov 14 2018 16:38:00 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.141
- New Git version build: 2.1.0.141
* Tue Nov 13 2018 21:39:33 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.139
- New Git version build: 2.1.0.139
* Tue Nov 13 2018 20:41:43 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.137
- New Git version build: 2.1.0.137
* Tue Nov 13 2018 16:08:16 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.135
- New Git version build: 2.1.0.135
* Mon Nov 12 2018 19:09:05 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.131
- New Git version build: 2.1.0.131
* Mon Nov 12 2018 11:17:22 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.129
- New Git version build: 2.1.0.129
* Fri Nov 09 2018 05:39:07 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.119
- New Git version build: 2.1.0.119
* Thu Nov 08 2018 23:09:35 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.0
- New Git version build: 2.1.0.0
* Thu Nov 08 2018 21:13:19 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.117
- New Git version build: 2.1.0.117
* Thu Nov 08 2018 20:39:11 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.115
- New Git version build: 2.1.0.115
* Thu Nov 08 2018 16:38:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.113
- New Git version build: 2.1.0.113
* Thu Nov 08 2018 15:38:09 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.97
- New Git version build: 2.1.0.97
* Thu Nov 08 2018 13:08:08 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.94
- New Git version build: 2.1.0.94
* Thu Nov 08 2018 12:38:12 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.92
- New Git version build: 2.1.0.92
* Thu Nov 08 2018 07:07:47 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.89
- New Git version build: 2.1.0.89
* Thu Nov 08 2018 03:07:57 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.86
- New Git version build: 2.1.0.86
* Wed Nov 07 2018 21:37:34 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.83
- New Git version build: 2.1.0.83
* Wed Nov 07 2018 21:10:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.81
- New Git version build: 2.1.0.81
* Wed Nov 07 2018 20:39:30 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.78
- New Git version build: 2.1.0.78
* Wed Nov 07 2018 18:09:03 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.76
- New Git version build: 2.1.0.76
* Wed Nov 07 2018 09:50:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.74
- New Git version build: 2.1.0.74
* Tue Nov 06 2018 21:39:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.74
- New Git version build: 2.1.0.74
* Tue Nov 06 2018 20:40:32 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.72
- New Git version build: 2.1.0.72
* Tue Nov 06 2018 20:10:16 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.68
- New Git version build: 2.1.0.68
* Tue Nov 06 2018 17:37:32 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.66
- New Git version build: 2.1.0.66
* Tue Nov 06 2018 17:07:29 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.64
- New Git version build: 2.1.0.64
* Tue Nov 06 2018 15:37:51 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.60
- New Git version build: 2.1.0.60
* Tue Nov 06 2018 02:07:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.58
- New Git version build: 2.1.0.58
* Mon Nov 05 2018 16:37:31 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.49
- New Git version build: 2.1.0.49
* Mon Nov 05 2018 15:38:34 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.47
- New Git version build: 2.1.0.47
* Mon Nov 05 2018 14:18:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 14:11:03 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 14:05:06 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 14:02:44 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 13:51:04 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 13:32:55 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 13:29:55 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Fri Nov 02 2018 19:08:19 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Fri Nov 02 2018 15:38:15 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.43
- New Git version build: 2.1.0.43
* Fri Nov 02 2018 15:08:22 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.40
- New Git version build: 2.1.0.40
* Thu Nov 01 2018 21:08:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.38
- New Git version build: 2.1.0.38
* Thu Nov 01 2018 17:07:42 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.36
- New Git version build: 2.1.0.36
* Thu Nov 01 2018 16:08:02 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.0
- New Git version build: 2.1.0.0
* Thu Nov 01 2018 15:08:07 +0000 Martin Juhl <mj@casalogic.dk> 2.0.2.0
- New Git version build: 2.0.2.0
* Fri Oct 12 2018 09:43:14 +0000 Martin Juhl <mj@casalogic.dk> 2.0.1
- New Git version build: 2.0.1
* Thu Oct 11 2018 13:51:00 +0000 Martin Juhl <mj@casalogic.dk> 2.0.1
- New Git version build: 2.0.1
* Thu Oct 04 2018 08:59:15 +0000 Martin Juhl <mj@casalogic.dk> 2.0.0
- New Git version build: 2.0.0
* Mon Oct 01 2018 14:36:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.8.22
- New Git version build: 1.0.8.22
* Fri Sep 28 2018 14:36:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.8.18
- New Git version build: 1.0.8.18
* Wed Sep 26 2018 21:07:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.8.16
- New Git version build: 1.0.8.16
* Wed Sep 26 2018 12:17:23 +0000 Martin Juhl <mj@casalogic.dk> 1.0.8.14
- New Git version build: 1.0.8.14
* Mon Sep 24 2018 19:37:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.9
- New Git version build: 1.0.7.9
* Thu Sep 20 2018 22:07:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.8
- New Git version build: 1.0.7.8
* Tue Sep 18 2018 18:36:45 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.7
- New Git version build: 1.0.7.7
* Tue Sep 18 2018 17:06:39 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.6
- New Git version build: 1.0.7.6
* Tue Sep 18 2018 13:07:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.5
- New Git version build: 1.0.7.5
* Tue Aug 28 2018 08:53:44 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.4
- New Git version build: 1.0.7.4
* Fri Aug 17 2018 23:43:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.3
- New Git version build: 1.0.7.3
* Fri Aug 10 2018 04:08:26 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.47
- New Git version build: 1.0.6.47
* Fri Aug 10 2018 03:39:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.46
- New Git version build: 1.0.6.46
* Thu Aug 09 2018 14:10:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.44
- New Git version build: 1.0.6.44
* Thu Aug 02 2018 20:10:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.43
- New Git version build: 1.0.6.43
* Thu Aug 02 2018 17:39:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.42
- New Git version build: 1.0.6.42
* Thu Jul 26 2018 16:37:26 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.41
- New Git version build: 1.0.6.41
* Thu Jul 26 2018 13:37:43 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.40
- New Git version build: 1.0.6.40
* Tue Jul 24 2018 16:37:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.39
- New Git version build: 1.0.6.39
* Tue Jul 24 2018 16:08:29 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.38
- New Git version build: 1.0.6.38
* Wed Jul 18 2018 20:37:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.37
- New Git version build: 1.0.6.37
* Wed Jul 18 2018 16:38:26 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.36
- New Git version build: 1.0.6.36
* Mon Jul 16 2018 19:08:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.35
- New Git version build: 1.0.6.35
* Mon Jul 16 2018 18:37:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.34
- New Git version build: 1.0.6.34
* Mon Jul 16 2018 18:06:37 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.33
- New Git version build: 1.0.6.33
* Mon Jul 16 2018 17:07:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.31
- New Git version build: 1.0.6.31
* Mon Jul 16 2018 14:37:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.30
- New Git version build: 1.0.6.30
* Mon Jul 16 2018 14:09:16 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.29
- New Git version build: 1.0.6.29
* Fri Jul 13 2018 16:17:23 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.28
- New Git version build: 1.0.6.28
* Fri Jul 13 2018 13:53:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.27
- New Git version build: 1.0.6.27
* Tue Jul 10 2018 19:52:42 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.26
- New Git version build: 1.0.6.26
* Mon Jul 09 2018 16:49:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.25
- New Git version build: 1.0.6.25
* Mon Jul 09 2018 14:54:38 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.24
- New Git version build: 1.0.6.24
* Mon Jun 25 2018 20:37:47 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.23
- New Git version build: 1.0.6.23
* Mon Jun 25 2018 20:08:45 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.22
- New Git version build: 1.0.6.22
* Mon Jun 25 2018 17:38:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.18
- New Git version build: 1.0.6.18
* Mon Jun 18 2018 18:39:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.17
- New Git version build: 1.0.6.17
* Tue Jun 12 2018 12:38:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.16
- New Git version build: 1.0.6.16
* Mon Jun 04 2018 21:10:31 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.15
- New Git version build: 1.0.6.15
* Thu May 31 2018 20:38:37 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.14
- New Git version build: 1.0.6.14
* Thu May 31 2018 14:08:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.13
- New Git version build: 1.0.6.13
* Wed May 30 2018 14:39:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.12
- New Git version build: 1.0.6.12
* Thu May 24 2018 19:07:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.11
- New Git version build: 1.0.6.11
* Thu May 24 2018 17:00:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.10
- New Git version build: 1.0.6.10
* Thu May 24 2018 16:06:56 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.10
- New Git version build: 1.0.6.10
* Thu May 17 2018 20:37:49 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.8
- New Git version build: 1.0.6.8
* Tue May 15 2018 20:36:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.7
- New Git version build: 1.0.6.7
* Tue May 15 2018 18:07:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.6
- New Git version build: 1.0.6.6
* Fri May 04 2018 23:19:25 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.5
- New Git version build: 1.0.6.5
* Fri May 04 2018 23:02:53 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.5
- New Git version build: 1.0.6.5
* Tue May 01 2018 08:06:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.3
- New Git version build: 1.0.6.3
* Fri Apr 27 2018 20:35:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.1
- New Git version build: 1.0.6.1
* Fri Apr 27 2018 16:36:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.0
- New Git version build: 1.0.6.0
* Fri Apr 27 2018 16:06:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.33
- New Git version build: 1.0.5.33
* Thu Apr 26 2018 18:06:36 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.32
- New Git version build: 1.0.5.32
* Wed Apr 25 2018 19:35:55 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.31
- New Git version build: 1.0.5.31
* Wed Apr 25 2018 15:36:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.30
- New Git version build: 1.0.5.30
* Fri Apr 20 2018 18:06:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.29
- New Git version build: 1.0.5.29
* Fri Apr 20 2018 13:36:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.28
- New Git version build: 1.0.5.28
* Fri Apr 20 2018 03:06:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.27
- New Git version build: 1.0.5.27
* Wed Apr 18 2018 15:06:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.26
- New Git version build: 1.0.5.26
* Tue Apr 17 2018 15:36:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.25
- New Git version build: 1.0.5.25
* Mon Apr 16 2018 21:36:32 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.24
- New Git version build: 1.0.5.24
* Wed Apr 11 2018 17:06:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.23
- New Git version build: 1.0.5.23
* Thu Apr 05 2018 18:35:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.22
- New Git version build: 1.0.5.22
* Thu Apr 05 2018 15:35:37 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.21
- New Git version build: 1.0.5.21
* Tue Apr 03 2018 23:35:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.20
- New Git version build: 1.0.5.20
* Thu Mar 29 2018 00:19:40 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.19
- New Git version build: 1.0.5.19
* Wed Mar 28 2018 13:08:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.14
- New Git version build: 1.0.5.14
* Tue Mar 27 2018 16:05:37 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.13
- New Git version build: 1.0.5.13
* Mon Mar 26 2018 19:35:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.11
- New Git version build: 1.0.5.11
* Mon Mar 26 2018 18:35:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.7
- New Git version build: 1.0.5.7
* Mon Mar 26 2018 17:35:32 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.6
- New Git version build: 1.0.5.6
* Mon Mar 26 2018 16:35:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.5
- New Git version build: 1.0.5.5
* Mon Mar 26 2018 15:36:50 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.3
- New Git version build: 1.0.5.3
* Mon Mar 26 2018 14:35:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.134
- New Git version build: 1.0.4.134
* Mon Mar 26 2018 14:05:17 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.132
- New Git version build: 1.0.4.132
* Mon Mar 26 2018 13:35:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.131
- New Git version build: 1.0.4.131
* Fri Mar 23 2018 17:05:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.130
- New Git version build: 1.0.4.130
* Fri Mar 23 2018 15:04:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.129
- New Git version build: 1.0.4.129
* Fri Mar 23 2018 14:04:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.128
- New Git version build: 1.0.4.128
* Thu Mar 22 2018 19:35:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.126
- New Git version build: 1.0.4.126
* Thu Mar 22 2018 12:35:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.125
- New Git version build: 1.0.4.125
* Thu Mar 22 2018 02:04:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.124
- New Git version build: 1.0.4.124
* Thu Mar 22 2018 00:04:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.123
- New Git version build: 1.0.4.123
* Wed Mar 21 2018 20:05:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.122
- New Git version build: 1.0.4.122
* Wed Mar 21 2018 19:05:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.121
- New Git version build: 1.0.4.121
* Wed Mar 21 2018 18:35:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.119
- New Git version build: 1.0.4.119
* Wed Mar 21 2018 16:05:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.118
- New Git version build: 1.0.4.118
* Wed Mar 21 2018 03:35:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.115
- New Git version build: 1.0.4.115
* Tue Mar 20 2018 21:35:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.114
- New Git version build: 1.0.4.114
* Tue Mar 20 2018 16:05:39 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.113
- New Git version build: 1.0.4.113
* Tue Mar 20 2018 14:35:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.112
- New Git version build: 1.0.4.112
* Tue Mar 20 2018 11:35:17 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.110
- New Git version build: 1.0.4.110
* Tue Mar 20 2018 01:35:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.109
- New Git version build: 1.0.4.109
* Mon Mar 19 2018 17:35:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.108
- New Git version build: 1.0.4.108
* Mon Mar 19 2018 17:08:44 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.107
* Mon Mar 19 2018 15:05:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.107
- New Git version build: 1.0.4.107
* Sat Mar 17 2018 21:05:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.106
- New Git version build: 1.0.4.106
* Sat Mar 17 2018 03:05:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.105
- New Git version build: 1.0.4.105
* Fri Mar 16 2018 20:05:44 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.104
- New Git version build: 1.0.4.104
* Fri Mar 16 2018 19:35:42 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.103
- New Git version build: 1.0.4.103
* Fri Mar 16 2018 19:05:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.102
- New Git version build: 1.0.4.102
* Fri Mar 16 2018 18:05:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.100
- New Git version build: 1.0.4.100
* Fri Mar 16 2018 15:35:17 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.99
- New Git version build: 1.0.4.99
* Fri Mar 16 2018 14:05:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.98
- New Git version build: 1.0.4.98
* Thu Mar 15 2018 20:35:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.97
- New Git version build: 1.0.4.97
* Thu Mar 15 2018 19:05:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.95
- New Git version build: 1.0.4.95
* Thu Mar 15 2018 18:35:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.94
- New Git version build: 1.0.4.94
* Wed Mar 14 2018 21:04:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.93
- New Git version build: 1.0.4.93
* Wed Mar 14 2018 19:35:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.92
- New Git version build: 1.0.4.92
* Wed Mar 14 2018 19:05:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.91
- New Git version build: 1.0.4.91
* Wed Mar 14 2018 15:34:50 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.89
- New Git version build: 1.0.4.89
* Wed Mar 14 2018 15:04:54 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.88
- New Git version build: 1.0.4.88
* Wed Mar 14 2018 14:34:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.87
- New Git version build: 1.0.4.87
* Wed Mar 14 2018 13:34:45 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.86
- New Git version build: 1.0.4.86
* Wed Mar 14 2018 13:04:44 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.85
- New Git version build: 1.0.4.85
* Wed Mar 14 2018 11:34:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.84
- New Git version build: 1.0.4.84
* Wed Mar 14 2018 10:10:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.83
- New Git version build: 1.0.4.83
* Fri Mar 09 2018 21:14:34 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.70
- New Git version build

* Fri Mar 09 2018 18:13:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.69
- New Git version build

* Fri Mar 09 2018 17:14:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.68
- New Git version build

* Fri Mar 09 2018 16:14:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.67
- New Git version build

* Fri Mar 09 2018 15:14:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.65
- New Git version build

* Fri Mar 09 2018 00:14:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.64
- New Git version build

* Thu Mar 08 2018 23:14:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.63
- New Git version build

* Thu Mar 08 2018 18:14:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.62
- New Git version build

* Thu Mar 08 2018 16:14:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.61
- New Git version build

* Thu Mar 08 2018 15:14:16 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.59
- New Git version build

* Thu Mar 08 2018 14:14:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.58
- New Git version build

* Wed Mar 07 2018 21:14:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.57
- New Git version build

* Wed Mar 07 2018 17:14:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.56
- New Git version build

* Wed Mar 07 2018 14:14:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.54
- New Git version build

* Tue Mar 06 2018 21:14:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.53
- New Git version build

* Tue Mar 06 2018 20:14:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.52
- New Git version build

* Tue Mar 06 2018 19:14:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.51
- New Git version build

* Tue Mar 06 2018 17:14:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.50
- New Git version build

* Tue Mar 06 2018 13:14:00 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.49
- New Git version build

* Tue Mar 06 2018 00:04:00 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.48
- New Git version build

* Mon Mar 05 2018 22:34:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.48
- New Git version build

* Mon Mar 05 2018 22:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.47
- New Git version build

* Mon Mar 05 2018 21:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.46
- New Git version build

* Mon Mar 05 2018 20:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.45
- New Git version build

* Sat Mar 03 2018 16:11:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.43
- New Git version build

* Sat Mar 03 2018 02:11:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.42
- New Git version build

* Fri Mar 02 2018 21:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.41
- New Git version build

* Fri Mar 02 2018 17:11:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.40
- New Git version build

* Fri Mar 02 2018 15:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.39
- New Git version build

* Thu Mar 01 2018 23:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.38
- New Git version build

* Thu Mar 01 2018 18:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.37
- New Git version build

* Thu Mar 01 2018 17:11:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.36
- New Git version build

* Thu Mar 01 2018 16:11:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.35
- New Git version build

* Thu Mar 01 2018 15:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.34
- New Git version build

* Wed Feb 28 2018 21:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.33
- New Git version build

* Wed Feb 28 2018 19:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.32
- New Git version build

* Wed Feb 28 2018 18:11:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.31
- New Git version build

* Wed Feb 28 2018 14:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.29
- New Git version build

* Wed Feb 28 2018 02:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.27
- New Git version build

* Tue Feb 27 2018 22:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.26
- New Git version build

* Tue Feb 27 2018 21:11:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.23
- New Git version build

* Tue Feb 27 2018 19:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.22
- New Git version build

* Tue Feb 27 2018 16:11:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.21
- New Git version build

* Tue Feb 27 2018 16:11:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.21
- New Git version build

* Tue Feb 27 2018 15:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.20
- New Git version build

* Mon Feb 26 2018 22:11:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.18
- New Git version build

* Mon Feb 26 2018 21:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.17
- New Git version build

* Mon Feb 26 2018 18:11:00 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.16
- New Git version build

* Mon Feb 26 2018 17:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.15
- New Git version build

* Fri Feb 23 2018 21:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.14
- New Git version build

* Thu Feb 22 2018 22:00:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.12
- New Git version build

* Fri Feb 16 2018 22:11:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.56
- New Git version build

* Thu Feb 15 2018 22:11:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.55
- New Git version build

* Thu Feb 15 2018 20:11:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.54
- New Git version build

* Thu Feb 15 2018 15:11:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.53
- New Git version build

* Wed Feb 14 2018 21:11:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.52
- New Git version build

* Wed Feb 14 2018 19:11:23 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.51
- New Git version build

* Wed Feb 14 2018 16:11:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.50
- New Git version build

* Wed Feb 14 2018 14:11:17 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.48
- New Git version build

* Tue Feb 13 2018 23:11:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.47
- New Git version build

* Tue Feb 13 2018 21:11:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.46
- New Git version build

* Tue Feb 13 2018 18:11:29 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.44
- New Git version build

* Tue Feb 13 2018 17:11:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.42
- New Git version build

* Tue Feb 13 2018 14:19:47 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:16:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:10:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:09:38 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:09:20 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Thu Feb 08 2018 16:11:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.23
- New Git version build

* Thu Feb 08 2018 15:11:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.20
- New Git version build

* Wed Feb 07 2018 23:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.18
- New Git version build

* Wed Feb 07 2018 22:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.17
- New Git version build

* Wed Feb 07 2018 21:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.16
- New Git version build

* Wed Feb 07 2018 17:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.15
- New Git version build

* Wed Feb 07 2018 15:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.14
- New Git version build

* Wed Feb 07 2018 01:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.13
- New Git version build

* Tue Feb 06 2018 20:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.12
- New Git version build

* Tue Feb 06 2018 17:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.11
- New Git version build

* Mon Feb 05 2018 21:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.9
- New Git version build

* Mon Feb 05 2018 20:11:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.8
- New Git version build

* Mon Feb 05 2018 15:11:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.7
- New Git version build

* Sun Feb 04 2018 00:03:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.5
- New Git version build

* Sat Feb 03 2018 23:39:39 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.33
- New Git version build

* Sat Feb 03 2018 23:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.33
- New Git version build

* Thu Jan 25 2018 18:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.445
- New Git version build

* Thu Jan 25 2018 16:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.443
- New Git version build

* Wed Jan 24 2018 21:11:45 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.440
- New Git version build

* Wed Jan 24 2018 15:11:49 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.438
- New Git version build

* Tue Jan 23 2018 19:11:35 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.436
- New Git version build

* Mon Jan 22 2018 20:11:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.432
- New Git version build

* Mon Jan 22 2018 16:11:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.430
- New Git version build

* Fri Jan 19 2018 19:11:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.428
- New Git version build

* Fri Jan 19 2018 14:11:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.426
- New Git version build

* Thu Jan 18 2018 22:11:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.424
- New Git version build

* Thu Jan 18 2018 21:11:35 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.424
- New Git version build

* Thu Jan 18 2018 20:11:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.424
- New Git version build

* Thu Jan 18 2018 19:11:26 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.422
- New Git version build

* Thu Jan 18 2018 18:11:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.422
- New Git version build

* Thu Jan 18 2018 17:11:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.418
- New Git version build

* Thu Jan 18 2018 16:11:32 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.416
- New Git version build

* Thu Jan 18 2018 14:11:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.414
- New Git version build

* Thu Jan 18 2018 05:11:32 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.411
- New Git version build

* Wed Jan 17 2018 20:11:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.403
- New Git version build

* Wed Jan 17 2018 18:11:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.399
- New Git version build

* Wed Jan 17 2018 17:11:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.397
- New Git version build

* Tue Jan 16 2018 20:11:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.388
- New Git version build

* Tue Jan 16 2018 06:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.386
- New Git version build

* Tue Jan 16 2018 02:11:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.384
- New Git version build

* Mon Jan 15 2018 17:18:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.380
- New Git version build

* Mon Jan 15 2018 17:11:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.380
- New Git version build

* Mon Jan 15 2018 17:05:29 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.380
- New Git version build

* Mon Jan 15 2018 16:11:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.374
- New Git version build

* Sat Jan 13 2018 02:11:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.372
- New Git version build

* Thu Jan 11 2018 22:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.370
- New Git version build

* Thu Jan 11 2018 20:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.368
- New Git version build

* Thu Jan 11 2018 17:12:23 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.364
- New Git version build

* Thu Jan 11 2018 00:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.358
- New Git version build

* Wed Jan 10 2018 20:10:55 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.356
- New Git version build

* Wed Jan 10 2018 18:10:54 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.352
- New Git version build

* Wed Jan 10 2018 15:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.350
- New Git version build

* Wed Jan 10 2018 06:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.339
- New Git version build

* Wed Jan 10 2018 01:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.337
- New Git version build

* Mon Jan 08 2018 16:10:55 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.335
- New Git version build

* Fri Jan 05 2018 14:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.327
- New Git version build

* Fri Jan 05 2018 13:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.325
- New Git version build

* Thu Jan 04 2018 20:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.322
- New Git version build

* Thu Jan 04 2018 18:11:00 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.317
- New Git version build

* Thu Jan 04 2018 17:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.315
- New Git version build

* Tue Jan 02 2018 19:10:56 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.307
- New Git version build

* Tue Jan 02 2018 15:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.305
- New Git version build

* Thu Dec 21 2017 19:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.303
- New Git version build

* Mon Dec 18 2017 22:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.301
- New Git version build

* Fri Dec 15 2017 16:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.293
- New Git version build

* Fri Dec 15 2017 05:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.291
- New Git version build

* Thu Dec 14 2017 16:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.289
- New Git version build

* Thu Dec 14 2017 04:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.285
- New Git version build

* Thu Dec 14 2017 01:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.283
- New Git version build

* Thu Dec 14 2017 00:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.281
- New Git version build

* Wed Dec 13 2017 22:10:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.279
- New Git version build

* Wed Dec 13 2017 21:12:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.278
- New Git version build

* Wed Dec 13 2017 20:12:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.274
- New Git version build

* Wed Dec 13 2017 19:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.272
- New Git version build

* Wed Dec 13 2017 18:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.268
- New Git version build

* Wed Dec 13 2017 17:11:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.0
- New Git version build

* Wed Dec 13 2017 15:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.325
- New Git version build

* Wed Dec 13 2017 00:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.323
- New Git version build

* Tue Dec 12 2017 20:11:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.321
- New Git version build

* Tue Dec 12 2017 16:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.319
- New Git version build

* Tue Dec 12 2017 02:10:56 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.316
- New Git version build

* Mon Dec 11 2017 22:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.314
- New Git version build

* Mon Dec 11 2017 20:01:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.314
- New Git version build

* Mon Dec 11 2017 18:36:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.312
- New Git version build

* Mon Dec 11 2017 15:01:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.310
- New Git version build

* Thu Nov 21 2017 18:14:55 +0300 Matvey Kruglov <kubuzzzz@gmail.com> 1.0.1.225-1
- Update upstream version
- Improve centos 7 support

* Wed Sep 21 2017 14:44:23 +0300 Matvey Kruglov <kubuzzzz@gmail.com> 1.0.0.505-1
- Initial RPM release
