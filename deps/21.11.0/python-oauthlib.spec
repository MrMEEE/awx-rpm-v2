Name:           python-oauthlib
Version:        3.2.2
Release:        1%{?dist}
Summary:        A generic, spec-compliant, thorough implementation of the OAuth request-signing logic

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/oauthlib/oauthlib
Source:         %{pypi_source oauthlib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'oauthlib' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-oauthlib
Summary:        %{summary}

%description -n python3-oauthlib %_description


%prep
%autosetup -p1 -n oauthlib-%{version}


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


%files -n python3-oauthlib -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 3.2.2-1
- Initial package