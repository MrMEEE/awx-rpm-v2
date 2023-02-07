Name:           python-scikit-build
Version:        0.16.6
Release:        1%{?dist}
Summary:        Improved build system generator for Python C/C++/Fortran/Cython extensions

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/scikit-build/scikit-build
Source:         %{pypi_source scikit-build}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'scikit-build' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-scikit-build
Summary:        %{summary}

%description -n python3-scikit-build %_description


%prep
%autosetup -p1 -n scikit-build-%{version}


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


%files -n python3-scikit-build -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 0.16.6-1
- Initial package