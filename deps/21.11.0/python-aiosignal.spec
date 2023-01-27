Name:           python-aiosignal
Version:        1.3.1
Release:        1%{?dist}
Summary:        aiosignal: a list of registered asynchronous callbacks

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/aio-libs/aiosignal
Source:         %{pypi_source aiosignal}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'aiosignal' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-aiosignal
Summary:        %{summary}

%description -n python3-aiosignal %_description


%prep
%autosetup -p1 -n aiosignal-%{version}


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


%files -n python3-aiosignal -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 1.3.1-1
- Initial package