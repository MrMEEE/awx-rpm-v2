Name:           python-cachetools
Version:        5.2.0
Release:        1%{?dist}
Summary:        Extensible memoizing collections and decorators

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/tkem/cachetools/
Source:         %{pypi_source cachetools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cachetools' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-cachetools
Summary:        %{summary}

%description -n python3-cachetools %_description


%prep
%autosetup -p1 -n cachetools-%{version}


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


%files -n python3-cachetools -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 5.2.0-1
- Initial package