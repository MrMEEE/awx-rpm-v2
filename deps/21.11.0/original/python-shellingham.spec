Name:           python-shellingham
Version:        1.5.0^post1
Release:        1%{?dist}
Summary:        Tool to Detect Surrounding Shell

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://github.com/sarugaku/shellingham
Source:         %{pypi_source shellingham 1.5.0.post1}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'shellingham' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-shellingham
Summary:        %{summary}

%description -n python3-shellingham %_description


%prep
%autosetup -p1 -n shellingham-1.5.0.post1


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


%files -n python3-shellingham -f %{pyproject_files}


%changelog
* Mon Feb 06 2023 Martin Juhl <m@rtinjuhl.dk> - 1.5.0^post1-1
- Initial package