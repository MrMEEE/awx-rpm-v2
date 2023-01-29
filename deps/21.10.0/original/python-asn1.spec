Name:           python-asn1
Version:        2.6.0
Release:        1%{?dist}
Summary:        Python-ASN1 is a simple ASN.1 encoder and decoder for Python 2.7+ and 3.5+.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/andrivet/python-asn1
Source:         %{pypi_source asn1}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'asn1' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-asn1
Summary:        %{summary}

%description -n python3-asn1 %_description


%prep
%autosetup -p1 -n asn1-%{version}


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


%files -n python3-asn1 -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 2.6.0-1
- Initial package