Name:           python-types-setuptools
Version:        67.6.0.7
Release:        1%{?dist}
Summary:        Typing stubs for setuptools

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python/typeshed
Source:         %{pypi_source types-setuptools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'types-setuptools' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-types-setuptools
Summary:        %{summary}

%description -n python3-types-setuptools %_description


%prep
%autosetup -p1 -n types-setuptools-%{version}


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


%files -n python3-types-setuptools -f %{pyproject_files}


%changelog
* Wed Apr 05 2023 Martin Juhl <m@rtinjuhl.dk> - 67.6.0.7-1
- Initial package