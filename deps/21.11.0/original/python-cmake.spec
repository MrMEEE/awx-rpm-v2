Name:           python-cmake
Version:        3.25.2
Release:        1%{?dist}
Summary:        CMake is an open-source, cross-platform family of tools designed to build, test and package software

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL and BSD
URL:            https://cmake.org/
Source:         %{pypi_source cmake}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cmake' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-cmake
Summary:        %{summary}

%description -n python3-cmake %_description


%prep
%autosetup -p1 -n cmake-%{version}


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


%files -n python3-cmake -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 3.25.2-1
- Initial package