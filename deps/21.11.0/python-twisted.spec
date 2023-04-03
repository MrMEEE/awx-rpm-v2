%bcond_without check

Name:           python-twisted
Version:        22.10.0
Release:        1%{?dist}
Summary:        An asynchronous networking framework written in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://twistedmatrix.com/
Source:         %{pypi_source Twisted}

BuildArch:      noarch
BuildRequires:  python3-devel python3-cryptography python3-bcrypt python3-pyasn1 python3-tkinter python3-hamcrest glibc-langpack-en python3-pyopenssl

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'twisted' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-twisted
Summary:        %{summary}
Provides: python3dist(twisted[tls]) python3.9dist(twisted[tls])

%description -n python3-twisted %_description


%prep
%autosetup -p1 -n Twisted-%{version}


%generate_buildrequires
%pyproject_buildrequires -x tls -x http2


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-twisted -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 22.10.0-1
- Initial package
