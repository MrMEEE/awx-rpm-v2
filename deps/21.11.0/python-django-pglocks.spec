Name:           python-django-pglocks
Version:        1.0.4
Release:        1%{?dist}
Summary:        django_pglocks provides useful context managers for advisory locks for PostgreSQL.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Xof/django-pglocks
Source:         %{pypi_source django-pglocks}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-pglocks' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-pglocks
Summary:        %{summary}

%description -n python3-django-pglocks %_description


%prep
%autosetup -p1 -n django-pglocks-%{version}


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


%files -n python3-django-pglocks -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 1.0.4-1
- Initial package