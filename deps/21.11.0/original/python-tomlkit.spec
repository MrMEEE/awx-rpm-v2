Name:           python-tomlkit
Version:        0.11.6
Release:        1%{?dist}
Summary:        Style preserving TOML library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/sdispater/tomlkit
Source:         %{pypi_source tomlkit}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tomlkit' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-tomlkit
Summary:        %{summary}

%description -n python3-tomlkit %_description


%prep
%autosetup -p1 -n tomlkit-%{version}


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


%files -n python3-tomlkit -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 0.11.6-1
- Initial package