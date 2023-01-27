Name:           python-kubernetes
Version:        25.3.0
Release:        1%{?dist}
Summary:        Kubernetes python client

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/kubernetes-client/python
Source:         %{pypi_source kubernetes}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'kubernetes' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-kubernetes
Summary:        %{summary}

%description -n python3-kubernetes %_description


%prep
%autosetup -p1 -n kubernetes-%{version}


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


%files -n python3-kubernetes -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 25.3.0-1
- Initial package