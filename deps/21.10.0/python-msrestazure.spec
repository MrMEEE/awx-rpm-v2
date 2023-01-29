Name:           python-msrestazure
Version:        0.6.4
Release:        1%{?dist}
Summary:        AutoRest swagger generator Python client runtime. Azure-specific module.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Azure/msrestazure-for-python
Source:         %{pypi_source msrestazure}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'msrestazure' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-msrestazure
Summary:        %{summary}

%description -n python3-msrestazure %_description


%prep
%autosetup -p1 -n msrestazure-%{version}


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


%files -n python3-msrestazure -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 0.6.4-1
- Initial package