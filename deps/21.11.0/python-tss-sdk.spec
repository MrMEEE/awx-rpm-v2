Name:           python-tss-sdk
Version:        1.2.0
Release:        1%{?dist}
Summary:        The Delinea Secret Server Python SDK

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://pypi.org/project/python-tss-sdk/
Source:         %{pypi_source python-tss-sdk}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'python-tss-sdk' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-python-tss-sdk
Summary:        %{summary}

%description -n python3-python-tss-sdk %_description


%prep
%autosetup -p1 -n python-tss-sdk-%{version}


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


%files -n python3-python-tss-sdk -f %{pyproject_files}


%changelog
* Thu Feb 16 2023 Martin Juhl <m@rtinjuhl.dk> - 1.2.0-1
- Initial package