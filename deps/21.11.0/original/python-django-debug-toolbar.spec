Name:           python-django-debug-toolbar
Version:        3.8.1
Release:        1%{?dist}
Summary:        A configurable set of panels that display various debug information about the current request/response.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/jazzband/django-debug-toolbar
Source:         %{pypi_source django_debug_toolbar}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-debug-toolbar' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-debug-toolbar
Summary:        %{summary}

%description -n python3-django-debug-toolbar %_description


%prep
%autosetup -p1 -n django_debug_toolbar-%{version}


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


%files -n python3-django-debug-toolbar -f %{pyproject_files}


%changelog
* Mon Feb 13 2023 Martin Juhl <m@rtinjuhl.dk> - 3.8.1-1
- Initial package