Name:           python-jinja2
Version:        3.1.2
Release:        1%{?dist}
Summary:        A very fast and expressive template engine.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://palletsprojects.com/p/jinja/
Source:         %{pypi_source Jinja2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'jinja2' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-jinja2
Summary:        %{summary}

%description -n python3-jinja2 %_description


%prep
%autosetup -p1 -n Jinja2-%{version}


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


%files -n python3-jinja2 -f %{pyproject_files}


%changelog
* Sun Jan 29 2023 Martin Juhl <m@rtinjuhl.dk> - 3.1.2-1
- Initial package