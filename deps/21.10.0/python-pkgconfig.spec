Name:           python-pkgconfig
Version:        1.5.5
Release:        1%{?dist}
Summary:        Interface Python with pkg-config

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/matze/pkgconfig
Source:         %{pypi_source pkgconfig}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pkgconfig' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pkgconfig
Summary:        %{summary}

%description -n python3-pkgconfig %_description


%prep
%autosetup -p1 -n pkgconfig-%{version}


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


%files -n python3-pkgconfig -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 1.5.5-1
- Initial package