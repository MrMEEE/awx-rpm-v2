Name:           python-wheel
Version:        0.38.4
Release:        1%{?dist}
Summary:        A built-package format for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/wheel
Source:         %{pypi_source wheel}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'wheel' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-wheel
Summary:        %{summary}

%description -n python3-wheel %_description


%prep
%autosetup -p1 -n wheel-%{version}


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


%files -n python3-wheel -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 0.38.4-1
- Initial package