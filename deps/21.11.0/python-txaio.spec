Name:           python-txaio
Version:        22.2.1
Release:        1%{?dist}
Summary:        Compatibility API between asyncio/Twisted/Trollius

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/crossbario/txaio
Source:         %{pypi_source txaio}

BuildArch:      noarch
BuildRequires:  python3-devel python3-twisted


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'txaio' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-txaio
Summary:        %{summary}

%description -n python3-txaio %_description


%prep
%autosetup -p1 -n txaio-%{version}


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


%files -n python3-txaio -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 22.2.1-1
- Initial package
