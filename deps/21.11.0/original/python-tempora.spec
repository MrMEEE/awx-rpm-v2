Name:           python-tempora
Version:        5.1.0
Release:        1%{?dist}
Summary:        Objects and routines pertaining to date and time (tempora)

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/jaraco/tempora
Source:         %{pypi_source tempora}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'tempora' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-tempora
Summary:        %{summary}

%description -n python3-tempora %_description


%prep
%autosetup -p1 -n tempora-%{version}


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


%files -n python3-tempora -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 5.1.0-1
- Initial package