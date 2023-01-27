Name:           python-importlib-metadata
Version:        5.1.0
Release:        1%{?dist}
Summary:        Read metadata from Python packages

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/python/importlib_metadata
Source:         %{pypi_source importlib_metadata}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'importlib-metadata' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-importlib-metadata
Summary:        %{summary}

%description -n python3-importlib-metadata %_description


%prep
%autosetup -p1 -n importlib_metadata-%{version}


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


%files -n python3-importlib-metadata -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 5.1.0-1
- Initial package