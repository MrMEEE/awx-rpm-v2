Name:           python-build
Version:        0.10.0
Release:        1%{?dist}
Summary:        A simple, correct Python build frontend

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/build/
Source:         %{pypi_source build}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'build' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-build
Summary:        %{summary}

%description -n python3-build %_description


%prep
%autosetup -p1 -n build-%{version}


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


%files -n python3-build -f %{pyproject_files}


%changelog
* Mon Feb 13 2023 Martin Juhl <m@rtinjuhl.dk> - 0.10.0-1
- Initial package