Name:           python-calver
Version:        2022.6.26
Release:        1%{?dist}
Summary:        Setuptools extension for CalVer package versions

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/di/calver
Source:         %{pypi_source calver}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'calver' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-calver
Summary:        %{summary}

%description -n python3-calver %_description


%prep
%autosetup -p1 -n calver-%{version}


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


%files -n python3-calver -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 2022.6.26-1
- Initial package