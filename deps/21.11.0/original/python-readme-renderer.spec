Name:           python-readme-renderer
Version:        37.3
Release:        1%{?dist}
Summary:        readme_renderer is a library for rendering "readme" descriptions for Warehouse

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ASL
URL:            https://github.com/pypa/readme_renderer
Source:         %{pypi_source readme_renderer}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'readme-renderer' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-readme-renderer
Summary:        %{summary}

%description -n python3-readme-renderer %_description


%prep
%autosetup -p1 -n readme_renderer-%{version}


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


%files -n python3-readme-renderer -f %{pyproject_files}


%changelog
* Tue Feb 07 2023 Martin Juhl <m@rtinjuhl.dk> - 37.3-1
- Initial package