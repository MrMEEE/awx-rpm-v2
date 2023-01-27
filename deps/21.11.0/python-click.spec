Name:           python-click
Version:        8.1.3
Release:        1%{?dist}
Summary:        Composable command line interface toolkit

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://palletsprojects.com/p/click/
Source:         %{pypi_source click}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'click' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-click
Summary:        %{summary}

%description -n python3-click %_description


%prep
%autosetup -p1 -n click-%{version}


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


%files -n python3-click -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 8.1.3-1
- Initial package