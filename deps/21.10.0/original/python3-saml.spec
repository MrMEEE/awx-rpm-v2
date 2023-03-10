Name:           python3-saml
Version:        1.13.0
Release:        1%{?dist}
Summary:        Saml Python Toolkit. Add SAML support to your Python software using this library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/SAML-Toolkits/python3-saml
Source:         %{pypi_source python3-saml}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python3-saml' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-python3-saml
Summary:        %{summary}

%description -n python3-python3-saml %_description


%prep
%autosetup -p1 -n python3-saml-%{version}


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


%files -n python3-python3-saml -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 1.13.0-1
- Initial package