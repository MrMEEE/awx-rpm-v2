Name:           python-more-itertools
Version:        9.0.0
Release:        1%{?dist}
Summary:        More routines for operating on iterables, beyond itertools

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/more-itertools/more-itertools
Source:         %{pypi_source more-itertools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'more-itertools' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-more-itertools
Summary:        %{summary}

%description -n python3-more-itertools %_description


%prep
%autosetup -p1 -n more-itertools-%{version}


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


%files -n python3-more-itertools -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 9.0.0-1
- Initial package