Name:           python-future
Version:        0.18.3
Release:        1%{?dist}
Summary:        Clean single-source support for Python 3 and 2

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://python-future.org
Source:         %{pypi_source future}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'future' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-future
Summary:        %{summary}

%description -n python3-future %_description


%prep
%autosetup -p1 -n future-%{version}


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


%files -n python3-future -f %{pyproject_files}


%changelog
* Tue Feb 21 2023 Martin Juhl <m@rtinjuhl.dk> - 0.18.3-1
- Initial package