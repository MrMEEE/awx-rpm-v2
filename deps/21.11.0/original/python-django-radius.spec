Name:           python-django-radius
Version:        1.5.0
Release:        1%{?dist}
Summary:        Django authentication backend for RADIUS

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            http://robgolding63.github.com/django-radius/
Source:         %{pypi_source django-radius}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-radius' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-radius
Summary:        %{summary}

%description -n python3-django-radius %_description


%prep
%autosetup -p1 -n django-radius-%{version}


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


%files -n python3-django-radius -f %{pyproject_files}


%changelog
* Tue Feb 21 2023 Martin Juhl <m@rtinjuhl.dk> - 1.5.0-1
- Initial package