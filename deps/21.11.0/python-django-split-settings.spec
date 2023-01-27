Name:           python-django-split-settings
Version:        1.0.0
Release:        1%{?dist}
Summary:        Organize Django settings into multiple files and directories. Easily override and modify settings. Use wildcards and optional settings files.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://django-split-settings.readthedocs.io
Source:         %{pypi_source django-split-settings}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'django-split-settings' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-django-split-settings
Summary:        %{summary}

%description -n python3-django-split-settings %_description


%prep
%autosetup -p1 -n django-split-settings-%{version}


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


%files -n python3-django-split-settings -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 1.0.0-1
- Initial package