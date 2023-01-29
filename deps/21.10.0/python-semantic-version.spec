Name:           python-semantic-version
Version:        2.10.0
Release:        1%{?dist}
Summary:        A library implementing the 'SemVer' scheme.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/rbarrois/python-semanticversion
Source:         %{pypi_source semantic_version}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'semantic-version' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-semantic-version
Summary:        %{summary}

%description -n python3-semantic-version %_description


%prep
%autosetup -p1 -n semantic_version-%{version}


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


%files -n python3-semantic-version -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 2.10.0-1
- Initial package