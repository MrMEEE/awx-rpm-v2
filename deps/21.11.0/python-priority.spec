Name:           python-priority
Version:        1.3.0
Release:        1%{?dist}
Summary:        A pure-Python implementation of the HTTP/2 priority tree

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        gpl
URL:            https://github.com/python-hyper/priority/
Source:         %{pypi_source priority}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'priority' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-priority
Summary:        %{summary}

%description -n python3-priority %_description


%prep
%autosetup -p1 -n priority-%{version}


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


%files -n python3-priority -f %{pyproject_files}


%changelog
* Mon Feb 27 2023 Martin Juhl <m@rtinjuhl.dk> - 1.3.0-1
- Initial package