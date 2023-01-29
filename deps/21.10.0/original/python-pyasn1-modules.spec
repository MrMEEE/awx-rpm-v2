Name:           python-pyasn1-modules
Version:        0.2.8
Release:        1%{?dist}
Summary:        A collection of ASN.1-based protocols modules.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/etingof/pyasn1-modules
Source:         %{pypi_source pyasn1-modules}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyasn1-modules' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pyasn1-modules
Summary:        %{summary}

%description -n python3-pyasn1-modules %_description


%prep
%autosetup -p1 -n pyasn1-modules-%{version}


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


%files -n python3-pyasn1-modules -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 0.2.8-1
- Initial package