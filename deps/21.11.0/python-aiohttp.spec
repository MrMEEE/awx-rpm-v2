Name:           python-aiohttp
Version:        3.8.3
Release:        1%{?dist}
Summary:        Async http client/server framework (asyncio)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/aio-libs/aiohttp
Source:         %{pypi_source aiohttp}

BuildArch:      x86_64
BuildRequires:  python3-devel gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aiohttp' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-aiohttp
Summary:        %{summary}

%description -n python3-aiohttp %_description


%prep
%autosetup -p1 -n aiohttp-%{version}


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


%files -n python3-aiohttp -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 3.8.3-1
- Initial package
