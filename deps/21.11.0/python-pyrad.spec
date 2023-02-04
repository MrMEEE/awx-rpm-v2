Name:           python-pyrad
Version:        2.4
Release:        1%{?dist}
Summary:        RADIUS tools

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/pyradius/pyrad
Source:         %{pypi_source pyrad}

BuildArch:      noarch
BuildRequires:  python3-devel python3-poetry


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyrad' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-pyrad
Summary:        %{summary}

%description -n python3-pyrad %_description


%prep
%autosetup -p1 -n pyrad-%{version}


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


%files -n python3-pyrad -f %{pyproject_files}


%changelog
* Fri Jan 27 2023 root - 2.4-1
- Initial package
