Name:           python-django-oauth-toolkit
Version:        1.4.1
Release:        1%{?dist}
Summary:        OAuth2 Provider for Django

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/jazzband/django-oauth-toolkit
Source:         %{pypi_source django-oauth-toolkit}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-oauth-toolkit' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-oauth-toolkit
Summary:        %{summary}

%description -n python3-django-oauth-toolkit %_description


%prep
%autosetup -p1 -n django-oauth-toolkit-%{version}


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


%files -n python3-django-oauth-toolkit -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 1.4.1-1
- Initial package