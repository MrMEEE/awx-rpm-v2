Name:           python-yarl
Version:        1.8.1
Release:        1%{?dist}
Summary:        Yet another URL library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/aio-libs/yarl/
Source:         %{pypi_source yarl}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'yarl' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-yarl
Summary:        %{summary}

%description -n python3-yarl %_description


%prep
%autosetup -p1 -n yarl-%{version}


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


%files -n python3-yarl -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 1.8.1-1
- Initial package