Name:           python-platformdirs
Version:        2.6.2
Release:        1%{?dist}
Summary:        A small Python package for determining appropriate platform-specific dirs, e.g. a "user data dir".

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/platformdirs/platformdirs
Source:         %{pypi_source platformdirs}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'platformdirs' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-platformdirs
Summary:        %{summary}

%description -n python3-platformdirs %_description


%prep
%autosetup -p1 -n platformdirs-%{version}


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


%files -n python3-platformdirs -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 2.6.2-1
- Initial package