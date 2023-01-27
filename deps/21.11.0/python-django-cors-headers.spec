Name:           python-django-cors-headers
Version:        3.13.0
Release:        1%{?dist}
Summary:        django-cors-headers is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/adamchainz/django-cors-headers
Source:         %{pypi_source django-cors-headers}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-cors-headers' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-cors-headers
Summary:        %{summary}

%description -n python3-django-cors-headers %_description


%prep
%autosetup -p1 -n django-cors-headers-%{version}


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


%files -n python3-django-cors-headers -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 3.13.0-1
- Initial package