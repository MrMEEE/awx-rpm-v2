Name:           python-social-auth-core
Version:        4.3.0
Release:        1%{?dist}
Summary:        Python social authentication made simple.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/python-social-auth/social-core
Source:         %{pypi_source social-auth-core}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'social-auth-core' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-social-auth-core
Summary:        %{summary}

%description -n python3-social-auth-core %_description


%prep
%autosetup -p1 -n social-auth-core-%{version}


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


%files -n python3-social-auth-core -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 4.3.0-1
- Initial package