Name:           python-django-guid
Version:        3.2.1
Release:        1%{?dist}
Summary:        Middleware that enables single request-response cycle tracing by injecting a unique ID into project logs

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD and Proprietary License
URL:            https://github.com/snok/django-guid
Source:         %{pypi_source django-guid}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-guid' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-guid
Summary:        %{summary}

%description -n python3-django-guid %_description


%prep
%autosetup -p1 -n django-guid-%{version}


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


%files -n python3-django-guid -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 3.2.1-1
- Initial package