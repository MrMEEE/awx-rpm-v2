Name:           python-ninja
Version:        1.11.1
Release:        1%{?dist}
Summary:        Ninja is a small build system with a focus on speed

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL and BSD
URL:            http://ninja-build.org/
Source:         %{pypi_source ninja}

BuildArch:      noarch
BuildRequires:  python3-devel cmake gcc gcc-c++


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ninja' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-ninja
Summary:        %{summary}

%description -n python3-ninja %_description


%prep
%autosetup -p1 -n ninja-%{version}


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


%files -n python3-ninja -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 1.11.1-1
- Initial package
