Name:           python-social-auth-app-django
Version:        5.0.0
Release:        1%{?dist}
Summary:        Python Social Authentication, Django integration.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/python-social-auth/social-app-django
Source:         %{pypi_source social-auth-app-django}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'social-auth-app-django' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-social-auth-app-django
Summary:        %{summary}

%description -n python3-social-auth-app-django %_description


%prep
%autosetup -p1 -n social-auth-app-django-%{version}


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


%files -n python3-social-auth-app-django -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 5.0.0-1
- Initial package