Name:           python-frozenlist
Version:        1.3.3
Release:        1%{?dist}
Summary:        A list-like structure which implements collections.abc.MutableSequence

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/aio-libs/frozenlist
Source:         %{pypi_source frozenlist}

BuildArch:      x86_64
BuildRequires:  python3-devel gcc

patch: frozenlist-wheel-version.patch

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'frozenlist' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-frozenlist
Summary:        %{summary}

%description -n python3-frozenlist %_description


%prep
%autosetup -p1 -n frozenlist-%{version}


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


%files -n python3-frozenlist -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 1.3.3-1
- Initial package
