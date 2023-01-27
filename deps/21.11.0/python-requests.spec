Name:           python-requests
Version:        2.28.1
Release:        1%{?dist}
Summary:        Python HTTP for Humans.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://requests.readthedocs.io
Source:         %{pypi_source requests}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'requests' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-requests
Summary:        %{summary}

%description -n python3-requests %_description


%prep
%autosetup -p1 -n requests-%{version}


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


%files -n python3-requests -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 2.28.1-1
- Initial package