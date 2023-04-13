Name:           python-requirements-parser
Version:        0.5.0
Release:        1%{?dist}
Summary:        This is a small Python module for parsing Pip requirement files.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/madpah/requirements-parser
Source:         %{pypi_source requirements-parser}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'requirements-parser' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-requirements-parser
Summary:        %{summary}

%description -n python3-requirements-parser %_description


%prep
%autosetup -p1 -n requirements-parser-%{version}


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


%files -n python3-requirements-parser -f %{pyproject_files}


%changelog
* Wed Apr 05 2023 Martin Juhl <m@rtinjuhl.dk> - 0.5.0-1
- Initial package