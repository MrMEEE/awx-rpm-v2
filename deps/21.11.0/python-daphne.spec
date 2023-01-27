Name:           python-daphne
Version:        3.0.2
Release:        1%{?dist}
Summary:        Django ASGI (HTTP/WebSocket) server

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/django/daphne
Source:         %{pypi_source daphne}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'daphne' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-daphne
Summary:        %{summary}

%description -n python3-daphne %_description


%prep
%autosetup -p1 -n daphne-%{version}


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


%files -n python3-daphne -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 3.0.2-1
- Initial package