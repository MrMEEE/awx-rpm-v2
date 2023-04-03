Name:           python-onelogin
Version:        3.1.0
Release:        1%{?dist}
Summary:        OneLogin API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/onelogin/
Source:         %{pypi_source onelogin}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'onelogin' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-onelogin
Summary:        %{summary}

%description -n python3-onelogin %_description


%prep
%autosetup -p1 -n onelogin-%{version}


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


%files -n python3-onelogin -f %{pyproject_files}


%changelog
* Tue Feb 21 2023 Martin Juhl <m@rtinjuhl.dk> - 3.1.0-1
- Initial package