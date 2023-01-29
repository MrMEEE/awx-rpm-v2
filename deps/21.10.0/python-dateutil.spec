Name:           python-dateutil
Version:        2.8.2
Release:        1%{?dist}
Summary:        Extensions to the standard Python datetime module

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL and BSD
URL:            https://github.com/dateutil/dateutil
Source:         %{pypi_source python-dateutil}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-dateutil' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-python-dateutil
Summary:        %{summary}

%description -n python3-python-dateutil %_description


%prep
%autosetup -p1 -n python-dateutil-%{version}


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


%files -n python3-python-dateutil -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 2.8.2-1
- Initial package