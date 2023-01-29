Name:           python-django-taggit
Version:        3.1.0
Release:        1%{?dist}
Summary:        django-taggit is a reusable Django application for simple tagging.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/jazzband/django-taggit
Source:         %{pypi_source django-taggit}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-taggit' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-taggit
Summary:        %{summary}

%description -n python3-django-taggit %_description


%prep
%autosetup -p1 -n django-taggit-%{version}


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


%files -n python3-django-taggit -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 3.1.0-1
- Initial package