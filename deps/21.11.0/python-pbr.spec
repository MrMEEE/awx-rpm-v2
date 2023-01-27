Name:           python-pbr
Version:        5.11.0
Release:        1%{?dist}
Summary:        Python Build Reasonableness

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://docs.openstack.org/pbr/latest/
Source:         %{pypi_source pbr}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pbr' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pbr
Summary:        %{summary}

%description -n python3-pbr %_description


%prep
%autosetup -p1 -n pbr-%{version}


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


%files -n python3-pbr -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 5.11.0-1
- Initial package