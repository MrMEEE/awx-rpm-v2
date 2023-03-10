Name:           python-prometheus-client
Version:        0.15.0
Release:        1%{?dist}
Summary:        Python client for the Prometheus monitoring system.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/prometheus/client_python
Source:         %{pypi_source prometheus_client}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'prometheus-client' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-prometheus-client
Summary:        %{summary}

%description -n python3-prometheus-client %_description


%prep
%autosetup -p1 -n prometheus_client-%{version}


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


%files -n python3-prometheus-client -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 0.15.0-1
- Initial package