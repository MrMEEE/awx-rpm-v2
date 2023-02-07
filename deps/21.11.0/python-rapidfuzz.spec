Name:           python-rapidfuzz
Version:        2.13.7
Release:        1%{?dist}
Summary:        rapid fuzzy string matching

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/maxbachmann/RapidFuzz
Source:         %{pypi_source rapidfuzz}

BuildArch:      noarch
BuildRequires:  python3-devel cmake gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rapidfuzz' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-rapidfuzz
Summary:        %{summary}

%description -n python3-rapidfuzz %_description


%prep
%autosetup -p1 -n rapidfuzz-%{version}


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


%files -n python3-rapidfuzz -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 2.13.7-1
- Initial package
