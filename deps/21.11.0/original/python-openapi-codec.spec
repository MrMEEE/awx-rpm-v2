Name:           python-openapi-codec
Version:        1.3.2
Release:        1%{?dist}
Summary:        An OpenAPI codec for Core API.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            http://github.com/core-api/python-openapi-codec/
Source:         %{pypi_source openapi-codec}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'openapi-codec' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-openapi-codec
Summary:        %{summary}

%description -n python3-openapi-codec %_description


%prep
%autosetup -p1 -n openapi-codec-%{version}


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


%files -n python3-openapi-codec -f %{pyproject_files}


%changelog
* Mon Feb 13 2023 Martin Juhl <m@rtinjuhl.dk> - 1.3.2-1
- Initial package