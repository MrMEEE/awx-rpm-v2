Name:           python-jsonschema
Version:        4.17.3
Release:        1%{?dist}
Summary:        An implementation of JSON Schema validation for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/python-jsonschema/jsonschema
Source:         %{pypi_source jsonschema}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jsonschema' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-jsonschema
Summary:        %{summary}

%description -n python3-jsonschema %_description


%prep
%autosetup -p1 -n jsonschema-%{version}


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


%files -n python3-jsonschema -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 4.17.3-1
- Initial package