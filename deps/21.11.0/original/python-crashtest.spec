Name:           python-crashtest
Version:        0.4.1
Release:        1%{?dist}
Summary:        Manage Python errors with ease

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/sdispater/crashtest
Source:         %{pypi_source crashtest}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'crashtest' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-crashtest
Summary:        %{summary}

%description -n python3-crashtest %_description


%prep
%autosetup -p1 -n crashtest-%{version}


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


%files -n python3-crashtest -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 0.4.1-1
- Initial package