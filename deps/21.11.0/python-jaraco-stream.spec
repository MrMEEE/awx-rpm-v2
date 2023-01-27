Name:           python-jaraco-stream
Version:        3.0.3
Release:        1%{?dist}
Summary:        routines for dealing with data streams

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jaraco/jaraco.stream
Source:         %{pypi_source jaraco.stream}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jaraco-stream' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-jaraco-stream
Summary:        %{summary}

%description -n python3-jaraco-stream %_description


%prep
%autosetup -p1 -n jaraco.stream-%{version}


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


%files -n python3-jaraco-stream -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 3.0.3-1
- Initial package