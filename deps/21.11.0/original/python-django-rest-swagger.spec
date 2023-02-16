Name:           python-django-rest-swagger
Version:        2.2.0
Release:        1%{?dist}
Summary:        Swagger UI for Django REST Framework 3.5+

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/marcgibbons/django-rest-swagger
Source:         %{pypi_source django-rest-swagger}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-rest-swagger' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-rest-swagger
Summary:        %{summary}

%description -n python3-django-rest-swagger %_description


%prep
%autosetup -p1 -n django-rest-swagger-%{version}


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


%files -n python3-django-rest-swagger -f %{pyproject_files}


%changelog
* Mon Feb 13 2023 Martin Juhl <m@rtinjuhl.dk> - 2.2.0-1
- Initial package