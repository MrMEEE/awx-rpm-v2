Name:           python-ansible-runner
Version:        2.3.1
Release:        1%{?dist}
Summary:        "Consistent Ansible Python API and CLI with container and process isolation runtime capabilities"

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://ansible-runner.readthedocs.io
Source:         %{pypi_source ansible-runner}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ansible_runner' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-ansible-runner
Summary:        %{summary}

%description -n python3-ansible-runner %_description


%prep
%autosetup -p1 -n ansible-runner-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-ansible-runner -f %{pyproject_files}


%changelog
* Mon Feb 13 2023 Martin Juhl <m@rtinjuhl.dk> - 2.3.1-1
- Initial package