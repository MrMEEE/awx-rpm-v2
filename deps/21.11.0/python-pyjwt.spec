Name:           python-pyjwt
Version:        2.6.0
Release:        1%{?dist}
Summary:        JSON Web Token implementation in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jpadilla/pyjwt
Source:         %{pypi_source PyJWT}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyjwt' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pyjwt
Summary:        %{summary}

%description -n python3-pyjwt %_description


%prep
%autosetup -p1 -n PyJWT-%{version}


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


%files -n python3-pyjwt -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 2.6.0-1
- Initial package