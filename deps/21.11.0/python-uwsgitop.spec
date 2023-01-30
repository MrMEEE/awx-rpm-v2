%debug_package %{nil}

Name:           python-uwsgitop
Version:        0.11
Release:        1%{?dist}
Summary:        uWSGI top-like interface

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pypi.org/project/uwsgitop/
Source:         %{pypi_source uwsgitop}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'uwsgitop' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-uwsgitop
Summary:        %{summary}

%description -n python3-uwsgitop %_description


%prep
%autosetup -p1 -n uwsgitop-%{version}


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


%files -n python3-uwsgitop -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 0.11-1
- Initial package
