#!/bin/bash

# Requirements: Enable EPEL and CRB

echo "Before running the bootstrap build, please fork https://github.com/MrMEEE/awx-rpm-versions and https://github.com/MrMEEE/awx-rpm-v2 and setup ssh key authentication"
echo "Please enter your versions repo:"
read VERSIONREPO

echo "Please enter your awx-rpm-v2 repo:"
read AWXRPMREPO

echo "Bootstrap build"

# Dependencies
dnf -y install podman git rpm-build rpmdevtools rpmautospec-rpm-macros expect mock createrepo_c wget vim

# Mock Config
mkdir -p /root/.config/mock/
cat <<EOF >> /root/.config/mock/epel-9-x86_64.cfg
include('rhel-9-x86_64.cfg')
include('templates/epel-9.tpl')

config_opts['root'] = "rhel+epel-9-{{ target_arch }}"
config_opts['description'] = 'RHEL 9 + EPEL'
config_opts['update_before_build'] = False
config_opts['module_enable'] = ['nodejs:18']
EOF

git clone $AWXRPMREPO /opt/awx-rpm-v2
git clone $VERSIONREPO /opt/awx-rpm-v2/versions
git clone https://github.com/ansible/awx/ /opt/awx-rpm-v2/awx
