Name:           python-hatch-fancy-pypi-readme
Version:        22.8.0
Release:        1%{?dist}
Summary:        Fancy PyPI READMEs with Hatch

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pypi.org/project/hatch-fancy-pypi-readme/
Source:         %{pypi_source hatch_fancy_pypi_readme}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hatch-fancy-pypi-readme' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-hatch-fancy-pypi-readme
Summary:        %{summary}

%description -n python3-hatch-fancy-pypi-readme %_description


%prep
%autosetup -p1 -n hatch_fancy_pypi_readme-%{version}


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


%files -n python3-hatch-fancy-pypi-readme -f %{pyproject_files}


%changelog
* Tue Feb 07 2023 Martin Juhl <m@rtinjuhl.dk> - 22.8.0-1
- Initial package