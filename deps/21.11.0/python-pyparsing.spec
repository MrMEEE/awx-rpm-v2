Name:           python-pyparsing
Version:        2.4.6
Release:        1%{?dist}
Summary:        pyparsing module - Classes and methods to define and execute parsing grammars

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pyparsing/pyparsing/
Source:         %{pypi_source pyparsing}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyparsing' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pyparsing
Summary:        %{summary}

%description -n python3-pyparsing %_description


%prep
%autosetup -p1 -n pyparsing-%{version}


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


%files -n python3-pyparsing -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 2.4.6-1
- Initial package