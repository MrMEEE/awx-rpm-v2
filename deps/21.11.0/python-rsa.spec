Name:           python-rsa
Version:        4.9
Release:        1%{?dist}
Summary:        Pure-Python RSA implementation

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://stuvel.eu/rsa
Source:         %{pypi_source rsa}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rsa' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-rsa
Summary:        %{summary}

%description -n python3-rsa %_description


%prep
%autosetup -p1 -n rsa-%{version}


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


%files -n python3-rsa -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 4.9-1
- Initial package