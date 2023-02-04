Name:           python-cffi
Version:        1.15.1
Release:        1%{?dist}
Summary:        Foreign Function Interface for Python calling C code.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            http://cffi.readthedocs.org
Source:         %{pypi_source cffi}

BuildArch:      x86_64
BuildRequires:  python3-devel gcc libffi-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cffi' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-cffi
Summary:        %{summary}

%description -n python3-cffi %_description


%prep
%autosetup -p1 -n cffi-%{version}


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


%files -n python3-cffi -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 1.15.1-1
- Initial package
