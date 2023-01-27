Name:           python-pip
Version:        21.2.4
Release:        1%{?dist}
Summary:        The PyPA recommended tool for installing Python packages.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pip.pypa.io/
Source:         %{pypi_source pip}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pip' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pip
Summary:        %{summary}

%description -n python3-pip %_description


%prep
%autosetup -p1 -n pip-%{version}


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


%files -n python3-pip -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 21.2.4-1
- Initial package