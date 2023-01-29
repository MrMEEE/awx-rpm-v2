Name:           python-xmlsec
Version:        1.3.13
Release:        1%{?dist}
Summary:        Python bindings for the XML Security Library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/mehcode/python-xmlsec
Source:         %{pypi_source xmlsec}

BuildArch:      x86_64
BuildRequires:  python3-devel xmlsec1-openssl xmlsec1-nss xmlsec1 xmlsec1-devel gcc libtool-ltdl-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xmlsec' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-xmlsec
Summary:        %{summary}

%description -n python3-xmlsec %_description


%prep
%autosetup -p1 -n xmlsec-%{version}


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


%files -n python3-xmlsec -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 1.3.13-1
- Initial package
