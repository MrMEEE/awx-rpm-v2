Name:           python-ldap
Version:        3.4.3
Release:        1%{?dist}
Summary:        Python modules for implementing LDAP clients

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Python
URL:            https://www.python-ldap.org/
Source:         %{pypi_source python-ldap}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-ldap' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-python-ldap
Summary:        %{summary}

%description -n python3-python-ldap %_description


%prep
%autosetup -p1 -n python-ldap-%{version}


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


%files -n python3-python-ldap -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 3.4.3-1
- Initial package