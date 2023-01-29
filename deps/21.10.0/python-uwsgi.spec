Name:           python-uwsgi
Version:        2.0.21
Release:        1%{?dist}
Summary:        The uWSGI server

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL2
URL:            https://uwsgi-docs.readthedocs.io/en/latest/
Source:         %{pypi_source uwsgi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uwsgi' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-uwsgi
Summary:        %{summary}

%description -n python3-uwsgi %_description


%prep
%autosetup -p1 -n uwsgi-%{version}


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


%files -n python3-uwsgi -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 2.0.21-1
- Initial package